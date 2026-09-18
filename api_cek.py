#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""API ÇEKİCİ — ücretsiz ve ANAHTARSIZ futbol API'lerinden bugünün verisini toplar.

Kaynaklar (hepsi test edildi, ücretsiz, API anahtarı istemiyor):
  espn        site.api.espn.com      — fikstür, skor, puan durumu, form (219 lig!)
  365scores   webws.365scores.com    — bugün + canlı + oran (291+ maç/gün)
  openligadb  api.openligadb.de      — Bundesliga fikstür/skor (sınırsız)
  thesportsdb thesportsdb.com        — günün tüm futbol maçları (test anahtarı "3")
  openfootball GitHub openfootball   — 2026-27 sezon fikstürleri (8 büyük lig)
  statsbomb   GitHub hudl/open-data  — olay bazlı açık veri kataloğu (xG/analiz)
  scorebat    scorebat.com           — özet videolar (ESKİDİ — isteğe bağlı)

Kullanım:
  python3 api_cek.py                    # tüm kaynaklar
  python3 api_cek.py --kaynak espn,365scores
  python3 api_cek.py --gun 2026-09-19
  python3 api_cek.py --ligler tur.1,eng.1   # ESPN lig seçimi

Çıktılar:
  veri/api/<kaynak>.json    — kaynak bazında normalize edilmiş veri
  veri/api_bugun.json       — bugünün birleşik fikstürü (mükerrerler ayıklanmış)
  veri/api_durum.json       — hangi kaynak çalıştı, ne aldı
"""
import argparse
import html as H
import json
import os
import re
import sys
import time
import urllib.request
from datetime import datetime, timedelta, timezone

KOK = os.path.dirname(os.path.abspath(__file__))
VERI = os.path.join(KOK, "veri")
API_DIR = os.path.join(VERI, "api")

# --- taban adresleri (testlerde ortam değişkeniyle değiştirilebilir) --------
TABAN = {
    "espn": os.environ.get("ESPN_TABAN", "https://site.api.espn.com"),
    "365scores": os.environ.get("X365_TABAN", "https://webws.365scores.com"),
    "openligadb": os.environ.get("OLDB_TABAN", "https://api.openligadb.de"),
    "thesportsdb": os.environ.get("TSDB_TABAN", "https://www.thesportsdb.com/api/v1/json/3"),
    "scorebat": os.environ.get("SCOREBAT_TABAN", "https://www.scorebat.com"),
    "gh": os.environ.get("GH_API", "https://api.github.com"),
}

ESPN_LIGLER = [  # (kod, ülke, lig)
    ("tur.1", "Türkiye", "Süper Lig"),
    ("eng.1", "İngiltere", "Premier Lig"), ("eng.2", "İngiltere", "Championship"),
    ("esp.1", "İspanya", "La Liga"), ("esp.2", "İspanya", "La Liga 2"),
    ("ger.1", "Almanya", "Bundesliga"), ("ger.2", "Almanya", "2. Bundesliga"),
    ("ita.1", "İtalya", "Serie A"), ("ita.2", "İtalya", "Serie B"),
    ("fra.1", "Fransa", "Ligue 1"), ("fra.2", "Fransa", "Ligue 2"),
    ("ned.1", "Hollanda", "Eredivisie"), ("por.1", "Portekiz", "Primeira Liga"),
    ("bel.1", "Belçika", "Jupiler"), ("sco.1", "İskoçya", "Premiership"),
    ("gre.1", "Yunanistan", "Super League"),
    ("uefa.champions", "Avrupa", "Şampiyonlar Ligi"),
    ("uefa.europa", "Avrupa", "Avrupa Ligi"),
    ("uefa.europa.conf", "Avrupa", "Konferans Ligi"),
    ("usa.1", "ABD", "MLS"), ("bra.1", "Brezilya", "Serie A"),
]
OPENFOOTBALL_LIGLER = ["en.1", "en.2", "es.1", "de.1", "it.1", "fr.1", "nl.1", "pt.1"]

_TR = {"ç": "c", "ğ": "g", "ı": "i", "ö": "o", "ş": "s", "ü": "u"}


def norm(s):
    s = "".join(_TR.get(c, c) for c in (s or "").lower())
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9\s]", " ", s)).strip()


def http_json(url, zaman_asimi=20):
    istek = urllib.request.Request(
        url, headers={"User-Agent": "Mozilla/5.0 (Bulten/1.0; +api-cekici)",
                      "Accept": "application/json"})
    with urllib.request.urlopen(istek, timeout=zaman_asimi) as cevap:
        return json.loads(cevap.read().decode("utf-8-sig", errors="replace"))


def utc_to_tr(iso):
    """ISO UTC → İstanbul yerel saati (Türkiye tüm yıl UTC+3)."""
    try:
        d = datetime.fromisoformat(iso.replace("Z", "+00:00"))
        return (d + timedelta(hours=3)).strftime("%H:%M")
    except (ValueError, AttributeError):
        return ""


# ================================================================== ESPN
def espn_cek(ligler, gun_iso):
    """ESPN scoreboard: günün maçları (skor/durum/form) + Süper Lig puan durumu."""
    maclar = []
    for kod, ulke, lig_adi in ligler:
        try:
            url = ("%s/apis/site/v2/sports/soccer/%s/scoreboard?dates=%s"
                   % (TABAN["espn"], kod, gun_iso.replace("-", "")))
            d = http_json(url)
            for ev in d.get("events") or []:
                try:
                    c = ev["competitions"][0]
                    takim = {}
                    for t in c.get("competitors") or []:
                        takim[t.get("homeAway", "")] = t
                    h, a = takim.get("home", {}), takim.get("away", {})
                    if not h.get("team") or not a.get("team"):
                        continue
                    mac = {
                        "saat": utc_to_tr(ev.get("date", "")),
                        "tarih_utc": ev.get("date", ""),
                        "lig": lig_adi, "ulke": ulke, "lig_kod": kod,
                        "ev": h["team"].get("displayName", ""),
                        "dep": a["team"].get("displayName", ""),
                        "durum": (c.get("status", {}).get("type", {})
                                  .get("description", "")),
                        "skor": ("%s-%s" % (h.get("score", "?"), a.get("score", "?"))
                                 if c.get("status", {}).get("type", {})
                                 .get("state", "") in ("in", "post") else ""),
                        "kaynak": "espn",
                    }
                    if h.get("form") or a.get("form"):
                        mac["form"] = [h.get("form", ""), a.get("form", "")]
                    maclar.append(mac)
                except (KeyError, IndexError, TypeError):
                    continue
        except Exception as e:  # noqa: BLE001
            print("  espn %s hatası: %s" % (kod, e))
    puan = espn_puan_durumu(ligler[:1])  # varsayılan: Süper Lig
    return {"maclar": maclar, "puan_durumu": puan}


def espn_puan_durumu(ligler):
    tablolar = {}
    for kod, ulke, lig_adi in ligler:
        try:
            d = http_json("%s/apis/v2/sports/soccer/%s/standings" % (TABAN["espn"], kod))
            satirlar = []
            for cocuk in d.get("children") or []:
                for ent in cocuk.get("standings", {}).get("entries") or []:
                    s = {}
                    for x in ent.get("stats") or []:
                        s[x.get("name")] = x.get("displayValue")
                        if x.get("abbreviation"):
                            s[x["abbreviation"]] = x.get("displayValue")
                    takim = ent.get("team", {}).get("displayName", "")
                    if not takim:
                        continue
                    satirlar.append({
                        "takim": takim,
                        "o": s.get("GP") or s.get("gamesPlayed"),
                        "g": s.get("W") or s.get("wins"),
                        "b": s.get("D") or s.get("ties"),
                        "m": s.get("L") or s.get("losses"),
                        "av": s.get("GD") or s.get("pointDifferential"),
                        "p": s.get("P") or s.get("points"),
                        "sonuc": next((x.get("summary") for x in ent.get("stats", [])
                                       if x.get("name") == "overall"), "")})
            if satirlar:
                tablolar[lig_adi] = satirlar
        except Exception as e:  # noqa: BLE001
            print("  espn puan %s hatası: %s" % (kod, e))
    return tablolar


# ============================================================== 365Scores
def x365_cek(gun_iso):
    """365Scores: bugünün/canın tüm maçları (spor=1 futbol), oran dahil."""
    url = ("%s/web/games/current/?appTypeId=5&langId=1&timezoneName=Europe/Istanbul"
           "&userCountryId=94&appVersion=12&showOdds=true" % TABAN["365scores"])
    d = http_json(url, zaman_asimi=25)
    komp = {}
    for c in d.get("competitions") or []:
        ulke = ""
        for lk in (c.get("countries") or [{}]):
            ulke = lk.get("name", "")
            break
        komp[c.get("id")] = {"lig": c.get("name", ""), "ulke": ulke}
    maclar = []
    for g in d.get("games") or []:
        try:
            if g.get("sportId") not in (1, "1"):
                continue
            h = g.get("homeCompetitor") or {}
            a = g.get("awayCompetitor") or {}
            if not h.get("name") or not a.get("name"):
                continue
            k = komp.get(g.get("competitionId"), {})
            oynaniyor = str(g.get("statusGroup", "")).lower() in ("live", "finished") or \
                str(g.get("statusText", "")).lower() in ("ft", "finished", "live", "ms")
            mac = {
                "saat": (g.get("startTime", "")[11:16] or ""),
                "tarih_utc": g.get("startTime", ""),
                "lig": k.get("lig", ""), "ulke": k.get("ulke", ""),
                "ev": h.get("name", ""), "dep": a.get("name", ""),
                "durum": g.get("statusText", ""),
                "skor": ("%s-%s" % (h.get("score", "?"), a.get("score", "?"))
                         if oynaniyor else ""),
                "kaynak": "365scores",
            }
            # oran: alan adı sürüme göre değişebilir — olası yerleri tara
            for aday in (g.get("odds"), g.get("mainOdds"), g.get("preGameOdds")):
                if isinstance(aday, dict):
                    o = aday.get("odds") or aday
                    try:
                        mac["oran"] = [float(o[k]) for k in ("1", "x", "2")
                                       if o.get(k) is not None] or None
                    except (TypeError, ValueError, KeyError):
                        mac["oran_ham"] = aday
                    break
            maclar.append(mac)
        except (KeyError, TypeError):
            continue
    return {"maclar": maclar, "canli_sayisi": d.get("liveGamesCount", 0)}


# ============================================================== OpenLigaDB
def openligadb_cek():
    maclar = []
    for lig, kod in (("1. Bundesliga", "bl1"), ("2. Bundesliga", "bl2"),
                     ("3. Liga", "bl3")):
        try:
            d = http_json("%s/getmatchdata/%s" % (TABAN["openligadb"], kod))
            for m in d:
                if not m.get("team1") or not m.get("team2"):
                    continue
                mac = {
                    "saat": (m.get("matchDateTimeUTC", "")[11:16] or ""),
                    "tarih_utc": m.get("matchDateTimeUTC", ""),
                    "lig": lig, "ulke": "Almanya",
                    "ev": m["team1"].get("teamName", ""),
                    "dep": m["team2"].get("teamName", ""),
                    "durum": ("MS" if m.get("matchIsFinished") else "—"),
                    "kaynak": "openligadb",
                }
                goller = m.get("goals") or []
                if goller:
                    son = goller[-1]
                    mac["skor"] = "%s-%s" % (son.get("scoreTeam1", "?"),
                                             son.get("scoreTeam2", "?"))
                maclar.append(mac)
        except Exception as e:  # noqa: BLE001
            print("  openligadb %s hatası: %s" % (kod, e))
    return {"maclar": maclar}


# ============================================================ TheSportsDB
def thesportsdb_cek(gun_iso):
    url = "%s/eventsday.php?d=%s&s=Soccer" % (TABAN["thesportsdb"], gun_iso)
    d = http_json(url)
    maclar = []
    for e in d.get("events") or []:
        maclar.append({
            "saat": (e.get("strTime", "") or "")[:5],
            "tarih_utc": (e.get("strTimestamp") or "").replace(" ", "T") + ("Z" if e.get("strTimestamp") and "Z" not in e.get("strTimestamp", "") and "+" not in e.get("strTimestamp", "") else ""),
            "lig": e.get("strLeague", ""), "ulke": e.get("strCountry", ""),
            "ev": e.get("strHomeTeam", ""), "dep": e.get("strAwayTeam", ""),
            "durum": e.get("strStatus", "") or ("MS" if e.get("intHomeScore") is not None else "—"),
            "skor": ("%s-%s" % (e.get("intHomeScore", "?"), e.get("intAwayScore", "?"))
                     if e.get("intHomeScore") is not None else ""),
            "kaynak": "thesportsdb",
        })
    return {"maclar": maclar}


# ============================================================== openfootball
def openfootball_cek():
    """GitHub'daki openfootball/football.json — 2026-27 sezon fikstürleri.
    api.github.com üzerinden çekilir (her ortamda erişilebilir)."""
    sezon = "%d-%d" % (datetime.now().year, (datetime.now().year + 1) % 100)
    maclar = []
    for kod in OPENFOOTBALL_LIGLER:
        try:
            url = "%s/repos/openfootball/football.json/contents/%s/%s.json"
            istek = urllib.request.Request(
                url % (TABAN["gh"], sezon, kod),
                headers={"User-Agent": "Bulten",
                         "Accept": "application/vnd.github.raw"})
            with urllib.request.urlopen(istek, timeout=25) as cevap:
                d = json.loads(cevap.read().decode("utf-8-sig", errors="replace"))
            for m in d.get("matches") or []:
                # format 2026+: düz liste (team1/team2 string);
                # eski format: turlar içinde matches listesi (team1 dict)
                if isinstance(m.get("team1"), dict):
                    t1 = (m.get("team1") or {}).get("name", "")
                    t2 = (m.get("team2") or {}).get("name", "")
                    saat = ""
                else:
                    t1 = m.get("team1") or ""
                    t2 = m.get("team2") or ""
                    saat = (m.get("time") or "")[:5]
                if not t1 or not t2:
                    continue
                skor = ""
                ft = (m.get("score") or {}).get("ft")
                if ft and len(ft) == 2:
                    skor = "%d-%d" % (ft[0], ft[1])
                maclar.append({
                    "saat": saat, "tarih": m.get("date", ""),
                    "lig": d.get("name", kod), "ulke": "",
                    "ev": t1, "dep": t2, "durum": "MS" if skor else "—",
                    "skor": skor, "kaynak": "openfootball",
                })
        except Exception:  # noqa: BLE001  — sezon dosyası henüz yok olabilir
            continue
    return {"maclar": maclar, "sezon": sezon}


# ================================================================ StatsBomb
def statsbomb_cek():
    """hudl/open-data (StatsBomb) — olay bazlı açık veri kataloğu (analiz/xG)."""
    try:
        istek = urllib.request.Request(
            "%s/repos/statsbomb/open-data/contents/data/competitions.json"
            % TABAN["gh"],
            headers={"User-Agent": "Bulten", "Accept": "application/vnd.github.raw"})
        with urllib.request.urlopen(istek, timeout=25) as cevap:
            d = json.loads(cevap.read().decode("utf-8"))
        katalog = [{"id": c.get("competition_id"), "ad": c.get("competition_name"),
                    "sezon": c.get("season_name"), "ulke": c.get("country_name")}
                   for c in d]
        return {"katalog": katalog, "turnuva_sayisi": len(katalog),
                "not": "olay verisi: data/matches/<id>/<sezon>/<maç>.json + data/events/"}
    except Exception as e:  # noqa: BLE001
        print("  statsbomb hatası: %s" % e)
        return {}


# ================================================================= ScoreBat
def scorebat_cek():
    """Özet video gömme kodları. DİKKAT: v3 artık güncellenmiyor (2026-04)."""
    try:
        d = http_json("%s/video-api/v3/" % TABAN["scorebat"])
        return {"uyari": d.get("warning", ""),
                "videolar": [{"mac": v.get("title"), "lig": v.get("competition"),
                              "tarih": v.get("date"),
                              "embed": v.get("matchviewUrl")}
                             for v in (d.get("response") or [])[:200]]}
    except Exception as e:  # noqa: BLE001
        print("  scorebat hatası: %s" % e)
        return {}


# ================================================================ BİRLEŞTİR
ONCELIK = ["365scores", "espn", "thesportsdb", "openfootball", "openligadb"]


def birlestir(kayitlar):
    """Kaynak bazlı fikstürleri tek bugün listesinde birleştirir."""
    birlesik = {}
    for kaynak in ONCELIK:
        for m in kayitlar.get(kaynak, {}).get("maclar") or []:
            if not m.get("ev") or not m.get("dep"):
                continue
            k = (norm(m["ev"]), norm(m["dep"]))
            if k in birlesik:
                mevcut = birlesik[k]
                mevcut["kaynaklar"] = sorted(set(mevcut.get("kaynaklar", [mevcut.get("kaynak")]) + [m.get("kaynak")]))
                # oranı veya skoru olan kaynak bilgisini koru
                if m.get("oran") and not mevcut.get("oran"):
                    mevcut["oran"] = m["oran"]
                if m.get("skor") and (not mevcut.get("skor") or "?" in mevcut.get("skor", "")):
                    mevcut["skor"] = m.get("skor")
                    mevcut["durum"] = m.get("durum")
                continue
            m2 = dict(m)
            m2["kaynaklar"] = [m.get("kaynak")]
            birlesik[k] = m2
    liste = sorted(birlesik.values(),
                   key=lambda m: (m.get("saat") or "99", norm(m.get("lig")), norm(m["ev"])))
    return liste


# ==================================================================== main
def main():
    p = argparse.ArgumentParser(description="Ücretsiz futbol API'lerini çek")
    p.add_argument("--kaynak", default="espn,365scores,openligadb,thesportsdb,"
                                       "openfootball,statsbomb",
                   help="virgüllü liste: espn,365scores,openligadb,thesportsdb,"
                        "openfootball,statsbomb,scorebat")
    p.add_argument("--gun", default=datetime.now(timezone(timedelta(hours=3))).strftime("%Y-%m-%d"))
    p.add_argument("--ligler", default="", help="ESPN lig kodları (tur.1,eng.1,...)")
    p.add_argument("--puan-ligler", default="", help="puan durumu için ESPN kodları")
    a = p.parse_args()

    os.makedirs(API_DIR, exist_ok=True)
    istenen = {x.strip() for x in a.kaynak.split(",") if x.strip()}
    espn_ligler = ESPN_LIGLER
    if a.ligler:
        secilen = {x.strip() for x in a.ligler.split(",")}
        espn_ligler = [l for l in ESPN_LIGLER if l[0] in secilen] or ESPN_LIGLER
    if a.puan_ligler:
        secilen = {x.strip() for x in a.puan_ligler.split(",")}
        espn_ligler_p = [l for l in ESPN_LIGLER if l[0] in secilen]
    else:
        espn_ligler_p = espn_ligler[:1]

    durum, kayitlar = {}, {}
    t0 = time.time()

    if "espn" in istenen:
        print("→ ESPN çekiliyor (%d lig)..." % len(espn_ligler))
        r = espn_cek(espn_ligler, a.gun)
        kayitlar["espn"] = r
        durum["espn"] = "%d maç, puan durumu: %s" % (
            len(r.get("maclar") or []), ", ".join(r.get("puan_durumu", {}).keys()) or "—")
    if "365scores" in istenen:
        print("→ 365Scores çekiliyor...")
        try:
            r = x365_cek(a.gun)
            kayitlar["365scores"] = r
            durum["365scores"] = "%d maç (%d canlı)" % (
                len(r.get("maclar") or []), r.get("canli_sayisi", 0))
        except Exception as e:  # noqa: BLE001
            durum["365scores"] = "HATA: %s" % e
    if "openligadb" in istenen:
        print("→ OpenLigaDB çekiliyor...")
        try:
            r = openligadb_cek()
            kayitlar["openligadb"] = r
            durum["openligadb"] = "%d maç" % len(r.get("maclar") or [])
        except Exception as e:  # noqa: BLE001
            durum["openligadb"] = "HATA: %s" % e
    if "thesportsdb" in istenen:
        print("→ TheSportsDB çekiliyor...")
        try:
            r = thesportsdb_cek(a.gun)
            kayitlar["thesportsdb"] = r
            durum["thesportsdb"] = "%d maç" % len(r.get("maclar") or [])
        except Exception as e:  # noqa: BLE001
            durum["thesportsdb"] = "HATA: %s" % e
    if "openfootball" in istenen:
        print("→ openfootball (GitHub) çekiliyor...")
        try:
            r = openfootball_cek()
            kayitlar["openfootball"] = r
            durum["openfootball"] = "%d maç (%s sezonu)" % (
                len(r.get("maclar") or []), r.get("sezon", "?"))
        except Exception as e:  # noqa: BLE001
            durum["openfootball"] = "HATA: %s" % e
    if "statsbomb" in istenen:
        print("→ StatsBomb kataloğu çekiliyor...")
        r = statsbomb_cek()
        if r:
            kayitlar["statsbomb"] = r
            durum["statsbomb"] = "%d turnuva/sezon" % r.get("turnuva_sayisi", 0)
    if "scorebat" in istenen:
        print("→ ScoreBat çekiliyor (ESKİDİ)...")
        r = scorebat_cek()
        if r:
            kayitlar["scorebat"] = r
            durum["scorebat"] = "%d video — %s" % (
                len(r.get("videolar") or []), "güncel değil")

    # kaydet
    for ad, veri in kayitlar.items():
        with open(os.path.join(API_DIR, "%s.json" % ad), "w", encoding="utf-8") as f:
            json.dump(veri, f, ensure_ascii=False, separators=(",", ":"))
    birlesik = birlestir(kayitlar)
    with open(os.path.join(VERI, "api_bugun.json"), "w", encoding="utf-8") as f:
        json.dump({"gun": a.gun, "uretim": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()),
                   "mac_sayisi": len(birlesik), "maclar": birlesik},
                  f, ensure_ascii=False, separators=(",", ":"))
    with open(os.path.join(VERI, "api_durum.json"), "w", encoding="utf-8") as f:
        json.dump({"gun": a.gun, "sure_saniye": round(time.time() - t0, 1),
                   "durum": durum}, f, ensure_ascii=False, indent=1)

    print("\n╔══════════════ ÜCRETSİZ FUTBOL APİLERİ ══════════════╗")
    for ad, ozet in durum.items():
        print("  %-12s %s" % (ad, ozet))
    print("╚══════════════════════════════════════════════════════╝")
    print("birleşik fikstür: %d maç → veri/api_bugun.json (%.1f sn)"
          % (len(birlesik), time.time() - t0))

    html_uret(durum, birlesik, a.gun)
    return 0


def html_uret(durum, maclar, gun):
    """API_DURUM.html — kaynak durumu + bugünün fikstürü (tek dosya, bağımlılıksız)."""
    css = ("body{margin:0;background:#f6f7f9;color:#16212e;font-family:-apple-system,"
           "BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif}"
           ".wrap{max-width:1080px;margin:0 auto;padding:14px 12px 60px}"
           ".card{background:#fff;border:1px solid #e3e8ee;border-radius:12px;"
           "padding:12px 14px;margin:10px 0}"
           "h1{font-size:19px;margin:6px 0 2px}h3{margin:0 0 8px;font-size:14px;color:#0d5c3a}"
           ".mini{font-size:11.5px;color:#68788a}"
           "table.kt{width:100%;border-collapse:collapse}table.kt th{background:#f2f5f8;"
           "text-align:left;padding:6px 7px;font-size:12px;position:sticky;top:0}"
           "table.kt td{padding:5px 7px;border-bottom:1px solid #eef1f4;font-size:12.5px}"
           "td.b{font-weight:700}.sar{max-height:72vh;overflow:auto}"
           ".ok{color:#0d5c3a;font-weight:600}.hata{color:#b3261e}")
    satirlar = "".join(
        "<tr><td>%s</td><td class='%s b'>%s</td><td>%s — %s</td><td>%s</td>"
        "<td>%s</td><td>%s</td><td class='mini'>%s</td></tr>"
        % (("&#8226;"), "b", H.escape(m.get("saat", "") or "—"),
           H.escape(m.get("ev", "")), H.escape(m.get("dep", "")),
           H.escape(m.get("skor", "") or "—"),
           (" / ".join("%.2f" % x for x in m["oran"]) if m.get("oran") else "—"),
           H.escape(m.get("durum", "") or "—"),
           H.escape(", ".join(m.get("kaynaklar", []) or [m.get("kaynak", "")])))
        for m in maclar)
    durum_satir = "".join(
        "<div class='card'><h3>%s</h3><div class='%s'>%s</div></div>"
        % (H.escape(ad), "ok" if not str(oz).startswith("HATA") else "hata",
           H.escape(str(oz)))
        for ad, oz in durum.items())
    belge = ("<!DOCTYPE html><html lang='tr'><head><meta charset='utf-8'>"
             "<meta name='viewport' content='width=device-width,initial-scale=1'>"
             "<title>Ücretsiz Futbol API'leri — %s</title><style>%s</style></head>"
             "<body><div class='wrap'><h1>&#9917; Ücretsiz Futbol API'leri — %s</h1>"
             "<div class='mini'>espn · 365scores · openligadb · thesportsdb · "
             "openfootball · statsbomb — hepsi anahtarsız ve ücretsiz</div>%s"
             "<div class='card'><h3>BUGÜN — %d maç</h3><div class='sar'>"
             "<table class='kt'><thead><tr><th>Saat</th><th>Maç</th><th>Skor</th>"
             "<th>Oran</th><th>Durum</th><th>Kaynak</th></tr></thead>"
             "<tbody>%s</tbody></table></div></div></div></body></html>"
             % (gun, css, gun, durum_satir, len(maclar), satirlar))
    hedef = os.path.join(KOK, "API_DURUM.html")
    with open(hedef, "w", encoding="utf-8") as f:
        f.write(belge)
    print("durum sayfası: %s" % hedef)


if __name__ == "__main__":
    sys.exit(main())
