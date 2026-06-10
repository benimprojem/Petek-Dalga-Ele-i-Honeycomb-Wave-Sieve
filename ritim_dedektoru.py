def ritim_dedektoru(asal_carpan):
    f_kokler = []
    g_kokler = []
    
    # 0'dan asal_carpan-1'e kadar olan modüler adımları tara
    for L in range(asal_carpan):
        if (9 * L**2 + 3 * L + 5) % asal_carpan == 0:
            f_kokler.append(L)
        if (8 * L**2 + 10 * L + 1) % asal_carpan == 0:
            g_kokler.append(L)
            
    print(f"=== {asal_carpan} Asalı İçin Geometrik Dalga Boyu ===")
    if f_kokler:
        f_fark = (f_kokler[1] - f_kokler[0] - 1, asal_carpan - f_kokler[1] + f_kokler[0] - 1)
        print(f"-> Sol Alt Kenarda (f) Atlama Ritmi: {f_fark[0]}-{f_fark[1]} katman arayla")
    else:
        print("-> Sol Alt Kenarda (f) Bu asal HİÇBİR katmanı kesmiyor! (Tam korumalı hat)")
        
    if g_kokler:
        g_fark = (g_kokler[1] - g_kokler[0] - 1, asal_carpan - g_kokler[1] + g_kokler[0] - 1)
        print(f"-> Alt Kenarda (g)     Atlama Ritmi: {g_fark[0]}-{g_fark[1]} katman arayla")
    else:
        print("-> Alt Kenarda (g)     Bu asal HİÇBİR katmanı kesmiyor! (Tam korumalı hat)")

# 7 ve 11'in ritim şifrelerini çöz
ritim_dedektoru(7)
ritim_dedektoru(11)
input("k")