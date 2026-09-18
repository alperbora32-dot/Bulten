#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MAÇ KIYASI — oran arşivi üzerinden benzer oranlı maçların sonuç dağılımı.

"Bu orana sahip maçlar daha önce nasıl bitmiş?" sorusunu yanıtlar.
Arşiv: veri/kapanis_arsiv_buyuk.json → kapanis_arsiv.json → oran_arsiv.json
(sırayla ilk bulunan kullanılır; oran_arsiv_cek.py --birlestir ile üretilen
büyük arşiv, paketteki KAPO motoruyla da birebir aynı formatı taşır.)

Yöntem (paketin kapanis_kiyas.py mantığıyla aynı):
  hedef 1X2 oranlarına her bacakta ±tolerans (±%2'den başlar, yeterli maç
  bulunamazsa ±%3 → ±%4.5 → ±%6'ya gevşetilir; kendi ligi için ±%13'e kadar)
  içinde kalan tüm tarihsel maçlar toplanır; 1/X/2 dağılımı, ortalama gol,
  alt/üst 2.5, en sık skorlar ve örnek maçlar listelenir.

Kullanım:
  # tek maç, elle oran vererek:
  python3 mac_kiyas.py --ev Galatasaray --dep "Fenerbahce" --lig "Süper Lig" \
      --ulke Türkiye --oran 1.90 3.60 4.10

  # bugünün tüm maçları (oranlar veri/tam_tarama.json veya veri/api_bugun.json'dan):
  python3 mac_kiyas.py --bugun          # → veri/kiyas_bugun.json + ORAN_KIYAS.html

  # arşiv dosyası belirtmek için:
  python3 mac_kiyas.py --arsiv veri/oran_arsiv.json --oran 2.5 3.2 2.9
"""
import argparse
import bisect
import html as H
import json
import os
import re
import sys
import time
from datetime import datetime

KOK = os.path.dirname(os.path.abspath(__file__))
VERI = os.path.join(KOK, "veri")

ARSIV_ONCELIGI = [
    os.path.join(VERI, "kapanis_arsiv_buyuk.json"),
    os.path.join(VERI, "kapanis_arsiv.json"),
    os.path.join(VERI, "oran_arsiv.json"),
]
TOL_TUM = (0.02, 0.03, 0.045, 0.06)       # tüm ligler merdiveni
TOL_LIG = (0.02, 0.03, 0.045, 0.06, 0.09, 0.13)  # kendi ligi merdiveni

# Türkçe karakter katlaması: "Süper Lig" ile "Super Lig" aynı sayılır
_TR = {"ç": "c", "ğ": "g", "ı": "i", "ö": "o", "ş": "s", "ü": "u"}


def norm(s):
    s = "".join(_TR.get(c, c) for c in (s or "").lower())
    s = re.sub(r"[^a-z0-9\s]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def arsiv_yukle(yol=None):
    yol = yol or next((a for a in ARSIV_ONCELIGI if os.path.exists(a)), None)
    if not yol:
        print("Arşiv bulunamadı! Önce: python3 oran_arsiv_cek.py --birlestir")
        return None, None
    ham = json.load(open(yol, encoding="utf-8"))
    sat = []
    for x in ham:
        kp = x.get("kp") or x.get("ac")
        if not kp or len(kp) != 3:
            continue
        try:
            sat.append((float(kp[0]), float(kp[1]), float(kp[2]),
                        norm(x.get("l", "")), (x.get("u") or "").lower(),
                        x.get("t", ""), x.get("e", ""), x.get("d", ""),
                        x.get("hg"), x.get("ag"), x.get("ih"), x.get("ia"),
                        x.get("ou")))
        except (TypeError, ValueError):
            continue
    sat.sort(key=lambda z: z[0])
    print("arşiv: %s — %d oranlı maç" % (os.path.basename(yol), len(sat)))
    return sat, [z[0] for z in sat]


class Kiyasci:
    def __init__(self, sat):
        self.sat = sat
        self.ilk = [z[0] for z in sat]

    def _aday(self, o1, ox, o2, tol, lig_n=None):
        a = bisect.bisect_left(self.ilk, o1 * (1 - tol))
        b = bisect.bisect_right(self.ilk, o1 * (1 + tol))
        s1, s2 = max(ox * tol, 0.06), max(o2 * tol, 0.06)
        return [z for z in self.sat[a:b]
                if abs(z[1] - ox) <= s1 and abs(z[2] - o2) <= s2
                and (lig_n is None or z[3] == lig_n)]

    def kiyas(self, oran, lig=None, ulke=None, en_az_tum=25, en_az_lig=8):
        o1, ox, o2 = [float(x) for x in oran]
        lig_n = norm(lig) if lig else None
        tum, tol = [], TOL_TUM[-1]
        for tol in TOL_TUM:
            tum = self._aday(o1, ox, o2, tol)
            if len(tum) >= en_az_tum:
                break
        kendi, tolg = [], TOL_LIG[-1]
        if lig_n:
            for tolg in TOL_LIG:
                kendi = self._aday(o1, ox, o2, tolg, lig_n=lig_n)
                if len(kendi) >= en_az_lig:
                    break
        return {"oran": [o1, ox, o2], "tol": tol, "tolg": tolg,
                "lig": lig, "ulke": ulke,
                "tum": self._ozet(tum), "kendi": self._ozet(kendi)}

    @staticmethod
    def _ozet(L):
        if not L:
            return None
        n = len(L)
        s1 = sum(1 for z in L if z[8] > z[9])
        sx = sum(1 for z in L if z[8] == z[9])
        s2 = n - s1 - sx
        toplam_gol = sum((z[8] or 0) + (z[9] or 0) for z in L)
        u25 = sum(1 for z in L if (z[8] or 0) + (z[9] or 0) <= 2)
        kg = sum(1 for z in L if (z[8] or 0) > 0 and (z[9] or 0) > 0)
        skorlar = {}
        for z in L:
            k = "%d-%d" % (z[8], z[9])
            skorlar[k] = skorlar.get(k, 0) + 1
        en_skor = sorted(skorlar.items(), key=lambda x: -x[1])[:5]
        return {
            "n": n,
            "dagilim": [round(100.0 * s1 / n, 1), round(100.0 * sx / n, 1),
                        round(100.0 * s2 / n, 1)],
            "ort_gol": round(toplam_gol / n, 2),
            "alt25": round(100.0 * u25 / n, 1),
            "kg_var": round(100.0 * kg / n, 1),
            "skorlar": [[k, round(100.0 * v / n, 1)] for k, v in en_skor],
            "ornek": [
                {"t": z[5], "l": z[3].title(), "e": z[6], "d": z[7],
                 "s": "%d-%d" % (z[8], z[9]),
                 "iy": ("%d-%d" % (z[10], z[11])) if z[10] is not None and z[11] is not None else None,
                 "o": [z[0], z[1], z[2]]}
                for z in sorted(L, key=lambda z: z[5], reverse=True)[:15]],
        }


# ------------------------------------------------------------------ bugün
def bugun_mac_lari_topla():
    """Bugünün maçlarını + oranlarını toplar (paket taraması > API)."""
    maclar = []
    tt = os.path.join(VERI, "tam_tarama.json")
    if os.path.exists(tt):
        try:
            for m in json.load(open(tt, encoding="utf-8")):
                o = m.get("o")
                if o and len(o) == 3 and m.get("home") and m.get("away"):
                    maclar.append({"ev": m["home"], "dep": m["away"],
                                   "lig": m.get("lig", ""), "saat": m.get("saat", ""),
                                   "oran": [float(x) for x in o], "kaynak": "bulten"})
        except Exception as e:  # noqa: BLE001
            print("tam_tarama.json okunamadı: %s" % e)
    ab = os.path.join(VERI, "api_bugun.json")
    if os.path.exists(ab):
        try:
            gorulen = {(norm(m["ev"]), norm(m["dep"])) for m in maclar}
            for m in (json.load(open(ab, encoding="utf-8")).get("maclar") or []):
                if not (m.get("oran") and len(m["oran"]) == 3):
                    continue
                k = (norm(m["ev"]), norm(m["dep"]))
                if k in gorulen:
                    continue
                gorulen.add(k)
                maclar.append({"ev": m["ev"], "dep": m["dep"], "lig": m.get("lig", ""),
                               "saat": m.get("saat", ""), "oran": m["oran"],
                               "kaynak": m.get("kaynak", "api")})
        except Exception as e:  # noqa: BLE001
            print("api_bugun.json okunamadı: %s" % e)
    maclar.sort(key=lambda m: (m.get("saat") or "99", norm(m["ev"])))
    return maclar


# ------------------------------------------------------------------- HTML
CSS = ("body{margin:0;background:#f6f7f9;color:#16212e;font-family:-apple-system,"
       "BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif}"
       ".wrap{max-width:1080px;margin:0 auto;padding:14px 12px 60px}"
       ".card{background:#fff;border:1px solid #e3e8ee;border-radius:12px;"
       "padding:12px 14px;margin:10px 0}"
       "h1{font-size:19px;margin:6px 0 2px}h3{margin:0 0 8px;font-size:14px;color:#0d5c3a}"
       ".mini{font-size:11.5px;color:#68788a}.buyuk{font-size:16px;font-weight:700}"
       ".bar{height:10px;border-radius:6px;overflow:hidden;background:#eef1f4;"
       "display:flex;margin:6px 0 2px}"
       ".b1{background:#1a7f4b}.bx{background:#8a8f98}.b2{background:#20508c}"
       ".yuz{font-size:12px;font-weight:600}"
       "table.kt{width:100%;border-collapse:collapse}table.kt th{background:#f2f5f8;"
       "text-align:left;padding:6px 7px;font-size:12px}"
       "table.kt td{padding:5px 7px;border-bottom:1px solid #eef1f4;font-size:12.5px}"
       "td.b{font-weight:700}.sar{max-height:44vh;overflow:auto}")


def _bar(dagilim):
    w = [max(x, 0.5) for x in dagilim]
    toplam = sum(w) or 1
    return ("<div class='bar'>"
            "<div class='b1' style='width:%.1f%%'></div>"
            "<div class='bx' style='width:%.1f%%'></div>"
            "<div class='b2' style='width:%.1f%%'></div></div>"
            "<div class='mini'><span class='yuz'>1 → %%%s</span> · "
            "<span class='yuz'>X → %%%s</span> · <span class='yuz'>2 → %%%s</span></div>"
            % (100 * w[0] / toplam, 100 * w[1] / toplam, 100 * w[2] / toplam,
               dagilim[0], dagilim[1], dagilim[2]))


def _kart(i, m, r):
    o = r["oran"]
    g = ["<div class='card'>"
         "<div style='display:flex;justify-content:space-between;align-items:baseline'>"
         "<div class='buyuk'>%d. %s — %s</div><div class='mini'>%s</div></div>"
         "<div class='mini'>%s · %s · oran %s · kaynak %s</div>"
         % (i, H.escape(m["ev"]), H.escape(m["dep"]), H.escape(m.get("saat", "")),
            H.escape(m.get("lig", "")),
            (H.escape(m.get("saat", "")) or "—"),
            " / ".join("%.2f" % x for x in o), H.escape(m.get("kaynak", "")))]
    g.append("<h3>TÜM LİGLER — %d benzer maç (±%%%d)</h3>" % ((r["tum"] or {}).get("n", 0), round(r["tol"] * 100)))
    if r["tum"]:
        t = r["tum"]
        g.append(_bar(t["dagilim"]))
        g.append("<div class='mini'>ort. gol %s · alt 2.5 %%%s · KG var %%%s · "
                 "en sık: %s</div>"
                 % (t["ort_gol"], t["alt25"], t["kg_var"],
                    ", ".join("%s (%%%s)" % (k, v) for k, v in t["skorlar"][:3])))
        g.append("<div class='sar'><table class='kt'>"
                 "<thead><tr><th>Tarih</th><th>Maç</th><th>MS</th><th>İY</th>"
                 "<th>Oran</th><th>Lig</th></tr></thead><tbody>"
                 + "".join(
                     "<tr><td>%s</td><td>%s — %s</td><td class='b'>%s</td>"
                     "<td class='b'>%s</td><td>%.2f/%.2f/%.2f</td><td class='mini'>%s</td></tr>"
                     % (H.escape(z["t"]), H.escape(z["e"]), H.escape(z["d"]), z["s"],
                        z.get("iy") or "–", z["o"][0], z["o"][1], z["o"][2],
                        H.escape(z["l"]))
                     for z in t["ornek"][:12]) + "</tbody></table></div>")
    if r["kendi"]:
        k = r["kendi"]
        g.append("<h3>KENDİ LİGİ (%s) — %d maç (±%%%d)</h3>"
                 % (H.escape(m.get("lig", "")), k["n"], round(r["tolg"] * 100)))
        g.append(_bar(k["dagilim"]))
    g.append("</div>")
    return "".join(g)


def html_uret(kayitlar, hedef):
    bugun = datetime.now().strftime("%d.%m.%Y")
    govde = ["<h1>⚽ Oran Kıyası — %s</h1>"
             "<div class='mini'>Benzer oranlı tarihsel maçların sonuç dağılımı · "
             "arşiv: %s</div>" % (bugun, H.escape(str(kayitlar.get("arsiv", ""))))]
    for i, (m, r) in enumerate(kayitlar["maclar"], 1):
        govde.append(_kart(i, m, r))
    belge = ("<!DOCTYPE html><html lang='tr'><head><meta charset='utf-8'>"
             "<meta name='viewport' content='width=device-width,initial-scale=1'>"
             "<title>Oran Kıyası — %s</title><style>%s</style></head>"
             "<body><div class='wrap'>%s</div></body></html>"
             % (bugun, CSS, "".join(govde)))
    with open(hedef, "w", encoding="utf-8") as f:
        f.write(belge)
    print("HTML: %s" % hedef)


# ------------------------------------------------------------------- main
def main():
    p = argparse.ArgumentParser(description="Benzer oranlı maç kıyası")
    p.add_argument("--arsiv", default="", help="arşiv JSON yolu (boşsa otomatik)")
    p.add_argument("--bugun", action="store_true", help="bugünün maçlarının hepsini kıyasla")
    p.add_argument("--ev", default=""); p.add_argument("--dep", default="")
    p.add_argument("--lig", default=""); p.add_argument("--ulke", default="")
    p.add_argument("--oran", nargs=3, type=float, metavar=("1", "X", "2"))
    p.add_argument("--html", default=os.path.join(KOK, "ORAN_KIYAS.html"))
    p.add_argument("--sinir", type=int, default=60, help="bugün modunda en fazla kaç maç")
    a = p.parse_args()

    sat, _ = arsiv_yukle(a.arsiv or None)
    if not sat:
        return 1
    k = Kiyasci(sat)

    if a.bugun or not a.oran:
        maclar = bugun_mac_lari_topla()
        if not maclar:
            print("Bugün için oranlı maç bulunamadı "
                  "(veri/tam_tarama.json veya veri/api_bugun.json gerekli).")
            return 1
        kayitlar = []
        for m in maclar[:a.sinir]:
            r = k.kiyas(m["oran"], lig=m.get("lig"), ulke=m.get("ulke"))
            kayitlar.append((m, r))
            t = r["tum"] or {}
            print("· %s — %s [%s] %s → %d maç: 1 %%%s · X %%%s · 2 %%%s"
                  % (m["ev"], m["dep"], m.get("saat", ""),
                     "/".join("%.2f" % x for x in m["oran"]),
                     t.get("n", 0), t.get("dagilim", ["-"] * 3)[0],
                     t.get("dagilim", ["-"] * 3)[1], t.get("dagilim", ["-"] * 3)[2]))
        out = {"uretim": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()),
               "arsiv": len(sat),
               "maclar": [{"mac": m, "kiyas": r} for m, r in kayitlar]}
        with open(os.path.join(VERI, "kiyas_bugun.json"), "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
        print("\n%d maç kıyaslandı → veri/kiyas_bugun.json" % len(kayitlar))
        html_uret({"arsiv": len(sat), "maclar": kayitlar}, a.html)
        return 0

    # tek maç modu
    r = k.kiyas(a.oran, lig=a.lig or None, ulke=a.ulke or None)
    print("\n%s — %s  ·  oran %s"
          % (a.ev or "?", a.dep or "?", " / ".join("%.2f" % x for x in a.oran)))
    for ad, oz, tol_deger in (("TÜM LİGLER", r["tum"], r["tol"]),
                              ("KENDİ LİGİ", r["kendi"], r["tolg"])):
        if not oz:
            print("%s: yeterli maç yok" % ad)
            continue
        print("%s (±%%%d): %d maç → 1 %%%s · X %%%s · 2 %%%s · ort.gol %s · "
              "alt2.5 %%%s · en sık %s"
              % (ad, round(tol_deger * 100),
                 oz["n"], oz["dagilim"][0], oz["dagilim"][1], oz["dagilim"][2],
                 oz["ort_gol"], oz["alt25"],
                 ", ".join("%s(%%%s)" % (x, y) for x, y in oz["skorlar"][:3])))
    with open(os.path.join(VERI, "kiyas_son.json"), "w", encoding="utf-8") as f:
        json.dump({"ev": a.ev, "dep": a.dep, "lig": a.lig, "ulke": a.ulke,
                   "kiyas": r}, f, ensure_ascii=False, indent=1)
    print("\n→ veri/kiyas_son.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
