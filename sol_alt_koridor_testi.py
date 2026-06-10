def is_prime(n):
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0 or n % 3 == 0: return False
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0: return False
    return True

def f_sol_alt(L):
    return 9 * L**2 + 3 * L + 5

def sol_alt_potansiyel_dusmanlari_uret(ust_sinir):
    """Diskriminant -171 kuralına uyan asalları dinamik üretir."""
    dusmanlar = [5] # 5 özel olarak dahil edilir
    for p in range(7, ust_sinir + 1, 2):
        if is_prime(p):
            # Mod p tabanında -171'in karesel kalan kontrolü
            # Python'da negatif mod yönetimini garantiye almak için (-171 % p) kullanılır
            hedef_kalan = -171 % p
            for x in range(p):
                if (x * x) % p == hedef_kalan:
                    dusmanlar.append(p)
                    break
    return dusmanlar

def sol_alt_koridor_testi(max_layer):
    """
    Sol Alt Kenar Kalkanı: -171 diskriminant köklerini 
    otomatik olarak tarar ve eler.
    """
    maks_sayi = f_sol_alt(max_layer)
    asal_filtresi = sol_alt_potansiyel_dusmanlari_uret(int(maks_sayi**0.5) + 1)
    
    aday_sayisi = 0
    gercek_asal_sayisi = 0
    kacirma_noktasi = None
    
    for L in range(1, max_layer + 1):
        sayi = f_sol_alt(L)
        elenmeli_mi = False
        
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
            
    print(f"\n=== SOL ALT KENAR OTOMATİK TAHMİNLİ KALKAN (İlk {max_layer} Katman) ===")
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
        print("Müjde! Sol alt hat üzerinde de %100 saf asal koridoru başarıyla üretildi.")
    print("=" * 65)

# --- SÜREKLİ YENİ TEST DÖNGÜSÜ ---
print("Sol Alt Kenar için -171 koruma kalkanı devrede.")

while True:
    user_input = input("\nTest etmek istediğiniz katman derinliğini girin (Örn: 1000) veya çıkış için 'q': ")
    
    if user_input.lower() == 'q':
        print("Sistem kapatıldı.")
        break
        
    try:
        katman_siniri = int(user_input)
        if katman_siniri < 1:
            print("[Hata] Geçersiz katman.")
            continue
            
        sol_alt_koridor_testi(katman_siniri)
        
    except ValueError:
        print("[Hata] Lütfen tamsayı girin.")