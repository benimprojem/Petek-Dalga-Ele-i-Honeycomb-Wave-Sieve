def yeni_dalga_boyu_hesapla(asal_carpan):
    g_kokler = []
    
    # Alt kenar formülünün (g) bu asal tabanındaki köklerini bul
    for L in range(asal_carpan):
        if (8 * L**2 + 10 * L + 1) % asal_carpan == 0:
            g_kokler.append(L)
            
    print(f"=== {asal_carpan} Asalı İçin Alt Kenar Koruma Analizi ===")
    if len(g_kokler) == 2:
        # İki kök arasındaki zıplama adımlarını hesapla
        fark_1 = g_kokler[1] - g_kokler[0] - 1
        fark_2 = asal_carpan - g_kokler[1] + g_kokler[0] - 1
        print(f"-> {asal_carpan}'nin Zıplama Ritmi: {fark_1}-{fark_2} katman arayla.")
        print(f"-> İlk vurduğu katmanlar (Mod tabanı): L ≡ {g_kokler[0]} ve L ≡ {g_kokler[1]}")
    elif len(g_kokler) == 1:
        print(f"-> {asal_carpan}'nin Zıplama Ritmi: Sabit {asal_carpan} katmanda bir (Tek kök).")
    else:
        print(f"-> {asal_carpan} bu hattı ASLA KESEMEZ! (Tam korumalı)")

# 17 ve sonraki asalların ritim kodlarını çözüyoruz
yeni_dalga_boyu_hesapla(17)
yeni_dalga_boyu_hesapla(19)
yeni_dalga_boyu_hesapla(23)
input("k")