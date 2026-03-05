import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import math

def calculate_metrics(original, compressed):
    """Fungsi untuk menghitung Mean Squared Error (MSE) dan PSNR"""
    mse = np.mean((original.astype("float") - compressed.astype("float")) ** 2)
    if mse == 0:
        return 0, float('inf') 
    max_pixel = 255.0
    psnr = 20 * math.log10(max_pixel / math.sqrt(mse))
    return mse, psnr

def view_quantization(image_name: str) -> None:
    img_path = Path(image_name)
    
    if not img_path.is_file():
        print(f"[-] Error: File '{image_name}' tidak ditemukan.")
        return

    try:
        img_gray = cv2.imread(str(img_path), cv2.IMREAD_GRAYSCALE)
        print(f"[+] Memulai Analisis Kuantisasi Mendalam pada: {img_path.name}\n")
        
        bits_to_test = [8, 4, 2]
        
        plt.figure(figsize=(18, 9))
        plt.suptitle(f"Evaluasi Kuantisasi Citra dengan PSNR & MSE: {img_path.name}", 
                     fontsize=20, fontweight='heavy', color='black')

        for i, bit in enumerate(bits_to_test):
            levels = 2 ** bit
            
            if bit == 8:
                quantized_img = img_gray
                mse, psnr = 0, float('inf')
                title_text = f"Citra Asli (8-bit)\n256 Level Keabuan\nMSE: 0 | PSNR: \u221E dB"
            else:
                step = 256 / levels
                quantized_img = (np.floor(img_gray / step) * step).astype(np.uint8)
                mse, psnr = calculate_metrics(img_gray, quantized_img)
                title_text = f"Kuantisasi {bit}-bit ({levels} Level)\nMSE: {mse:.2f} | PSNR: {psnr:.2f} dB"
            
            if psnr == float('inf'):
                psnr_display = "Sempurna (\u221E)"
            else:
                psnr_display = f"{psnr:.2f} dB"
                
            print(f"[{bit}-bit] Diproses | Level: {levels:<3} | Error (MSE): {mse:<7.2f} | Kualitas (PSNR): {psnr_display}")
            
            ax_img = plt.subplot(2, 3, i + 1)
            ax_img.imshow(quantized_img, cmap='gray', vmin=0, vmax=255)
            box_color = '#e8f5e9' if bit == 8 else ('#fff3e0' if bit == 4 else '#ffebee')
            ax_img.set_title(title_text, fontsize=12, pad=12, 
                             bbox=dict(facecolor=box_color, alpha=0.9, edgecolor='silver'))
            ax_img.axis('off')
            
            ax_hist = plt.subplot(2, 3, i + 4)
            ax_hist.hist(quantized_img.ravel(), bins=256, range=[0, 256], color='steelblue', edgecolor='black', linewidth=0.5)
            ax_hist.set_title(f"Distribusi Piksel {bit}-bit", fontsize=11, fontweight='bold')
            ax_hist.set_xlabel("Intensitas (0-255)", fontsize=9)
            ax_hist.set_ylabel("Jumlah Piksel", fontsize=9)
            ax_hist.grid(axis='y', linestyle='--', alpha=0.7)

        plt.tight_layout()
        print("\n[+] Analisis Selesai! Menampilkan grafik di layar...")
        plt.show()

    except Exception as e:
        print(f"[-] Fatal Error:\n    {e}")

if __name__ == "__main__":
    file_gambar = 'Image.jpg' 
    view_quantization(file_gambar)