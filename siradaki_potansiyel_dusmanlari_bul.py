def is_prime(n):
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0 or n % 3 == 0: return False
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0: return False
    return True

def siradaki_potansiyel_dusmanlari_bul(ust_asal_siniri):
    """68 diskriminantına göre bizi vurabilecek tüm asalları önceden listeler."""
    dusman_asallar = []
    for p in range(5, ust_asal_siniri + 1):
        if is_prime(p):
            # Mod p tabanında karesel kalan kontrolü (x^2 % p == 68 % p)
            hedef_kalan = 68 % p
            for x in range(p):
                if (x * x) % p == hedef_kalan:
                    dusman_asallar.append(p)
                    break
    return dusman_asallar

# --- ANALİZ BAŞLANGICI ---
print("=== GEOMETRİK TAHMİN MATRİSİ ===")
print("Diskriminant D = 68 kuralına göre bizi vurabilecek asalların listesi:")
tahmin_listesi = siradaki_potansiyel_dusmanlari_bul(150)
print(tahmin_listesi)
print("-" * 65)
input("k")
# Şimdi bu tahmin listesini bir önceki kodumuzda çalıştırıp 1000 katmanda 
# bir sonraki kaçağın kim olacağını gözümüzle görelim.
