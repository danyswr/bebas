#!/usr/bin/env python3
"""
Secure portable terminal worker for Claw3D / OpenClaw manager.

Design goal:
- worker is only a remote terminal executor
- worker does not need direct Supabase access by default
- worker receives tasks from manager/C2 only
- worker executes only explicitly allowed commands
- worker reports back stdout/stderr/exit code only

Recommended deployment:
- run manager on VPS
- set DISTRIBUTED_WORKER_TOKEN on manager
- set the same CLAW3D_WORKER_TOKEN on the worker
- expose manager over HTTPS / Tailscale if possible
"""

from __future__ import annotations

import json
import os
import platform
import shlex
import shutil
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.request
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any


DEFAULT_MANAGER_URL = f"http://{os.getenv('CLAW3D_MANAGER_HOST', '104.208.76.22')}:3000"
DEFAULT_ALLOWED_PREFIXES = [
    "bash",
    "sh",
    "python",
    "python3",
    "node",
    "npm",
    "npx",
    "go",
    "cargo",
    "git",
    "curl",
    "wget",
    "ls",
    "cat",
    "pwd",
    "echo",
    "whoami",
    "uname",
    "id",
    "env",
    "rg",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def env_bool(name: str, default: bool = False) -> bool:
    raw = os.getenv(name, "").strip().lower()
    if not raw:
        return default
    return raw in {"1", "true", "yes", "on"}


def env_csv(name: str, default: list[str]) -> list[str]:
    raw = os.getenv(name, "").strip()
    if not raw:
        return default
    return [item.strip() for item in raw.split(",") if item.strip()]


def truncate(text: str, limit: int) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 16] + "\n...[truncated]..."


@dataclass
class Config:
    manager_url: str
    studio_cookie: str
    worker_token: str
    worker_id: str
    worker_label: str
    device_class: str
    capabilities: list[str]
    tags: list[str]
    heartbeat_interval: int
    idle_sleep: int
    command_timeout: int
    command_max_output: int
    shell_mode: bool
    allowed_prefixes: list[str]
    run_once: bool


class HttpJsonClient:
    def __init__(self, base_headers: dict[str, str] | None = None, timeout: int = 30):
        self.base_headers = base_headers or {}
        self.timeout = timeout

    def request(
        self,
        url: str,
        method: str = "GET",
        body: Any | None = None,
        headers: dict[str, str] | None = None,
    ) -> Any:
        merged_headers = {"Accept": "application/json", **self.base_headers, **(headers or {})}
        data = None
        if body is not None:
            data = json.dumps(body).encode("utf-8")
            merged_headers["Content-Type"] = "application/json"
        request = urllib.request.Request(url=url, data=data, headers=merged_headers, method=method)
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                raw = response.read().decode("utf-8")
                return json.loads(raw) if raw else None
        except urllib.error.HTTPError as exc:
            payload = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"{method} {url} failed: {exc.code} {payload}") from exc
        except urllib.error.URLError as exc:
            raise RuntimeError(f"{method} {url} failed: {exc.reason}") from exc


class TerminalWorker:
    def __init__(self, config: Config):
        headers: dict[str, str] = {}
        if config.studio_cookie:
            headers["Cookie"] = f"studio_access={config.studio_cookie}"
        if config.worker_token:
            headers["x-claw3d-worker-token"] = config.worker_token
        self.config = config
        self.client = HttpJsonClient(base_headers=headers)

    def manager_url(self, path: str) -> str:
        return f"{self.config.manager_url.rstrip('/')}{path}"

    def log(self, message: str) -> None:
        print(f"[{utc_now()}] {message}", flush=True)

    def register(self) -> dict[str, Any]:
        payload = {
            "id": self.config.worker_id,
            "label": self.config.worker_label,
            "deviceClass": self.config.device_class,
            "endpoint": os.getenv("CLAW3D_WORKER_ENDPOINT", ""),
            "capabilities": self.config.capabilities,
            "tags": self.config.tags,
            "meta": {
                "hostname": socket.gethostname(),
                "platform": platform.platform(),
                "python": platform.python_version(),
                "shell_mode": str(self.config.shell_mode).lower(),
                "allowed_prefixes": ",".join(self.config.allowed_prefixes),
            },
        }
        response = self.client.request(self.manager_url("/api/distributed/workers"), method="PUT", body=payload)
        return response.get("worker", {})

    def heartbeat(self) -> dict[str, Any]:
        response = self.client.request(
            self.manager_url("/api/distributed/workers"),
            method="POST",
            body={"workerId": self.config.worker_id},
        )
        return response.get("worker", {})

    def claim_task(self) -> dict[str, Any]:
        return self.client.request(
            self.manager_url("/api/distributed/tasks/claim"),
            method="POST",
            body={"workerId": self.config.worker_id},
        )

    def report_task(
        self,
        task_id: str,
        lease_id: str,
        success: bool,
        output: str,
        failure_reason: str = "",
    ) -> None:
        self.client.request(
            self.manager_url("/api/distributed/tasks/report"),
            method="POST",
            body={
                "workerId": self.config.worker_id,
                "taskId": task_id,
                "leaseId": lease_id,
                "success": success,
                "output": output,
                "failureReason": failure_reason,
            },
        )

    def resolve_command(self, task: dict[str, Any]) -> str:
        candidates = [
            task.get("command"),
            task.get("terminal_command"),
            task.get("shell_command"),
            task.get("description"),
            task.get("title"),
        ]
        for item in candidates:
            if isinstance(item, str) and item.strip():
                return item.strip()
        return ""

    def validate_command(self, command: str) -> tuple[bool, str]:
        if not command:
            return False, "Empty command."
        try:
            parts = shlex.split(command)
        except ValueError as exc:
            return False, f"Invalid command syntax: {exc}"
        if not parts:
            return False, "Command parsing produced no executable."
        executable = parts[0]
        if executable not in self.config.allowed_prefixes:
            return False, f"Executable '{executable}' is not in the worker allowlist."
        if shutil.which(executable) is None:
            return False, f"Executable '{executable}' is not available on this worker."
        dangerous_tokens = {"rm -rf /", ":(){", "mkfs", "shutdown", "reboot", "halt"}
        lowered = command.lower()
        if any(token in lowered for token in dangerous_tokens):
            return False, "Command rejected by safety policy."
        return True, ""

    def execute_command(self, command: str) -> tuple[bool, str]:
        allowed, reason = self.validate_command(command)
        if not allowed:
            return False, reason
        try:
            if self.config.shell_mode:
                completed = subprocess.run(
                    command,
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=self.config.command_timeout,
                    cwd=os.getenv("CLAW3D_WORKER_CWD") or None,
                )
            else:
                completed = subprocess.run(
                    shlex.split(command),
                    shell=False,
                    capture_output=True,
                    text=True,
                    timeout=self.config.command_timeout,
                    cwd=os.getenv("CLAW3D_WORKER_CWD") or None,
                )
        except subprocess.TimeoutExpired as exc:
            return False, truncate(f"Command timed out after {self.config.command_timeout}s.\n{exc}", self.config.command_max_output)
        except Exception as exc:  # noqa: BLE001
            return False, truncate(f"Command execution failed: {exc}", self.config.command_max_output)

        stdout = completed.stdout or ""
        stderr = completed.stderr or ""
        payload = {
            "command": command,
            "exit_code": completed.returncode,
            "stdout": truncate(stdout, self.config.command_max_output),
            "stderr": truncate(stderr, self.config.command_max_output),
        }
        success = completed.returncode == 0
        return success, json.dumps(payload, ensure_ascii=True)

    def execute_task(self, task: dict[str, Any]) -> tuple[bool, str]:
        command = self.resolve_command(task)
        task_id = str(task.get("id") or "unknown-task")
        if not command:
            return False, json.dumps(
                {"task_id": task_id, "error": "No executable command found in task payload."},
                ensure_ascii=True,
            )
        self.log(f"Executing task {task_id}: {command}")
        return self.execute_command(command)

    def run(self) -> None:
        worker = self.register()
        self.log(f"Connected to manager as {worker.get('label', self.config.worker_label)}")
        while True:
            try:
                self.heartbeat()
                claimed = self.claim_task()
                task = claimed.get("task")
                lease = claimed.get("lease")
                if task and lease:
                    success, output = self.execute_task(task)
                    failure_reason = "" if success else output
                    self.report_task(
                        str(task.get("id")),
                        str(lease.get("leaseId")),
                        success,
                        output,
                        failure_reason=failure_reason,
                    )
                else:
                    self.log("No task available.")
                    if self.config.run_once:
                        return
                    time.sleep(self.config.idle_sleep)
                    continue
            except Exception as exc:  # noqa: BLE001
                self.log(f"Worker loop error: {exc}")
                if self.config.run_once:
                    raise
                time.sleep(max(self.config.heartbeat_interval, 5))
                continue

            if self.config.run_once:
                return
            time.sleep(self.config.heartbeat_interval)


def load_config() -> Config:
    generated_id = f"worker-{uuid.uuid4()}"
    label_default = f"{platform.node() or 'sandbox'}-{platform.system().lower() or 'python'}"
    return Config(
        manager_url=os.getenv("CLAW3D_MANAGER_URL", DEFAULT_MANAGER_URL).strip(),
        studio_cookie=os.getenv("CLAW3D_STUDIO_ACCESS_COOKIE", "").strip(),
        worker_token=os.getenv("CLAW3D_WORKER_TOKEN", "").strip(),
        worker_id=os.getenv("CLAW3D_WORKER_ID", generated_id).strip(),
        worker_label=os.getenv("CLAW3D_WORKER_LABEL", label_default).strip(),
        device_class=os.getenv("CLAW3D_WORKER_DEVICE_CLASS", "sandbox").strip(),
        capabilities=env_csv("CLAW3D_WORKER_CAPABILITIES", ["terminal"]),
        tags=env_csv("CLAW3D_WORKER_TAGS", ["terminal-only", "portable-worker"]),
        heartbeat_interval=int(os.getenv("CLAW3D_HEARTBEAT_INTERVAL", "20")),
        idle_sleep=int(os.getenv("CLAW3D_IDLE_SLEEP", "15")),
        command_timeout=int(os.getenv("CLAW3D_COMMAND_TIMEOUT", "120")),
        command_max_output=int(os.getenv("CLAW3D_COMMAND_MAX_OUTPUT", "12000")),
        shell_mode=env_bool("CLAW3D_ALLOW_SHELL_MODE", False),
        allowed_prefixes=env_csv("CLAW3D_ALLOWED_PREFIXES", DEFAULT_ALLOWED_PREFIXES),
        run_once=env_bool("CLAW3D_WORKER_RUN_ONCE", False),
    )


def main() -> int:
    config = load_config()
    if not config.manager_url:
        print("CLAW3D_MANAGER_URL is required.", file=sys.stderr)
        return 1
    worker = TerminalWorker(config)
    worker.run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
