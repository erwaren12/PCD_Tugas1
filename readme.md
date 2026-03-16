# 🌟 Tugas Pengolahan Citra Digital (PCD)

Repositori ini berisi implementasi algoritma Pengolahan Citra Digital menggunakan bahasa pemrograman Python dalam format **Jupyter Notebook**. Proyek ini mencakup analisis konektivitas matriks, *image sampling* (resize), dan evaluasi tingkat lanjut untuk kuantisasi citra menggunakan metrik pengukuran standar industri (MSE & PSNR).

## 👨‍💻 Profil Mahasiswa
* **Nama:** Alif
* **NPM:** 23424034
* **Program Studi:** Teknik Informatika
* **Universitas:** UNUSIDA

## 📁 Struktur Repositori
Proyek ini dikerjakan secara modular menggunakan Jupyter Notebook agar visualisasi data dan citra dapat langsung dilihat bersamaan dengan kode sumbernya:

* `Soal_1.ipynb` - Algoritma *Connected Component Labeling* untuk menghitung jumlah objek pada citra biner (matriks) berdasarkan 4-connectivity. Dilengkapi dengan visualisasi sebaran objek.
* `Soal_2.ipynb` - Proses *Image Sampling* (Downsampling) citra ke berbagai resolusi (512x512, 256x256, 128x128, 64x64) menggunakan interpolasi OpenCV.
* `Soal_3.ipynb` - Proses Kuantisasi Citra (8-bit, 4-bit, 2-bit) lengkap dengan visualisasi Histogram, serta kalkulasi nilai *Mean Squared Error* (MSE) dan *Peak Signal-to-Noise Ratio* (PSNR).
* `Image.jpg` - Citra uji coba yang digunakan dalam program.

## 🛠️ Pustaka (Library) yang Digunakan
Proyek ini bergantung pada beberapa pustaka eksternal Python:
* `numpy` - Untuk manipulasi array dan perhitungan matematis.
* `scipy` - Untuk fungsi *labeling* pada matriks.
* `opencv-python` (cv2) - Untuk membaca, memproses (*resize* & konversi warna), dan manipulasi citra.
* `matplotlib` - Untuk visualisasi hasil citra dan plot histogram.
* `ipykernel` & `notebook` - Lingkungan eksekusi Jupyter Notebook.

## 🚀 Cara Menjalankan Program

1. Pastikan Anda sudah menginstal ekstensi **Jupyter** di dalam Visual Studio Code atau menggunakan Jupyter Lab/Notebook melalui *browser*.
2. Pastikan semua pustaka yang dibutuhkan telah terinstal di *environment* Python Anda:
   ```bash
   pip install numpy scipy opencv-python matplotlib notebook ipykernel
