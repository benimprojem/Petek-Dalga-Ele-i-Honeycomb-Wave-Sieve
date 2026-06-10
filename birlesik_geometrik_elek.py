def g_alt(L):
    return 8 * L ** 2 + 10 * L + 1

def f_sol_alt(L):
    return 9 * L ** 2 + 3 * L + 5

def dusman_asallari_uret_g(ust_sinir):
    """g(L) için Diskriminant 68 kuralına uyan asalları üretir."""
    dusmanlar = [5]
    # Basit bir tek sayı taraması (Asallık kontrolü yerine sadece modüler elek için üst sınır)
    for p in range(7, ust_sinir + 1, 2):
        # p'nin asal olup olmadığını test etmek yerine, 68'in mod p'deki durumuna bakıyoruz
        hedef_kalan = 68 % p
        for x in range(p):
            if (x * x) % p == hedef_kalan:
                dusmanlar.append(p)
                break
    return dusmanlar

def dusman_asallari_uret_f(ust_sinir):
    """f(L) için Diskriminant -171 kuralına uyan asalları üretir."""
    dusmanlar = [5]
    for p in range(7, ust_sinir + 1, 2):
        hedef_kalan = -171 % p
        for x in range(p):
            if (x * x) % p == hedef_kalan:
                dusmanlar.append(p)
                break
    return dusmanlar

def birlesik_geometrik_elek(max_layer):
    """
    ASALLIK KONTROLÜ YAPMAZ.
    Sadece geometrik ritimleri kullanarak iki hattın asallarını ayıklar ve kaydeder.
    """
    # Filtre üst sınırlarını polinomların maksimum değerlerine göre belirliyoruz
    maks_g = g_alt(max_layer)
    maks_f = f_sol_alt(max_layer)
    
    filtre_g = dusman_asallari_uret_g(int(maks_g ** 0.5) + 1)
    filtre_f = dusman_asallari_uret_f(int(maks_f ** 0.5) + 1)
    
    toplanan_asallar = set()  # Çakışmaları önlemek için set kullanıyoruz
    
    # --- 1. HAT: ALT KENAR (g) TARAMASI ---
    for L in range(1, max_layer + 1):
        sayi = g_alt(L)
        elenmeli_mi = False
        for p in filtre_g:
            if sayi % p == 0 and sayi > p:
                elenmeli_mi = True
                break
        if not elenmeli_mi:
            toplanan_asallar.add(sayi)
            
    # --- 2. HAT: SOL ALT KENAR (f) TARAMASI ---
    for L in range(1, max_layer + 1):
        sayi = f_sol_alt(L)
        elenmeli_mi = False
        for p in filtre_f:
            if sayi % p == 0 and sayi > p:
                elenmeli_mi = True
                break
        if not elenmeli_mi:
            toplanan_asallar.add(sayi)
            
    # Asalları sıralı listeye dönüştür
    sirali_asallar = sorted(list(toplanan_asallar))
    
    # VERİ KAYDETME ADIMI (Dosyaya yazım)
    dosya_adi = "petek_asallari.txt"
    with open(dosya_adi, "w", encoding="utf-8") as f:
        f.write(f"# İlk {max_layer} Katman İçin Üretilen Saf Petek Asalları\n")
        f.write(f"# Toplam Yakalanan Asal Sayısı: {len(sirali_asallar)}\n")
        for asal in sirali_asallar:
            f.write(f"{asal}\n")
            
    print(f"\n=== BİRLEŞİK GEOMETRİK ELEK RAPORU ===")
    print(f"Klasik asallık kontrolü (is_prime) KULLANILMADI.")
    print(f"Alt Kenar Filtre Genişliği    : {len(filtre_g)} asal dalgası")
    print(f"Sol Alt Kenar Filtre Genişliği: {len(filtre_f)} asal dalgası")
    print(f"Filtrelerden Sızmadan Geçen Toplam Saf Asal: {len(sirali_asallar)}")
    print(f"Veriler '{dosya_adi}' dosyasına başarıyla kaydedildi.")
    print("=" * 40)

# --- SÜREKLİ YENİ TEST DÖNGÜSÜ ---
print("Saf Geometrik Elek İstasyonu Hazır. Asallık testi devre dışı.")

while True:
    user_input = input("\nÜretim yapılacak katman derinliğini girin (Çıkış için 'q'): ")
    
    if user_input.lower() == 'q':
        print("Sistem kapatıldı.")
        break
        
    try:
        katman_siniri = int(user_input)
        if katman_siniri < 1:
            print("[Hata] Geçersiz katman.")
            continue
            
        birlesik_geometrik_elek(katman_siniri)
        
    except ValueError:
        print("[Hata] Lütfen geçerli bir tamsayı girin.")