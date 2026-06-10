import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import numpy as np

# 1. Klasik ve Hızlı Asallık Testi
def is_prime(n):
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0 or n % 3 == 0: return False
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0: return False
    return True

# 2. Spiral Üretimi ve Bölgesel Veri Yakalama
def generate_and_analyze_spiral(target_count):
    coords = {}
    sol_alt_sayilar = []
    alt_sayilar = []
    
    # 60 derece dönüşlü yön vektörleri
    # 0: Sağ, 1: Sağ Üst, 2: Sol Üst, 3: Sol, 4: Sol Alt, 5: Sağ Alt
    angles = np.radians([0, 60, 120, 180, 240, 300])
    directions = list(zip(np.cos(angles), np.sin(angles)))
    
    # 6n ± 1 sayı dizisini oluştur
    sequence = []
    n = 1
    while len(sequence) < target_count:
        sequence.append(6 * n - 1)
        sequence.append(6 * n + 1)
        n += 1
        
    x, y = 0.0, 0.0
    dir_idx = 0
    seq_idx = 0
    layer = 1
    
    while seq_idx < target_count:
        for side in range(6): # 6 kenar (0-5 arası)
            for step in range(layer):
                if seq_idx >= target_count: break
                
                current_num = sequence[seq_idx]
                coords[current_num] = (x, y)
                
                # İTTİFAK EDEN KENARLARI YAKALA (Görseldeki alt ve sol alt bölgeler)
                # side == 3 son adımları veya side == 4 (Sol Alt Kenar adımları)
                if side == 4:
                    sol_alt_sayilar.append(current_num)
                # side == 5 (Alt / Sağ Alt Kenar adımları)
                elif side == 5:
                    alt_sayilar.append(current_num)
                
                x += directions[dir_idx][0]
                y += directions[dir_idx][1]
                seq_idx += 1
                
            dir_idx = (dir_idx + 1) % 6
        layer += 1
        
    return coords, sol_alt_sayilar, alt_sayilar

# 3. Hesaplamayı Başlat
SAYI_ADEDI = 20000
veriler, sol_alt_hattı, alt_hattı = generate_and_analyze_spiral(SAYI_ADEDI)

# 4. Matematiksel Polinom Matrisi Analizi
print("=== GEOMETRİK POLİNOM ANALİZİ ===")

def hat_analizi(hat_adi, sayi_listesi):
    print(f"\n--- {hat_adi} İncelemesi ---")
    filtreli_asallar = [n for n in sayi_listesi if is_prime(n)]
    print(f"Bu hattaki toplam nokta: {len(sayi_listesi)}, Asal adedi: {len(filtreli_asallar)}")
    print(f"Asal Oranı: %{(len(filtreli_asallar)/len(sayi_listesi))*100:.2f}")
    
    # Sıralı örnekler
    yakin_sayilar = sorted(sayi_listesi)[:12]
    print(f"Hattın ilk sayıları: {yakin_sayilar}")
    
    # Ardışık eleman farkları (Birinci Fark)
    farklar = [yakin_sayilar[i+1] - yakin_sayilar[i] for i in range(len(yakin_sayilar)-1)]
    print(f"Ardışık Farklar (D_1): {farklar}")
    
    # Farkların farkı (İkinci Fark -> Sabit çıkarsa Polinom derecesi 2'dir)
    if len(farklar) > 1:
        ikinci_farklar = [farklar[i+1] - farklar[i] for i in range(len(farklar)-1)]
        print(f"Farkların Farkı (D_2): {ikinci_farklar}")

hat_analizi("SOL ALT KENAR", sol_alt_hattı)
hat_analizi("ALT KENAR", alt_hattı)

# 5. Görseli Yeniden Çizip Sağlama Alma
fig, ax = plt.subplots(figsize=(12, 12))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

x_primes, y_primes = [], []
x_composites, y_composites = [], []

for num, (x, y) in veriler.items():
    if is_prime(num):
        x_primes.append(x)
        y_primes.append(y)
    else:
        x_composites.append(x)
        y_composites.append(y)

ax.scatter(x_composites, y_composites, s=1, c='#1A1A1A', marker='.', alpha=0.4)
ax.scatter(x_primes, y_primes, s=6, c='cyan', marker='o', alpha=0.9)
ax.axis('off')
plt.tight_layout()

dosya_adi = 'petek_analiz_sonuc.png'
plt.savefig(dosya_adi, dpi=300, facecolor='black')
print(f"\nGörsel doğrulama için '{dosya_adi}' adıyla kaydedildi.")