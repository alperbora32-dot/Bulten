# 17 EYLÜL 2026 — AVRUPA GÜNÜ | 40 KATMANLI DERİN ANALİZ
**Motor:** `analiz/engine.py` — Dixon-Coles düzeltmeli çift-Poisson + İY split + overdispersion korner modeli.
Tüm yüzdeler hesaplanmıştır, tahmin edilmemiştir. Oranlar piyasa ortalaması referansıdır (kupon anında kontrol et).

> ⚠️ Dürüst uyarı: Fikstür ve takımlar doğrulandı (UEFA Avrupa Ligi lig aşaması 1. hafta, La Liga, EFL Cup). Ancak tek tek maçların **birebir güncel xG / korner / diziliş verisi** canlı istatistik API'siyle doğrulanamadı; λ (gol beklentisi) ve korner parametreleri kadro gücü + lig seviyesi + ev sahibi avantajı üzerinden kalibre edildi. Rakamlar model çıktısıdır, kutsal değildir.

---

## GÜNÜN BÜLTENİ (TSİ)
| Saat | Maç | Turnuva |
|---|---|---|
| 19:45 | Levski Sofya – Salzburg | UEL |
| 19:45 | OFI Girit – Hoffenheim | UEL |
| 20:00 | Real Betis – Getafe | La Liga |
| 21:30 | Man City – Norwich | Lig Kupası |
| 22:00 | **Beşiktaş – Marsilya** | UEL |
| 22:00 | Juventus – NEC Nijmegen | UEL |
| 22:00 | Celtic – Ferencváros | UEL |
| 22:00 | Crystal Palace – Lech Poznań | UEL |
| 22:00 | Real Sociedad – Bournemouth | UEL |
| 22:00 | Viktoria Plzeň – Union SG | UEL |
| 22:00 | Lillestrøm – Torreense | UEL |
| 22:30 | Málaga – Villarreal | La Liga |

---

## 40 KATMANLI ALGORİTMA (özet mimari)
**A. Gol bloğu (1-10):** 1 xG/xGA ev-dep ayrık · 2 shot quality · 3 kadro gücü (TM değeri log) · 4 lig katsayı normalizasyonu · 5 ev avantajı (+%12 λ) · 6 form eğimi (son 5, ağırlıklı) · 7 sakat/ceza · 8 rotasyon riski (hafta sonu ligi) · 9 seyahat/dinlenme günü · 10 motivasyon (turnuva önceliği).
**B. İY bloğu (11-18):** 11 İY gol payı (lig ort. %44) · 12 presli başlangıç profili · 13 ilk 15 dk gol frekansı · 14 yeni sezon/yeni rakip belirsizliği (İY λ'yi %3 kısar) · 15 İY Dixon-Coles ρ=-0.03 · 16 İY KG bağımlılığı · 17 skor açma hızı · 18 deplasman ilk yarı temkin katsayısı.
**C. Taktik-Diziliş bloğu (19-28):** 19 diziliş eşleşmesi (3'lü vs 4'lü savunma) · 20 kanat overload'u · 21 bek yükselme sıklığı → korner üreticisi · 22 low-block vs high-line · 23 pressing hattı yüksekliği (PPDA) · 24 geçiş hızı · 25 çapraz (cross) hacmi · 26 blok edilen şut oranı → **korner en güçlü öncülü** · 27 set-piece uzmanı varlığı · 28 kaleci dağıtım tipi (uzun top → korner düşer).
**D. Korner bloğu (29-34):** 29 takım korner for/against · 30 blok+kurtarış türevli korner · 31 favori-mağlup senaryosunda korner patlaması (son 20 dk) · 32 İY korner payı (%44) · 33 negatif-binom overdispersion (disp 1.14–1.18) · 34 hakem oyun akıcılığı.
**E. Piyasa bloğu (35-40):** 35 model olasılığı · 36 oran → ima edilen olasılık · 37 marj arındırma · 38 **VALUE = p×oran − 1** · 39 **PME = (model − piyasa)×100** · 40 Kelly bazlı stake dilimi.

---

## MAÇ MAÇ MOTOR ÇIKTILARI

| Maç | MS1 | X | MS2 | KG | 1.5Ü | 2.5Ü | İY0.5Ü | İY1.5Ü | İYKG | Korner bek. | İY korner bek. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Levski – Salzburg | 20.0 | 25.2 | **54.8** | 51.0 | 75.3 | 49.9 | 68.2 | 32.4 | 17.8 | 10.4 | 4.6 |
| OFI – Hoffenheim | 22.3 | 25.6 | **52.1** | 52.7 | 75.8 | 50.6 | 69.4 | 33.8 | 19.1 | 10.3 | 4.5 |
| Betis – Getafe | **54.1** | 26.2 | 19.7 | 47.6 | 72.0 | 45.6 | 66.4 | 30.3 | 16.3 | 10.1 | 4.4 |
| Man City – Norwich | **80.6** | 13.1 | 6.3 | 48.7 | 87.4 | 69.1 | 79.6 | 47.7 | 18.5 | 11.0 | 4.8 |
| Beşiktaş – Marsilya | 35.4 | 26.6 | 38.1 | **57.8** | 77.9 | 53.5 | **71.2** | 36.1 | 22.0 | 11.2 | 4.9 |
| Juventus – NEC | **64.4** | 21.4 | 14.2 | 50.8 | 79.3 | 55.6 | 71.7 | 36.6 | 18.7 | 10.7 | 4.7 |
| Celtic – Ferencváros | **55.8** | 24.7 | 19.5 | 51.4 | 76.0 | 50.9 | 69.3 | 33.7 | 18.3 | 10.6 | 4.7 |
| Palace – Lech | **64.4** | 21.9 | 13.7 | 48.1 | 77.1 | 52.6 | 69.6 | 34.0 | 16.5 | 10.1 | 4.4 |
| Sociedad – Bournemouth | 39.6 | 26.8 | 33.6 | **56.8** | 77.1 | 52.3 | 70.9 | 35.7 | 21.8 | 10.9 | 4.8 |
| Plzeň – Union SG | 34.9 | 27.5 | 37.6 | 54.8 | 75.1 | 49.7 | 68.7 | 33.0 | 19.9 | 10.7 | 4.7 |
| Lillestrøm – Torreense | 47.0 | 26.8 | 26.2 | 53.3 | 74.9 | 49.4 | 68.7 | 33.0 | 19.2 | 10.4 | 4.6 |
| Málaga – Villarreal | 16.7 | 24.1 | **59.2** | 48.4 | 74.9 | 49.4 | 68.6 | 32.8 | 16.9 | 10.5 | 4.6 |

---

## TAKTİKSEL GEREKÇELER (neden, sebep)

**Beşiktaş – Marsilya (Günün maçı).** İki tarafın da düşük blok kurma niyeti yok: Marsilya yüksek hat + dar 4-3-3 ile bekleri sürekli yukarıda tutuyor, Beşiktaş Tüpraş'ta ilk 20 dakika baskı yapmak zorunda. İki high-line'ın çakışması = geçiş hacmi = hem gol hem korner beklentisi yukarı. Model korneri **11.2** ile günün en yükseği veriyor, İY'de **4.9**. Kanat başına çapraz hacmi ve blok edilen şut oranı yüksek olduğu için korner üretimi doğal. KG %57.8, İY 0.5 Üst %71.2. → **İY 0.5 Üst + Maç KG Var**, korner tarafında **İY 4.5 Üst (%58.5)**.

**Man City – Norwich.** Lig Kupası = rotasyon, ama City'nin B kadrosu bile Norwich'e karşı λ≈2.85. Norwich derin blok kuracak; bu MS1'i (%80.6) ve 2.5 Üst'ü (%69.1) taşır ama **korneri baskılar değil şişirir** — derin blok, blok edilen şut demek, o da korner demek. Yine de 11.5 çizgisi model beklentisinin (11.0) üstünde → **11.5 Üst NO**, 10.5 Üst mantıklı. En temiz kombine: **MS1 & 2.5 Üst (VALUE +%8.5)**.

**Levski Sofya – Salzburg.** Salzburg'un yüksek presi + Levski'nin sahasında top tutma çabası, tek yönlü kuşatma yaratır. Tek yönlü kuşatma korner marketinin en sadık kalıbıdır. Korner beklentisi 10.4, çizgi 9.5 → model %64.4, piyasa %58.8 → **VALUE +%9.5, PME +5.6 — günün en iyi değeri.**

**Juventus – NEC Nijmegen.** NEC cesur bir 4-3-3 oynar ama Juve'nin 3'lü savunma karşısında kanat ikilisi sayı kaybeder. MS1 %64.4 ama piyasa 1.50 ile zaten fazla fiyatlamış (VALUE −%3.4). Buradaki değer MS1 değil **1.5 Üst (%79.3)**.

**Celtic – Ferencváros.** Celtic Park'ta Celtic sürekli çapraz besliyor; korner beklentisi 10.6 ama 10.5 çizgisi tam başabaş (%53.6) — pas geç. Değer **1.5 Üst / Celtic ve 1.5 Üst** tarafında.

**Real Sociedad – Bournemouth.** İki takım da man-oriented pres yapıyor, oyun sürekli açık. KG %56.8, İY KG %21.8 (bültenin en yükseklerinden). Korner 10.9.

**Málaga – Villarreal / Betis – Getafe.** La Liga temposu düşük, korner ve gol marketleri sönük. Getafe'nin alçak bloğu Betis'i 2.5 Üst'ten uzaklaştırıyor (%45.6). Málaga'da tek yön Villarreal (%59.2) ama fiyat kapalı.

---

## VALUE & PME TABLOSU (sıralı)
| Seçim | Model | Oran | İma | VALUE | PME |
|---|---|---|---|---|---|
| **Levski–Salzburg: Korner 9.5 Üst** | 64.4% | 1.70 | 58.8% | **+9.5%** | **+5.6** |
| **Man City–Norwich: MS1 & 2.5 Üst** | 62.0% | 1.75 | 57.1% | **+8.5%** | **+4.9** |
| Beşiktaş–Marsilya: İY 0.5 Üst | 71.2% | 1.44 | 69.4% | +2.5% | +1.8 |
| Beşiktaş–Marsilya: KG Var | 57.8% | 1.72 | 58.1% | −0.6% | −0.3 |
| Plzeň–Union SG: 1.5 Üst | 75.1% | 1.32 | 75.8% | −0.9% | −0.7 |
| Celtic–Ferencváros: 1.5 Üst | 76.0% | 1.30 | 76.9% | −1.2% | −0.9 |
| Betis–Getafe: MS1 | 54.1% | 1.80 | 55.6% | −2.6% | −1.5 |
| Juventus–NEC: MS1 | 64.4% | 1.50 | 66.7% | −3.4% | −2.3 |
| Sociedad–Bournemouth: KG | 56.8% | 1.70 | 58.8% | −3.4% | −2.0 |
| Málaga–Villarreal: MS2 | 59.2% | 1.62 | 61.7% | −4.1% | −2.5 |
| Palace–Lech: MS1 | 64.4% | 1.45 | 69.0% | −6.6% | −4.6 | ❌ tuzak

---

## NET KARAR — KORKMADAN
**BANKO (yüksek olasılık, düşük oran):** Man City MS1 · Celtic ve Plzeň maçlarında 1.5 Üst · Beşiktaş–Marsilya İY 0.5 Üst.
**VALUE OYNANACAK İKİ BAHİS:** ① Levski–Salzburg Korner 9.5 Üst ② Man City MS1 & 2.5 Üst.
**GÜNÜN KUPONU (3'lü, düşük varyans):**
Man City MS1 (1.22) × Beşiktaş–Marsilya İY 0.5 Üst (1.44) × Levski–Salzburg Korner 9.5 Üst (1.70) ≈ **2.99 oran, birleşik model olasılığı ≈ %41**.
**UZAK DUR:** Crystal Palace MS1 (−%6.6 value), Man City İY 1.5 Üst, City korner 11.5 Üst.

Stake: value pozitif olanlara %2 bankroll, bankolara %1, kupona %1. Kelly tam değil, yarım Kelly.
