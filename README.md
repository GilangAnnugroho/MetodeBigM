
```markdown
<div align="center">

# 🥗 OPTIMASI MENU MBG (BIG M)
**Sistem Pendukung Keputusan Penentuan Porsi Makan Bergizi Gratis**

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

<p align="center">
  <b>Solusi Cerdas Pemenuhan Gizi:</b><br>
  Menghitung kombinasi menu makanan optimal berdasarkan anggaran dan standar gizi<br>
  menggunakan <i>Algoritma Big M (Simplex).</i>
</p>

[Fitur Utama](#-fitur-unggulan) • [Teknologi](#-teknologi) • [Instalasi](#-panduan-instalasi-cepat) • [Live Demo](#-akses-demo)

</div>

---

## 📖 Tentang Aplikasi

**Sistem Optimasi Menu MBG** adalah aplikasi berbasis web yang dirancang untuk membantu nutrisionis atau penyedia layanan katering dalam program *Makan Bergizi Gratis*. Sistem ini menerapkan metode *Operations Research* (Linear Programming) untuk meminimalkan biaya produksi per porsi tanpa mengurangi standar nilai gizi (Protein, Karbohidrat, Lemak, dll) yang telah ditetapkan.

---

## 🌟 Fitur Unggulan

| Modul | Deskripsi & Fungsionalitas |
| :--- | :--- |
| **📝 Input Variabel & Kendala** | • **Fleksibilitas Data:** Input bahan makanan (variabel keputusan) dan harga secara dinamis.<br>• **Batasan Gizi:** Tentukan batasan minimum/maksimum nutrisi sebagai fungsi kendala (`Constraint`). |
| **🧮 Big M Solver Engine** | • **Algoritma Presisi:** Menggunakan metode Big M untuk menangani kendala "lebih besar dari" ($\ge$) dan "sama dengan" ($=$).<br>• **Matriks Otomatis:** Konversi input user menjadi tabel simpleks secara *backend*. |
| **📊 Analisa Hasil** | • **Solusi Optimal:** Menampilkan jumlah porsi eksak untuk setiap jenis makanan.<br>• **Total Cost:** Kalkulasi biaya termurah yang memenuhi semua syarat gizi.<br>• **Status Solver:** Indikator apakah solusi *feasible* atau *infeasible*. |

---

## 🛠 Teknologi

Project ini dibangun menggunakan stack Python yang powerful untuk komputasi numerik:

* **Backend Framework:** `Flask` (Microframework Python)
* **Computational Core:** `NumPy` & `Pandas` (Matriks & Data Processing)
* **Web Server:** `Gunicorn` (Production Ready)
* **Frontend:** `HTML5`, `CSS3`, `Jinja2 Templates`
* **Deployment:** `PythonAnywhere`

---

## 🚀 Panduan Instalasi Cepat

Ikuti langkah-langkah berikut untuk menjalankan project di local environment Anda:

### 1. Persiapan Awal
Pastikan komputer Anda sudah terinstall: `Python >= 3.x` dan `Git`.

### 2. Clone & Setup Environment
Salin repository dan buat virtual environment agar library terisolasi:

```bash
# Clone repository
git clone [https://github.com/USERNAME-KAMU/repo-metode-bigm.git](https://github.com/USERNAME-KAMU/repo-metode-bigm.git)

# Masuk ke direktori project
cd "PROGRAM METODE BIG M"

# Buat Virtual Environment (Windows)
python -m venv .venv
.venv\Scripts\activate

# Buat Virtual Environment (Mac/Linux)
python3 -m venv .venv
source .venv/bin/activate

```

### 3. Install Dependencies

Install library matematika dan framework yang dibutuhkan:

```bash
pip install -r requirements.txt

```

*Pastikan `requirements.txt` berisi: Flask, numpy, pandas, gunicorn.*

### 4. Menjalankan Server

Jalankan aplikasi Flask:

```bash
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

Kami sangat terbuka untuk kolaborasi! Jika Anda ingin mengembangkan fitur baru:

1. **Fork** repository ini.
2. Buat branch fitur baru: `git checkout -b fitur-algoritma-baru`.
3. Commit perubahan: `git commit -m 'Menambahkan fitur visualisasi grafik'`.
4. Push ke branch: `git push origin fitur-algoritma-baru`.
5. Submit **Pull Request**.

---

<div align="center">

**OPTIMASI MENU MBG** © 2026 • Dilindungi oleh Lisensi [MIT](https://opensource.org/licenses/MIT).

</div>
