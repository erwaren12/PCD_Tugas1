import cv2
import matplotlib.pyplot as plt
from pathlib import Path

def view_image_sampling(image_name: str) -> None:
    img_path = Path(image_name)
    
    if not img_path.is_file():
        print(f"[-] Waduh, file '{image_name}' tidak ditemukan di folder ini.")
        return

    try:
        img = cv2.imread(str(img_path))
        print(f"[+] Berhasil memuat: {img_path.name}")
        
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        sizes = [512, 256, 128, 64]
        
        plt.figure(figsize=(15, 6))
        plt.suptitle(f"Analisis Sampling Citra: {img_path.name}", 
                     fontsize=18, fontweight='bold', color='navy')

        for i, size in enumerate(sizes):
            resized = cv2.resize(img_rgb, (size, size), interpolation=cv2.INTER_AREA)
            
            ax = plt.subplot(1, 4, i + 1)
            ax.imshow(resized)
            
            title_text = f"Resolusi: {size}x{size}"
            ax.set_title(title_text, fontsize=12, pad=10, 
                         bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))
            ax.axis('off')
            
            print(f"[>] Memproses dan menampilkan resolusi: {size}x{size}")

        plt.tight_layout()
        print("\n[+] Eksekusi Selesai! Menampilkan grafik di layar...")
        plt.show()

    except Exception as e:
        print(f"[-] Terjadi kesalahan sistem saat memproses gambar:\n    {e}")

if __name__ == "__main__":
    file_gambar = 'Image.jpg' 
    view_image_sampling(file_gambar)