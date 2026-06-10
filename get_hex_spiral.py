import matplotlib.pyplot as plt
import numpy as np
import math

# 1. Asallık kontrol fonksiyonu
def is_prime(n):
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0: return False
    return True

# 2. Koordinat üretici (Altıgen spiral)
def generate_honeycomb_spiral(n_limit, side_len):
    coords = {}
    x, y = 0.0, 0.0
    
    # 60 derecelik 6 ana yön
    angles = np.radians([0, 60, 120, 180, 240, 300])
    directions = list(zip(np.cos(angles), np.sin(angles)))
    
    num = 1
    coords[num] = (x, y)
    num += 1
    
    # Spiral genişlemesi
    # side_len arttıkça dışa doğru daha büyük bir yapı oluşur
    for layer in range(1, 50): 
        for dir_idx in range(6):
            for step in range(side_len * layer):
                if num > n_limit: break
                x += directions[dir_idx][0]
                y += directions[dir_idx][1]
                coords[num] = (x, y)
                num += 1
        if num > n_limit: break
    return coords

# 3. Ayarlar
limit = 10000
side_len = 1

# 4. Veri üretimi
coordinates = generate_honeycomb_spiral(limit, side_len)

# 5. Görselleştirme
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Asal ve bileşikleri ayır
x_primes, y_primes = [], []
x_others, y_others = [], []

for n, (x, y) in coordinates.items():
    if is_prime(n):
        x_primes.append(x)
        y_primes.append(y)
    else:
        x_others.append(x)
        y_others.append(y)

# Çizim
ax.scatter(x_others, y_others, s=0.5, c='#222222', marker='.', label='Bileşik')
ax.scatter(x_primes, y_primes, s=5, c='cyan', marker='o', label='Asal')

plt.title(f"Altıgen Spiral Yapısı ({limit} Sayı)", color='white')
plt.axis('off')
plt.show()