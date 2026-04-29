# MyWork - SOC Dashboard 2D

## 🚀 Technical Stack (Agreed)

Project ini dibangun sesuai dengan spesifikasi yang telah disetujui:

### Backend
- **Language**: Python
- **Server**: Uvicorn
- **Communication**: Socket (WebSockets)

---

## 🧠 Core Concept: Autonomous AI Syndicate

Sistem ini dirancang sebagai ekosistem AI otonom yang fleksibel, dengan spesialisasi utama pada CTF dan Bug Bounty, namun mampu menangani peran operasional lainnya.

### 👥 The AI Worker Roles
1. **Supervisor (OpenClaw)**: Pusat komando tunggal. Mengelola orchestrasi, strategi jangka panjang, dan pembagian tugas ke worker.
2. **Cyber Worker (The Operator)**: Eksekutor teknis (Recon, Exploitation). Menjalankan perintah terminal di lingkungan terisolasi.
3. **Programmer Worker (The Armorer)**: Membangun *custom tools* dan script eksploitasi. Dilengkapi dengan *Automated Sandbox Testing* sebelum senjata dikirim ke Cyber Worker.
4. **Finance Worker (The Throttle)**: Bertindak sebagai *Load Balancer* kuota API. Memantau multi-API OpenRouter dan mengoptimalkan penggunaan token secara proaktif.
5. **Management Worker (The Q&A)**: Analisis prioritas tugas dan koordinasi antar departemen AI untuk efisiensi maksimal.

### 🛠️ Technical Infrastructure
- **Worker Bridge**: Koneksi terenkripsi (WSS) dari FastAPI Hub ke resource luar (Google Colab, V0 Sandbox, Docker) untuk komputasi gratis tanpa membebani host utama.
- **Telegram C2**: Bot Command & Control untuk kontrol jarak jauh (perintah `/status`, `/deploy`, dll).
- **The Brain (Supabase RAG)**: Penyimpanan memori jangka panjang menggunakan Vector Search (FAISS) untuk recall teknis dari log eksploitasi masa lalu.
- **State Machine**: Sistem jabat tangan (*handshake*) ketat antara Supervisor dan Worker untuk mencegah infinite loop dan pemborosan API.

---

## 🗺️ Execution Roadmap

1. **Phase 1: Remote Bridge**: Membangun Jantung (FastAPI Hub) dan Jembatan (Colab WebSocket Script).
2. **Phase 2: Orchestration**: Implementasi State Machine dan logika Supervisor-Worker.
3. **Phase 3: Command & Control**: Integrasi Telegram Bot sebagai pusat kendali.
4. **Phase 4: Deep Memory**: Integrasi Supabase dan arsitektur RAG.

## 📚 Reference Integration (Agreed)

Berikut adalah 10 poin integrasi algoritma dan desain dari repository referensi:

1. **Supervisor Design (ClawLibrary)**: Menggunakan aset **Capybara** (`capy-claw-emoji-v2`) sebagai representasi visual OpenClaw.
2. **Task Factory Logic (Claw3D)**: Implementasi *Massive Task Distribution* (berdasarkan `task_store.py`). Supervisor men-generate ratusan task sekaligus ke antrian untuk di-claim oleh worker aktif.
3. **Worker 2D Sprites (Multi-Source)**: Menggunakan kombinasi aset karakter pixel art dari `agent-fridays-pixel-office` dan `generative_agents` (termasuk `atlas.json` untuk animasi jalan).
4. **2D Environment Design**: Menggunakan tileset `walls.png` dan `default-layout.json` dari `agent-fridays` untuk membangun kantor SOC Top-Down.
5. **Cognitive Brain (Stanford RAG)**: Mengadopsi algoritma `retrieve.py` dan `reflect.py` dari `generative_agents` untuk memori teknis eksploitasi.
6. **Autonomous Execution**: Menggunakan logika `execute.py` dari `generative_agents` agar worker bisa mandiri mengeksekusi tugas terminal.
7. **Room Management**: Mengatur layout kordinat khusus untuk Red Team, Blue Team, dan Management.
8. **Bulletin Board Feature**: Mengadopsi fitur papan informasi dari `Claw3D` yang diubah ke visual 2D untuk memantau target bounty.
9. **High-Speed Socket Sync**: Implementasi ulang `GatewayClient.ts` dari `Claw3D` ke Python untuk sinkronisasi posisi 1:1 antara server dan dashboard.
10. **Data Normalization**: Menggunakan strategi `layoutSnapshot.ts` untuk memastikan konsistensi data kordinat antar departemen.

11. **Agent-to-Agent Dialogue**: Implementasi `converse.py` (Stanford) agar worker bisa "ngobrol" teknis saat berdekatan di kordinat yang sama.
12. **Peak Productivity**: Menghilangkan sistem fatigue; semua worker berjalan di kecepatan maksimal 24/7.
13. **2D Collision System**: Menggunakan grid-based collision dari `ClawLibrary` untuk mencegah worker menembus tembok atau bertumpukan.
14. **API-Based Log Storage**: Log eksekusi terminal disimpan via API dan bisa diakses lewat furniture "Berkas/Arsip" di dashboard.
15. **Emergency Broadcast System**: Fitur pengumuman global dari Supervisor yang muncul di layar dashboard saat ada temuan krusial.
16. **Advanced C2 Telegram Commands**:
    - `/worker`: Pantau jumlah worker aktif dan perannya.
    - `/task`: Cek antrian perkerjaan yang sedang diproses.
    - `/target`: Memberikan goals spesifik (misal: "Scan IP lokal dan ambil flag CTF").
17. **Dynamic Room Resizing**: Ruangan kantor (Red/Blue/Management) bisa meluas otomatis jika jumlah worker bertambah banyak.
18. **Socket Diffing & Telegram Monitoring**: Optimasi bandwidth socket dan integrasi penuh agar monitoring tidak wajib buka browser (bisa via Telegram).
19. **Visual Status Emotes**: Menggunakan capy-emoji untuk menandakan status worker (Idle, Hacking, Error).
20. **Continuous Operation**: Sistem berjalan 24/7 tanpa siklus istirahat (High Availability).

21. **Automated Victory Report**: Management Worker otomatis men-generate laporan Markdown saat target/flag berhasil didapatkan dan mengirimkannya ke Telegram.
22. **Self-Reflection Recovery**: Worker akan menganalisa log error jika eksploitasi gagal dan mencoba teknik alternatif secara otonom.
23. **Defensive Swarm Intelligence**: Mode "Keroyokan" khusus untuk pertahanan (Defend) agar banyak worker bisa fokus memproteksi satu infrastruktur secara bersamaan.
24. **Server Rack API Monitoring**: Visual rak server di dashboard dengan indikator lampu status untuk memantau limitasi 3 API OpenRouter secara real-time.
25. **Wall of Fame & Telegram Alerts**: Papan prestasi di dashboard (dan notifikasi Telegram) untuk setiap temuan Critical bug atau flag CTF.
26. **Target Visual Heatmap**: Indikator pada papan buletin dashboard yang menunjukkan area target yang paling intens diserang/di-scan.
27. **Visual Loot Animation**: Animasi worker membawa "kotak data" ke ruang Management saat berhasil mengambil informasi dari target.
28. **Socket Auto-Reconnect**: Sistem jabat tangan tangguh dari `Claw3D` untuk menjamin dashboard tidak terputus saat koneksi internet tidak stabil.
29. **Autonomous Stealth/Aggressive Logic**: Supervisor secara otomatis menentukan ritme serangan (Stealth vs Aggressive) berdasarkan respon target dan risiko deteksi.

30. **Optimized Multi-Floor Workspace**: Sistem lantai virtual untuk memisahkan proyek (misal: Lantai 1 CTF, Lantai 2 Bug Bounty) dengan optimasi logic agar tetap ringan.
31. **Encrypted Log Storage**: Enkripsi AES pada semua log teknis di Supabase untuk menjamin kerahasiaan eksploitasi.
32. **The "/nuke" Command**: Perintah darurat via Telegram untuk mematikan semua sesi aktif dan menghapus log sementara secara instan.
33. **Supervisor "Hunch" Alerts**: Notifikasi anomali dari Supervisor jika mendeteksi potensi celah yang membutuhkan perhatian manual Bos.
34. **API Key Hot-Swap**: Automasi penggantian API Key OpenRouter oleh Finance Worker jika terdeteksi adanya limit atau blokir.
35. **Resource Bidding System**: Sistem antrian worker berbasis prioritas tugas dan potensi profit untuk efisiensi penggunaan Colab.

---
**Operational Command**: USER (Commander-in-Chief)
**Executing Unit**: AGENT (Tactical Adversary Simulator)

---

## 📁 Implemented Workspace Structure

Struktur project awal sekarang dipisah supaya gampang dioprek:

- `frontend/` → Next.js App Router dashboard
- `backend/` → FastAPI hub + WebSocket
- `backend/app/services/supervisor/` → logic supervisor
- `backend/app/services/workers/` → logic worker per role
- `backend/app/services/memory/` → memory / reflection layer
- `backend/app/services/bridge/` → bridge placeholder
- `docs/architecture.md` → catatan arsitektur implementasi

## ▶️ Local Run

### Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Backend akan aktif di `http://127.0.0.1:8000`.

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend akan aktif di `http://127.0.0.1:3000`.

Jika ingin pakai endpoint custom:

```bash
NEXT_PUBLIC_BACKEND_HTTP_URL=http://127.0.0.1:8000
NEXT_PUBLIC_BACKEND_WS_URL=ws://127.0.0.1:8000/ws/dashboard
```

## 🛡️ Safety Note


