# 📱 Telefondan GitHub Rehberi — Sıfırdan

Bu dosya, **hiç kod bilmeyen** biri için yazıldı. Sadece telefon kullanarak
GitHub'a dosya eklemeyi, kendi siteni kurmayı ve bir şeyler öğrenmeyi anlatır.

---

## 1) Önce şunu bil: "eklenti" ne demek?

GitHub'da "eklenti" diye ayrı bir şey yok. Senin elindeki şey şunlardan oluşuyor:

| Parça | Ne işe yarar |
|---|---|
| **Repo** (depo) | Projenin klasörü. Senin depon: `alperbora32-dot/Bulten` |
| **Dosya** | Kod, veri, sayfa. GitHub'a dosya **ekleyebilirsin** |
| **Actions** | GitHub'ın bedava sunucusu. Dosyaları **senin yerine** çalıştırır |
| **Pages** | O çalışmanın sonucunu **internet sitesi** olarak yayınlar |
| **Workflow** | Actions'a "şunu şunu yap" diyen tarif dosyası (`guncelle.yml`) |

Yani "eklenti eklemek" pratikte **iki şeyden biri**:
1. Depoya yeni bir **dosya** koymak, ya da
2. Yeni bir **workflow** (`.github/workflows/xxx.yml`) eklemek.

---

## 2) Telefonun tarayıcısı yeter (uygulama şart değil)

En kolay yol: **Chrome / Safari** ile `github.com` → giriş yap.
Fakat masaüstü sürüm daha rahattır:

- Chrome: sağ üst **⋮** → **Masaüstü sitesi** işaretle
- Safari: adres çubuğundaki **ᴀA** → **Masaüstü Web Sitesi**

Alternatif: **GitHub Mobile** uygulaması (App Store / Play Store). Dosya
**okumak, yorum yazmak, issue açmak** için çok iyi; ama **yeni dosya oluşturmak
ve Actions'ı yönetmek** için tarayıcı hâlâ daha güçlü.

---

## 3) Depoya dosya eklemek (en sık yapacağın iş)

1. `github.com/alperbora32-dot/Bulten` adresini aç
2. **Add file ▾ → Upload files** (mevcut dosyayı yüklemek için)
   ya da **Add file ▾ → Create new file** (sıfırdan yazmak için)
3. Yeni dosya oluşturuyorsan **ad alanına yolu yaz**: örneğin
   `.github/workflows/guncelle.yml`
   → Eğik çizgi yazınca GitHub klasörleri **kendi oluşturur**, sen klasör açmıyorsun.
4. Alt taraftaki **Commit changes** (yeşil düğme) → **Commit changes**
5. Bitti. Dosya depoda.

> ⚠️ **Önemli:** Yol **`.github`** ile başlamalı (başında nokta var).
> `github/workflows/...` (noktasız) olursa Actions o dosyayı **görmez**.

---

## 4) Bu depoda zaten hazır olanlar

| Dosya | Durum |
|---|---|
| `bulten-paket.zip` | ✅ Var (6,9 MB) — kodun tamamı ve veri burada |
| `.github/workflows/guncelle.yml` | ✅ Var — her 30 dakikada bir çalışır |

### Sırada ne var? (tek seferlik kurulum, 3 adım)

**A) Pages'i aç**
`Settings → Pages → Build and deployment → Source: **GitHub Actions**`

**B) Actions iznini ver**
`Settings → Actions → General → Workflow permissions → **Read and write permissions** → Save`

**C) İlk turu başlat**
`Actions → sol tarafta **Bulten guncelle** → **Run workflow** → Run workflow`
İlk tur **10–25 dakika** sürer. Yeşil ✓ olunca site hazır.

**Site adresin:** `https://alperbora32-dot.github.io/Bulten/`

Sonra telefonda o adresi aç → tarayıcı menüsü → **Ana ekrana ekle** → uygulama gibi olur.

---

## 5) "Bir şey eklemek" için 5 gerçek fikir

Acemi olarak adım adım ilerlemek için bu sırayı öner:

### Fikir 1 — Depoya bir not dosyası ekle (5 dakika, risksiz)
`Add file → Create new file` → ad: `notlarim.md` → birkaç satır yaz → Commit.
Bu, "dosya ekleme" kasını geliştirir. Hiçbir şeyi bozmaz.

### Fikir 2 — Saati değiştir (10 dakika)
`.github/workflows/guncelle.yml` → sağ üst **kalem (✏️)** → `cron: '*/30 * * * *'`
satırını bul → `*/15` yap (15 dakikada bir) veya `0 * * * *` (saatte bir) → Commit.
⚠️ Çok sık çalıştırmak GitHub'ı yorar; 15 dakikadan aşağı inme.

### Fikir 3 — Sayfa tasarımını değiştir (30 dakika, orta)
Sitenin rengi/yazısı `bulten_v3.py` içinde. Ama bu dosya **zip'in içinde**.
Zip'i güncellemek zahmetli olduğu için ilk aşamada **elleme**.
Bunun yerine `README.md` dosyasını düzenleyip projeni tanıt — GitHub'da
deponun ana sayfasında görünür.

### Fikir 4 — Yeni bir workflow ekle (öğretici, risksiz)
Örnek: her sabah deponun "sağlık kontrolünü" yapan basit bir dosya.
Ad: `.github/workflows/kontrol.yml`

```yaml
name: Kontrol
on:
  workflow_dispatch:
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: |
          echo "Depo sağlam görünüyor"
          ls -la
          du -h bulten-paket.zip
```

Çalıştır: `Actions → Kontrol → Run workflow`. Yeşil ✓ → öğrendin.

### Fikir 5 — Issue açmayı öğren (iletişim)
`Issues → New issue` → bir hata veya istek yaz. Bu senin "yapılacaklar" listen olur.
Ayrıca GitHub'da 60 gün hiç işlem yapılmazsa **zamanlanmış workflow'lar durur**;
issue açmak/commit atmak bunu önler.

---

## 6) Terimler sözlüğü (kısa)

| Terim | Anlamı |
|---|---|
| **Commit** | "Değişikliği kaydet" düğmesi. Her commit bir kayıt noktası |
| **Branch** | Projenin bir kopyası; denemeleri bozmadan yaparsın |
| **Pull request (PR)** | "Bu değişikliği ana koda alalım mı?" teklifi |
| **Actions** | Bedava çalıştırıcı (sunucu) |
| **Workflow** | Actions'a verilen tarif (`.github/workflows/*.yml`) |
| **Run** | Bir workflow'un tek çalışması; **yeşil ✓** = başarılı, **kırmızı ✗** = hata |
| **Artifact** | Bir run'ın ürettiği dosya (indirilebilir) |
| **Pages** | Repoyu web sitesi olarak yayınlama |
| **Secret** | Gizli anahtar (şifre, token). Settings → Secrets |
| **.gitignore** | "Bu dosyaları takip etme" listesi |

---

## 7) Bir şey bozulursa (panik yok)

| Belirti | Çözüm |
|---|---|
| Actions'ta kırmızı ✗ | Kırmızı adıma dokun → kırmızı satırı oku. Genelde mesaj Türkçe/İngilizce açıktır |
| Site 404 | `Settings → Pages → Source: GitHub Actions` seçili mi? |
| "Permission denied / 403" | `Settings → Actions → General → Read and write permissions` |
| "bulten-paket.zip yok" | Zip silinmiş. `Add file → Upload files` ile geri yükle |
| Zamanlanmış iş durdu | Depo 60 gün hareketsiz kalmış. `Run workflow` ile elle çalıştır, düzelir |
| Her şey karıştı | `Code → Commits` → hatalı commit'in yanındaki **Revert** (geri al) |

**Altın kural:** Bir şeyi bozmaktan korkma. GitHub her commit'i saklar;
eski sürüme dönmek her zaman mümkündür.

---

## 8) Öğrenme sırası (2 hafta planı)

| Gün | Yapılacak | Süre |
|---|---|---|
| 1 | Depoyu gez, dosyaları oku, `notlarim.md` ekle | 20 dk |
| 2 | Actions sekmesini incele, son run'ın loglarını oku | 15 dk |
| 3 | `cron` saatini değiştir, geri al | 15 dk |
| 4 | Kendi `kontrol.yml` workflow'unu ekle ve çalıştır | 30 dk |
| 5 | Issue aç, README'yi düzenle | 20 dk |
| 6 | Markdown öğren (başlık, liste, kalın, bağlantı) | 30 dk |
| 7 | Branch açmayı dene (`main` → `deneme`) — korkusuz deneme alanı | 20 dk |
| 8–14 | Küçük bir Python betiği ekle, workflow'da çalıştır | günde 20 dk |

---

## 9) Faydalı bağlantılar

- GitHub Docs (Türkçe): `https://docs.github.com/tr`
- Actions öğren: `https://docs.github.com/tr/actions`
- Pages: `https://docs.github.com/tr/pages`
- Markdown tablosu: `https://docs.github.com/tr/get-started/writing-on-github`

---

## 10) Bu depoyla ilgili notlar

- `bulten-paket.zip` **silinmemeli** — her turda kod ondan okunur.
- Zip'in içindeki Python dosyalarında sabit `/home/user` yolu var; workflow bunu
  otomatik olarak çalışma klasörüne çevirir (`sed` adımı). Zip'i elle güncellersen
  bu dönüşüm yine çalışır, endişelenme.
- Veri (`veri/` klasörü) **Actions önbelleğinde** tutulur, repoya girmez
  (24 MB'lık arşivler repoyu şişirmesin diye).
