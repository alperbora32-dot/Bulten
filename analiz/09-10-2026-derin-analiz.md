# Derin analiz — 09.10.2026 (Cuma): bültenin sinyal kuralıyla seçilen 4 maç

> **Bu rapor bahis tavsiyesi değildir.** Olasılıklar geçmiş benzer oranlı maçlardan ve bir modelden türetilmiştir; geleceği kesin belirlemez. Oranlar BetExplorer ana sayfa listesinden alınmıştır ve değişebilir.

- **Tarih / saat dilimi:** 09.10.2026 (Europe/Istanbul, TSİ). Maç saatleri BetExplorer'ın gösterdiği saatlerdir; TSİ karşılığı bülten kalibrasyonuna göre **+2 saat** alınarak verilmiştir (11.09.2026 ölçümü: site 17:08 = TSİ 19:08). Bu dönüşüm bugün yeniden doğrulanmadı.
- **Veri:** BetExplorer listesi (09.10.2026, 109 maç, 1/X/2 oranlı; liste kısmi, ~45 lig). Geçmiş arşiv: 76.208 maç, 1/X/2 oranlı, en geç **11.09.2026**. Bülten snapshot'ı (BULTEN.html, 11.09.2026) bu analizde kullanılmadı; eski ve oynanmış maçları içeriyor.
- **Kapsam:** Bülten mantığıyla seçilen 4 maç için MS (1/X/2), çifte şans, alt/üst (0,5–4,5), KG, toplam gol dağılımı, İY sonuçları, İY/MS (9'lu), 2. yarı, handikap/kazanma farkı ve doğru skor olasılıkları. Her olasılığın yanında örneklem sayısı (n) ve %95 aralığı verilmiştir.

## 1. Özet

| Sıra | Maç (lig) | Saat: BetExplorer / TSİ | Oran 1 / X / 2 | Sinyal | Tarihsel % (n) | Piyasa % | Avantaj (puan) | Sağlamlık değerlendirmesi |
|---|---|---|---|---|---|---|---|---|
| 1 | **Southampton U21 – QPR U21** (Premier League Cup) | 14:00 / 16:00 | 1,46 / 4,80 / 4,80 | **Deplasman** (4,80) | 42,3 (26) | 18,9 | +23,4 | Zayıf–orta. Deplasman fazlası geniş pencerelerde de görülüyor ama etkin örneklem küçük (≈30–216). |
| 2 | **Peterborough U21 – Nottingham U21** (Premier League Cup) | 14:00 / 16:00 | 3,20 / 4,10 / 1,84 | **Deplasman** (1,84) | 71,8 (39) | 49,4 | +22,4 | Zayıf. Pencere genişledikçe fark küçülüyor; 0,28 penceresinde (n=360) yok. |
| 3 | **Al Khalidiyah – Al Muharraq** (Premier League) | 12:00 / 14:00 | 2,14 / 3,55 / 2,85 | **Deplasman** (2,85) | 51,2 (43) | 31,9 | +19,3 | Yok. Fark yalnızca ±0,05 penceresinde (n=43); ±0,08'de (n=152) piyasa ile aynı. |
| 4 | **Union de Santa Fe – Defensa y Justicia** (Liga Profesional) | 20:45 / 22:45 | 2,20 / 3,15 / 3,37 | **Beraberlik** (3,15) | 39,1 (92) | 29,7 | +9,4 | Yok. Beraberlik fazlası dar pencerede; yumuşatılmış tahminde fark ≈0–2,5 puan. |

**Tek bakışta olasılıklar** (piyasa = marjı çıkarılmış BetExplorer oranı; tarihsel = aynı oran penceresindeki maçlar; model = bülten Poisson/İY modeli; n = tarihsel örneklem)

| Maç | MS Ev / X / Dep: piyasa % | MS Ev / X / Dep: tarihsel % (n) | MS Ev / X / Dep: model % | 2,5 Üst: tarihsel / model % | KG Var: tarihsel / model % | İY 0,5 Üst: tarihsel / model % |
|---|---|---|---|---|---|---|
| Southampton U21 – QPR U21 | 62,2 / 18,9 / 18,9 | 46,2 / 11,5 / 42,3 (n=26) | 43,9 / 21,8 / 34,3 | 61,5 / 65,8 | 53,8 / 66,0 | 100,0 (n=11) / 78,3 |
| Peterborough U21 – Nottingham U21 | 28,4 / 22,2 / 49,4 | 15,4 / 12,8 / 71,8 (n=39) | 19,0 / 19,1 / 61,9 | 56,4 / 55,4 | 53,8 / 51,4 | 72,2 (n=18) / 73,8 |
| Al Khalidiyah – Al Muharraq | 42,5 / 25,6 / 31,9 | 34,9 / 14,0 / 51,2 (n=43) | 33,6 / 20,1 / 46,2 | 53,5 / 54,0 | 51,2 / 54,7 | 70,8 (n=24) / 66,4 |
| Union de Santa Fe – Defensa y Justicia | 42,5 / 29,7 / 27,8 | 38,0 / 39,1 / 22,8 (n=92) | 41,3 / 32,3 / 26,4 | 42,4 / 43,3 | 55,4 / 50,9 | veri yok / 65,7 |

Tam tablolar her maçın bölümündedir (Bölüm 5). Küçük örneklemlerde (n < 30) yüzdeler ±10–25 puan oynayabilir.

**Ana bulgular**

1. **Bülten kuralı tam 4 maçta sinyal verdi** (109 maçın tamamına uygulandı). Bu 4 maç, bu raporda "en güçlü 4" olarak seçildi; sıralama bültenin kendi kuralı olan avantaja göre yapıldı.
2. **Sinyaller sağlam değil.** Al Khalidiyah ve Union Santa Fe'deki farklar yalnızca çok dar oran penceresinde çıkıyor; komşu pencerelerde veya yumuşatılmış tahminde kayboluyor. Southampton U21 ve Peterborough U21'de deplasman fazlası daha tutarlı, ama örneklemler küçük ve farklı liglerden geliyor.
3. **Kuralın kendisi ayırt edici değil.** Piyasa oranları doğru olsaydı bile bu kural 109 maçta ortalama **6,7 sinyal** (standart sapma 2,5) üretirdi; gözlenen 4 bu beklentinin altında. Yani 4 sinyal "değer var" kanıtı değildir (bkz. Bölüm 4).
4. **İY ve alt-pazar olasılıklarının çoğu çok küçük örnekten gelir** (0–24 maç). Union Santa Fe için İY verisi hiç yok; İY değerleri yalnızca modelden türetildi.
5. **Model bağımsız bir doğrulama değildir.** Poisson λ değerleri her maçın kendi takımlarından değil, aynı oran komşuluğundaki geçmiş maçların ortalama gollerinden alınmıştır.
6. **Piyasa oranları (takım gücü, kadro, form gibi bilgileri içerir) bu yaklaşımdan daha bilgilendiricidir.** Aşağıdaki olasılıklar bilgi amaçlıdır; bahis kararı için kullanılmasını önermiyoruz.

## 2. Maç seçimi

- **Liste:** BetExplorer ana sayfasındaki 09.10.2026 maçları (109 maç, 1/X/2 oranlı). Liste kısmidir: Serie A, İskoçya, İskandinavya ve ABD gibi ligler listede yoktur. "En güçlü 4" bu 109 maç içinde geçerlidir.
- **Kural (bülten ile birebir):** Arşivde aynı 1/X/2 oranına sahip maçlar kademeli bir pencerede (0,03 → 1,10; en az 12 maç) bulunur. Bir sonuç **sinyal** sayılır, eğer: n ≥ 18, Wilson %95 alt sınırı > piyasa olasılığı, avantaj (tarihsel − piyasa) ≥ 3 puan ve pencere ≤ 0,20. Birden fazla sonuç varsa en iyi sonuç `avantaj × (1 − e^(−n/18))` ile seçilir.
- **Sonuç:** 109 maçtan 4'ü sinyal aldı: Southampton U21–QPR U21, Peterborough U21–Nottingham U21, Al Khalidiyah–Al Muharraq, Union Santa Fe–Defensa y Justicia. Diğer 105 maç Ek A'da listelenmiştir.
- **Saat kontrolü:** Dört maçın BetExplorer saatleri 12:00–20:45 arasındadır. TSİ karşılığı (+2 saat varsayımıyla) 14:00–22:45'tir. Analiz sırasında TSİ yaklaşık 10:40 idi; dört maç da henüz başlamamıştı. Site saatinin TSİ ile aynı olduğu varsayılsa bile en erken maç (12:00) 10:40'tan sonradır.
- **Bülten snapshot'ı:** BULTEN.html 11.09.2026 tarihlidir ve içindeki 148 maç oynanmıştır. Bu rapor o snapshot'ı kullanmaz; yalnızca arşiv ve bugünkü oranlar kullanılmıştır.

## 3. Yöntem

- **Tarihsel olasılık (ana sonuç):** Bülten `karsilastir` fonksiyonu; arşivdeki eşleşen maçların sonuç yüzdeleri. Pazar satırlarında (çifte şans, alt/üst, KG, İY, İY/MS vb.) her satırın n'i kendi örneklemidir; İY satırlarında n, İY verisi bulunan maç sayısıdır.
- **Duyarlılık testi (yeni):** (a) Oran penceresi 0,03–0,28 arası değiştirildi. (b) Gauss çekirdeği (h = 0,03–0,18) ile tüm arşivde yumuşatılmış tahmin; etkin örneklem büyüklüğü neff = (Σw)² / Σw². Her çekirdek tahmini için aynı komşuluğun piyasa ortalaması da hesaplandı (karşılaştırma adil olsun diye).
- **Küresel kalibrasyon (yeni):** 76.208 arşiv maçında, örtük (marjı çıkarılmış) olasılık bantlarına göre gerçekleşme oranları. Bir sonucun geçmişte bu fiyat bandında ne sıklıkla geldiğini gösterir.
- **Model:** Bülten `model_pazar` (bağımsız Poisson; İY payı = örneklemin İY/MS gol oranı; Dixon-Coles ρ). λ = örneklemin ev/deplasman ortalama golleri. Sonuç olarak model, örneklemin kendi gol ortalamasını yansıtır; takım gücünü ayrıca modellemez.
- **Küçültülmüş (Bayes) 1/X/2:** (n · tarihsel + 12 · piyasa) / (n + 12). 12, bültende kullanılan küçültme ağırlığıdır; piyasayı önsel kabul eder.
- **Aralıklar:** Pazar satırlarında Wilson %95; çekirdek tahminlerinde yaklaşık ±1,96·√(p(1−p)/neff).
- **Simülasyon (yeni):** Her maçta sonuçlar, bugünkü (marjı çıkarılmış) piyasa olasılıklarından ve o maçın gerçek örneklem büyüklüğünden çekildi (multinomial, B = 4.000). Aynı sinyal kuralı uygulandı.

## 4. Sinyal kuralının kalibrasyonu (çoklu karşılaştırma)

Her maçta üç sonuç ve 109 maç var; kural her maçta en iyi sonucu seçiyor. Piyasa doğru fiyatlasa da bu seçim, rastgele "değer" sinyalleri üretir. Simülasyon bunu ölçer:

| Ölçüt (piyasa doğru varsayımıyla, B = 4.000) | Değer |
|---|---|
| Ortalama sinyal sayısı | 6,7 |
| Standart sapma | 2,5 |
| Olasılık: en az 4 sinyal | 0,92 |
| Olasılık: en az 1 sinyal | 1,00 |

Gözlenen 4 sinyal, şansla da açıklanabilecek bir sayıdır. Bu nedenle bu 4 maç için "değer" iddiası, yalnızca sinyal sayısına dayanarak yapılamaz; aşağıdaki sağlamlık testlerine bakılmalıdır. (Simülasyon, örneklemlerin birbirini kısmen paylaştığını ve piyasa olasılıklarını marjı çıkararak aldığını varsayar; bu basitleştirmeler sonucu büyük ölçüde değiştirmez.)

## 5. Maç analizleri

Maçlar bültenin sıralamasına (avantaj) göre verilmiştir.

### 5.1 Southampton U21 – QPR U21

**Künye:** England: Premier League Cup · BetExplorer 14:00 / TSİ ≈ 16:00 · Oran 1,46 / 4,80 / 4,80 · Marj %10,2

**Bülten sinyali:** Deplasman @ 4,80 · tarihsel %42,3 (26 maç) · piyasa %18,9 · avantaj +23,4 puan · Wilson %95 [25,5–61,1] · pencere ±0,12 · bülten kalite etiketi: iyi

**Örneklem:** 26 maç · 17 farklı lig/ülke · aynı ligden 0 maç · 20 farklı oran üçlüsü · yıllar: 2019 (3), 2020 (5), 2021 (1), 2022 (1), 2023 (4), 2024 (3), 2025 (2), 2026 (7)
· en sık oran üçlüsü 1,57/4,75/4,75 (6 maç)

**Duyarlılık: pencere ve çekirdek (yumuşatılmış) tahminler**

| Yöntem | Örneklem (n / neff) | Ev % | Beraberlik % | Deplasman % | Aynı komşuluğun piyasa ort. (Ev / X / Dep) |
|---|---|---|---|---|---|
| Pencere ±0,03 | 1 | 100,0 | 0,0 | 0,0 | 62,3 / 18,8 / 18,8 |
| Pencere ±0,05 | 8 | 75,0 | 0,0 | 25,0 | 62,6 / 18,7 / 18,7 |
| Pencere ±0,08 | 10 | 70,0 | 0,0 | 30,0 | 62,4 / 18,8 / 18,8 |
| Pencere ±0,12 | 26 | 46,2 | 11,5 | 42,3 | 61,7 / 19,2 / 19,1 |
| Pencere ±0,18 | 43 | 51,2 | 14,0 | 34,9 | 61,5 / 19,4 / 19,1 |
| Pencere ±0,28 | 114 | 56,1 | 20,2 | 23,7 | 61,6 / 19,5 / 19,0 |
| Çekirdek h = 0,03 | 4 | 73,2 | 0,1 | 26,8 | 62,3 / 18,8 / 18,8 |
| Çekirdek h = 0,05 | 11 | 67,3 | 3,4 | 29,4 | 62,3 / 18,9 / 18,9 |
| Çekirdek h = 0,08 | 30 | 55,8 | 10,0 | 34,2 | 61,9 / 19,1 / 19,0 |
| Çekirdek h = 0,12 | 73 | 54,2 | 15,8 | 30,0 | 61,6 / 19,3 / 19,0 |
| Çekirdek h = 0,18 | 216 | 55,8 | 20,3 | 23,9 | 61,2 / 19,7 / 19,0 |

**1/X/2 karşılaştırması**

| Sonuç | Piyasa % (marjsız) | Adil oran (piyasa) | Tarihsel % (n) [Wilson %95] | Çekirdek h=0,12 % (±) | Model % | Bayes (k=12) % | Küresel bant: gerçekleşen / piyasa ort. |
|---|---|---|---|---|---|---|---|
| Ev | 62,2 | 1,61 | 46,2 (n=26) [28,8–64,5] | 54,2 (±11,4) | 43,9 | 51,2 | 68,2 / 64,4 (n=6.378) |
| Beraberlik | 18,9 | 5,29 | 11,5 (n=26) [4,0–29,0] | 15,8 (±8,4) | 21,8 | 13,9 | 15,0 / 18,0 (n=5.756) |
| Deplasman | 18,9 | 5,29 | 42,3 (n=26) [25,5–61,1] | 30,0 (±10,5) | 34,3 | 34,9 | 17,2 / 17,7 (n=8.266) |

**Tüm pazarlar (tarihsel, Wilson %95, model, adil oran)**

| Kategori | Olay | n | Tarihsel % | %95 aralık | Model % | Adil oran (tarihsel) |
|---|---|---|---|---|---|---|
| Maç sonucu (1X2) | 1 (Ev) | 26 | 46,2 | [28,8–64,5] | 43,9 | 2,16 |
| Maç sonucu (1X2) | X (Beraberlik) | 26 | 11,5 | [4,0–29,0] | 21,8 | 8,70 |
| Maç sonucu (1X2) | 2 (Dep) | 26 | 42,3 | [25,5–61,1] | 34,3 | 2,36 |
| Çifte şans | 1X | 26 | 57,7 | [38,9–74,5] | 65,7 | 1,73 |
| Çifte şans | 12 | 26 | 88,5 | [71,0–96,0] | 78,2 | 1,13 |
| Çifte şans | X2 | 26 | 53,8 | [35,5–71,2] | 56,1 | 1,86 |
| Alt/Üst | 0,5 Üst | 26 | 100,0 | [87,1–100,0] | 97,0 | 1,00 |
| Alt/Üst | 0,5 Alt | 26 | 0,0 | [0,0–12,9] | 3,0 | — |
| Alt/Üst | 1,5 Üst | 26 | 88,5 | [71,0–96,0] | 84,8 | 1,13 |
| Alt/Üst | 1,5 Alt | 26 | 11,5 | [4,0–29,0] | 15,2 | 8,70 |
| Alt/Üst | 2,5 Üst | 26 | 61,5 | [42,5–77,6] | 65,8 | 1,63 |
| Alt/Üst | 2,5 Alt | 26 | 38,5 | [22,4–57,5] | 34,2 | 2,60 |
| Alt/Üst | 3,5 Üst | 26 | 38,5 | [22,4–57,5] | 43,9 | 2,60 |
| Alt/Üst | 3,5 Alt | 26 | 61,5 | [42,5–77,6] | 56,1 | 1,63 |
| Alt/Üst | 4,5 Üst | 26 | 23,1 | [11,0–42,1] | 25,4 | 4,33 |
| Alt/Üst | 4,5 Alt | 26 | 76,9 | [57,9–89,0] | 74,6 | 1,30 |
| KG ve takım golleri | KG Var | 26 | 53,8 | [35,5–71,2] | 66,0 | 1,86 |
| KG ve takım golleri | KG Yok | 26 | 46,2 | [28,8–64,5] | 34,0 | 2,16 |
| KG ve takım golleri | Ev 0,5 Üst | 26 | 80,8 | [62,1–91,5] | 83,6 | 1,24 |
| KG ve takım golleri | Ev 1,5 Üst | 26 | 42,3 | [25,5–61,1] | 54,0 | 2,36 |
| KG ve takım golleri | Dep 0,5 Üst | 26 | 73,1 | [53,9–86,3] | 79,4 | 1,37 |
| KG ve takım golleri | Dep 1,5 Üst | 26 | 50,0 | [32,1–67,9] | 46,9 | 2,00 |
| Gol aralığı | 0-1 gol | 26 | 11,5 | [4,0–29,0] | 15,2 | 8,70 |
| Gol aralığı | 2-3 gol | 26 | 50,0 | [32,1–67,9] | 40,9 | 2,00 |
| Gol aralığı | 4+ gol | 26 | 38,5 | [22,4–57,5] | 43,9 | 2,60 |
| Handikap / kazanma farkı / iade | Beraberlikte İade (Ev) | 26 | 57,7 | [38,9–74,5] | 65,7 | 1,73 |
| Handikap / kazanma farkı / iade | Beraberlikte İade (Dep) | 26 | 53,8 | [35,5–71,2] | 56,1 | 1,86 |
| Handikap / kazanma farkı / iade | Handikap Ev -1 | 26 | 34,6 | [19,4–53,8] | 23,4 | 2,89 |
| Handikap / kazanma farkı / iade | Handikap Dep +1 | 26 | 53,8 | [35,5–71,2] | 56,1 | 1,86 |
| Handikap / kazanma farkı / iade | Kazanma farkı: Ev 1 gol | 26 | 11,5 | [4,0–29,0] | 20,5 | 8,70 |
| Handikap / kazanma farkı / iade | Kazanma farkı: Ev 2+ gol | 26 | 34,6 | [19,4–53,8] | 23,4 | 2,89 |
| Handikap / kazanma farkı / iade | Kazanma farkı: Dep 1 gol | 26 | 23,1 | [11,0–42,1] | 18,0 | 4,33 |
| Handikap / kazanma farkı / iade | Kazanma farkı: Dep 2+ gol | 26 | 19,2 | [8,5–37,9] | 16,4 | 5,21 |
| Handikap / kazanma farkı / iade | Tek gol (toplam) | 26 | 53,8 | [35,5–71,2] | 50,7 | 1,86 |
| Handikap / kazanma farkı / iade | Çift gol (toplam) | 26 | 46,2 | [28,8–64,5] | 49,3 | 2,16 |
| Handikap / kazanma farkı / iade | Ev 2+ gol atar | 26 | 42,3 | [25,5–61,1] | 54,0 | 2,36 |
| Handikap / kazanma farkı / iade | Dep 2+ gol atar | 26 | 50,0 | [32,1–67,9] | 46,9 | 2,00 |
| Kombinasyonlar | 2,5Ü + KG | 26 | 42,3 | [25,5–61,1] | 56,8 | 2,36 |
| Kombinasyonlar | 2,5A + KG Yok | 26 | 26,9 | [13,7–46,1] | 24,9 | 3,72 |
| Kombinasyonlar | 1,5Ü + İY 0-0 (yalnız İY verili maçlar) | 11 | 0,0 | [0,0–25,9] | 12,0 | — |
| Kombinasyonlar | MS 1 + 2,5Ü | 26 | 26,9 | [13,7–46,1] | 31,9 | 3,72 |

**Toplam gol dağılımı**

| Toplam gol | 0 | 1 | 2 | 3 | 4 | 5+ |
|---|---|---|---|---|---|---|
| Tarihsel % | 0,0 | 11,5 | 26,9 | 23,1 | 15,4 | 23,1 |
| Model % | 3,0 | 12,2 | 19,0 | 21,9 | 18,6 | 25,4 |

Örneklem ortalama gol: 3,38 · λ (ev / dep) = 1,81 / 1,58 · İY payı 0,45 · Dixon-Coles ρ = 0,04

**İlk yarı ve İY/MS**

İY verisi olan maç sayısı: **11 / 26** — çok küçük örnek, aşağıdaki tarihsel değerler güvenilmez.

| Olay | n_İY | Tarihsel % | %95 aralık | Model % | Adil oran (tarihsel) |
|---|---|---|---|---|---|
| İY 1 (Ev) | 11 | 18,2 | [5,1–47,7] | 34,9 | 5,49 |
| İY X | 11 | 45,5 | [21,3–72,0] | 36,1 | 2,20 |
| İY 2 (Dep) | 11 | 36,4 | [15,2–64,6] | 28,9 | 2,75 |
| İY 0-0 | 11 | 0,0 | [0,0–25,9] | 21,7 | — |
| İY 0,5 Üst | 11 | 100,0 | [74,1–100,0] | 78,3 | 1,00 |
| İY 1,5 Üst | 11 | 81,8 | [52,3–94,9] | 45,0 | 1,22 |
| İY KG | 11 | 63,6 | [35,4–84,8] | 28,3 | 1,57 |
| Her iki yarıda 0,5Ü | 11 | 72,7 | [43,4–90,3] | 65,9 | 1,38 |
| En çok gol 2. yarıda | 11 | 18,2 | [5,1–47,7] | 46,1 | 5,49 |
| En çok gol 1. yarıda | 11 | 72,7 | [43,4–90,3] | 32,1 | 1,38 |
| İY KG Yok → MS KG Var | 11 | 9,1 | [1,6–37,7] | 37,7 | 10,99 |
| İY 0-0 → 2Y gol var | 11 | 0,0 | [0,0–25,9] | 18,7 | — |
| 2Y 0,5 Üst | 11 | 72,7 | [43,4–90,3] | 84,6 | 1,38 |
| 2Y 1,5 Üst | 11 | 27,3 | [9,7–56,6] | 55,5 | 3,66 |
| 2Y Ev gol atar | 11 | 36,4 | [15,2–64,6] | 63,0 | 2,75 |
| 2Y Dep gol atar | 11 | 45,5 | [21,3–72,0] | 58,1 | 2,20 |
| 2Y KG | 11 | 9,1 | [1,6–37,7] | 36,5 | 10,99 |

| İY/MS (9'lu) | n_İY | Tarihsel % | %95 aralık | Model % | Adil oran (tarihsel) |
|---|---|---|---|---|---|
| İY 1 → MS 1 | 11 | 18,2 | [5,1–47,7] | 26,9 | 5,49 |
| İY 1 → MS X | 11 | 0,0 | [0,0–25,9] | 5,3 | — |
| İY 1 → MS 2 | 11 | 0,0 | [0,0–25,9] | 2,7 | — |
| İY X → MS 1 | 11 | 0,0 | [0,0–25,9] | 13,8 | — |
| İY X → MS X | 11 | 18,2 | [5,1–47,7] | 11,1 | 5,49 |
| İY X → MS 2 | 11 | 27,3 | [9,7–56,6] | 11,3 | 3,66 |
| İY 2 → MS 1 | 11 | 18,2 | [5,1–47,7] | 3,2 | 5,49 |
| İY 2 → MS X | 11 | 0,0 | [0,0–25,9] | 5,3 | — |
| İY 2 → MS 2 | 11 | 18,2 | [5,1–47,7] | 20,4 | 5,49 |

**Doğru skor (tarihsel ve modelde en olası skorlar)**

| Skor | Tarihsel % (örneklem) | Model % |
|---|---|---|
| 1 - 2 | 15,4 | 7,6 |
| 2 - 0 | 11,5 | 5,5 |
| 1 - 1 | 11,5 | 9,3 |
| 0 - 4 | 7,7 | — |
| 1 - 0 | 7,7 | 6,5 |
| 0 - 2 | 3,8 | 4,2 |
| 5 - 1 | 3,8 | — |
| 5 - 2 | 3,8 | — |
| 2 - 1 | 0,0 (örneklemde yok) | 8,7 |

**Yorum**

- **Neden sinyal?** Ev (1,46) için tarihsel oran %46,2 ve piyasa %62,2; deplasman (4,80) için tarihsel %42,3 (11/26) ve piyasa %18,9. Fark, deplasman tarafında.
- **Sağlamlık:** Deplasman tahmini 0,12–0,28 pencerelerinde %23,7 ile %42,3 arasında değişiyor. Yumuşatılmış tahminlerde h=0,08'de %34,2 (etkin n≈30), h=0,18'de %23,9 (etkin n≈216), komşuluk piyasası ise %19,0. Yani fazlalık, geniş komşulukta da +4–5 puan düzeyinde görünüyor ama bu, etkin örneklemin küçüklüğü nedeniyle güçlü bir kanıt değil.
- **Küresel bağlam:** Arşivde deplasman olasılığı %15–20 olan maçlarda gerçekleşen deplasman oranı %17,2 (n=8.266); yani bu bant genelde doğru fiyatlanıyor. Ev sahibi %60–70 bandında ise gerçekleşen %68,2 (piyasa %64,4): bu, favorilerin genelde piyasadan biraz fazla kazandığını gösteriyor, ama bu maçın yerel verisi (ev %46,2) bununla çelişiyor. Yerel sapmanın bu örneklemin oran profiline özgü olma ihtimali yüksek.
- **Örneklem kalitesi:** Aynı ligden (PL Cup) maç yok; 17 farklı lig var; en sık olanlar Hollanda 1. Lig (4), Avustralya Victoria PL (3) ve bazı Avusturya/Avustralya bölgesel ligleri (2'şer). Bu nedenle sonuçlar U21 PL Cup'a değil, benzer oranlı alt düzey maçlara aittir.
- **İY:** Yalnızca 11 maçta İY verisi var; İY sonuçları anlamsızdır (örneğin İY 0-0 %0, n=11). Model değerleri bu nedenle daha bilgilendiricidir, ama model λ'ları örneklemden geldiği için bağımsız değildir.

### 5.2 Peterborough U21 – Nottingham U21

**Künye:** England: Premier League Cup · BetExplorer 14:00 / TSİ ≈ 16:00 · Oran 3,20 / 4,10 / 1,84 · Marj %10,0

**Bülten sinyali:** Deplasman @ 1,84 · tarihsel %71,8 (39 maç) · piyasa %49,4 · avantaj +22,4 puan · Wilson %95 [56,2–83,5] · pencere ±0,12 · bülten kalite etiketi: iyi

**Örneklem:** 39 maç · 21 farklı lig/ülke · aynı ligden 1 maç · 34 farklı oran üçlüsü · yıllar: 2019 (2), 2020 (5), 2021 (5), 2022 (5), 2023 (4), 2024 (2), 2025 (3), 2026 (13)
· en sık oran üçlüsü 3,30/4,00/1,95 (3 maç)

**Duyarlılık: pencere ve çekirdek (yumuşatılmış) tahminler**

| Yöntem | Örneklem (n / neff) | Ev % | Beraberlik % | Deplasman % | Aynı komşuluğun piyasa ort. (Ev / X / Dep) |
|---|---|---|---|---|---|
| Pencere ±0,03 | 1 | 0,0 | 0,0 | 100,0 | 28,3 / 22,2 / 49,5 |
| Pencere ±0,05 | 4 | 25,0 | 0,0 | 75,0 | 28,4 / 22,4 / 49,1 |
| Pencere ±0,08 | 11 | 18,2 | 0,0 | 81,8 | 28,2 / 22,2 / 49,6 |
| Pencere ±0,12 | 39 | 15,4 | 12,8 | 71,8 | 28,4 / 22,5 / 49,1 |
| Pencere ±0,18 | 114 | 27,2 | 18,4 | 54,4 | 28,7 / 22,8 / 48,5 |
| Pencere ±0,28 | 360 | 29,2 | 22,8 | 48,1 | 28,7 / 23,1 / 48,2 |
| Çekirdek h = 0,03 | 4 | 20,6 | 0,2 | 79,2 | 28,4 / 22,2 / 49,4 |
| Çekirdek h = 0,05 | 12 | 18,5 | 4,9 | 76,6 | 28,3 / 22,3 / 49,4 |
| Çekirdek h = 0,08 | 49 | 20,2 | 12,8 | 67,0 | 28,4 / 22,5 / 49,1 |
| Çekirdek h = 0,12 | 185 | 24,1 | 18,3 | 57,6 | 28,5 / 22,8 / 48,7 |
| Çekirdek h = 0,18 | 592 | 27,0 | 21,2 | 51,8 | 28,4 / 23,3 / 48,2 |

**1/X/2 karşılaştırması**

| Sonuç | Piyasa % (marjsız) | Adil oran (piyasa) | Tarihsel % (n) [Wilson %95] | Çekirdek h=0,12 % (±) | Model % | Bayes (k=12) % | Küresel bant: gerçekleşen / piyasa ort. |
|---|---|---|---|---|---|---|---|
| Ev | 28,4 | 3,52 | 15,4 (n=39) [7,2–29,7] | 24,1 (±6,2) | 19,0 | 18,4 | 26,5 / 27,6 (n=6.409) |
| Beraberlik | 22,2 | 4,51 | 12,8 (n=39) [5,6–26,7] | 18,3 (±5,6) | 19,1 | 15,0 | 21,2 / 23,1 (n=17.780) |
| Deplasman | 49,4 | 2,02 | 71,8 (n=39) [56,2–83,5] | 57,6 (±7,1) | 61,9 | 66,5 | 49,4 / 47,4 (n=4.219) |

**Tüm pazarlar (tarihsel, Wilson %95, model, adil oran)**

| Kategori | Olay | n | Tarihsel % | %95 aralık | Model % | Adil oran (tarihsel) |
|---|---|---|---|---|---|---|
| Maç sonucu (1X2) | 1 (Ev) | 39 | 15,4 | [7,2–29,7] | 19,0 | 6,49 |
| Maç sonucu (1X2) | X (Beraberlik) | 39 | 12,8 | [5,6–26,7] | 19,1 | 7,81 |
| Maç sonucu (1X2) | 2 (Dep) | 39 | 71,8 | [56,2–83,5] | 61,9 | 1,39 |
| Çifte şans | 1X | 39 | 28,2 | [16,5–43,8] | 38,1 | 3,55 |
| Çifte şans | 12 | 39 | 87,2 | [73,3–94,4] | 80,9 | 1,15 |
| Çifte şans | X2 | 39 | 84,6 | [70,3–92,8] | 81,0 | 1,18 |
| Alt/Üst | 0,5 Üst | 39 | 97,4 | [86,8–99,5] | 95,7 | 1,03 |
| Alt/Üst | 0,5 Alt | 39 | 2,6 | [0,5–13,2] | 4,3 | 38,46 |
| Alt/Üst | 1,5 Üst | 39 | 82,1 | [67,3–91,0] | 77,3 | 1,22 |
| Alt/Üst | 1,5 Alt | 39 | 17,9 | [9,0–32,7] | 22,7 | 5,59 |
| Alt/Üst | 2,5 Üst | 39 | 56,4 | [41,0–70,7] | 55,4 | 1,77 |
| Alt/Üst | 2,5 Alt | 39 | 43,6 | [29,3–59,0] | 44,6 | 2,29 |
| Alt/Üst | 3,5 Üst | 39 | 30,8 | [18,6–46,4] | 33,0 | 3,25 |
| Alt/Üst | 3,5 Alt | 39 | 69,2 | [53,6–81,4] | 67,0 | 1,45 |
| Alt/Üst | 4,5 Üst | 39 | 12,8 | [5,6–26,7] | 16,8 | 7,81 |
| Alt/Üst | 4,5 Alt | 39 | 87,2 | [73,3–94,4] | 83,2 | 1,15 |
| KG ve takım golleri | KG Var | 39 | 53,8 | [38,6–68,4] | 51,4 | 1,86 |
| KG ve takım golleri | KG Yok | 39 | 46,2 | [31,6–61,4] | 48,6 | 2,16 |
| KG ve takım golleri | Ev 0,5 Üst | 39 | 59,0 | [43,4–72,9] | 61,3 | 1,69 |
| KG ve takım golleri | Ev 1,5 Üst | 39 | 25,6 | [14,6–41,1] | 24,6 | 3,91 |
| KG ve takım golleri | Dep 0,5 Üst | 39 | 92,3 | [79,7–97,3] | 85,8 | 1,08 |
| KG ve takım golleri | Dep 1,5 Üst | 39 | 61,5 | [45,9–75,1] | 58,0 | 1,63 |
| Gol aralığı | 0-1 gol | 39 | 17,9 | [9,0–32,7] | 22,7 | 5,59 |
| Gol aralığı | 2-3 gol | 39 | 51,3 | [36,2–66,1] | 44,3 | 1,95 |
| Gol aralığı | 4+ gol | 39 | 30,8 | [18,6–46,4] | 33,0 | 3,25 |
| Handikap / kazanma farkı / iade | Beraberlikte İade (Ev) | 39 | 28,2 | [16,5–43,8] | 38,1 | 3,55 |
| Handikap / kazanma farkı / iade | Beraberlikte İade (Dep) | 39 | 84,6 | [70,3–92,8] | 81,0 | 1,18 |
| Handikap / kazanma farkı / iade | Handikap Ev -1 | 39 | 7,7 | [2,7–20,3] | 6,0 | 12,99 |
| Handikap / kazanma farkı / iade | Handikap Dep +1 | 39 | 84,6 | [70,3–92,8] | 81,0 | 1,18 |
| Handikap / kazanma farkı / iade | Kazanma farkı: Ev 1 gol | 39 | 7,7 | [2,7–20,3] | 13,0 | 12,99 |
| Handikap / kazanma farkı / iade | Kazanma farkı: Ev 2+ gol | 39 | 7,7 | [2,7–20,3] | 6,0 | 12,99 |
| Handikap / kazanma farkı / iade | Kazanma farkı: Dep 1 gol | 39 | 38,5 | [24,9–54,1] | 25,5 | 2,60 |
| Handikap / kazanma farkı / iade | Kazanma farkı: Dep 2+ gol | 39 | 33,3 | [20,6–49,0] | 36,4 | 3,00 |
| Handikap / kazanma farkı / iade | Tek gol (toplam) | 39 | 53,8 | [38,6–68,4] | 52,3 | 1,86 |
| Handikap / kazanma farkı / iade | Çift gol (toplam) | 39 | 46,2 | [31,6–61,4] | 47,7 | 2,16 |
| Handikap / kazanma farkı / iade | Ev 2+ gol atar | 39 | 25,6 | [14,6–41,1] | 24,6 | 3,91 |
| Handikap / kazanma farkı / iade | Dep 2+ gol atar | 39 | 61,5 | [45,9–75,1] | 58,0 | 1,63 |
| Kombinasyonlar | 2,5Ü + KG | 39 | 46,2 | [31,6–61,4] | 42,4 | 2,16 |
| Kombinasyonlar | 2,5A + KG Yok | 39 | 35,9 | [22,7–51,6] | 35,6 | 2,79 |
| Kombinasyonlar | 1,5Ü + İY 0-0 (yalnız İY verili maçlar) | 18 | 11,1 | [3,1–32,8] | 11,9 | 9,01 |
| Kombinasyonlar | MS 1 + 2,5Ü | 39 | 10,3 | [4,1–23,6] | 10,1 | 9,71 |

**Toplam gol dağılımı**

| Toplam gol | 0 | 1 | 2 | 3 | 4 | 5+ |
|---|---|---|---|---|---|---|
| Tarihsel % | 2,6 | 15,4 | 25,6 | 25,6 | 17,9 | 12,8 |
| Model % | 4,3 | 18,4 | 21,9 | 22,4 | 16,2 | 16,8 |

Örneklem ortalama gol: 2,90 · λ (ev / dep) = 0,95 / 1,95 · İY payı 0,46 · Dixon-Coles ρ = 0,12

**İlk yarı ve İY/MS**

İY verisi olan maç sayısı: **18 / 39** — çok küçük örnek, aşağıdaki tarihsel değerler güvenilmez.

| Olay | n_İY | Tarihsel % | %95 aralık | Model % | Adil oran (tarihsel) |
|---|---|---|---|---|---|
| İY 1 (Ev) | 18 | 16,7 | [5,8–39,2] | 17,5 | 5,99 |
| İY X | 18 | 33,3 | [16,3–56,3] | 37,3 | 3,00 |
| İY 2 (Dep) | 18 | 50,0 | [29,0–71,0] | 45,2 | 2,00 |
| İY 0-0 | 18 | 27,8 | [12,5–50,9] | 26,2 | 3,60 |
| İY 0,5 Üst | 18 | 72,2 | [49,1–87,5] | 73,8 | 1,39 |
| İY 1,5 Üst | 18 | 38,9 | [20,3–61,4] | 38,1 | 2,57 |
| İY KG | 18 | 11,1 | [3,1–32,8] | 20,6 | 9,01 |
| Her iki yarıda 0,5Ü | 18 | 55,6 | [33,7–75,4] | 57,6 | 1,80 |
| En çok gol 2. yarıda | 18 | 38,9 | [20,3–61,4] | 44,0 | 2,57 |
| En çok gol 1. yarıda | 18 | 38,9 | [20,3–61,4] | 33,2 | 2,57 |
| İY KG Yok → MS KG Var | 18 | 33,3 | [16,3–56,3] | 30,8 | 3,00 |
| İY 0-0 → 2Y gol var | 18 | 22,2 | [9,0–45,2] | 21,9 | 4,50 |
| 2Y 0,5 Üst | 18 | 77,8 | [54,8–91,0] | 79,6 | 1,29 |
| 2Y 1,5 Üst | 18 | 33,3 | [16,3–56,3] | 46,2 | 3,00 |
| 2Y Ev gol atar | 18 | 38,9 | [20,3–61,4] | 40,2 | 2,57 |
| 2Y Dep gol atar | 18 | 55,6 | [33,7–75,4] | 65,2 | 1,80 |
| 2Y KG | 18 | 16,7 | [5,8–39,2] | 25,9 | 5,99 |

| İY/MS (9'lu) | n_İY | Tarihsel % | %95 aralık | Model % | Adil oran (tarihsel) |
|---|---|---|---|---|---|
| İY 1 → MS 1 | 18 | 11,1 | [3,1–32,8] | 10,4 | 9,01 |
| İY 1 → MS X | 18 | 0,0 | [0,0–17,6] | 4,1 | — |
| İY 1 → MS 2 | 18 | 5,6 | [1,0–25,8] | 3,0 | 17,86 |
| İY X → MS 1 | 18 | 5,6 | [1,0–25,8] | 7,4 | 17,86 |
| İY X → MS X | 18 | 5,6 | [1,0–25,8] | 10,9 | 17,86 |
| İY X → MS 2 | 18 | 22,2 | [9,0–45,2] | 19,0 | 4,50 |
| İY 2 → MS 1 | 18 | 0,0 | [0,0–17,6] | 1,2 | — |
| İY 2 → MS X | 18 | 11,1 | [3,1–32,8] | 4,1 | 9,01 |
| İY 2 → MS 2 | 18 | 38,9 | [20,3–61,4] | 40,0 | 2,57 |

**Doğru skor (tarihsel ve modelde en olası skorlar)**

| Skor | Tarihsel % (örneklem) | Model % |
|---|---|---|
| 0 - 2 | 15,4 | 10,5 |
| 1 - 2 | 15,4 | 9,9 |
| 0 - 1 | 12,8 | 12,0 |
| 1 - 1 | 7,7 | 9,0 |
| 0 - 4 | 5,1 | — |
| 3 - 1 | 5,1 | — |
| 0 - 3 | 5,1 | 6,8 |
| 1 - 3 | 5,1 | 6,5 |
| 1 - 0 | 2,6 | 6,5 |

**Yorum**

- **Neden sinyal?** Deplasman (1,84, Nottingham U21) için tarihsel %71,8 (28/39) ve piyasa %49,4; avantaj +22,4 puan, Wilson %95 [56,2–83,5].
- **Sağlamlık:** Pencere genişledikçe deplasman oranı %81,8 (±0,08, n=11) → %71,8 (±0,12, n=39) → %54,4 (±0,18, n=114) → %48,1 (±0,28, n=360) yönünde düşüyor; geniş pencerelerde piyasa ile aynı. Çekirdek tahminlerde h=0,12'de %57,6 (etkin n≈185, komşuluk piyasası %48,7), h=0,18'de %51,8 (etkin n≈592, piyasa %48,2). Yani fark, geniş komşulukta +3–4 puana iniyor.
- **Küresel bağlam:** Deplasman olasılığı %45–50 olan arşiv maçlarında gerçekleşen oran %49,4 (piyasa %47,4; n=4.219). Bu bantta gerçekleşen oran zaten piyasanın hafifçe üzerinde (+2,0 puan); yerel fazlalığın bir kısmı bu genel eğilimle açıklanabilir.
- **Ev sahibi:** Yerel tarihsel ev oranı %15,4 (piyasa %28,4); küresel bantta ev %25–30 olan maçlar %26,5 gerçekleşiyor. Yerel ev düşüklüğü de bu oran profiline özgü görünüyor.
- **İY:** 18 maçta İY verisi var. İY 2 (deplasman önde) %50,0 (9/18), model %45,2; ikinci yarıda 1,5 üst tarihsel %33,3 (n=18), model %46,2. Bu sayılar çok küçük örnekten geldiği için yalnızca yön bilgisi olarak okunmalıdır.

### 5.3 Al Khalidiyah – Al Muharraq

**Künye:** Bahrain: Premier League · BetExplorer 12:00 / TSİ ≈ 14:00 · Oran 2,14 / 3,55 / 2,85 · Marj %10,0

**Bülten sinyali:** Deplasman @ 2,85 · tarihsel %51,2 (43 maç) · piyasa %31,9 · avantaj +19,3 puan · Wilson %95 [36,8–65,4] · pencere ±0,05 · bülten kalite etiketi: kesin

**Örneklem:** 43 maç · 25 farklı lig/ülke · aynı ligden 0 maç · 38 farklı oran üçlüsü · yıllar: 2020 (1), 2021 (5), 2023 (4), 2024 (7), 2025 (7), 2026 (19)
· en sık oran üçlüsü 2,15/3,50/2,90 (4 maç)

**Duyarlılık: pencere ve çekirdek (yumuşatılmış) tahminler**

| Yöntem | Örneklem (n / neff) | Ev % | Beraberlik % | Deplasman % | Aynı komşuluğun piyasa ort. (Ev / X / Dep) |
|---|---|---|---|---|---|
| Pencere ±0,03 | 8 | 25,0 | 12,5 | 62,5 | 42,4 / 25,7 / 31,9 |
| Pencere ±0,05 | 43 | 34,9 | 14,0 | 51,2 | 42,5 / 25,8 / 31,7 |
| Pencere ±0,08 | 152 | 44,7 | 24,3 | 30,9 | 42,4 / 25,7 / 31,9 |
| Pencere ±0,12 | 434 | 42,2 | 27,9 | 30,0 | 42,2 / 25,8 / 32,0 |
| Pencere ±0,18 | 1585 | 44,4 | 24,2 | 31,4 | 41,9 / 26,1 / 31,9 |
| Pencere ±0,28 | 4622 | 42,8 | 24,4 | 32,8 | 41,5 / 26,5 / 32,0 |
| Çekirdek h = 0,03 | 41 | 29,5 | 16,4 | 54,1 | 42,5 / 25,6 / 31,9 |
| Çekirdek h = 0,05 | 187 | 39,8 | 22,5 | 37,7 | 42,4 / 25,7 / 31,9 |
| Çekirdek h = 0,08 | 715 | 42,8 | 24,6 | 32,6 | 42,2 / 25,8 / 31,9 |
| Çekirdek h = 0,12 | 2073 | 43,0 | 24,7 | 32,3 | 42,0 / 26,1 / 32,0 |
| Çekirdek h = 0,18 | 5114 | 42,6 | 24,9 | 32,5 | 41,6 / 26,5 / 31,9 |

**1/X/2 karşılaştırması**

| Sonuç | Piyasa % (marjsız) | Adil oran (piyasa) | Tarihsel % (n) [Wilson %95] | Çekirdek h=0,12 % (±) | Model % | Bayes (k=12) % | Küresel bant: gerçekleşen / piyasa ort. |
|---|---|---|---|---|---|---|---|
| Ev | 42,5 | 2,35 | 34,9 (n=43) [22,4–49,8] | 43,0 (±2,1) | 33,6 | 36,5 | 43,3 / 42,5 (n=10.158) |
| Beraberlik | 25,6 | 3,90 | 14,0 (n=43) [6,6–27,3] | 24,7 (±1,9) | 20,1 | 16,5 | 26,9 / 27,5 (n=39.362) |
| Deplasman | 31,9 | 3,13 | 51,2 (n=43) [36,8–65,4] | 32,3 (±2,0) | 46,2 | 47,0 | 32,8 / 32,4 (n=10.540) |

**Tüm pazarlar (tarihsel, Wilson %95, model, adil oran)**

| Kategori | Olay | n | Tarihsel % | %95 aralık | Model % | Adil oran (tarihsel) |
|---|---|---|---|---|---|---|
| Maç sonucu (1X2) | 1 (Ev) | 43 | 34,9 | [22,4–49,8] | 33,6 | 2,87 |
| Maç sonucu (1X2) | X (Beraberlik) | 43 | 14,0 | [6,6–27,3] | 20,1 | 7,14 |
| Maç sonucu (1X2) | 2 (Dep) | 43 | 51,2 | [36,8–65,4] | 46,2 | 1,95 |
| Çifte şans | 1X | 43 | 48,8 | [34,6–63,2] | 53,8 | 2,05 |
| Çifte şans | 12 | 43 | 86,0 | [72,7–93,4] | 79,9 | 1,16 |
| Çifte şans | X2 | 43 | 65,1 | [50,2–77,6] | 66,4 | 1,54 |
| Alt/Üst | 0,5 Üst | 43 | 97,7 | [87,9–99,6] | 96,5 | 1,02 |
| Alt/Üst | 0,5 Alt | 43 | 2,3 | [0,4–12,1] | 3,5 | 43,48 |
| Alt/Üst | 1,5 Üst | 43 | 74,4 | [59,8–85,1] | 75,2 | 1,34 |
| Alt/Üst | 1,5 Alt | 43 | 25,6 | [14,9–40,2] | 24,8 | 3,91 |
| Alt/Üst | 2,5 Üst | 43 | 53,5 | [38,9–67,5] | 54,0 | 1,87 |
| Alt/Üst | 2,5 Alt | 43 | 46,5 | [32,5–61,1] | 46,0 | 2,15 |
| Alt/Üst | 3,5 Üst | 43 | 30,2 | [18,6–45,1] | 31,7 | 3,31 |
| Alt/Üst | 3,5 Alt | 43 | 69,8 | [54,9–81,4] | 68,3 | 1,43 |
| Alt/Üst | 4,5 Üst | 43 | 16,3 | [8,1–30,0] | 15,9 | 6,13 |
| Alt/Üst | 4,5 Alt | 43 | 83,7 | [70,0–91,9] | 84,1 | 1,19 |
| KG ve takım golleri | KG Var | 43 | 51,2 | [36,8–65,4] | 54,7 | 1,95 |
| KG ve takım golleri | KG Yok | 43 | 48,8 | [34,6–63,2] | 45,3 | 2,05 |
| KG ve takım golleri | Ev 0,5 Üst | 43 | 65,1 | [50,2–77,6] | 72,2 | 1,54 |
| KG ve takım golleri | Ev 1,5 Üst | 43 | 30,2 | [18,6–45,1] | 36,6 | 3,31 |
| KG ve takım golleri | Dep 0,5 Üst | 43 | 83,7 | [70,0–91,9] | 79,0 | 1,19 |
| KG ve takım golleri | Dep 1,5 Üst | 43 | 53,5 | [38,9–67,5] | 46,2 | 1,87 |
| Gol aralığı | 0-1 gol | 43 | 25,6 | [14,9–40,2] | 24,8 | 3,91 |
| Gol aralığı | 2-3 gol | 43 | 44,2 | [30,4–58,9] | 43,5 | 2,26 |
| Gol aralığı | 4+ gol | 43 | 30,2 | [18,6–45,1] | 31,7 | 3,31 |
| Handikap / kazanma farkı / iade | Beraberlikte İade (Ev) | 43 | 48,8 | [34,6–63,2] | 53,8 | 2,05 |
| Handikap / kazanma farkı / iade | Beraberlikte İade (Dep) | 43 | 65,1 | [50,2–77,6] | 66,4 | 1,54 |
| Handikap / kazanma farkı / iade | Handikap Ev -1 | 43 | 14,0 | [6,6–27,3] | 13,4 | 7,14 |
| Handikap / kazanma farkı / iade | Handikap Dep +1 | 43 | 65,1 | [50,2–77,6] | 66,4 | 1,54 |
| Handikap / kazanma farkı / iade | Kazanma farkı: Ev 1 gol | 43 | 20,9 | [11,4–35,2] | 20,2 | 4,78 |
| Handikap / kazanma farkı / iade | Kazanma farkı: Ev 2+ gol | 43 | 14,0 | [6,6–27,3] | 13,4 | 7,14 |
| Handikap / kazanma farkı / iade | Kazanma farkı: Dep 1 gol | 43 | 30,2 | [18,6–45,1] | 24,1 | 3,31 |
| Handikap / kazanma farkı / iade | Kazanma farkı: Dep 2+ gol | 43 | 20,9 | [11,4–35,2] | 22,1 | 4,78 |
| Handikap / kazanma farkı / iade | Tek gol (toplam) | 43 | 55,8 | [41,1–69,6] | 54,5 | 1,79 |
| Handikap / kazanma farkı / iade | Çift gol (toplam) | 43 | 44,2 | [30,4–58,9] | 45,5 | 2,26 |
| Handikap / kazanma farkı / iade | Ev 2+ gol atar | 43 | 30,2 | [18,6–45,1] | 36,6 | 3,31 |
| Handikap / kazanma farkı / iade | Dep 2+ gol atar | 43 | 53,5 | [38,9–67,5] | 46,2 | 1,87 |
| Kombinasyonlar | 2,5Ü + KG | 43 | 44,2 | [30,4–58,9] | 45,4 | 2,26 |
| Kombinasyonlar | 2,5A + KG Yok | 43 | 39,5 | [26,4–54,4] | 36,7 | 2,53 |
| Kombinasyonlar | 1,5Ü + İY 0-0 (yalnız İY verili maçlar) | 24 | 8,3 | [2,3–25,8] | 16,9 | 12,05 |
| Kombinasyonlar | MS 1 + 2,5Ü | 43 | 25,6 | [14,9–40,2] | 19,0 | 3,91 |

**Toplam gol dağılımı**

| Toplam gol | 0 | 1 | 2 | 3 | 4 | 5+ |
|---|---|---|---|---|---|---|
| Tarihsel % | 2,3 | 23,3 | 20,9 | 23,3 | 14,0 | 16,3 |
| Model % | 3,5 | 21,3 | 21,2 | 22,3 | 15,8 | 15,9 |

Örneklem ortalama gol: 2,84 · λ (ev / dep) = 1,28 / 1,56 · İY payı 0,38 · Dixon-Coles ρ = 0,20 (**sınır değer**)

**İlk yarı ve İY/MS**

İY verisi olan maç sayısı: **24 / 43**.

| Olay | n_İY | Tarihsel % | %95 aralık | Model % | Adil oran (tarihsel) |
|---|---|---|---|---|---|
| İY 1 (Ev) | 24 | 25,0 | [12,0–44,9] | 24,6 | 4,00 |
| İY X | 24 | 37,5 | [21,2–57,3] | 43,8 | 2,67 |
| İY 2 (Dep) | 24 | 37,5 | [21,2–57,3] | 31,6 | 2,67 |
| İY 0-0 | 24 | 29,2 | [14,9–49,2] | 33,6 | 3,42 |
| İY 0,5 Üst | 24 | 70,8 | [50,8–85,1] | 66,4 | 1,41 |
| İY 1,5 Üst | 24 | 29,2 | [14,9–49,2] | 29,0 | 3,42 |
| İY KG | 24 | 16,7 | [6,7–35,9] | 16,9 | 5,99 |
| Her iki yarıda 0,5Ü | 24 | 54,2 | [35,1–72,1] | 53,6 | 1,85 |
| En çok gol 2. yarıda | 24 | 66,7 | [46,7–82,0] | 55,3 | 1,50 |
| En çok gol 1. yarıda | 24 | 16,7 | [6,7–35,9] | 24,7 | 5,99 |
| İY KG Yok → MS KG Var | 24 | 33,3 | [18,0–53,3] | 37,8 | 3,00 |
| İY 0-0 → 2Y gol var | 24 | 25,0 | [12,0–44,9] | 30,1 | 4,00 |
| 2Y 0,5 Üst | 24 | 79,2 | [59,5–90,8] | 83,7 | 1,26 |
| 2Y 1,5 Üst | 24 | 58,3 | [38,8–75,5] | 51,6 | 1,72 |
| 2Y Ev gol atar | 24 | 54,2 | [35,1–72,1] | 54,8 | 1,85 |
| 2Y Dep gol atar | 24 | 62,5 | [42,7–78,8] | 62,0 | 1,60 |
| 2Y KG | 24 | 37,5 | [21,2–57,3] | 33,0 | 2,67 |

| İY/MS (9'lu) | n_İY | Tarihsel % | %95 aralık | Model % | Adil oran (tarihsel) |
|---|---|---|---|---|---|
| İY 1 → MS 1 | 24 | 20,8 | [9,2–40,5] | 17,2 | 4,81 |
| İY 1 → MS X | 24 | 0,0 | [0,0–13,8] | 4,5 | — |
| İY 1 → MS 2 | 24 | 4,2 | [0,7–20,2] | 2,9 | 23,81 |
| İY X → MS 1 | 24 | 20,8 | [9,2–40,5] | 14,2 | 4,81 |
| İY X → MS X | 24 | 4,2 | [0,7–20,2] | 11,2 | 23,81 |
| İY X → MS 2 | 24 | 12,5 | [4,3–31,0] | 18,4 | 8,00 |
| İY 2 → MS 1 | 24 | 0,0 | [0,0–13,8] | 2,2 | — |
| İY 2 → MS X | 24 | 4,2 | [0,7–20,2] | 4,5 | 23,81 |
| İY 2 → MS 2 | 24 | 33,3 | [18,0–53,3] | 24,9 | 3,00 |

**Doğru skor (tarihsel ve modelde en olası skorlar)**

| Skor | Tarihsel % (örneklem) | Model % |
|---|---|---|
| 1 - 2 | 16,3 | 9,1 |
| 0 - 1 | 14,0 | 11,4 |
| 0 - 2 | 14,0 | 7,1 |
| 1 - 0 | 9,3 | 9,8 |
| 3 - 2 | 7,0 | — |
| 1 - 1 | 7,0 | 9,3 |
| 3 - 1 | 4,7 | — |
| 0 - 4 | 4,7 | — |
| 2 - 1 | 2,3 | 7,5 |

**Yorum**

- **Neden sinyal?** Deplasman (2,85, Al Muharraq) için tarihsel %51,2 (22/43) ve piyasa %31,9; avantaj +19,3 puan, Wilson %95 [36,8–65,4].
- **Sağlamlık (bu maçta en önemli bulgu):** Fark tamamen dar pencerede. Pencere ±0,05 (n=43) → %51,2; ±0,08 (n=152) → %30,9 (piyasa %31,9); ±0,12 (n=434) → %30,0; ±0,18 (n=1.585) → %31,4. Yani ±0,08'e genişletildiğinde deplasman fazlası tamamen kayboluyor. Çekirdek tahminler de aynısını gösteriyor: h=0,05'te %37,7 (etkin n≈187), h=0,08'de %32,6 (piyasa %31,9), h=0,12'de %32,3 (piyasa %32,0).
- **Sonuç:** Bu sinyal, belirli bir oran noktasında yerel bir sapmadır; geniş komşulukta piyasa ile uyumludur. Güvenilir bir değer kanıtı değildir.
- **Küresel bağlam:** Deplasman piyasa olasılığı %30–35 olan arşiv maçlarında gerçekleşen oran %32,8 (piyasa ort. %32,4; n=10.540). Yani bu bantta genel kalibrasyon iyi.
- **Örneklem kalitesi:** Bahreyn Premier League arşivde yalnızca 2 maç içeriyor; aynı ligden örnek yok. 25 farklı lig/ülke var; en sık olanlar Avusturya 2. Lig (9), Almanya 3. Lig (3) ve Belçika Challenger (3). Ayrıca 2026 yılındaki maçlar (19/43, %44) örneklemin büyük bölümünü oluşturuyor.
- **İY (n=24):** İY 0,5 üst %70,8 (17/24; model %66,4), İY 0-0 %29,2 (model %33,6), İY/MS 2/2 %33,3 (8/24; model %24,9). Örneklem küçük; model ve tarihsel değerler arasında fark, kesin yorum için yetersiz.

### 5.4 Union de Santa Fe – Defensa y Justicia

**Künye:** Argentina: Liga Profesional · BetExplorer 20:45 / TSİ ≈ 22:45 · Oran 2,20 / 3,15 / 3,37 · Marj %6,9

**Bülten sinyali:** Beraberlik @ 3,15 · tarihsel %39,1 (92 maç) · piyasa %29,7 · avantaj +9,4 puan · Wilson %95 [29,8–49,3] · pencere ±0,05 · bülten kalite etiketi: kesin

**Örneklem:** 92 maç · 28 farklı lig/ülke · aynı ligden 1 maç · 33 farklı oran üçlüsü · yıllar: 2019 (4), 2020 (10), 2021 (11), 2022 (12), 2023 (13), 2024 (16), 2025 (21), 2026 (5)
· en sık oran üçlüsü 2,25/3,10/3,40 (46 maç)

**Duyarlılık: pencere ve çekirdek (yumuşatılmış) tahminler**

| Yöntem | Örneklem (n / neff) | Ev % | Beraberlik % | Deplasman % | Aynı komşuluğun piyasa ort. (Ev / X / Dep) |
|---|---|---|---|---|---|
| Pencere ±0,03 | 10 | 60,0 | 30,0 | 10,0 | 42,5 / 29,7 / 27,8 |
| Pencere ±0,05 | 92 | 38,0 | 39,1 | 22,8 | 42,2 / 30,1 / 27,7 |
| Pencere ±0,08 | 341 | 42,5 | 32,8 | 24,6 | 42,4 / 29,7 / 27,9 |
| Pencere ±0,12 | 802 | 42,1 | 31,8 | 26,1 | 42,5 / 29,6 / 27,9 |
| Pencere ±0,18 | 2913 | 44,4 | 28,9 | 26,7 | 42,5 / 29,5 / 28,0 |
| Pencere ±0,28 | 6893 | 43,7 | 29,2 | 27,1 | 42,7 / 29,3 / 28,0 |
| Çekirdek h = 0,03 | 96 | 45,4 | 32,0 | 22,7 | 42,6 / 29,7 / 27,8 |
| Çekirdek h = 0,05 | 440 | 42,5 | 32,2 | 25,3 | 42,5 / 29,7 / 27,8 |
| Çekirdek h = 0,08 | 1397 | 43,3 | 30,3 | 26,4 | 42,6 / 29,6 / 27,9 |
| Çekirdek h = 0,12 | 3252 | 43,8 | 29,4 | 26,8 | 42,6 / 29,5 / 27,9 |
| Çekirdek h = 0,18 | 6778 | 43,8 | 29,1 | 27,1 | 42,7 / 29,3 / 28,0 |

**1/X/2 karşılaştırması**

| Sonuç | Piyasa % (marjsız) | Adil oran (piyasa) | Tarihsel % (n) [Wilson %95] | Çekirdek h=0,12 % (±) | Model % | Bayes (k=12) % | Küresel bant: gerçekleşen / piyasa ort. |
|---|---|---|---|---|---|---|---|
| Ev | 42,5 | 2,35 | 38,0 (n=92) [28,8–48,3] | 43,8 (±1,7) | 41,3 | 38,6 | 43,3 / 42,5 (n=10.158) |
| Beraberlik | 29,7 | 3,37 | 39,1 (n=92) [29,8–49,3] | 29,4 (±1,6) | 32,3 | 38,0 | 26,9 / 27,5 (n=39.362) |
| Deplasman | 27,8 | 3,60 | 22,8 (n=92) [15,4–32,4] | 26,8 (±1,5) | 26,4 | 23,4 | 27,1 / 27,5 (n=12.091) |

**Tüm pazarlar (tarihsel, Wilson %95, model, adil oran)**

| Kategori | Olay | n | Tarihsel % | %95 aralık | Model % | Adil oran (tarihsel) |
|---|---|---|---|---|---|---|
| Maç sonucu (1X2) | 1 (Ev) | 92 | 38,0 | [28,8–48,3] | 41,3 | 2,63 |
| Maç sonucu (1X2) | X (Beraberlik) | 92 | 39,1 | [29,8–49,3] | 32,3 | 2,56 |
| Maç sonucu (1X2) | 2 (Dep) | 92 | 22,8 | [15,4–32,4] | 26,4 | 4,39 |
| Çifte şans | 1X | 92 | 77,2 | [67,6–84,6] | 73,6 | 1,30 |
| Çifte şans | 12 | 92 | 60,9 | [50,7–70,2] | 67,7 | 1,64 |
| Çifte şans | X2 | 92 | 62,0 | [51,7–71,2] | 58,7 | 1,61 |
| Alt/Üst | 0,5 Üst | 92 | 83,7 | [74,8–89,9] | 88,5 | 1,19 |
| Alt/Üst | 0,5 Alt | 92 | 16,3 | [10,1–25,2] | 11,5 | 6,13 |
| Alt/Üst | 1,5 Üst | 92 | 70,7 | [60,7–79,0] | 71,9 | 1,41 |
| Alt/Üst | 1,5 Alt | 92 | 29,3 | [21,0–39,3] | 28,1 | 3,41 |
| Alt/Üst | 2,5 Üst | 92 | 42,4 | [32,8–52,6] | 43,3 | 2,36 |
| Alt/Üst | 2,5 Alt | 92 | 57,6 | [47,4–67,2] | 56,7 | 1,74 |
| Alt/Üst | 3,5 Üst | 92 | 28,3 | [20,1–38,2] | 22,3 | 3,53 |
| Alt/Üst | 3,5 Alt | 92 | 71,7 | [61,8–79,9] | 77,7 | 1,39 |
| Alt/Üst | 4,5 Üst | 92 | 13,0 | [7,6–21,4] | 9,7 | 7,69 |
| Alt/Üst | 4,5 Alt | 92 | 87,0 | [78,6–92,4] | 90,3 | 1,15 |
| KG ve takım golleri | KG Var | 92 | 55,4 | [45,3–65,2] | 50,9 | 1,81 |
| KG ve takım golleri | KG Yok | 92 | 44,6 | [34,8–54,7] | 49,1 | 2,24 |
| KG ve takım golleri | Ev 0,5 Üst | 92 | 71,7 | [61,8–79,9] | 74,3 | 1,39 |
| KG ve takım golleri | Ev 1,5 Üst | 92 | 40,2 | [30,8–50,4] | 39,4 | 2,49 |
| KG ve takım golleri | Dep 0,5 Üst | 92 | 67,4 | [57,3–76,1] | 65,0 | 1,48 |
| KG ve takım golleri | Dep 1,5 Üst | 92 | 27,2 | [19,1–37,0] | 28,3 | 3,68 |
| Gol aralığı | 0-1 gol | 92 | 29,3 | [21,0–39,3] | 28,1 | 3,41 |
| Gol aralığı | 2-3 gol | 92 | 42,4 | [32,8–52,6] | 49,6 | 2,36 |
| Gol aralığı | 4+ gol | 92 | 28,3 | [20,1–38,2] | 22,3 | 3,53 |
| Handikap / kazanma farkı / iade | Beraberlikte İade (Ev) | 92 | 77,2 | [67,6–84,6] | 73,6 | 1,30 |
| Handikap / kazanma farkı / iade | Beraberlikte İade (Dep) | 92 | 62,0 | [51,7–71,2] | 58,7 | 1,61 |
| Handikap / kazanma farkı / iade | Handikap Ev -1 | 92 | 18,5 | [11,9–27,6] | 20,6 | 5,41 |
| Handikap / kazanma farkı / iade | Handikap Dep +1 | 92 | 62,0 | [51,7–71,2] | 58,7 | 1,61 |
| Handikap / kazanma farkı / iade | Kazanma farkı: Ev 1 gol | 92 | 19,6 | [12,7–28,8] | 20,7 | 5,10 |
| Handikap / kazanma farkı / iade | Kazanma farkı: Ev 2+ gol | 92 | 18,5 | [11,9–27,6] | 20,6 | 5,41 |
| Handikap / kazanma farkı / iade | Kazanma farkı: Dep 1 gol | 92 | 13,0 | [7,6–21,4] | 15,4 | 7,69 |
| Handikap / kazanma farkı / iade | Kazanma farkı: Dep 2+ gol | 92 | 9,8 | [5,2–17,6] | 11,0 | 10,20 |
| Handikap / kazanma farkı / iade | Tek gol (toplam) | 92 | 37,0 | [27,8–47,2] | 44,5 | 2,70 |
| Handikap / kazanma farkı / iade | Çift gol (toplam) | 92 | 63,0 | [52,8–72,2] | 55,5 | 1,59 |
| Handikap / kazanma farkı / iade | Ev 2+ gol atar | 92 | 40,2 | [30,8–50,4] | 39,4 | 2,49 |
| Handikap / kazanma farkı / iade | Dep 2+ gol atar | 92 | 27,2 | [19,1–37,0] | 28,3 | 3,68 |
| Kombinasyonlar | 2,5Ü + KG | 92 | 37,0 | [27,8–47,2] | 35,5 | 2,70 |
| Kombinasyonlar | 2,5A + KG Yok | 92 | 39,1 | [29,8–49,3] | 41,3 | 2,56 |
| Kombinasyonlar | MS 1 + 2,5Ü | 92 | 25,0 | [17,3–34,7] | 23,4 | 4,00 |

**Toplam gol dağılımı**

| Toplam gol | 0 | 1 | 2 | 3 | 4 | 5+ |
|---|---|---|---|---|---|---|
| Tarihsel % | 16,3 | 13,0 | 28,3 | 14,1 | 15,2 | 13,0 |
| Model % | 11,5 | 16,5 | 28,6 | 21,0 | 12,6 | 9,7 |

Örneklem ortalama gol: 2,41 · λ (ev / dep) = 1,36 / 1,05 · İY payı 0,45 · Dixon-Coles ρ = -0,20 (**sınır değer**)

**İlk yarı ve İY/MS**

Bu örneklemde İY skoru verisi yok (n_İY = 0). Aşağıdaki değerler **yalnızca modelden** türetilmiştir.

| Olay | Model % |
|---|---|
| İY 1 (Ev) | 31,9 |
| İY X | 45,4 |
| İY 2 (Dep) | 22,7 |
| İY 0-0 | 34,3 |
| İY 0,5 Üst | 65,7 |
| İY 1,5 Üst | 30,0 |
| İY KG | 17,8 |

| İY/MS | Model % |
|---|---|
| İY 1 → MS 1 | 24,8 |
| İY 1 → MS X | 5,5 |
| İY 1 → MS 2 | 1,6 |
| İY X → MS 1 | 14,3 |
| İY X → MS X | 21,3 |
| İY X → MS 2 | 9,7 |
| İY 2 → MS 1 | 2,1 |
| İY 2 → MS X | 5,5 |
| İY 2 → MS 2 | 15,1 |

**Doğru skor (tarihsel ve modelde en olası skorlar)**

| Skor | Tarihsel % (örneklem) | Model % |
|---|---|---|
| 1 - 1 | 18,5 | 15,4 |
| 0 - 0 | 16,3 | 11,5 |
| 2 - 0 | 7,6 | 8,3 |
| 0 - 1 | 7,6 | 6,9 |
| 2 - 1 | 7,6 | 8,7 |
| 3 - 2 | 6,5 | — |
| 1 - 0 | 5,4 | 9,6 |
| 3 - 1 | 5,4 | 4,0 |
| 1 - 2 | 4,3 | 6,7 |

**Yorum**

- **Neden sinyal?** Beraberlik (3,15) için tarihsel %39,1 (36/92) ve piyasa %29,7; avantaj +9,4 puan, Wilson %95 [29,8–49,3]. Bültendeki "kesin" etiketi yalnızca pencerenin dar olduğunu (±0,05) gösterir; sonucun güvenilir olduğunu göstermez.
- **Sağlamlık:** Beraberlik oranı pencereye göre %30,0 (±0,03, n=10), %39,1 (±0,05, n=92), %32,8 (±0,08, n=341), %31,8 (±0,12, n=802), %28,9 (±0,18, n=2.913). Çekirdek tahminler: h=0,03–0,05'te %32,0–32,2; h=0,08'de %30,3 (piyasa %29,6); h=0,12'de %29,4 (piyasa %29,5). Yani geniş komşulukta fark sıfıra yakın.
- **Oran kümelenmesi:** ±0,05 penceresindeki 92 maçın 46'sı tam olarak aynı oran üçlüsünü (2,25 / 3,10 / 3,40) paylaşıyor; bu kümede beraberlik %41,3. Bu üçlü arşivde toplam 46 maçta, 2019–2024 arasında 44 farklı günde geçiyor. Kalan 46 maçta beraberlik %37,0 — ama bu alt örneklem de çok küçük (±7 puan).
- **Küresel bağlam:** Beraberlik piyasa olasılığı %25–30 olan 39.362 maçta gerçekleşen oran %26,9 (piyasa ort. %27,5). Yani arşiv genelinde beraberlikler, fiyatına göre hafif az geliyor; bu maçın beraberlik lehine küresel bir kanıtı yok.
- **Model:** Model 1/X/2'yi %41,3 / %32,3 / %26,4 veriyor; λ (1,36 / 1,05) örneklemden geliyor ve Dixon-Coles ρ = −0,20 (sınır değer). Model beraberliği biraz yukarı çekiyor, ama bu da örneklemin kendi skor yapısından kaynaklanıyor.
- **İY:** Bu örneklemde hiç İY verisi yok. Tüm İY değerleri yalnızca modelden gelir ve bu nedenle tarihsel doğrulaması yoktur. "1,5Ü + İY 0-0" satırı da İY verisi gerektirdiği için hesaplanamadı.

## 6. Sınırlamalar ve dürüst değerlendirme

1. **Oran zamanı:** Oranlar BetExplorer ana sayfa listesinden alındı; değişebilir. Karar öncesi güncel oran ve kadro bilgisi mutlaka kontrol edilmelidir.
2. **Arşiv tarihi:** Arşiv en geç 11.09.2026'da bitiyor; 12.09–08.10 arası maçlar yok. Bu, son dönemdeki oran-sonuç ilişkilerini kaçırmak anlamına gelir.
3. **Takım gücü yok:** Örneklem yalnızca oran benzerliğine göre seçiliyor. Takım kalitesi, sakatlık, form, ev/deplasman etkisi, motivasyon veya hakem gibi bilgiler hesaba katılmıyor. Piyasa oranı bu bilgileri zaten içerir.
4. **Model bağımsız değil:** Poisson λ değerleri örneklemin gol ortalamalarından alındı; bu nedenle model, tarihsel örneklemin kendisini yeniden üretir. Dixon-Coles ρ iki maçta (Union, Khalidiyah) arama sınırında (±0,20) çıktı; model düzeltmesi aşırı olabilir.
5. **Çoklu karşılaştırma:** 109 maç × 3 sonuç. Bölüm 4'te gösterildiği gibi, piyasa doğru olsa bile kural birkaç sinyal üretir.
6. **Küçük örneklem:** Dar pencerelerde ve çekirdeklerde etkin örneklem 30'un altına düşüyor (ör. Southampton için h=0,03'te neff ≈ 4); İY değerleri 0–24 maça dayanıyor. Bu değerlerdeki yüzde farkları (ör. %0 vs %20) çoğu zaman gürültüdür.
7. **Oran üçlüsü tekrarı:** Arşivde bazı oran üçlüleri sık tekrar ediyor (ör. 2,25 / 3,10 / 3,40 — arşivde 46 maç). Bunun bir kaynak artefaktı (oranların sabit değerlerle kaydedilmesi gibi) olup olmadığı doğrulanmadı; tam eşleşen kümeler bu nedenle ihtiyatla okunmalıdır.
8. **Güven aralıkları:** Yalnızca örnekleme hatasını yansıtır. Veri kaynağı yanlılığı (hangi maçların arşivde olduğu), lig karışımı ve oran değişimi bu aralıklara dahil değildir.
9. **Saat dilimi:** TSİ karşılıkları bülten kalibrasyonuna dayanır; bugün doğrulanmadı.
10. **Bülten hatası (bu raporda düzeltildi):** Bültenin pazar hesabında "BAHİS KOMBİNASYONLARI › 1,5Ü + İY 0-0" satırı, İY verisi olmayan maçlarda İY skorunu 0-0 varsayıyor. Bu yüzden değer şişiyor: Southampton U21 için bülten %50,0 gösterir; İY verisi olan 11 maçta gerçek değer %0,0. Peterborough için %51,3 yerine %11,1 (n=18), Al Khalidiyah için %39,5 yerine %8,3 (n=24). Union Santa Fe'de İY verisi hiç olmadığı için bu satır bu raporda gösterilmedi. Rapordaki değerler yalnızca İY verili maçlarla yeniden hesaplanmıştır. Bülten kodunda (detay.py, tum_pazar, yaklaşık satır 192) aynı düzeltme yapılmalıdır; bu rapor bülten kodunu değiştirmemiştir.

## 7. Sonuç

- Bültenin kuralı bugünkü 109 maçtan 4 sinyal verdi: Southampton U21–QPR U21 (deplasman), Peterborough U21–Nottingham U21 (deplasman), Al Khalidiyah–Al Muharraq (deplasman) ve Union Santa Fe–Defensa y Justicia (beraberlik).
- Sağlamlık testleri, Al Khalidiyah ve Union Santa Fe sinyallerinin büyük ölçüde dar oran penceresine bağlı olduğunu gösteriyor. Southampton ve Peterborough'da deplasman fazlası tutarlı ama zayıf ve küçük örneklemde.
- Kuralın kendisi piyasa doğru olsa bile ortalama ~6,7 sinyal veriyor; 4 sinyal, değer için kanıt sayılmaz.
- Yukarıdaki olasılıklar veriden türetilmiş tahminlerdir; piyasa oranlarından anlamlı biçimde ayrılacak kadar güçlü bir kanıt yoktur. **Bahis kararı için kullanılmamalıdır.**

## Ek A — 09.10.2026 listesindeki 109 maçın taraması

Bültenin sinyal kuralı, BetExplorer listesindeki tüm 109 maça uygulandı. Sıralama: önce sinyal, sonra avantaj. TSİ = BetExplorer saati + 2 saat (bülten kalibrasyonu).
*Not:* Analiz sırasında TSİ yaklaşık 10:40 idi. TSİ sütununda 10:40'tan önceki saatler (ör. 08:00 BetExplorer = 10:00 TSİ) analiz anında başlamış ya da bitmiş olabilir; bu maçlar seçimi etkilemedi, çünkü dört sinyalin tamamı 12:00 ve sonrasındadır.


| # | BetExplorer / TSİ | Lig | Ev – Deplasman | Oran 1/X/2 | n | Pencere | En iyi sonuç | Tarihsel % | Piyasa % | Avantaj | Sinyal |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 14:00 / 16:00 | Premier League Cup | Southampton U21 – QPR U21 | 1,46 / 4,80 / 4,80 | 26 | ±0,12 | Deplasman | 42,3 | 18,9 | +23,4 | **EVET** |
| 2 | 14:00 / 16:00 | Premier League Cup | Peterborough U21 – Nottingham U21 | 3,20 / 4,10 / 1,84 | 39 | ±0,12 | Deplasman | 71,8 | 49,4 | +22,4 | **EVET** |
| 3 | 12:00 / 14:00 | Premier League | Al Khalidiyah – Al Muharraq | 2,14 / 3,55 / 2,85 | 43 | ±0,05 | Deplasman | 51,2 | 31,9 | +19,3 | **EVET** |
| 4 | 20:45 / 22:45 | Liga Profesional | Union de Santa Fe – Defensa y Justicia | 2,20 / 3,15 / 3,37 | 92 | ±0,05 | Beraberlik | 39,1 | 29,7 | +9,4 | **EVET** |
| 5 | 14:00 / 16:00 | Premier League Cup | Cardiff U21 – Leicester U21 | 2,32 / 4,00 / 2,37 | 12 | ±0,08 | Ev | 75,0 | 39,1 | +35,9 | hayır |
| 6 | 14:00 / 16:00 | Premier League Cup | Brighton U21 – Sheffield Utd U21 | 1,63 / 4,30 / 3,95 | 15 | ±0,08 | Deplasman | 46,7 | 23,0 | +23,6 | hayır |
| 7 | 11:00 / 13:00 | ChNL | Slavia Prague B – Vlasim | 2,15 / 3,52 / 2,73 | 17 | ±0,05 | Ev | 64,7 | 41,7 | +23,0 | hayır |
| 8 | 09:00 / 11:00 | Leumit League | Ironi Modiin – Hapoel Afula | 2,73 / 3,30 / 2,24 | 17 | ±0,05 | Beraberlik | 47,1 | 27,2 | +19,9 | hayır |
| 9 | 12:30 / 14:30 | Esiliiga | Tartu Welco – Elva | 1,68 / 4,00 / 3,63 | 12 | ±0,05 | Beraberlik | 41,7 | 22,3 | +19,4 | hayır |
| 10 | 14:00 / 16:00 | Premier League Cup | Reading U21 – Norwich U21 | 2,33 / 4,20 / 2,33 | 12 | ±0,12 | Deplasman | 58,3 | 39,1 | +19,2 | hayır |
| 11 | 14:00 / 16:00 | Ligue 2 | Sochaux – Boulogne | 2,23 / 3,13 / 3,10 | 24 | ±0,03 | Ev | 58,3 | 41,1 | +17,2 | hayır |
| 12 | 14:00 / 16:00 | Premier League Cup | Leeds U21 – Stockport U21 | 1,64 / 4,40 / 3,75 | 35 | ±0,12 | Ev | 71,4 | 55,2 | +16,2 | hayır |
| 13 | 14:00 / 16:00 | Premier League Cup | Stoke City U21 – Charlton U21 | 2,45 / 4,10 / 2,24 | 23 | ±0,12 | Deplasman | 56,5 | 40,6 | +15,9 | hayır |
| 14 | 14:00 / 16:00 | Ligue 2 | Nancy – Guingamp | 1,93 / 3,38 / 3,62 | 30 | ±0,03 | Ev | 63,3 | 47,5 | +15,8 | hayır |
| 15 | 11:00 / 13:00 | Esiliiga | Nomme Utd U21 – Levadia U21 | 2,50 / 3,95 / 2,15 | 21 | ±0,08 | Deplasman | 57,1 | 41,6 | +15,6 | hayır |
| 16 | 14:00 / 16:00 | Premier League Cup | Millwall U21 – West Ham U21 | 3,15 / 4,10 / 1,85 | 31 | ±0,12 | Deplasman | 64,5 | 49,1 | +15,5 | hayır |
| 17 | 12:30 / 14:30 | 2. Liga | Amstetten – BW Linz | 2,88 / 3,50 / 2,14 | 38 | ±0,05 | Deplasman | 57,9 | 42,5 | +15,4 | hayır |
| 18 | 12:30 / 14:30 | 2. Bundesliga | Heidenheim – Kaiserslautern | 1,93 / 3,75 / 3,50 | 19 | ±0,03 | Deplasman | 42,1 | 26,7 | +15,4 | hayır |
| 19 | 09:00 / 11:00 | Leumit League | H. Akko – Maccabi Bnei Raina | 6,20 / 4,37 / 1,40 | 14 | ±0,12 | Beraberlik | 35,7 | 20,7 | +15,0 | hayır |
| 20 | 08:00 / 10:00 | Premier League | Araz – Kapaz | 2,12 / 3,45 / 2,88 | 14 | ±0,03 | Ev | 57,1 | 42,5 | +14,6 | hayır |
| 21 | 08:00 / 10:00 | Premier League | Eastern AA – North District | 3,65 / 3,95 / 1,71 | 18 | ±0,08 | Ev | 38,9 | 24,6 | +14,2 | hayır |
| 22 | 14:45 / 16:45 | Division 1 | UC Dublin – Longford | 1,70 / 3,78 / 3,90 | 21 | ±0,05 | Beraberlik | 38,1 | 23,9 | +14,2 | hayır |
| 23 | 14:00 / 16:00 | Challenger Pro League | Dender – Club Brugge U23 | 1,43 / 4,28 / 5,53 | 26 | ±0,08 | Ev | 76,9 | 62,8 | +14,1 | hayır |
| 24 | 12:30 / 14:30 | 2. Bundesliga | Braunschweig – Holstein Kiel | 2,82 / 3,72 / 2,25 | 23 | ±0,05 | Beraberlik | 39,1 | 25,2 | +14,0 | hayır |
| 25 | 09:00 / 11:00 | Carioca U20 | Boavista U20 – Bangu U20 | 2,85 / 3,20 / 2,27 | 19 | ±0,03 | Beraberlik | 42,1 | 28,3 | +13,8 | hayır |
| 26 | 19:00 / 21:00 | Primera A | Alianza – Aguilas Doradas | 2,41 / 3,15 / 2,85 | 13 | ±0,03 | Deplasman | 46,2 | 32,4 | +13,8 | hayır |
| 27 | 14:00 / 16:00 | Premier League Cup | Wolves U21 – Fleetwood U21 | 1,31 / 5,60 / 6,40 | 12 | ±0,12 | Ev | 83,3 | 69,5 | +13,8 | hayır |
| 28 | 14:00 / 16:00 | Ligue 2 | Pau FC – Laval | 2,00 / 3,32 / 3,48 | 22 | ±0,03 | Ev | 59,1 | 45,9 | +13,2 | hayır |
| 29 | 16:00 / 18:00 | Primera B | Real Cundinamarca – Real Santander | 1,51 / 4,00 / 5,20 | 23 | ±0,05 | Deplasman | 30,4 | 17,4 | +13,0 | hayır |
| 30 | 14:45 / 16:45 | Division 1 | Cobh Ramblers – Kerry | 2,27 / 3,25 / 2,73 | 21 | ±0,03 | Ev | 52,4 | 39,5 | +12,9 | hayır |
| 31 | 12:00 / 14:00 | Premier League | Malkia – Al Riffa | 8,60 / 5,20 / 1,27 | 13 | ±0,12 | Deplasman | 84,6 | 71,8 | +12,8 | hayır |
| 32 | 20:00 / 22:00 | Primera Division | Inca Aruba – Platense Municipal | 2,70 / 2,95 / 2,55 | 31 | ±0,05 | Deplasman | 48,4 | 35,6 | +12,8 | hayır |
| 33 | 14:00 / 16:00 | Eredivisie | PSV – Heerenveen | 1,27 / 6,53 / 8,20 | 15 | ±0,28 | Beraberlik | 26,7 | 14,4 | +12,3 | hayır |
| 34 | 07:35 / 09:35 | Super League | Shenzhen Xinpengcheng – Henan Songshan Longmen | 2,73 / 3,50 / 2,29 | 13 | ±0,03 | Beraberlik | 38,5 | 26,2 | +12,2 | hayır |
| 35 | 08:30 / 10:30 | Division 2 A | WE SC – El Mansoura | 2,03 / 2,80 / 4,00 | 16 | ±0,05 | Ev | 56,2 | 44,8 | +11,5 | hayır |
| 36 | 13:00 / 15:00 | Superliga | Nordsjaelland – Odense | 1,48 / 4,68 / 5,30 | 32 | ±0,08 | Beraberlik | 31,2 | 19,8 | +11,4 | hayır |
| 37 | 09:00 / 11:00 | Leumit League | Kiryat Gat – Kiryat Yam | 3,45 / 3,55 / 1,85 | 15 | ±0,05 | Deplasman | 60,0 | 48,6 | +11,4 | hayır |
| 38 | 15:00 / 17:00 | LaLiga | Malaga – Espanyol | 2,81 / 3,19 / 2,59 | 20 | ±0,03 | Ev | 45,0 | 33,7 | +11,3 | hayır |
| 39 | 14:00 / 16:00 | Ligue 2 | Dunkerque – Annecy | 2,19 / 3,37 / 2,98 | 13 | ±0,03 | Beraberlik | 38,5 | 27,3 | +11,2 | hayır |
| 40 | 14:45 / 16:45 | National League | Sutton – Boreham Wood | 4,20 / 3,85 / 1,73 | 58 | ±0,08 | Deplasman | 63,8 | 53,7 | +10,1 | hayır |
| 41 | 11:30 / 13:30 | Premier League | Neftci Baku – Sabah Baku | 2,65 / 3,23 / 2,36 | 27 | ±0,05 | Deplasman | 48,1 | 38,2 | +10,0 | hayır |
| 42 | 04:30 / 06:30 | Super League | Persik Kediri – Madura United | 2,38 / 3,30 / 2,65 | 40 | ±0,05 | Beraberlik | 37,5 | 27,5 | +10,0 | hayır |
| 43 | 14:45 / 16:45 | FAI Cup | Bohemians – Waterford | 1,53 / 4,05 / 4,75 | 28 | ±0,05 | Beraberlik | 32,1 | 22,2 | +9,9 | hayır |
| 44 | 09:30 / 11:30 | Persian Gulf Pro League | Persepolis – Sanat Naft | 1,28 / 4,80 / 9,40 | 26 | ±0,12 | Ev | 80,8 | 71,3 | +9,5 | hayır |
| 45 | 12:00 / 14:00 | HNL | Gorica – Rudes | 1,59 / 3,80 / 4,88 | 15 | ±0,05 | Beraberlik | 33,3 | 24,0 | +9,3 | hayır |
| 46 | 12:00 / 14:00 | Chance Liga | Zlin – Slavia Prague | 9,32 / 5,30 / 1,28 | 22 | ±0,18 | Deplasman | 81,8 | 72,5 | +9,3 | hayır |
| 47 | 14:00 / 16:00 | Liga Pro | Libertad – Leones del Norte | 2,38 / 3,02 / 2,84 | 38 | ±0,05 | Ev | 47,4 | 38,1 | +9,3 | hayır |
| 48 | 14:00 / 16:00 | Premier League Cup | Burnley U21 – Preston U21 | 1,75 / 4,20 / 3,45 | 14 | ±0,08 | Deplasman | 35,7 | 26,4 | +9,3 | hayır |
| 49 | 17:00 / 19:00 | Liga Profesional | Gimnasia L.P. – Atl. Tucuman | 1,91 / 3,23 / 4,23 | 57 | ±0,05 | Ev | 57,9 | 49,0 | +8,9 | hayır |
| 50 | 14:00 / 16:00 | Premier League Cup | Ipswich U21 – West Brom U21 | 2,08 / 4,00 / 2,70 | 21 | ±0,08 | Ev | 52,4 | 43,7 | +8,7 | hayır |
| 51 | 12:45 / 14:45 | Stars League | Al Naft – Diyala | 1,98 / 3,05 / 3,70 | 39 | ±0,05 | Beraberlik | 38,5 | 29,7 | +8,7 | hayır |
| 52 | 15:15 / 17:15 | Liga Portugal | Braga – Sporting CP | 3,00 / 3,30 / 2,30 | 38 | ±0,03 | Ev | 39,5 | 31,1 | +8,4 | hayır |
| 53 | 13:00 / 15:00 | 1st Division | AB Copenhagen – Aarhus Fremad | 2,08 / 3,43 / 3,08 | 48 | ±0,05 | Ev | 52,1 | 43,8 | +8,3 | hayır |
| 54 | 23:00 / 01:00 (+1g) | Liga MX | Tigres UANL – Toluca | 2,84 / 3,58 / 2,28 | 61 | ±0,05 | Deplasman | 49,2 | 41,0 | +8,2 | hayır |
| 55 | 12:00 / 14:00 | 1st Division | Vejle – Hvidovre IF | 1,66 / 3,90 / 4,23 | 19 | ±0,05 | Ev | 63,2 | 55,0 | +8,2 | hayır |
| 56 | 13:00 / 15:00 | Premier League | Gaborone Utd – Morupule | 1,53 / 3,45 / 5,80 | 12 | ±0,08 | Ev | 66,7 | 58,6 | +8,1 | hayır |
| 57 | 11:00 / 13:00 | Veikkausliiga | SJK – Lahti | 2,52 / 3,43 / 2,44 | 34 | ±0,05 | Ev | 44,1 | 36,1 | +8,0 | hayır |
| 58 | 15:00 / 17:00 | Championship | West Ham – QPR | 1,47 / 4,61 / 6,00 | 17 | ±0,08 | Deplasman | 23,5 | 15,7 | +7,9 | hayır |
| 59 | 08:30 / 10:30 | Division 2 A | Team FC – Pharco | 3,25 / 2,75 / 2,32 | 13 | ±0,05 | Deplasman | 46,2 | 39,1 | +7,1 | hayır |
| 60 | 09:30 / 11:30 | Prva NL | Mladost Zdralovi – Cibalia | 2,10 / 3,15 / 3,05 | 69 | ±0,08 | Deplasman | 36,2 | 29,2 | +7,0 | hayır |
| 61 | 14:00 / 16:00 | Premier League Cup | Birmingham U21 – Huddersfield U21 | 2,08 / 3,95 / 2,75 | 20 | ±0,08 | Deplasman | 40,0 | 33,1 | +6,9 | hayır |
| 62 | 14:45 / 16:45 | Division 1 | Bray – Wexford | 1,54 / 4,15 / 4,55 | 14 | ±0,05 | Beraberlik | 28,6 | 21,7 | +6,9 | hayır |
| 63 | 12:00 / 14:00 | Cyprus League | Karmiotissa – Omonia | 11,00 / 6,20 / 1,18 | 31 | ±0,28 | Deplasman | 83,9 | 77,1 | +6,8 | hayır |
| 64 | 21:10 / 23:10 | Primera A | Once Caldas – Llaneros | 1,52 / 4,00 / 5,80 | 57 | ±0,05 | Beraberlik | 29,8 | 23,1 | +6,7 | hayır |
| 65 | 14:30 / 16:30 | Bundesliga | Dortmund – Werder Bremen | 1,30 / 5,83 / 8,41 | 24 | ±0,12 | Ev | 79,2 | 72,6 | +6,6 | hayır |
| 66 | 09:00 / 11:00 | Prva NL | Sesvete – Jadran LP | 2,18 / 3,05 / 2,95 | 62 | ±0,08 | Beraberlik | 35,5 | 29,1 | +6,4 | hayır |
| 67 | 09:15 / 11:15 | Persian Gulf Pro League | Chadormalu – Kheybar Khorramabad | 2,42 / 2,85 / 2,95 | 34 | ±0,05 | Beraberlik | 38,2 | 31,8 | +6,4 | hayır |
| 68 | 12:45 / 14:45 | Ligue 1 | Kabylie – ASO Chlef | 1,43 / 3,90 / 6,25 | 29 | ±0,12 | Ev | 69,0 | 62,7 | +6,3 | hayır |
| 69 | 21:00 / 23:00 | Liga MX | Puebla – Club Leon | 2,83 / 3,35 / 2,40 | 85 | ±0,05 | Beraberlik | 34,1 | 27,9 | +6,2 | hayır |
| 70 | 12:00 / 14:00 | Prva NL | Karlovac – Bijelo Brdo | 2,45 / 3,00 / 2,63 | 15 | ±0,05 | Deplasman | 40,0 | 33,9 | +6,1 | hayır |
| 71 | 14:00 / 16:00 | Premier League Cup | Newcastle Utd U21 – Luton U21 | 1,46 / 5,20 / 4,50 | 19 | ±0,28 | Deplasman | 26,3 | 20,2 | +6,1 | hayır |
| 72 | 09:00 / 11:00 | Leumit League | M. Herzliya – M. Nazareth | 1,83 / 3,43 / 3,73 | 33 | ±0,05 | Deplasman | 30,3 | 24,2 | +6,1 | hayır |
| 73 | 12:00 / 14:00 | Vysshaya Liga | Arsenal Dzerzhinsk – Dynamo Brest | 5,75 / 3,95 / 1,47 | 43 | ±0,12 | Deplasman | 67,4 | 61,4 | +6,0 | hayır |
| 74 | 15:00 / 17:00 | Division Profesional | SA Bulo Bulo – Tomayapo | 1,65 / 3,75 / 4,23 | 30 | ±0,05 | Beraberlik | 30,0 | 24,0 | +6,0 | hayır |
| 75 | 08:30 / 10:30 | Division 2 A | El Ismaily – Tanta | 2,11 / 2,85 / 3,65 | 26 | ±0,05 | Deplasman | 30,8 | 24,9 | +5,8 | hayır |
| 76 | 12:00 / 14:00 | Prva Liga RS | Potkozarje – Slavija | 1,52 / 3,65 / 5,75 | 14 | ±0,05 | Deplasman | 21,4 | 15,7 | +5,7 | hayır |
| 77 | 12:00 / 14:00 | ChNL | Usti nad Labem – Opava | 1,94 / 3,43 / 3,23 | 18 | ±0,05 | Deplasman | 33,3 | 27,7 | +5,6 | hayır |
| 78 | 14:00 / 16:00 | Ligue 2 | Montpellier – Grenoble | 1,58 / 3,67 / 5,38 | 22 | ±0,08 | Ev | 63,6 | 58,0 | +5,6 | hayır |
| 79 | 13:45 / 15:45 | Liga Portugal | Moreirense – Gil Vicente | 3,57 / 3,18 / 2,10 | 38 | ±0,05 | Deplasman | 50,0 | 44,5 | +5,5 | hayır |
| 80 | 18:30 / 20:30 | Liga Profesional | Instituto – Boca Juniors | 2,94 / 2,91 / 2,62 | 17 | ±0,05 | Deplasman | 41,2 | 35,8 | +5,4 | hayır |
| 81 | 13:00 / 15:00 | Super Lig | Galatasaray – Kasimpasa | 1,27 / 5,45 / 9,10 | 36 | ±0,12 | Beraberlik | 22,2 | 17,0 | +5,2 | hayır |
| 82 | 11:00 / 13:00 | Stars League | Zakho – Newroz | 2,75 / 2,55 / 2,85 | 32 | ±0,12 | Beraberlik | 40,6 | 35,4 | +5,2 | hayır |
| 83 | 08:00 / 10:00 | Super League | Isenmulang Kalteng – Persebaya | 5,80 / 4,60 / 1,40 | 43 | ±0,12 | Deplasman | 69,8 | 64,7 | +5,1 | hayır |
| 84 | 04:30 / 06:30 | Championship | Persipura Jayapura – RANS Nusantara | 1,51 / 3,85 / 5,00 | 25 | ±0,08 | Ev | 64,0 | 59,0 | +5,0 | hayır |
| 85 | 15:00 / 17:00 | Ligue 1 | MC Alger – CR Temouchent | 1,20 / 5,25 / 12,50 | 108 | ±0,70 | Deplasman | 12,0 | 7,2 | +4,8 | hayır |
| 86 | 14:45 / 16:45 | Ligue 1 | Lens – Lyon | 2,33 / 3,65 / 2,81 | 55 | ±0,05 | Deplasman | 38,2 | 33,6 | +4,6 | hayır |
| 87 | 14:45 / 16:45 | Division 1 | Athlone – Treaty United | 1,41 / 4,40 / 5,88 | 16 | ±0,08 | Beraberlik | 25,0 | 20,5 | +4,5 | hayır |
| 88 | 13:00 / 15:00 | 3. Liga | Preussen Munster – RW Essen | 3,45 / 3,60 / 1,96 | 64 | ±0,05 | Ev | 31,2 | 26,9 | +4,4 | hayır |
| 89 | 08:00 / 10:00 | Super League | Zhejiang Professional – Shanghai Port | 2,39 / 3,90 / 2,42 | 18 | ±0,08 | Beraberlik | 27,8 | 23,6 | +4,2 | hayır |
| 90 | 13:30 / 15:30 | Stars League | Al Gharraf – Al Golan | 2,45 / 2,85 / 2,90 | 34 | ±0,05 | Ev | 41,2 | 37,0 | +4,2 | hayır |
| 91 | 13:30 / 15:30 | Liga Profesional | Aldosivi – Sarmiento Junin | 2,55 / 3,00 / 2,97 | 31 | ±0,03 | Beraberlik | 35,5 | 31,4 | +4,1 | hayır |
| 92 | 07:35 / 09:35 | Super League | Qingdao Hainiu – Beijing Guoan | 6,03 / 4,83 / 1,42 | 36 | ±0,12 | Ev | 19,4 | 15,4 | +4,0 | hayır |
| 93 | 17:00 / 19:00 | Liga Nacional | Platense – Juticalpa | 1,90 / 3,28 / 3,58 | 37 | ±0,05 | Ev | 51,4 | 47,4 | +4,0 | hayır |
| 94 | 14:00 / 16:00 | Challenger Pro League | Anderlecht U23 – Eupen | 3,40 / 3,67 / 1,82 | 32 | ±0,08 | Deplasman | 53,1 | 49,2 | +3,9 | hayır |
| 95 | 12:30 / 14:30 | 2. Liga | Kapfenberg – Austria Vienna (Am) | 2,80 / 3,53 / 2,20 | 33 | ±0,05 | Ev | 36,4 | 32,6 | +3,7 | hayır |
| 96 | 09:30 / 11:30 | Prva NL | Opatija – Kustosija | 2,10 / 3,10 / 3,10 | 13 | ±0,05 | Ev | 46,2 | 42,5 | +3,7 | hayır |
| 97 | 12:00 / 14:00 | ChNL | Jihlava – Prostejov | 1,64 / 3,67 / 4,38 | 43 | ±0,08 | Beraberlik | 27,9 | 24,5 | +3,4 | hayır |
| 98 | 14:45 / 16:45 | Division 1 | Cork City – Finn Harps | 1,14 / 7,68 / 11,50 | 12 | ±0,45 | Ev | 83,3 | 80,2 | +3,2 | hayır |
| 99 | 12:00 / 14:00 | ChNL | Taborsko – Karvina | 2,95 / 3,33 / 2,09 | 61 | ±0,08 | Deplasman | 45,9 | 42,8 | +3,1 | hayır |
| 100 | 09:00 / 11:00 | Leumit League | MS Kafr Qasim – Bnei Yehuda | 5,33 / 4,30 / 1,45 | 40 | ±0,12 | Ev | 20,0 | 16,9 | +3,1 | hayır |
| 101 | 14:30 / 16:30 | 2. Liga | First Vienna – St. Polten | 2,06 / 3,35 / 3,10 | 40 | ±0,05 | Beraberlik | 30,0 | 27,0 | +3,0 | hayır |
| 102 | 12:00 / 14:00 | WWIN Liga BiH | Velez Mostar – Siroki Brijeg | 2,06 / 3,05 / 3,25 | 56 | ±0,08 | Beraberlik | 32,1 | 29,2 | +2,9 | hayır |
| 103 | 08:30 / 10:30 | Division 2 A | El Entag El Harby – La Viena | 2,04 / 2,90 / 3,75 | 36 | ±0,05 | Ev | 47,2 | 44,5 | +2,7 | hayır |
| 104 | 14:45 / 16:45 | Jupiler Pro League | Beveren – Lommel SK | 1,82 / 3,72 / 3,90 | 29 | ±0,05 | Beraberlik | 27,6 | 25,0 | +2,6 | hayır |
| 105 | 08:00 / 10:00 | Championship | PSIS Semarang – Persiraja Aceh | 1,44 / 3,95 / 5,80 | 28 | ±0,08 | Beraberlik | 25,0 | 22,6 | +2,4 | hayır |
| 106 | 19:00 / 21:00 | Copa do Brasil U20 | Palmeiras U20 – Santos U20 | 1,63 / 3,85 / 4,40 | 22 | ±0,05 | Deplasman | 22,7 | 20,7 | +2,1 | hayır |
| 107 | 08:30 / 10:30 | Division 2 A | Maleyeit Kafr El Zayiat – Baladiyat El Mahalla | 2,46 / 2,60 / 3,20 | 18 | ±0,08 | Ev | 38,9 | 36,8 | +2,1 | hayır |
| 108 | 14:45 / 16:45 | Premier Division | Shelbourne – Sligo Rovers | 1,30 / 4,83 / 8,10 | 98 | ±0,12 | Deplasman | 13,3 | 11,2 | +2,0 | hayır |
| 109 | 16:30 / 18:30 | Liga Pro | Delfin – Mushuc Runa | 2,11 / 3,05 / 3,27 | 26 | ±0,05 | Beraberlik | 30,8 | 29,6 | +1,2 | hayır |

*Not:* "Avantaj" = tarihsel − piyasa (normalize edilmiş). Sinyal = n ≥ 18, Wilson alt sınır > piyasa, avantaj ≥ 3 ve pencere ≤ 0,20.

## Ek B — Veri ve hesap kaynakları

- Maç listesi: BetExplorer ana sayfası (09.10.2026). Oranlar 1/X/2 olarak bu listeden alındı.
- Arşiv: `bulten-paket.zip` içindeki `veri/all_matches.json` (76.208 maç, 1/X/2 oranlı; en geç 11.09.2026). İY skorları: `veri/ht_cache.json`.
- Bülten hesap kodu: `tam_tarama.py` (karsilastir, eslesen, wilson), `detay.py` (grup_detay, tum_pazar, kucult), `bulten_v3.py` (model_pazar, bootstrap). Bülten dosyaların kendisi değiştirilmedi. `bulten_v3.py` Python 3.11 ile ayrıştırılamadığı için model_pazar ve bootstrap fonksiyonları metin olarak ayıklanıp çalıştırıldı; veri yolları bir harness (hat.py) üzerinden yönlendirildi.
- Yeni eklenen kontroller: pencere duyarlılığı, Gauss çekirdek tahminleri, küresel kalibrasyon bantları, sinyal kuralının çoklu karşılaştırma simülasyonu.
- Bülten hatası: `detay.py` › `tum_pazar` içinde İY gerektirmeyen kategoriler `c.get("ht_h", 0)` ile çağrılıyor; İY verisi olmayan maçlarda İY 0-0 varsayılıyor. Yalnızca "1.5Ü + İY 0-0" satırı bu hatadan etkileniyor (diğer İY satırları İY verili maçlarla hesaplanıyor).
- Bu analiz kodu ve ara dosyaları repoda değil, çalışma ortamında tutulmuştur.

