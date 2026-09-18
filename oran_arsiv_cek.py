#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ORAN ARŞİVİ ÇEKİCİ — ücretsiz kaynaklardan maç + oran arşivi kurar.

Kaynaklar (hepsi anahtarsız / ücretsiz):
  1) football-data.co.uk  — 55+ lig, 1993'ten beri MAÇ SONUÇLARI + KAPANIŞ ORANLARI (CSV)
      · Pinnacle kapanış: PSCH / PSCD / PSCA   (kıyas için altın standart)
      · Açılış öncesi toplama: B365H / PSH / AvgH ... (Cuma akşamı anlık oranlar)
      · Alt/Üst 2.5: B365>2.5, Avg>2.5, P>2.5 ...
  2) EPL aynası (GitHub: AnishKhetani/premier-league-data)
      — Premier Lig 1993-94 → bugün, ~20 bahisçinin AÇILIŞ ve KAPANIŞ oranları.
      GitHub üzerinden indirildiği için football-data.co.uk'e erişilemeyen
      ortamlarda bile (ör. bu sandbox) ÇALIŞIR.

Çıktı formatı, paketteki mevcut kapanis_arsiv.json ile BİREBİR aynıdır:
  {"u": ülke, "l": lig, "t": "GG/AA/YYYY", "e": ev, "d": dep,
   "ac": [1, X, 2] açılış, "kp": [1, X, 2] kapanış,
   "hg": ev gol, "ag": dep gol, "ih": ilk yarı ev, "ia": ilk yarı dep,
   "ou": [alt2.5, üst2.5]  (varsa)}

Böylece üretilen arşiv, kapanis_kiyas.py içindeki KAPO motoruna
(yol parametresi değiştirilerek) doğrudan verilebilir; --birlestir
seçeneği mevcut 161 binlik arşivle tek dosyada birleştirir.

Kullanım:
  python3 oran_arsiv_cek.py                 # EPL aynası + football-data (erişilebilirse)
  python3 oran_arsiv_cek.py --sezon 20      # son 20 sezon (0 = tümü, 1993'ten beri)
  python3 oran_arsiv_cek.py --ligler E0,T1  # sadece Premier Lig + Süper Lig
  python3 oran_arsiv_cek.py --epl-mirror    # sadece EPL aynası (her yerde çalışır)
  python3 oran_arsiv_cek.py --birlestir     # kapanis_arsiv.json ile birleştir
"""
import argparse
import base64
import csv
import io
import json
import os
import subprocess
import sys
import time
import urllib.request

KOK = os.path.dirname(os.path.abspath(__file__))
VERI = os.path.join(KOK, "veri")
FD_TABAN = os.environ.get("FD_TABAN", "https://www.football-data.co.uk")
GH_API = os.environ.get("GH_API", "https://api.github.com")

# football-data.co.uk lig kodları → (ülke, lig adı)
# Erişilemeyen sezon/lig dosyaları sessizce atlanır (404 normaldir).
FD_LIGLER = {
    # İngiltere
    "E0": ("England", "Premier League"), "E1": ("England", "Championship"),
    "E2": ("England", "League One"), "E3": ("England", "League Two"),
    "EC": ("England", "Conference"),
    # İskoçya
    "SC0": ("Scotland", "Premier League"), "SC1": ("Scotland", "Division 1"),
    "SC2": ("Scotland", "Division 2"), "SC3": ("Scotland", "Division 3"),
    # Büyük 5
    "D1": ("Germany", "Bundesliga"), "D2": ("Germany", "2. Bundesliga"),
    "I1": ("Italy", "Serie A"), "I2": ("Italy", "Serie B"),
    "SP1": ("Spain", "La Liga"), "SP2": ("Spain", "Segunda División"),
    "F1": ("France", "Ligue 1"), "F2": ("France", "Ligue 2"),
    # Diğer Avrupa
    "N1": ("Netherlands", "Eredivisie"), "B1": ("Belgium", "First Division A"),
    "P1": ("Portugal", "Primeira Liga"),
    "T1": ("Türkiye", "Süper Lig"), "T2": ("Türkiye", "1. Lig"),
    "G1": ("Greece", "Super League"),
}

# EPL aynası (GitHub) — football-data.co.uk verisinin açılış+kapanış oranlı hali
EPL_MIRROR_REPO = "AnishKhetani/premier-league-data"
EPL_MIRROR_DOSYALAR = {
    "sonuclar": "data/processed/results.csv",
    "oranlar": "data/processed/results_with_odds.csv",
}
FD_CACHE = os.path.join(VERI, "fd_cache")


# ------------------------------------------------------------------ yardımcı
def http_get(url, zaman_asimi=25, deneme=2):
    """Basit GET. Başarısızsa ValueError fırlatır."""
    son_hata = None
    for i in range(deneme):
        try:
            istek = urllib.request.Request(
                url, headers={"User-Agent": "Mozilla/5.0 (Bulten/1.0; +oran-arsivi)"})
            with urllib.request.urlopen(istek, timeout=zaman_asimi) as cevap:
                return cevap.read()
        except Exception as e:  # noqa: BLE001
            son_hata = e
            time.sleep(1.5 * (i + 1))
    raise ValueError(str(son_hata))


def gh_ham(repo, yol):
    """GitHub'dan dosya içeriği (ham). Önce normal URL, olmazsa gh CLI / blob API."""
    # 1) doğrudan contents API (api.github.com çoğu ortamda açıktır)
    try:
        url = "%s/repos/%s/contents/%s" % (GH_API, repo, yol)
        istek = urllib.request.Request(
            url, headers={"User-Agent": "Bulten", "Accept": "application/vnd.github.raw"})
        with urllib.request.urlopen(istek, timeout=30) as cevap:
            return cevap.read()
    except Exception:  # noqa: BLE001
        pass
    # 2) gh CLI varsa blob API ile (sandbox gibi ortamlarda güvenilir yol)
    try:
        sha = subprocess.check_output(
            ["gh", "api", "repos/%s/contents/%s" % (repo, yol), "--jq", ".sha"],
            stderr=subprocess.DEVNULL, timeout=60).decode().strip()
        ham = subprocess.check_output(
            ["gh", "api", "-H", "Accept: application/vnd.github.raw",
             "repos/%s/git/blobs/%s" % (repo, sha)],
            stderr=subprocess.DEVNULL, timeout=180)
        return ham
    except Exception as e:  # noqa: BLE001
        raise ValueError("GitHub indirme hatası (%s): %s" % (yol, e))


def f2(v):
    """CSV hücresini güvenli float'a çevirir (yoksa None)."""
    try:
        if v is None or v == "":
            return None
        f = float(v)
        return f if f > 1.0 else None  # 1.00 ve altı geçersiz oran
    except (TypeError, ValueError):
        return None


def tarih_norm(s, sezon_kodu=None):
    """football-data tarihi (14/08/93 veya 14/08/1993) → GG/AA/YYYY."""
    if not s:
        return None
    parca = s.strip().split("/")
    if len(parca) != 3:
        return s
    g, a, y = parca
    if len(y) == 2:  # iki haneli yıl → sezon kodundan tam yıl türet
        if sezon_kodu and len(sezon_kodu) == 4:
            y = ("19" if sezon_kodu[:2] >= "93" and sezon_kodu[:2] <= "99" else "20") + y
        else:
            y = ("19" if y >= "93" else "20") + y
    return "%s/%s/%s" % (g.zfill(2), a.zfill(2), y)


def kayit_uret(ulke, lig, tarih, ev, dep, ac, kp, hg, ag, ih, ia, ou=None):
    k = {"u": ulke, "l": lig, "t": tarih, "e": ev, "d": dep}
    if ac:
        k["ac"] = [round(x, 3) for x in ac]
    if kp:
        k["kp"] = [round(x, 3) for x in kp]
    k["hg"], k["ag"] = hg, ag
    if ih is not None and ia is not None:
        k["ih"], k["ia"] = ih, ia
    if ou:
        k["ou"] = [round(ou[0], 3), round(ou[1], 3)]
    return k


# ------------------------------------------------- football-data.co.uk CSV
def fd_parse(csv_metni, ulke, lig, sezon_kodu):
    """football-data.co.uk ham CSV'sini arşiv kayıtlarına çevirir."""
    kayitlar = []
    okuyucu = csv.DictReader(io.StringIO(csv_metni))
    for satir in okuyucu:
        try:
            ev = (satir.get("HomeTeam") or "").strip()
            dep = (satir.get("AwayTeam") or "").strip()
            if not ev or not dep:
                continue
            hg = satir.get("FTHG", "")
            ag = satir.get("FTAG", "")
            if hg == "" or ag == "":
                continue  # oynanmamış / skor girilmemiş
            hg, ag = int(float(hg)), int(float(ag))
            ih = ia = None
            if satir.get("HTHG", "") != "" and satir.get("HTAG", "") != "":
                ih, ia = int(float(satir["HTHG"])), int(float(satir["HTAG"]))
            # --- oranlar: kapanış için Pinnacle closing, açılış için toplanan anlık
            kp = None
            for on_ek in ("PSC", "PC"):  # PSCH/PSCD/PSCA (Pinnacle kapanış)
                k3 = [f2(satir.get(on_ek + "H")), f2(satir.get(on_ek + "D")),
                      f2(satir.get(on_ek + "A"))]
                if all(k3):
                    kp = k3
                    break
            ac = None
            for on_ek in ("PS", "B365", "Avg", "Max"):  # toplama anı oranları
                a3 = [f2(satir.get(on_ek + "H")), f2(satir.get(on_ek + "D")),
                      f2(satir.get(on_ek + "A"))]
                if all(a3):
                    ac = a3
                    break
            if not kp:
                kp = ac  # eski sezonlarda kapanış sütunu yok
            if not ac:
                ac = kp
            if not kp:
                continue  # oransız kayıt arşive girmez
            ou = None
            for on_ek in ("B365", "Avg", "P", "Max", "PC"):
                u_ = f2(satir.get(on_ek + ">2.5"))
                a_ = f2(satir.get(on_ek + "<2.5"))
                if u_ and a_:
                    ou = (a_, u_)  # [alt, üst]
                    break
            kayitlar.append(kayit_uret(ulke, lig, tarih_norm(satir.get("Date"), sezon_kodu),
                                       ev, dep, ac, kp, hg, ag, ih, ia, ou))
        except (KeyError, ValueError, IndexError):
            continue
    return kayitlar


def sezon_kodu(yil):
    """2026 → '2627' (2026-27 sezonu)."""
    return "%02d%02d" % (yil % 100, (yil + 1) % 100)


def fd_indir(ligler=None, sezon=12):
    """football-data.co.uk'ten istenen lig × sezon CSV'lerini indirip ayrıştırır."""
    os.makedirs(FD_CACHE, exist_ok=True)
    if ligler:
        kullanilan = {k: v for k, v in FD_LIGLER.items() if k in ligler}
    else:
        kullanilan = FD_LIGLER
    # güncel sezon: ağustos öncesiyse bir önceki yıl başlar
    simdiki_yil = time.gmtime().tm_year
    if time.gmtime().tm_mon < 7:
        simdiki_yil -= 1
    if sezon <= 0:
        yillar = list(range(1993, simdiki_yil + 1))
    else:
        yillar = list(range(simdiki_yil - sezon + 1, simdiki_yil + 1))
    tumu, hata, atlanan = [], 0, 0
    for kod, (ulke, lig) in sorted(kullanilan.items()):
        for yil in yillar:
            sk = sezon_kodu(yil)
            dosya = os.path.join(FD_CACHE, "%s_%s.csv" % (sk, kod))
            guncel = (yil == simdiki_yil)
            if os.path.exists(dosya) and os.path.getsize(dosya) > 200 and not guncel:
                metin = open(dosya, encoding="utf-8-sig", errors="replace").read()
            else:
                url = "%s/mmz4281/%s/%s.csv" % (FD_TABAN, sk, kod)
                try:
                    veri = http_get(url)
                    metin = veri.decode("utf-8-sig", errors="replace")
                    if len(metin) < 200 or "<html" in metin[:300].lower():
                        atlanan += 1
                        continue
                    with open(dosya, "w", encoding="utf-8") as f:
                        f.write(metin)
                except ValueError:
                    atlanan += 1
                    continue
            n_once = len(tumu)
            tumu.extend(fd_parse(metin, ulke, lig, sk))
            if len(tumu) > n_once and guncel:
                print("  · %s %s: %d maç" % (kod, sk, len(tumu) - n_once))
    print("football-data.co.uk: %d maç, %d atlanan dosya" % (len(tumu), atlanan))
    return tumu


# ------------------------------------------------------------- EPL aynası
def epl_mirror_indir():
    """GitHub'daki EPL aynasından 1993-94→bugün açılış+kapanış oranlı arşiv."""
    ham = {}
    for ad, yol in EPL_MIRROR_DOSYALAR.items():
        hedef = os.path.join(FD_CACHE, "epl_%s.csv" % ad)
        # 7 günden eski önbellek tazelenir
        taze = (os.path.exists(hedef)
                and os.path.getsize(hedef) > 10000
                and time.time() - os.path.getmtime(hedef) < 7 * 86400)
        if taze:
            ham[ad] = open(hedef, encoding="utf-8-sig", errors="replace").read()
        else:
            ham[ad] = gh_ham(EPL_MIRROR_REPO, yol).decode("utf-8-sig", errors="replace")
            os.makedirs(FD_CACHE, exist_ok=True)
            with open(hedef, "w", encoding="utf-8") as f:
                f.write(ham[ad])
    # skorlar
    skorlar = {}
    for satir in csv.DictReader(io.StringIO(ham["sonuclar"])):
        try:
            if satir["fthg"] != "" and satir["ftag"] != "":
                skorlar[satir["match_id"]] = (
                    int(satir["fthg"]), int(satir["ftag"]),
                    int(satir["hthg"]) if satir["hthg"] else None,
                    int(satir["htag"]) if satir["htag"] else None)
        except (KeyError, ValueError):
            continue
    # oranlar — sütun önceliği: kapanış için Pinnacle, açılış için Pinnacle/Bet365
    kayitlar = []
    for satir in csv.DictReader(io.StringIO(ham["oranlar"])):
        try:
            mid = satir.get("match_id")
            skor = skorlar.get(mid)
            if not skor:
                continue

            def uclu(h, d, a):
                x = (f2(satir.get(h)), f2(satir.get(d)), f2(satir.get(a)))
                return list(x) if all(x) else None

            # kapanış: Pinnacle → market ortalama → Bet365 → William Hill / Bwin / ...
            kp = (uclu("pinnacle_1x2_home_close", "pinnacle_1x2_draw_close", "pinnacle_1x2_away_close")
                  or uclu("market_avg_1x2_home_close", "market_avg_1x2_draw_close", "market_avg_1x2_away_close")
                  or uclu("bet365_1x2_home_close", "bet365_1x2_draw_close", "bet365_1x2_away_close")
                  or uclu("williamhill_1x2_home_close", "williamhill_1x2_draw_close", "williamhill_1x2_away_close")
                  or uclu("bwin_1x2_home_close", "bwin_1x2_draw_close", "bwin_1x2_away_close")
                  or uclu("interwetten_1x2_home_close", "interwetten_1x2_draw_close", "interwetten_1x2_away_close"))
            # açılış (toplanan an): Pinnacle → Bet365 → 90'lar bahisçileri
            ac = (uclu("pinnacle_1x2_home", "pinnacle_1x2_draw", "pinnacle_1x2_away")
                  or uclu("bet365_1x2_home", "bet365_1x2_draw", "bet365_1x2_away")
                  or uclu("market_avg_1x2_home", "market_avg_1x2_draw", "market_avg_1x2_away")
                  or uclu("gamebookers_1x2_home", "gamebookers_1x2_draw", "gamebookers_1x2_away")
                  or uclu("interwetten_1x2_home", "interwetten_1x2_draw", "interwetten_1x2_away")
                  or uclu("ladbrokes_1x2_home", "ladbrokes_1x2_draw", "ladbrokes_1x2_away")
                  or uclu("williamhill_1x2_home", "williamhill_1x2_draw", "williamhill_1x2_away"))
            if not kp:
                kp = ac
            if not ac:
                ac = kp
            if not kp:
                continue
            ou = None
            a_ = f2(satir.get("pinnacle_under25_close")) or f2(satir.get("bet365_under25"))
            u_ = f2(satir.get("pinnacle_over25_close")) or f2(satir.get("bet365_over25"))
            if a_ and u_:
                ou = (a_, u_)
            tarih = satir.get("date", "")
            if len(tarih) == 10 and tarih[4] == "-":  # 1993-08-14 → 14/08/1993
                tarih = "%s/%s/%s" % (tarih[8:10], tarih[5:7], tarih[:4])
            kayitlar.append(kayit_uret("England", "Premier League", tarih,
                                       satir.get("home_team", ""), satir.get("away_team", ""),
                                       ac, kp, skor[0], skor[1], skor[2], skor[3], ou))
        except (KeyError, ValueError, IndexError):
            continue
    print("EPL aynası: %d maç (1993-94 → bugün)" % len(kayitlar))
    return kayitlar


# -------------------------------------------------------------- birleştirme
def anahtar(k):
    return (k.get("l", "").lower(), k.get("t", ""), k.get("e", "").lower(), k.get("d", "").lower())


def birlestir(kaynak_yollar, hedef_yol):
    """Aynı formattaki arşivleri tek dosyada birleştirir (mükerrerleri atar).

    Öncelik: sonra gelen dosya öncekinin üzerine yazar (yenisi tutulur).
    """
    birlesik, gorulen = [], set()
    for yol in kaynak_yollar:
        if not os.path.exists(yol):
            print("  (atlandı, yok: %s)" % yol)
            continue
        veri = json.load(open(yol, encoding="utf-8"))
        ekle = [k for k in veri if k.get("kp") or k.get("ac")]
        print("  + %s: %d kayıt" % (os.path.basename(yol), len(ekle)))
        birlesik.extend(ekle)
    # mükerrerleri at: aynı (lig, tarih, ev, dep) → en son okunan tutulur
    sonuc = {}
    for k in birlesik:
        sonuc[anahtar(k)] = k
    liste = list(sonuc.values())
    with open(hedef_yol, "w", encoding="utf-8") as f:
        json.dump(liste, f, ensure_ascii=False, separators=(",", ":"))
    print("birleşik arşiv: %d maç → %s" % (len(liste), hedef_yol))
    return liste


# --------------------------------------------------------------------- main
def main():
    p = argparse.ArgumentParser(description="Ücretsiz oran arşivi kur")
    p.add_argument("--sezon", type=int, default=12,
                   help="kaç sezon çekilsin (0 = 1993'ten beri tümü, varsayılan 12)")
    p.add_argument("--ligler", default="",
                   help="virgüllü football-data lig kodları (E0,T1,...) — boşsa hepsi")
    p.add_argument("--epl-mirror", action="store_true",
                   help="sadece GitHub EPL aynası (her ortamda çalışır)")
    p.add_argument("--birlestir", action="store_true",
                   help="mevcut veri/kapanis_arsiv.json ile kapanis_arsiv_buyuk.json üret")
    p.add_argument("--cikti", default=os.path.join(VERI, "oran_arsiv.json"))
    a = p.parse_args()

    os.makedirs(VERI, exist_ok=True)
    tum = []
    if not a.epl_mirror:
        try:
            tum.extend(fd_indir(set(x.strip() for x in a.ligler.split(",") if x.strip()),
                                a.sezon))
        except Exception as e:  # noqa: BLE001
            print("football-data.co.uk erişilemedi (%s) — EPL aynası deneniyor" % e)
    try:
        tum.extend(epl_mirror_indir())
    except ValueError as e:
        print("EPL aynası da alınamadı: %s" % e)

    if not tum:
        print("Hiç kayıt alınamadı — ağ erişimini kontrol et.")
        return 1
    # mükerrerleri at (iki kaynak Premier Lig'i kapsayabilir; ayna tercih — en sona eklendi)
    sonuc = {}
    for k in tum:
        sonuc[anahtar(k)] = k
    liste = list(sonuc.values())
    liste.sort(key=lambda k: k.get("t", ""), reverse=True)
    with open(a.cikti, "w", encoding="utf-8") as f:
        json.dump(liste, f, ensure_ascii=False, separators=(",", ":"))
    lig_say = {}
    for k in liste:
        lig_say["%s · %s" % (k["u"], k["l"])] = lig_say.get("%s · %s" % (k["u"], k["l"]), 0) + 1
    meta = {
        "uretim": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()),
        "mac_sayisi": len(liste),
        "ligler": lig_say,
        "kaynaklar": ["football-data.co.uk", "github:" + EPL_MIRROR_REPO],
        "format": "kapanis_arsiv uyumlu {u,l,t,e,d,ac,kp,hg,ag,ih,ia,ou}",
    }
    with open(os.path.splitext(a.cikti)[0] + "_meta.json", "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=1)
    print("\n✔ ORAN ARŞİVİ: %d maç, %d lig → %s" % (len(liste), len(lig_say), a.cikti))
    for ad, n in sorted(lig_say.items(), key=lambda x: -x[1])[:12]:
        print("   %-38s %6d maç" % (ad, n))

    if a.birlestir:
        hedef = os.path.join(VERI, "kapanis_arsiv_buyuk.json")
        birlestir([os.path.join(VERI, "kapanis_arsiv.json"), a.cikti], hedef)
    return 0


if __name__ == "__main__":
    sys.exit(main())
