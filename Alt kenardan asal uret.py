def is_prime(n):
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0 or n % 3 == 0: return False
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0: return False
    return True

def g_alt(L):
    return 8 * L**2 + 10 * L + 1

def potansiyel_dusman_asallari_uret(ust_sinir):
    """Diskriminant 68 kuralına uyan tüm asalları dinamik üretir."""
    dusmanlar = [5] # 5 özel kök olarak dahil edilir
    for p in range(7, ust_sinir + 1, 2):
        if is_prime(p):
            hedef_kalan = 68 % p
            for x in range(p):
                if (x * x) % p == hedef_kalan:
                    dusmanlar.append(p)
                    break
    return dusmanlar

def korumali_koridor_testi(max_layer):
    """
    Nihai Akıllı Kalkan: Diskriminantı 68 olan asalların 
    tüm aktif modüler köklerini otomatik olarak eler.
    """
    # Güvenli bir asal tarama sınırı belirliyoruz (O katmandaki maksimum sayıya göre)
    maks_sayi = g_alt(max_layer)
    asal_filtresi = potansiyel_dusman_asallari_uret(int(maks_sayi**0.5) + 1)
    
    aday_sayisi = 0
    gercek_asal_sayisi = 0
    kacirma_noktasi = None
    
    for L in range(1, max_layer + 1):
        sayi = g_alt(L)
        elenmeli_mi = False
        
        # Akıllı elek: Sadece bizi vurabilecek asalların mod köklerine bakar
        for p in asal_filtresi:
            if sayi % p == 0 and sayi > p:
                elenmeli_mi = True
                break
                
        if elenmeli_mi:
            continue
            
        aday_sayisi += 1
        if is_prime(sayi):
            gercek_asal_sayisi += 1
        elif kacirma_noktasi is None:
            kacirma_noktasi = (L, sayi)
            
    print(f"\n=== ALT KENAR OTOMATİK TAHMİNLİ KALKAN (İlk {max_layer} Katman) ===")
    print(f"Aktif Filtre Edilen Zararlı Asal Sayısı: {len(asal_filtresi)}")
    print(f"Kalan Aday Sayısı: {aday_sayisi}")
    print(f"Gerçek Asal Sayısı: {gercek_asal_sayisi}")
    if aday_sayisi > 0:
        print(f"Nihai Asallık Kalitesi: %{(gercek_asal_sayisi / aday_sayisi) * 100:.2f}")
    if kacirma_noktasi:
        n = kacirma_noktasi[1]
        p_factor = next(i for i in range(2, n) if n % i == 0)
        print(f"Sistemi Delen Bir Sonraki Kaçak: Katman {kacirma_noktasi[0]} (Sayı: {n}) -> Çarpanı: {p_factor}")
    else:
        print("Müjde! Bu katman derinliğinde akıllı kalkan %100 saf asal koridoru üretti.")
    print("=" * 65)

# --- SÜREKLİ YENİ TEST DÖNGÜSÜ ---
print("Deterministik Akıllı Kalkan Aktif. Matematiksel tahminleyici devrede.")

while True:
    user_input = input("\nTest etmek istediğiniz katman derinliğini girin (Örn: 100, 1000) veya çıkış için 'q': ")
    
    if user_input.lower() == 'q':
        print("Sistem kapatıldı.")
        break
        
    try:
        katman_siniri = int(user_input)
        if katman_siniri < 1:
            print("[Hata] Geçersiz katman.")
            continue
            
        korumali_koridor_testi(katman_siniri)
        
    except ValueError:
        print("[Hata] Lütfen tamsayı girin.")