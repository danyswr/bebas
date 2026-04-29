# MyWork - Virtual 2D Cyber Security Company

## 🚀 Technical Stack (Agreed)

Project ini dibangun sesuai dengan spesifikasi yang telah disetujui:

### Backend
- **Language**: Python
- **Server**: Uvicorn
- **Communication**: Socket (WebSockets)

---

## 🧠 Core Concept: Virtual 2D Autonomous Syndicate

Sistem ini dirancang sebagai sebuah **Perusahaan/Kantor Virtual 2D** berbasis *pixel-art*. Fokus utama aplikasi ini bukanlah sekadar *dashboard* pemantauan, melainkan simulasi lingkungan kerja tempat entitas AI (Worker) bergerak, berinteraksi, dan mengeksekusi tugas secara *real-time* berdasarkan perintah dari Supervisor (OpenClaw). Perusahaan virtual ini memiliki spesialisasi utama pada operasi CTF dan Bug Bounty.

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
4. **2D Environment Design**: Menggunakan tileset `walls.png` dan `default-layout.json` dari `agent-fridays` untuk membangun kantor perusahaan keamanan siber Top-Down 2D.
5. **Cognitive Brain (Stanford RAG)**: Mengadopsi algoritma `retrieve.py` dan `reflect.py` dari `generative_agents` untuk memori teknis eksploitasi.
6. **Autonomous Execution**: Menggunakan logika `execute.py` dari `generative_agents` agar worker bisa mandiri mengeksekusi tugas terminal.
7. **Room Management**: Mengatur layout kordinat ruangan kerja khusus untuk Red Team, Blue Team, dan Management di dalam kantor virtual.
8. **Bulletin Board Feature**: Mengadopsi fitur papan informasi dari `Claw3D` yang diubah ke visual 2D sebagai papan target *bounty* di tengah kantor.
9. **High-Speed Socket Sync**: Implementasi ulang `GatewayClient.ts` dari `Claw3D` ke Python untuk sinkronisasi pergerakan 1:1 antar worker di dalam kantor virtual.
10. **Data Normalization**: Menggunakan strategi `layoutSnapshot.ts` untuk memastikan konsistensi data kordinat (posisi X/Y worker) antar departemen.

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

21. **Strict Terminal Operators**: Worker tidak butuh model machine learning yang kompleks untuk otonomi tingkat tinggi. Tugas mereka 100% mengeksekusi perintah terminal berdasarkan *task* yang digenerate oleh Supervisor.
22. **Self-Reflection Recovery**: Worker akan menganalisa log error secara basic jika eksploitasi gagal dan meminta instruksi/task baru dari Supervisor.
23. **Defensive Swarm Intelligence**: Mode "Keroyokan" khusus untuk simulasi pertahanan (Defend) agar banyak worker bisa fokus memproteksi satu infrastruktur secara bersamaan.
24. **Smart Rate-Limiting**: Mengingat risiko IP ban pada Bug Bounty/CTF, worker diatur untuk tidak terlalu barbar (kecuali pada skenario *defense*).
25. **Wall of Fame**: Papan prestasi di dashboard untuk setiap temuan Critical bug atau flag CTF.
26. **Telegram Visual Reports**: Mengirimkan visualisasi (seperti Heatmap target) langsung ke Telegram Bos.
27. **Bulletin Board Loot**: Hasil eksploitasi (Loot/Flag) akan langsung ditampilkan di Papan Buletin dashboard.
28. **Socket Auto-Reconnect**: Sistem jabat tangan tangguh dari `Claw3D` untuk menjamin dashboard tidak terputus saat koneksi internet tidak stabil.
29. **Supervisor-Driven Pacing**: Supervisor memegang kendali penuh atas ritme serangan (Stealth vs Aggressive), kapan harus diam dan kapan harus nge-gas.
30. **Supervisor "The Brain"**: Supervisor secara otonom menentukan strategi, memecahnya menjadi ribuan task terminal kecil, dan mendistribusikannya ke worker.

31. **Exploit Sandbox Auto-Test**: Programmer Worker (The Armorer) selalu menjalankan test lokal di Docker/Sandbox setiap kali selesai membuat script Python eksploitasi, sebelum diserahkan ke Cyber Worker.
32. **Reverse Shell Listener (The Catcher)**: Satu worker khusus dialokasikan sebagai "Listener" (seperti Netcat/Metasploit) yang stand-by menunggu koneksi balik dari target, dan langsung menginfokan ke Telegram jika ada shell masuk.
33. **Wordlist Auto-Generator**: Programmer Worker secara dinamis meracik custom wordlist berdasarkan recon awal target, bukannya pakai wordlist generic seperti `rockyou.txt`.
34. **Colab Notebook Spawner**: Worker Bridge memiliki kemampuan untuk me-restart atau me-spawn Colab notebook baru via API jika resource limit tercapai atau IP terblokir.
35. **The "/nuke" Command**: Perintah darurat via Telegram untuk memutus semua koneksi, menghapus log sementara, dan menghancurkan environment (Anti-Forensic) secara instan.
36. **API Key Hot-Swap**: Automasi penggantian API Key OpenRouter oleh Finance Worker secara seamless tanpa menghentikan operasi jika terdeteksi adanya limit atau rate-limit dari provider LLM.
37. **Vulnerability PoC Archiver**: Setelah sukses eksploit, Management Worker merangkum langkah-langkah ke dalam Markdown PoC (Proof of Concept) yang rapi untuk report Bug Bounty.
38. **Telegram Approval Gates**: Untuk eksekusi yang sifatnya destruktif (misal: Drop Database, Mass Delete), Supervisor wajib meminta konfirmasi Yes/No via Telegram ke Commander.
39. **Decoy Traffic Generator**: Sebagian Cyber Worker ditugaskan untuk mengirimkan traffic normal (seperti bot biasa) ke target untuk menutupi jejak worker lain yang sedang melakukan eksploitasi sungguhan (Stealth).
40. **Office Desk Loot Stacking**: Secara visual di 2D Dashboard, semakin banyak flag/bounty yang didapat, meja Management Worker akan terlihat semakin dipenuhi oleh tumpukan "berkas/uang".

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


