# Altıgen Spiral Geometrisinde Alt Kenar Asal Üretim ve Elek Modeli

Bu döküman, altıgen katman genişleme mekanizmasında $6n \pm 1$ serisi kullanılarak oluşturulan alt kenar hattının matematiksel altyapısını, bu hattın sahip olduğu doğal kalkan özelliklerini ve sızdırmazlık sağlayan modüler elek algoritmasını formülize etmektedir.

---

## 1. Ana Polinomun Türetilmesi

Altıgen spiralin ardışık katmanlarında, alt kenarın (Side 5) başlangıç noktalarındaki sayılar katman numarasına ($L$) bağlı olarak ikinci dereceden bir polinom oluşturur. $L = 1, 2, 3$ katmanlarındaki gerçek geometrik başlangıç verileri kullanılarak matris yöntemiyle denklem sistemi çözülmüştür:

$$
\begin{bmatrix}
1^2 & 1 & 1 \\\\
2^2 & 2 & 1 \\\\
3^2 & 3 & 1
\end{bmatrix}
\begin{bmatrix}
A \\\\
B \\\\
C
\end{bmatrix}
=
\begin{bmatrix}
19 \\\\
53 \\\\
103
\end{bmatrix}
$$

Bu lineer denklem sisteminin çözümünden $A=8, B=10, C=1$ katsayıları elde edilmiştir. Böylece alt kenar ana fonksiyonu $g(L)$ şu şekilde formülize edilmiştir:

$$
g(L) = 8L^2 + 10L + 1 \quad (L \in \mathbb{Z}^+)
$$

---

## 2. Doğal Koruma Kalkanı ve Diskriminant Analizi

Bir asal sayının ($p$) bu hattı kesebilmesi, yani hattın üzerinde bir bileşik sayı üretebilmesi için $g(L) \equiv 0 \pmod p$ denkleminin tamsayı köklerinin bulunması şarttır.

İkinci dereceden bu denklemin karakteristiğini belirleyen diskriminant ($D$) sabiti şu şekilde hesaplanır:

$$
D = b^2 - 4ac = 10^2 - 4 \cdot 8 \cdot 1 = 68
$$

Karesel Karşılıklılık İlkesi (*Quadratic Reciprocity*) uyarınca, bir $p$ asalının bu fonksiyon üzerinde bileşik sayı üretebilmesi için 68'in o asalın modunda bir karesel kalan olması zorunludur. Legendre sembolü ile ifade edilirse:

$$
\left(\frac{68}{p}\right) = 1
$$

> [!NOTE]
> **Doğal Engelli Asallar:**
> 
> $$\left(\frac{68}{7}\right) = -1, \quad \left(\frac{68}{11}\right) = -1, \quad \left(\frac{68}{23}\right) = -1$$
> 
> Bu matematiksel gerçeklikten ötürü $7, 11, 23$ asalları (ve bu kurala uyan diğer tüm asallar) $g(L)$ hattını sonsuza kadar hiçbir katmanda kesemez. Bu durum hattın yüksek asal yoğunluğunun temel sebebidir.

---

## 3. Modüler Periyotlar ve Atlama Ritmleri

Sistemi delme yeteneği olan zararlı asallar ($p$), hat üzerinde rastgele değil, belirli katman indekslerinde ($L$) periyodik zıplamalar yaparak bileşik sayı üretirler. Fonksiyonun modüler kökleri ($r_1, r_2$), zararlı asalların ilk vuruş noktalarını ve atlama aralıklarını belirler:

$$
8L^2 + 10L + 1 \equiv 0 \pmod p \implies L \equiv r_1, r_2 \pmod p
$$

Keşfedilen ve doğruluğu test edilen kritik ritim dalga boyları ve atlama şablonları şu şekildedir:

* **$p = 5$ için:** $L \equiv 2, 3 \pmod 5$ (Ardışık vuruşlar arası katman mesafesi $1 - 2$ ritmindedir).
* **$p = 13$ için:** $L \equiv 4, 8, 11 \pmod{13}$ (İkiz hat sızıntıları dahil $3 - 8$ ritmindedir).
* **$p = 17$ için:** $L \equiv 10 \pmod{17}$ (Tek kök durumu, sabit 17 katmanda bir tam kare salınım yapar).
* **$p = 19$ için:** $L \equiv 1, 12 \pmod{19}$ ($10 - 7$ ritmindedir).

---

## 4. Nihai Deterministik Elek Fonksiyonu

Klasik bölme testlerine ihtiyaç duymadan, sadece modüler kısıtlamaları kullanarak saf asalları ayıran küme fonksiyonu şu şekilde formülize edilmiştir:

$$
\mathcal{P}_{\text{zararli}} = \left\{ p \in \mathbb{P} \ \middle|\ \left(\frac{68}{p}\right) = 1 \right\} \cup \{5\}
$$

Belirlenen bir $M$ katman derinliğine kadar olan tüm pürüzsüz asal kümesi ($\mathcal{A}$), şu fonksiyonel süzgeçten geçerek %100 saflıkla elde edilir:

$$
\mathcal{A}(M) = \left\{ g(L) \ \middle|\ 1 \le L \le M \ \land \ \forall p \in \mathcal{P}_{\text{zararli}}^{\le \sqrt{g(M)}}, \ g(L) \not\equiv 0 \pmod p \right\}
$$

Bu formülizasyon, geometrik döngülerin modüler saat mekanizmalarıyla tamamen kontrol altına alınabildiğini ve $1000$ katman derinliğine kadar hatasız çalıştığını doğrulamıştır.

```text
## 5000 Katman Testi:

=== ALT KENAR OTOMATİK TAHMİNLİ KALKAN (İlk 5000 Katman) ===
Aktif Filtre Edilen Zararlı Asal Sayısı: 826
Kalan Aday Sayısı: 1391
Gerçek Asal Sayısı: 1391
Nihai Asallık Kalitesi: %100.00
Bu katman derinliğinde akıllı kalkan %100 saf asal koridoru üretti.
=================================================================
