Tentu, ini adalah draft **README.md** yang profesional dan terstruktur, disesuaikan dengan struktur folder di screenshot dan deskripsi yang kamu berikan.

Silakan salin kode di bawah ini ke dalam file `README.md` kamu.

```markdown
# 🥗 Sistem Optimasi Menu MBG (Metode Big M)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Flask](https://img.shields.io/badge/Framework-Flask-green?style=flat&logo=flask)
![Status](https://img.shields.io/badge/Status-Active-success)

**Aplikasi berbasis web untuk menghitung optimasi porsi menu MBG (Makan Bergizi Gratis) berdasarkan anggaran dan standar gizi menggunakan algoritma Big M (Simplex).**

Project ini bertujuan untuk membantu pengambilan keputusan dalam menentukan kombinasi menu makanan yang memenuhi standar gizi (seperti protein, karbohidrat, lemak) dengan biaya yang paling optimal (minimum cost) menggunakan pendekatan *Operations Research*.

## 🔗 Live Demo
Coba aplikasi secara langsung di sini:
👉 **[https://metodebigm.pythonanywhere.com](https://metodebigm.pythonanywhere.com)**

---

## 🛠️ Teknologi yang Digunakan

Project ini dibangun menggunakan stack berikut:

* **Bahasa Pemrograman:** Python
* **Web Framework:** Flask
* **Komputasi Numerik:** NumPy & Pandas (Untuk manipulasi matriks dan data iterasi Simplex)
* **Web Server (Production):** Gunicorn
* **Frontend:** HTML5, CSS (Jinja2 Templates)

---

## 📂 Struktur Project

Berdasarkan struktur folder repository:

```text
PROGRAM METODE BIG M/
│
├── .venv/                 # Virtual Environment
├── templates/             # Folder tampilan (Frontend)
│   ├── about.html         # Halaman Tentang Aplikasi
│   ├── base.html          # Base layout (Navbar/Footer)
│   ├── home.html          # Halaman Utama
│   ├── input.html         # Form Input Data (Gizi/Harga)
│   └── result.html        # Halaman Hasil Optimasi
│
├── app.py                 # Main application file (Flask Routes)
├── big_m_solver.py        # Core Logic Algoritma Big M
├── requirements.txt       # Daftar pustaka/library
└── README.md              # Dokumentasi Project

```

---

## 🚀 Cara Menjalankan di Local (Installation)

Ikuti langkah-langkah ini untuk menjalankan project di komputer kamu sendiri:

1. **Clone Repository**
```bash
git clone [https://github.com/username-anda/repo-ini.git](https://github.com/username-anda/repo-ini.git)
cd "PROGRAM METODE BIG M"

```


2. **Buat Virtual Environment (Opsional tapi disarankan)**
```bash
# Untuk Windows
python -m venv .venv
.venv\Scripts\activate

# Untuk Mac/Linux
python3 -m venv .venv
source .venv/bin/activate

```


3. **Install Dependencies**
Pastikan kamu sudah menginstall semua library yang dibutuhkan:
```bash
pip install -r requirements.txt

```


4. **Jalankan Aplikasi**
```bash
python app.py

```


Aplikasi akan berjalan di `http://127.0.0.1:5000/`

---

## 📝 Cara Penggunaan

1. Buka halaman **Home** untuk melihat ringkasan aplikasi.
2. Masuk ke menu **Input Data** (atau *Hitung Optimasi*).
3. Masukkan variabel keputusan (jenis makanan), fungsi tujuan (minimasi biaya), dan fungsi kendala (kebutuhan gizi minimum).
4. Klik tombol **Hitung**.
5. Sistem akan memproses menggunakan algoritma Big M di `big_m_solver.py`.
6. Hasil porsi optimal dan total biaya akan ditampilkan di halaman **Result**.
