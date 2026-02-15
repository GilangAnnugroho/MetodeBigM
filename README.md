

```markdown
<div align="center">

# 🥗 OPTIMASI MENU MBG
**Sistem Pendukung Keputusan Penentuan Porsi Makan Bergizi Gratis**

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

<p align="center">
  <b>Solusi Cerdas Pemenuhan Gizi:</b><br>
  Menghitung kombinasi menu makanan optimal berdasarkan anggaran dan standar gizi<br>
  menggunakan <i>Algoritma Big M (Simplex) — Cepat & Akurat.</i>
</p>

[Fitur Utama](#-fitur-unggulan) • [Teknologi](#-teknologi) • [Instalasi](#-panduan-instalasi-cepat) • [Demo](#-akses-demo)

</div>

---

## 🔳 Tentang Aplikasi

**Sistem Optimasi Menu MBG** adalah solusi perangkat lunak berbasis web yang dirancang khusus untuk nutrisionis dan penyedia layanan katering program *Makan Bergizi Gratis*. Sistem ini mentransformasi perhitungan manual menjadi digital, memastikan setiap porsi memenuhi standar gizi (Protein, Karbohidrat, Lemak) dengan biaya produksi yang paling efisien (minimum cost) menggunakan pendekatan *Operations Research*.

---

## 🌟 Fitur Unggulan

| Modul | Deskripsi & Fungsionalitas |
| :--- | :--- |
| **📝 Input & Kendala** | • **Manajemen Variabel:** Input dinamis untuk jenis makanan & harga bahan.<br>• **Fleksibilitas Constraint:** Atur batasan gizi minimum/maksimum sesuai kebutuhan (`Constraint`).<br>• **Validasi Data:** Pengecekan input otomatis sebelum diproses. |
| **🧮 Big M Engine** | • **Algoritma Presisi:** Implementasi metode Big M untuk menangani kendala $\ge$ dan $=$.<br>• **Matriks Otomatis:** Konversi model matematika ke tabel simpleks secara *backend*.<br>• **Iterasi Cepat:** Proses perhitungan optimasi dalam hitungan detik. |
| **📊 Analisa Hasil** | • **Solusi Optimal:** Menampilkan jumlah porsi eksak untuk setiap menu.<br>• **Kalkulasi Biaya:** Total anggaran termurah yang memenuhi syarat gizi.<br>• **Status Solver:** Indikator visual apakah solusi *feasible* atau *infeasible*. |

---

## 🛠 Teknologi

Project ini dibangun menggunakan fondasi teknologi Python modern yang powerful untuk komputasi numerik:

* **Backend Core:** `Flask 3.0` (Microframework Python)
* **Computational:** `NumPy` & `Pandas` (Matrix Operations)
* **Frontend Asset:** `HTML5`, `CSS3` (Jinja2 Templates)
* **Web Server:** `Gunicorn` (Production Ready)
* **Deployment:** `PythonAnywhere`

---

## 🚀 Panduan Instalasi Cepat

Ikuti langkah-langkah berikut untuk menjalankan project di local environment Anda:

### 1. Persiapan Awal
Pastikan komputer Anda sudah terinstall: `Python >= 3.x` dan `Git`.

### 2. Clone & Install Dependencies
Salin repository dan install library yang dibutuhkan:

```bash
# Clone repository
git clone [https://github.com/USERNAME-KAMU/repo-metode-bigm.git](https://github.com/USERNAME-KAMU/repo-metode-bigm.git)

# Masuk ke direktori project
cd "PROGRAM METODE BIG M"

# Install Dependencies
pip install -r requirements.txt

```

### 3. Konfigurasi Environment (Opsional)

Disarankan menggunakan virtual environment agar library terisolasi:

```bash
# Buat Virtual Environment (Windows)
python -m venv .venv
.venv\Scripts\activate

# Buat Virtual Environment (Mac/Linux)
python3 -m venv .venv
source .venv/bin/activate

```

### 4. Menjalankan Server

Jalankan perintah berikut untuk memulai aplikasi Flask:

```bash
# Jalankan aplikasi
python app.py

```

🚀 **Aplikasi siap diakses di:** `http://127.0.0.1:5000`

---

## 📂 Struktur Direktori Utama

Berikut adalah peta struktur folder untuk memudahkan navigasi kode:

```text
PROGRAM METODE BIG M/
├── .venv/                 # 🔒 Environment Python
├── templates/             # 🎨 Tampilan Frontend
│   ├── base.html          # Layout Utama (Navbar/Footer)
│   ├── input.html         # Form Input Variabel & Kendala
│   ├── result.html        # Halaman Hasil Optimasi
│   └── home.html          # Halaman Depan
├── app.py                 # 🔗 Routing & Controller Flask
├── big_m_solver.py        # 🧠 Core Logic Algoritma Big M
├── requirements.txt       # 📦 Daftar Library
└── README.md              # 📖 Dokumentasi Project

```

---

## 👤 Akses Demo

Anda dapat mencoba aplikasi secara langsung tanpa instalasi melalui tautan berikut:

| Platform | Link Akses | Status |
| --- | --- | --- |
| **PythonAnywhere** | **[metodebigm.pythonanywhere.com](https://metodebigm.pythonanywhere.com)** | 🟢 Online |

---

## 🤝 Kontribusi

Kami sangat terbuka untuk kolaborasi! Jika Anda ingin berkontribusi:

1. **Fork** repository ini.
2. Buat branch fitur baru: `git checkout -b fitur-algoritma-baru`.
3. Commit perubahan: `git commit -m 'Menambahkan fitur visualisasi grafik'`.
4. Push ke branch: `git push origin fitur-algoritma-baru`.
5. Submit **Pull Request**.

---

<div align="center">

**OPTIMASI MENU MBG** © 2026 • Dilindungi oleh Lisensi [MIT](https://opensource.org/licenses/MIT).

<small>Dibuat dengan ❤️ oleh Mahasiswa Teknik Informatika UMC.</small>

</div>

```

```
