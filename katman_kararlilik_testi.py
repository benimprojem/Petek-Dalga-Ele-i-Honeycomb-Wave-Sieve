import numpy as np

def is_prime(n):
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0 or n % 3 == 0: return False
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0: return False
    return True

# Formüllerimiz
def f_sol_alt(L):
    return 9 * L**2 + 3 * L + 5

def g_alt(L):
    return 8 * L**2 + 10 * L + 1

def kararlilik_testi(baslangic_L, bitis_L):
    """Belirlenen aralıktaki katmanlar için kırılma analizi yapar."""
    sol_alt_asallar = 0
    alt_asallar = 0
    toplam_katman = bitis_L - baslangic_L + 1
    
    sol_alt_ilk_bileşik = None
    alt_ilk_bileşik = None
    
    for L in range(baslangic_L, bitis_L + 1):
        # Sayıları üret
        sayi_sol_alt = f_sol_alt(L)
        sayi_alt = g_alt(L)
        
        # Sol Alt Kontrol
        if is_prime(sayi_sol_alt):
            sol_alt_asallar += 1
        elif sol_alt_ilk_bileşik is None:
            sol_alt_ilk_bileşik = (L, sayi_sol_alt)
            
        # Alt Kontrol
        if is_prime(sayi_alt):
            alt_asallar += 1
        elif alt_ilk_bileşik is None:
            alt_ilk_bileşik = (L, sayi_alt)
            
    # Raporlama
    print(f"\n--- {baslangic_L} ile {bitis_L}. Katmanlar Arası Test Raporu ---")
    print(f"Toplam Test Edilen Katman: {toplam_katman}")
    print("-" * 50)
    
    print(f"[Sol Alt Kenar] f(L) = 9L² + 3L + 5")
    print(f"  -> Üretilen Asal Adedi: {sol_alt_asallar} / {toplam_katman}")
    print(f"  -> Asal Yoğunluk Oranı: %{(sol_alt_asallar / toplam_katman) * 100:.2f}")
    if sol_alt_ilk_bileşik:
        print(f"  -> İLK KIRILMA NOKTASI: Katman {sol_alt_ilk_bileşik[0]} (Sayı: {sol_alt_ilk_bileşik[1]})")
    else:
        print("  -> Bu aralıkta HİÇ KIRILMA OLMADI! Tüm sayılar asal.")
        
    print(f"\n[Alt Kenar] g(L) = 8L² + 10L + 1")
    print(f"  -> Üretilen Asal Adedi: {alt_asallar} / {toplam_katman}")
    print(f"  -> Asal Yoğunluk Oranı: %{(alt_asallar / toplam_katman) * 100:.2f}")
    if alt_ilk_bileşik:
        print(f"  -> İLK KIRILMA NOKTASI: Katman {alt_ilk_bileşik[0]} (Sayı: {alt_ilk_bileşik[1]})")
    else:
        print("  -> Bu aralıkta HİÇ KIRILMA OLMADI! Tüm sayılar asal.")
    print("-" * 50)

# --- SÜREKLİ ÇALIŞAN UYGULAMA DÖNGÜSÜ ---
print("=== POLİNOM KIRILMA NOKTASI TEST MERKEZİ ===")
print("Sistem hazır. Formüller: f(L)=9L²+3L+5 ve g(L)=8L²+10L+1")


def moduler_elek_testi(ust_sinir):
    # Başlangıçta tüm katmanları "Asal Adayı" (True) kabul et
    f_asallik = [True] * (ust_sinir + 1)
    g_asallik = [True] * (ust_sinir + 1)
    
    # L=0 indeksini devre dışı bırakıyoruz
    f_asallik[0] = g_asallik[0] = False 
    
    # BİLİNEN RİTMİK ELEME ADIMLARI
    # 1. Sol Alt Kenarı (f) 5'in ritmiyle ele
    for L in range(1, ust_sinir + 1):
        if L % 5 == 3 or L % 5 == 1:
            if 9*L**2 + 3*L + 5 > 5: # Kendisi hariç katları ele
                f_asallik[L] = False
                
    # 2. Alt Kenarı (g) 13'ün ritmiyle ele
    for L in range(1, ust_sinir + 1):
        if L % 13 == 4 or L % 13 == 8:
            if 8*L**2 + 10*L + 1 > 13: # Kendisi hariç katları ele
                g_asallik[L] = False
                
    # Sonuçları raporla (İlk 20 katman için ritmik temizlik)
    print(f"--- Sadece 5 ve 13 Ritimleri Elendikten Sonra (İlk 20 Katman) ---")
    print("Katman | f(L) Durumu       | g(L) Durumu")
    print("-" * 45)
    for L in range(1, 41):
        f_durum = "ADAY" if f_asallik[L] else "ELENDİ (5'in katı)"
        g_durum = "ADAY" if g_asallik[L] else "ELENDİ (13'ün katı)"
        print(f" L={L:2d}  | {f_durum:17s} | {g_durum}")

moduler_elek_testi(200)

while True:
    print("\n[Yeni Test Bekleniyor]")
    user_input = input("Test etmek istediğiniz ÜST KATMAN sınırını girin (Örn: 100, 1000) veya çıkış için 'q': ")
    
    if user_input.lower() == 'q':
        print("Uygulama sonlandırıldı.")
        break
        
    try:
        bitis = int(user_input)
        if bitis < 1:
            print("[Hata] Lütfen 1'den büyük bir katman sayısı girin.")
            continue
            
        # 1. katmandan kullanıcının istediği katmana kadar kararlılığı ölç
        kararlilik_testi(1, bitis)
        
    except ValueError:
        print("[Hata] Geçersiz giriş. Lütfen bir tamsayı yazın.")