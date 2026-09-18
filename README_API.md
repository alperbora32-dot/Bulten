# 📋 Ücretsiz Futbol API'leri — Katalog ve Oran Arşivi Rehberi

Bu depo, **anahtarsız ve tamamen ücretsiz** futbol API'lerinden veri çeken üç araç +
otomasyon içerir. Hepsinde bağımlılık yok: yalnız Python 3 standart kütüphanesi.

| Araç | Ne yapar | Çıktı |
|---|---|---|
| `api_cek.py` | Ücretsiz API'lerden bugünün fikstür/skor/puan verisini çeker | `veri/api/*.json`, `veri/api_bugun.json`, `API_DURUM.html` |
| `oran_arsiv_cek.py` | **Oran arşivi** kurar: sonuç + açılış/kapanış oranlı 100 binlerce maç | `veri/oran_arsiv.json`, `veri/kapanis_arsiv_buyuk.json` |
| `mac_kiyas.py` | **Maç kıyası**: benzer oranlı tarihsel maçların sonuç dağılımı | `veri/kiyas_bugun.json`, `ORAN_KIYAS.html` |

Otomasyon: `.github/workflows/guncelle.yml` — 30 dakikada bir çalışır,
veriyi tazeler, kıyası üretir, siteyi GitHub Pages'e yayınlar (ücretsiz).

---

## 1) Ücretsiz futbol API'leri kataloğu

Hepsi 2026-09-18'de **canlı test edildi**. "Durum" bu repodaki sandbox ortamından;
GitHub Actions gibi tam internetli ortamlarda hepsi erişilebilir.

### Anahtarsız — kod doğrudan çalışır

| API | Ne verir | Limit | Durum |
|---|---|---|---|
| **ESPN** `site.api.espn.com` | Fikstür, skor, puan durumu, form, son 5 maç, 219 lig (Süper Lig dahil) | limitsiz görünüyor | ✅ test edildi |
| **365Scores** `webws.365scores.com` | Bugün + canlı tüm maçlar, oran, 290+ maç/gün | makul kullanım | ✅ test edildi |
| **OpenLigaDB** `api.openligadb.de` | Almanya fikstür/skor, topluluk veritabanı | sınırsız, anahtarsız | ✅ test edildi |
| **TheSportsDB** (test anahtarı `3`) | Günün tüm futbol maçları, logo, lig bilgisi | ~30 istek/dk | ✅ test edildi |
| **openfootball** (GitHub) | 8 büyük lig 2026-27 sezonu fikstürleri (düz JSON) | GitHub limitleri | ✅ test edildi |
| **StatsBomb Open Data** (GitHub) | Seçili turnuvalar için **olay bazlı** veri + xG (analiz) | — | ✅ test edildi |
| **football-data.co.uk** | ⭐ **Oran arşivi**: 55+ lig, 1993→bugün, kapanış oranları (CSV) | sınırsız | ✅ (Actions'ta; CSV doğrudan) |
| **EPL aynası** (GitHub: AnishKhetani/premier-league-data) | Premier Lig 1993→bugün ~20 bahisçinin **açılış+kapanış** oranları | GitHub limitleri | ✅ test edildi |
| **ScoreBat** | Özet video gömme kodları | sınırsız | ⚠️ v3 güncellenmiyor (2026-04'ten beri) — `--kaynak scorebat` ile isteğe bağlı |

### Ücretsiz ama anahtar isteyen (üye olunca ücretsiz katman)

| API | Ücretsiz kota | Not |
|---|---|---|
| **football-data.org** | 12 turnuva (Büyük 5 + CL), 10 istek/dk | Temiz REST + iyi dokümantasyon; kota başına istek atmalısınız (`X-Auth-Token` başlığı). Bu depoda varsayılan kapalı. |
| **API-Football** (api-sports.io) | 100 istek/gün, 1236 lig | Prototip için ideal |
| **TheOddsAPI** | 500 istek/ay | Canlı oran hareketi için en pratik ücretsiz seçenek |
| **Sportmonks** | 2 lig (Danimarka + İskoçya) | Çok dar |

### Bilinen ancak tercih edilmeyenler

- **Sofascore** → 403 Cloudflare koruması (resmî olmayan kullanım zaten engelleniyor)
- **FotMob** → bot koruması, ayda değişen imzalar
- **Understat** → xG verisi güzel ama JSON sayfa içine gömülü geliyor (kazıma gerekir)

> Paketin kendi `bulten_v3.py` zinciri **betexplorer.com**'u kazımaya devam eder;
> bu repodaki araçlar ona **ek** kaynaklar sağlar (bkz. Bölüm 4).

---

## 2) Oran arşivi (`oran_arsiv_cek.py`) — asıl hazine

"Bu orana sahip maçlar daha önce nasıl bitti?" sorusunun veri tabanı.

### Kaynaklar

1. **football-data.co.uk** — her sezon × lig için tek CSV:
   `https://www.football-data.co.uk/mmz4281/<sezon>/<lig>.csv`
   Örnek: `.../mmz4281/2627/T1.csv` → 2026-27 Süper Lig.
   Önemli sütunlar:

   | Sütun | Anlamı |
   |---|---|
   | `FTHG/FTAG`, `HTHG/HTAG` | MS ve İY skorları |
   | `B365H/B365D/B365A` | Bet365 toplanma anı (Cuma) oranları → **açılış proxy** |
   | `PSH/PSD/PSA` | Pinnacle toplanma anı oranları |
   | **`PSCH/PSCD/PSCA`** | **Pinnacle kapanış oranları → kıyasın altın standardı** |
   | `AvgH/AvgD/AvgA`, `MaxH/...` | Pazar ortalama/en yüksek |
   | `B365>2.5`, `Avg<2.5`, ... | Alt/Üst 2.5 oranları |

2. **EPL aynası** (GitHub) — football-data.co.uk Premier Lig verisinin
   açılış + kapanış ayrılmış hali (~20 bahisçi, 1993-94 → bugün).
   GitHub'dan indirildiği için football-data.co.uk'in erişilemediği ortamlarda bile çalışır.

3. **Paketin mevcut arşivi** — `bulten-paket.zip` içindeki `veri/kapanis_arsiv.json`
   (betexplorer kaynaklı, 161.110 maç, 2015→bugün, açılış+kapanış).

### Format — mevcut sistemle birebir uyumlu

```json
{"u":"England","l":"Premier League","t":"08/08/2015","e":"Bournemouth","d":"Aston Villa",
 "ac":[1.95,3.65,4.27],"kp":[1.82,3.88,4.70],"hg":0,"ag":1,"ih":0,"ia":0}
```
`ac` = açılış 1X2 · `kp` = kapanış 1X2 · `hg/ag` = MS · `ih/ia` = İY ·
`ou` = [alt 2.5, üst 2.5] (yeni kaynaklarda varsa)

### Kullanım

```bash
python3 oran_arsiv_cek.py                    # EPL aynası + football-data (12 sezon)
python3 oran_arsiv_cek.py --sezon 0          # 1993'ten beri TÜM sezonlar
python3 oran_arsiv_cek.py --ligler E0,T1     # sadece Premier Lig + Süper Lig
python3 oran_arsiv_cek.py --birlestir        # + mevcut kapanis_arsiv.json → kapanis_arsiv_buyuk.json
```

Mevcut durum (bu depoda üretilen): **167.190** maç = 161.110 (betexplorer) +
benzeri olmayan ~6.000 EPL maçı (1993-2015 arası, açılış+kapanış oranlı).

---

## 3) Maç kıyası (`mac_kiyas.py`)

Hedef maçın 1X2 oranlarına **±%2 toleransla** başlayıp yeterli maç bulunana kadar
(±%3 → ±%4.5 → ±%6; kendi ligi için ±%13'e kadar) gevşeterek arşivde arama yapar.
Paketin `kapanis_kiyas.py` motoruyla aynı mantık.

```bash
# tek maç:
python3 mac_kiyas.py --ev Galatasaray --dep Fenerbahce --lig "Süper Lig" \
    --oran 2.10 3.50 3.40

# bugünün tüm oranlı maçları (veri/tam_tarama.json + veri/api_bugun.json):
python3 mac_kiyas.py --bugun
```

Örnek gerçek çıktı (167 binlik arşivden):
```
Kasimpasa — Konyaspor · 2.30 / 3.30 / 3.10
TÜM LİGLER (±%2):  480 maç → 1 %44.8 · X %26.7 · 2 %28.5 · ort.gol 2.54 · alt2.5 %52.5
KENDİ LİGİ (±%2):   24 maç → 1 %45.8 · X %33.3 · 2 %20.8 · en sık 1-1
```

---

## 4) Paketin kendi sistemiyle birleştirme

Paketin `kapanis_kiyas.py` dosyasındaki `KAPO` sınıfı zaten bu formatı okur.
Büyük arşivi kullanması için tek satır yeterli:

```python
# paket içinde (paket/kapanis_kiyas.py):
YOL = '<repo>/veri/kapanis_arsiv_buyuk.json'   # eski: kapanis_arsiv.json
```

ya da kod içerisinden:

```python
import kapanis_kiyas as KK
kapo = KK.KAPO(yol="veri/kapanis_arsiv_buyuk.json")
sonuc = kapo.kiyas([2.30, 3.30, 3.10], lig="Super Lig", ulke="Turkey")
```

---

## 5) Otomasyon

`.github/workflows/guncelle.yml`:

1. `veri/` klasörünü önbellekten geri yükler (arşivler her turda yeniden indirilmez)
2. `bulten-paket.zip`'i `paket/` klasörüne açar (repodaki `veri/` korunur)
3. `api_cek.py` → bugünün verisi
4. `oran_arsiv_cek.py --sezon 12 --birlestir` → arşiv (güncel sezon tazelenir)
5. `mac_kiyas.py --bugun` → kıyas + `ORAN_KIYAS.html`
6. Küçük dosyaları repoya commit eder (8 MB üzeri dosyalar asla commit edilmez)
7. `_site/` klasörünü GitHub Pages'e yayınlar

**Gerekli ayarlar (bir kere):**
- Settings → Pages → Source: **GitHub Actions**
- Settings → Actions → General → Workflow permissions → **Read and write permissions**

Yayınlanan sayfalar: `ORAN_KIYAS.html` (kıyas), `API_DURUM.html` (API durumu + fikstür),
paketten geliyorsa `index.html` / `canli.html` / `kurulum.html`.

---

## 6) Hızlı başlangıç

```bash
python3 api_cek.py                 # bugünün maçları (tüm kaynaklar)
python3 oran_arsiv_cek.py --birlestir   # oran arşivini kur
python3 mac_kiyas.py --bugun       # kıyas raporu + HTML
```

Yerel sunucu: `python3 -m http.server` → http://localhost:8000/ORAN_KIYAS.html

---

## 6b) BULTEN_APP.html — tek dosyalık uygulama (kurulum YOK)

`python3 bulten_app_uret.py` → **BULTEN_APP.html** (~4 MB).

Dosyayı indirin, çift tıklayın. Python, sunucu, kurulum gerekmez.

| Sekme | Ne yapar | İnternet |
|---|---|---|
| ⚽ Bugün | ESPN (lig seçimli, Süper Lig varsayılan) + 365Scores (oranlı, tüm gün) canlı fikstür — 60 sn otomatik yenileme | gerekli |
| ⚖️ Oran Kıyası | **Gömülü 167 bin maçlık oran arşivi** ile benzer oranlı maç analizi — takım isimleri + lig filtresi + İY skorları | **gerekmez** |
| 📊 Puan Durumu | ESPN canlı puan durumları (16 lig) | gerekli |

Arşiv HTML içine 18 bayt/maç ikili formatta gömülür (oran×1000, skorlar, İY,
tarih, lig, takım sözlükleri) — kıyas sekmesi tamamen çevrimdışı çalışır.
Gömülü motor, `mac_kiyas.py` ile **birebir aynı sonuçları** verir
(üç sorguda test edildi: 480/33/267 maç, dağılımlar aynı).

Arşivi güncellemek için:
```bash
python3 oran_arsiv_cek.py --birlestir && python3 bulten_app_uret.py
```

---

## 7) İş akışı dosyası

Arena ortamı `.github/workflows/` altına dosya gönderme yetkisine sahip olmadığından
iş akışı repoya `guncelle-api.yml.txt` olarak eklendi. Repoda kullanmak için:

1. GitHub'da repoda **Add file → Create new file**
2. Dosya adı: `.github/workflows/guncelle.yml`
3. İçerik: `guncelle-api.yml.txt` dosyasının tamamı
4. Commit → Actions sekmesinden **Bulten guncelle** iş akışını **Run workflow** ile çalıştır

(Ellerinizle ekledikten sonra repoya kalıcı olur; bot sonraki turlarda onu kullanır.)
