import sys
import subprocess

def tampilkan_menu():
    while True:
        print("\n" + "="*55)
        print(" 🌟 TUGAS PENGOLAHAN CITRA DIGITAL (PCD) 🌟")
        print("="*55)
        print("  1. Soal 1: 4-Connectivity (Labeling Matriks)")
        print("  2. Soal 2: Image Sampling (Resize tanpa simpan)")
        print("  3. Soal 3: Kuantisasi, Histogram & PSNR/MSE")
        print("  0. Keluar dari Program")
        print("="*55)
        
        pilihan = input("Masukkan pilihan menu (0/1/2/3): ")
        
        if pilihan == '1':
            print("\n[>] Menjalankan Soal 1 (Connectivity)...")
            subprocess.run([sys.executable, "Soal_1.py"])
            
        elif pilihan == '2':
            print("\n[>] Menjalankan Soal 2 (Sampling)...")
            subprocess.run([sys.executable, "Soal_2.py"])
            
        elif pilihan == '3':
            print("\n[>] Menjalankan Soal 3 (Kuantisasi)...")
            subprocess.run([sys.executable, "Soal_3.py"])
            
        elif pilihan == '0':
            print("\n[+] Terima kasih! Menutup program...")
            break
            
        else:
            print("\n[-] Pilihan tidak valid. Silakan ketik angka 0, 1, 2, atau 3.")

if __name__ == "__main__":
    tampilkan_menu()