<div align="center">

# 🥗 SISTEM OPTIMASI MENU MBG (BIG M)
**Decision Support System for Nutritious Meal Distribution Optimization**

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

<p align="center">
  <b>Implementasi Riset Operasi Modern:</b><br>
  Optimasi porsi menu Makan Bergizi Gratis (MBG) menggunakan <i>Linear Programming</i><br>
  dengan pendekatan <i>Metode Big M (Simplex)</i> untuk pemenuhan gizi maksimal & biaya efisien.
</p>

</div>

---

## 📖 Tentang Proyek

**Sistem Optimasi Menu MBG** adalah aplikasi pendukung keputusan (*Decision Support System*) yang dirancang khusus untuk membantu institusi pendidikan atau penyedia katering dalam merencanakan distribusi makanan bergizi bagi siswa. 

Aplikasi ini menyelesaikan kompleksitas penentuan jumlah porsi yang ideal di tengah keterbatasan anggaran pemerintah, variasi kebutuhan gizi (kalori, protein, lemak), serta jumlah siswa yang dinamis. Dengan mesin *solver* berbasis **Metode Big M**, sistem ini menjamin solusi matematis yang paling akurat untuk setiap parameter yang diberikan.

---

## 🌟 Fitur Unggulan

| Modul | Deskripsi & Fungsionalitas |
| :--- | :--- |
| **🧮 Big M Solver Engine** | Implementasi murni algoritma Simplex Big M untuk menangani kendala bertipe $\ge$ dan $=$. |
| **🔄 Auto-Calculated RHS** | Menghitung otomatis *Right-Hand Side* (Batas Kebutuhan) dari (Standar per Siswa × Jumlah Siswa). |
| **📈 Multi-Objective Analysis** | Mendukung dua mode: **Minimasi Biaya** (Efisiensi) atau **Maksimasi Porsi** (Kuantitas). |
| **⚖️ Weight Analysis** | Perhitungan berat porsi akhir yang diterima siswa (gram) berdasarkan hasil pencampuran menu optimal. |
| **📜 Transparent Solver Logs** | Visualisasi langkah-demi-langkah tabel Simplex (Tableau) untuk audit perhitungan matematis. |

---

## 🧠 Alur Logika Optimasi

Sistem memodelkan permasalahan MBG ke dalam bentuk standar Linear Programming:

1. **Variabel Keputusan ($X_n$):** Jumlah porsi untuk setiap menu yang tersedia.
2. **Fungsi Tujuan:** * Minimasi: $\min Z = \sum (cost_j \cdot X_j)$
   * Maksimasi: $\max Z = \sum X_j$
3. **Fungsi Kendala:**
   * Kebutuhan Gizi: $\sum (gizi_j \cdot X_j) \ge standar\_total$
   * Kapasitas Anggaran: $\sum (cost_j \cdot X_j) \le budget$
   * Non-negativitas: $X_j \ge 0$


---

## 🛠 Teknologi

Dibangun menggunakan teknologi pilihan yang fokus pada performa komputasi dan kemudahan akses web:

* **Backend Core:** `Python 3.10+`
* **Computational Library:** `NumPy` (Optimasi Matriks) & `Pandas` (Struktur Data Log)
* **Web Framework:** `Flask 3.0` (Routing & Templating)
* **Frontend:** `Bootstrap 5.3` & `Jinja2` (Responsive Design)
* **Production Server:** `Gunicorn` (WSGI Server)

---

## 📂 Struktur Direktori

```text
PROGRAM METODE BIG M/
├── app.py                 # 🎮 Flask Controller (Routing & Logic Parsing)
├── big_m_solver.py        # 🧠 Core Algoritma Big M & Simplex Solver
├── requirements.txt       # 📦 Dependencies (flask, numpy, pandas, gunicorn)
├── templates/             # 🎨 UI Design (Jinja2)
│   ├── base.html          # Layout Master
│   ├── home.html          # Landing Page
│   ├── input.html         # Form Parameter & Kendala Dinamis
│   ├── result.html        # Dashboard Hasil & Log Iterasi
│   └── about.html         # Dokumentasi Metodologi
└── static/                # 🖼️ Assets (CSS, Image)

```

---

## 🚀 Panduan Instalasi

Ikuti langkah-langkah berikut untuk menjalankan sistem di lingkungan lokal:

### 1. Persiapan Environment

```bash
# Clone repository
git clone [https://github.com/USERNAME/repo-metode-bigm.git](https://github.com/USERNAME/repo-metode-bigm.git)
cd "PROGRAM METODE BIG M"

# Membuat virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

```

### 2. Install Dependensi

```bash
pip install -r requirements.txt

```

### 3. Jalankan Aplikasi

```bash
python app.py

```

Akses sistem melalui browser di: `http://127.0.0.1:5000`

---

## 📊 Hasil & Rekomendasi

Sistem ini memberikan *output* yang sangat mendetail bagi pengambil keputusan:

* **Analisis Baseline vs Aktual:** Perbandingan gizi sebelum dan sesudah optimasi per siswa.
* **Informasi Berat Porsi:** Estimasi berat makanan yang akan diterima setiap siswa secara adil.
* **Log Matematis:** Setiap iterasi pivot ditunjukkan untuk keperluan validasi data.

---

## 👤 Akses Demo

Aplikasi ini telah dideploy dan dapat diakses secara langsung melalui:

| Platform | Link Akses | Status |
| --- | --- | --- |
| **PythonAnywhere** | **[metodebigm.pythonanywhere.com](https://metodebigm.pythonanywhere.com)** | 🟢 Online |

---

<div align="center">

**Sistem Optimasi Menu MBG** © 2026 • Dilindungi oleh Lisensi [MIT](https://opensource.org/licenses/MIT).

</div>
