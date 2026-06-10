import numpy as np

def is_prime(n):
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0 or n % 3 == 0: return False
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0: return False
    return True

def katman_baslangiclarini_bul(max_layer):
    """Her katmandaki Sol Alt ve Alt kenarların İLK sayılarını ayıklar."""
    angles = np.radians([0, 60, 120, 180, 240, 300])
    directions = list(zip(np.cos(angles), np.sin(angles)))
    
    # 6n ± 1 dizisi
    sequence = []
    n = 1
    # Güvenli bir üst sınırla sayı üret
    while len(sequence) < max_layer * max_layer * 7:
        sequence.append(6 * n - 1)
        sequence.append(6 * n + 1)
        n += 1
        
    seq_idx = 0
    sol_alt_ilki = {}
    alt_ilki = {}
    
    for layer in range(1, max_layer + 1):
        for side in range(6):
            for step in range(layer):
                current_num = sequence[seq_idx]
                
                # Her katmanda kenarın İLK adımını yakala
                if side == 4 and step == 0:
                    sol_alt_ilki[layer] = current_num
                elif side == 5 and step == 0:
                    alt_ilki[layer] = current_num
                    
                seq_idx += 1
    return sol_alt_ilki, alt_ilki

def polinom_turet(veriler):
    """L=1, 2, 3 değerlerini kullanarak Ax^2 + Bx + C katsayılarını bulur."""
    # L = 1, 2, 3 için denklem matrisi kuruyoruz
    X = np.array([[1**2, 1, 1],
                  [2**2, 2, 1],
                  [3**2, 3, 1]])
    Y = np.array([veriler[1], veriler[2], veriler[3]])
    
    # Katsayıları çöz (A, B, C)
    A, B, C = np.linalg.solve(X, Y)
    return round(A), round(B), round(C)

# --- UYGULAMA BAŞLANGICI ---
print("Sistem kuruluyor, geometrik veriler analiz ediliyor...\n")
sol_alt_veri, alt_veri = katman_baslangiclarini_bul(100)

# Polinomları türet
A1, B1, C1 = polinom_turet(sol_alt_veri)
A2, B2, C2 = polinom_turet(alt_veri)

print("=== TÜRETİLEN POLİNOM FORMÜLLERİ ===")
print(f"Sol Alt Kenar Başlangıç Polinomu : f(L) = {A1}L² + ({B1})L + ({C1})")
print(f"Alt Kenar Başlangıç Polinomu     : g(L) = {A2}L² + ({B2})L + ({C2})")
print("====================================\n")

# Sürekli Test Döngüsü (Kullanıcı kapatana kadar yeni testleri bekler)
while True:
    print("-" * 50)
    user_input = input("Test etmek istediğiniz Katman Numarasını (L) girin (Çıkış için 'q'): ")
    
    if user_input.lower() == 'q':
        print("Test uygulaması kapatıldı.")
        break
        
    try:
        L = int(user_input)
        if L < 1 or L > 100:
            print("[Hata] L değeri 1 ile 100 arasında olmalıdır.")
            continue
            
        # Formül çıktıları
        hesaplanan_sol_alt = A1 * L**2 + B1 * L + C1
        hesaplanan_alt = A2 * L**2 + B2 * L + C2
        
        # Gerçek geometrik çıktılar ile karşılaştırma (Doğrulama)
        gercek_sol_alt = sol_alt_veri[L]
        gercek_alt = alt_veri[L]
        
        print(f"\n[Katman {L} Sonuçları]")
        print(f"-> Sol Alt Başlangıç Sayısı: {hesaplanan_sol_alt} | Gerçek: {gercek_sol_alt} | Asal mı?: {is_prime(hesaplanan_sol_alt)}")
        print(f"-> Alt Başlangıç Sayısı:    {hesaplanan_alt} | Gerçek: {gercek_alt} | Asal mı?: {is_prime(hesaplanan_alt)}")
        
        # Formülün kalibrasyon kontrolü
        if hesaplanan_sol_alt == gercek_sol_alt and hesaplanan_alt == gercek_alt:
            print("[✓] FORMÜL KUSURSUZ DOĞRULANDI: Geometri ile matematik tam uyumlu.")
        else:
            print("[X] UYARSIZLIK: Geometrik kayma tespit edildi.")
            
    except ValueError:
        print("[Hata] Lütfen geçerli bir tamsayı girin.")