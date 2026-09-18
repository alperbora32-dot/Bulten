#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BULTEN_APP.HTML ÜRETİCİ — tek dosyalık, tarayıcıda çalışan bülten uygulaması.

Üretilen HTML dosyası:
  · İnternet varken:  ücretsiz API'lerden (ESPN / TheSportsDB / 365Scores /
                      OpenLigaDB) bugünün maçlarını, skorları ve puan durumunu
                      CANLI çeker (tarayıcıdan doğrudan, kurulum yok).
  · İnternetsizken:   gömülü oran arşiviyle "benzer oranlı maç kıyası"
                      tamamen ÇEVRİMDIŞI çalışır.

Gömülü arşiv: veri/kapanis_arsiv_buyuk.json (kapanis_arsiv.json → oran_arsiv.json
geri dönüşümlü) 18 bayt/maç ikili formatta, base64 olarak HTML içine gömülür:
  o1,ox,o2 (uint16, ×1000) · hg,ag (uint8) · ih,ia (int8, -1=yok)
  · gün (uint16, 2000-01-01'den) · lig (uint16) · ev,dep (uint16)

Kullanım:
  python3 bulten_app_uret.py                # → BULTEN_APP.html
  python3 bulten_app_uret.py --cikti x.html
"""
import argparse
import base64
import json
import os
import struct
import sys
import time
from datetime import date

KOK = os.path.dirname(os.path.abspath(__file__))
VERI = os.path.join(KOK, "veri")
ARSIV_ONCELIGI = [
    os.path.join(VERI, "kapanis_arsiv_buyuk.json"),
    os.path.join(VERI, "kapanis_arsiv.json"),
    os.path.join(VERI, "oran_arsiv.json"),
]
EPOCH = date(2000, 1, 1)

ESPN_LIGLER = [
    ("tur.1", "Türkiye · Süper Lig"), ("eng.1", "İngiltere · Premier Lig"),
    ("eng.2", "İngiltere · Championship"), ("esp.1", "İspanya · La Liga"),
    ("ger.1", "Almanya · Bundesliga"), ("ita.1", "İtalya · Serie A"),
    ("fra.1", "Fransa · Ligue 1"), ("ned.1", "Hollanda · Eredivisie"),
    ("por.1", "Portekiz · Primeira Liga"), ("bel.1", "Belçika · Jupiler"),
    ("sco.1", "İskoçya · Premiership"), ("gre.1", "Yunanistan · Super League"),
    ("uefa.champions", "Avrupa · Şampiyonlar Ligi"),
    ("uefa.europa", "Avrupa · Avrupa Ligi"),
    ("usa.1", "ABD · MLS"), ("bra.1", "Brezilya · Serie A"),
]


def arsiv_yukle(yol=None):
    yol = yol or next((a for a in ARSIV_ONCELIGI if os.path.exists(a)), None)
    if not yol:
        print("Arşiv yok! Önce: python3 oran_arsiv_cek.py --birlestir")
        return None
    print("arşiv okunuyor: %s" % os.path.basename(yol))
    return json.load(open(yol, encoding="utf-8"))


def kodla(kayitlar):
    """Kayıtları 18 baytlık ikili bloğa + sözlüklere kodlar."""
    takimlar, takim_idx = [], {}
    ligler, lig_idx = [], {}
    buf = bytearray()
    atlanan = 0
    for m in kayitlar:
        kp = m.get("kp") or m.get("ac")
        try:
            o1, ox, o2 = (int(round(float(x) * 1000)) for x in kp)
        except (TypeError, ValueError):
            atlanan += 1
            continue
        if not all(1001 <= v <= 65535 for v in (o1, ox, o2)):
            atlanan += 1
            continue
        hg, ag = m.get("hg"), m.get("ag")
        if hg is None or ag is None:
            atlanan += 1
            continue
        hg, ag = int(hg), int(ag)
        if not (0 <= hg <= 255 and 0 <= ag <= 255):
            atlanan += 1
            continue
        ih = m.get("ih")
        ia = m.get("ia")
        ih = -1 if ih is None else max(-1, min(127, int(ih)))
        ia = -1 if ia is None else max(-1, min(127, int(ia)))
        gun = 0
        try:
            g, a, y = (m.get("t") or "").split("/")
            gun = (date(int(y), int(a), int(g)) - EPOCH).days
        except (ValueError, TypeError):
            gun = 0
        gun = max(0, min(65535, gun))
        lk = "%s · %s" % ((m.get("u") or "—"), (m.get("l") or "—"))
        li = lig_idx.get(lk)
        if li is None:
            li = len(ligler)
            lig_idx[lk] = li
            ligler.append(lk)
        adi = m.get("e") or "?"
        ei = takim_idx.get(adi)
        if ei is None:
            ei = len(takimlar)
            takim_idx[adi] = ei
            takimlar.append(adi)
        adi = m.get("d") or "?"
        di = takim_idx.get(adi)
        if di is None:
            di = len(takimlar)
            takim_idx[adi] = di
            takimlar.append(adi)
        buf += struct.pack("<HHHBBbbHHHH", o1, ox, o2, hg, ag, ih, ia,
                           gun, li, ei, di)
    return bytes(buf), takimlar, ligler, atlanan


SABLON = """<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Bülten — Canlı + Oran Kıyası</title>
<style>
body{margin:0;background:#f6f7f9;color:#16212e;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif}
.wrap{max-width:1080px;margin:0 auto;padding:12px 12px 70px}
nav{position:sticky;top:0;z-index:5;background:#fff;border-bottom:1px solid #e3e8ee;
display:flex;gap:6px;padding:8px 12px;max-width:1080px;margin:0 auto}
nav button{border:1px solid #d7dee8;background:#f2f5f8;border-radius:9px;padding:8px 14px;
font-size:13.5px;font-weight:600;color:#3a4a5c;cursor:pointer}
nav button.aktif{background:#0d5c3a;border-color:#0d5c3a;color:#fff}
.card{background:#fff;border:1px solid #e3e8ee;border-radius:12px;padding:12px 14px;margin:10px 0}
h1{font-size:19px;margin:6px 0 2px}h3{margin:0 0 8px;font-size:14px;color:#0d5c3a}
.mini{font-size:11.5px;color:#68788a}.buyuk{font-size:16px;font-weight:700}
input,select{border:1px solid #cfd8e3;border-radius:8px;padding:8px 9px;font-size:14px;background:#fff}
input[type=number]{width:86px}
button.islem{background:#0d5c3a;color:#fff;border:0;border-radius:9px;padding:9px 16px;
font-size:14px;font-weight:600;cursor:pointer}
table.kt{width:100%;border-collapse:collapse}
table.kt th{background:#f2f5f8;text-align:left;padding:6px 7px;font-size:12px;position:sticky;top:0}
table.kt td{padding:5px 7px;border-bottom:1px solid #eef1f4;font-size:12.5px}
td.b{font-weight:700}.sar{max-height:64vh;overflow:auto}
.bar{height:11px;border-radius:6px;overflow:hidden;background:#eef1f4;display:flex;margin:6px 0 2px}
.b1{background:#1a7f4b}.bx{background:#8a8f98}.b2{background:#20508c}
.yuz{font-size:12.5px;font-weight:600}
.hata{color:#b3261e}.ok{color:#0d5c3a;font-weight:600}
button.k{border:1px solid #bcd8cc;background:#eaf6f0;border-radius:7px;padding:3px 8px;
font-size:11.5px;cursor:pointer;color:#0d5c3a;font-weight:600}
.bosluk{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:8px 0}
</style>
</head>
<body>
<nav>
  <button id="sekme1" class="aktif" onclick="sekme(1)">⚽ Bugün</button>
  <button id="sekme2" onclick="sekme(2)">⚖️ Oran Kıyası</button>
  <button id="sekme3" onclick="sekme(3)">📊 Puan Durumu</button>
</nav>
<div class="wrap">

<!-- ==================================================== SEKME 1: BUGÜN -->
<section id="bolum1">
  <h1>⚽ Bugünün Maçları</h1>
  <div class="mini">ESPN + TheSportsDB + 365Scores — ücretsiz, anahtarsız API'ler ·
  saatler Türkiye saati · 60 sn'de otomatik yenilenir</div>
  <div class="card">
    <div class="bosluk">
      <b style="font-size:13.5px">Lig:</b>
      <select id="ligSec"></select>
      <button class="islem" onclick="bugunYukle(true)">Yenile</button>
      <span class="mini" id="bugunDurum"></span>
    </div>
    <div class="sar"><table class="kt">
      <thead><tr><th>Saat</th><th>Maç</th><th>Skor</th><th>Durum</th><th>Form</th><th></th></tr></thead>
      <tbody id="bugunTablo"></tbody>
    </table></div>
  </div>
  <div class="card">
    <h3>Günün tüm maçları — 365Scores (oranlı) <span class="mini" id="x365Durum"></span></h3>
    <div class="bosluk"><input id="x365Filtre" placeholder="takım/lig ara…" style="flex:1"
      oninput="x365Ciz()"></div>
    <div class="sar"><table class="kt">
      <thead><tr><th>Saat</th><th>Maç</th><th>Skor</th><th>Oran 1X2</th><th>Lig</th><th></th></tr></thead>
      <tbody id="x365Tablo"></tbody>
    </table></div>
  </div>
</section>

<!-- ==================================================== SEKME 2: KIYAS -->
<section id="bolum2" style="display:none">
  <h1>⚖️ Oran Kıyası</h1>
  <div class="mini">Gömülü arşiv: %%MAC%% maç (%%ARSKAYNAK%%) ·
  hedef orana ±%2'den başlayıp yeterli maç bulunana kadar gevşetilir · çevrimdışı çalışır</div>
  <div class="card">
    <div class="bosluk">
      <input id="kEv" placeholder="Ev sahibi" style="width:150px">
      <span class="buyuk">—</span>
      <input id="kDep" placeholder="Deplasman" style="width:150px">
      <input id="k1" type="number" step="0.01" value="2.30"> 
      <input id="kX" type="number" step="0.01" value="3.30">
      <input id="k2" type="number" step="0.01" value="3.10">
      <select id="kLig"></select>
      <button class="islem" onclick="kiyasCalistir()">Kıyasla</button>
    </div>
    <div class="mini">1 · X · 2 oranlarını gir (zorunlu). Takım adları etiket içindir.
    Lig seçilirse "kendi ligi" analizi de yapılır.</div>
  </div>
  <div id="kiyasSonuc"></div>
</section>

<!-- ==================================================== SEKME 3: PUAN -->
<section id="bolum3" style="display:none">
  <h1>📊 Puan Durumu</h1>
  <div class="mini">ESPN API — canlı</div>
  <div class="card">
    <div class="bosluk">
      <select id="puanLig"></select>
      <button class="islem" onclick="puanYukle()">Getir</button>
    </div>
    <div class="sar"><table class="kt">
      <thead><tr><th>#</th><th>Takım</th><th>O</th><th>G</th><th>B</th><th>M</th>
      <th>AV</th><th>P</th><th>Form</th></tr></thead>
      <tbody id="puanTablo"></tbody>
    </table></div>
  </div>
</section>

<div class="mini" style="margin:18px 2px">
  %%MAC%% maçlık oran arşivi gömülüdür (üretim: %%URETIM%%) · kaynaklar:
  betexplorer (paket arşivi) + football-data.co.uk + EPL aynası ·
  arşivi yenilemek için <code>python3 oran_arsiv_cek.py --birlestir &amp;&amp;
  python3 bulten_app_uret.py</code>
</div>
</div>

<script id="arsiv" type="application/json">%%PAKET%%</script>
<script>
"use strict";
const PAKET = JSON.parse(document.getElementById("arsiv").textContent);

/*CORE-START*/
function arsivAc(p){
  const bin = Uint8Array.from(atob(p.b64), c => c.charCodeAt(0));
  const dv = new DataView(bin.buffer);
  const N = Math.floor(bin.length / 18);
  const A = {n:N, o1:new Float64Array(N), ox:new Float64Array(N), o2:new Float64Array(N),
    hg:new Uint8Array(N), ag:new Uint8Array(N), ih:new Int8Array(N), ia:new Int8Array(N),
    gun:new Uint16Array(N), lig:new Uint16Array(N), ev:new Uint16Array(N), dep:new Uint16Array(N),
    takimlar:p.takimlar, ligler:p.ligler};
  for(let i=0;i<N;i++){
    const o=i*18;
    A.o1[i]=dv.getUint16(o,true)/1000;   A.ox[i]=dv.getUint16(o+2,true)/1000;
    A.o2[i]=dv.getUint16(o+4,true)/1000; A.hg[i]=dv.getUint8(o+6);
    A.ag[i]=dv.getUint8(o+7);            A.ih[i]=dv.getInt8(o+8);
    A.ia[i]=dv.getInt8(o+9);             A.gun[i]=dv.getUint16(o+10,true);
    A.lig[i]=dv.getUint16(o+12,true);    A.ev[i]=dv.getUint16(o+14,true);
    A.dep[i]=dv.getUint16(o+16,true);
  }
  return A;
}
function gunStr(g){
  const d = new Date(Date.UTC(2000,0,1) + g*86400000);
  return String(d.getUTCDate()).padStart(2,"0") + "/" +
         String(d.getUTCMonth()+1).padStart(2,"0") + "/" + d.getUTCFullYear();
}
function istatistik(A, idx){
  if(!idx.length) return null;
  const n = idx.length;
  let s1=0, sx=0, gol=0, u25=0, kg=0;
  const skor = {};
  for(const i of idx){
    const h=A.hg[i], a=A.ag[i];
    if(h>a) s1++; else if(h===a) sx++;
    gol += h+a; if(h+a<=2) u25++; if(h>0&&a>0) kg++;
    const k=h+"-"+a; skor[k]=(skor[k]||0)+1;
  }
  const skorlar = Object.entries(skor).sort((x,y)=>y[1]-x[1]).slice(0,5)
    .map(e => [e[0], Math.round(e[1]*1000/n)/10]);
  const ornek = idx.slice().sort((x,y)=>A.gun[y]-A.gun[x]).slice(0,15).map(i => ({
    t:gunStr(A.gun[i]), lig:A.ligler[A.lig[i]],
    ev:A.takimlar[A.ev[i]], dep:A.takimlar[A.dep[i]],
    ms:A.hg[i]+"-"+A.ag[i],
    iy:(A.ih[i]<0 ? null : A.ih[i]+"-"+A.ia[i]),
    o:[A.o1[i], A.ox[i], A.o2[i]]
  }));
  const r = v => Math.round(v*1000/n)/10;
  return {n:n, dagilim:[r(s1), r(sx), r(n-s1-sx)],
    ortGol: Math.round(gol*100/n)/100, alt25:r(u25), kg:r(kg),
    skorlar:skorlar, ornek:ornek};
}
function kiyas(A, oran, ligIdx){
  const o1=oran[0], ox=oran[1], o2=oran[2];
  const tara = (tol, ligFiltre) => {
    const out = [];
    const l1=o1*tol, lx=Math.max(ox*tol,0.06), l2=Math.max(o2*tol,0.06);
    for(let i=0;i<A.n;i++){
      if(ligFiltre!==null && A.lig[i]!==ligFiltre) continue;
      if(Math.abs(A.o1[i]-o1)<=l1 && Math.abs(A.ox[i]-ox)<=lx &&
         Math.abs(A.o2[i]-o2)<=l2) out.push(i);
    }
    return out;
  };
  let tum=[], tol=0.06;
  for(const t of [0.02,0.03,0.045,0.06]){
    tol=t; tum=tara(t,null); if(tum.length>=25) break;
  }
  let kendi=[], tolg=0.13;
  if(ligIdx!==null && ligIdx!==undefined){
    tolg=0.02;
    for(const t of [0.02,0.03,0.045,0.06,0.09,0.13]){
      tolg=t; kendi=tara(t,ligIdx); if(kendi.length>=8) break;
    }
  }
  return {tol:tol, tolg:tolg, tum:istatistik(A,tum), kendi:istatistik(A,kendi)};
}
/*CORE-END*/

const ARS = arsivAc(PAKET);

/* ------------------------------- sekmeler */
function sekme(n){
  for(const i of [1,2,3]){
    document.getElementById("sekme"+i).classList.toggle("aktif", i===n);
    document.getElementById("bolum"+i).style.display = (i===n ? "" : "none");
  }
}

/* ------------------------------- BUGÜN */
const LIGLER = %%ESPNLIGLER%%;
function ligDoldur(){
  const s1 = document.getElementById("ligSec");
  const s2 = document.getElementById("puanLig");
  for(const [kod, ad] of LIGLER){
    s1.add(new Option(ad, kod));
    s2.add(new Option(ad, kod));
  }
  s1.value = "tur.1"; s2.value = "tur.1";
}
function trSaat(iso){
  try{
    return new Date(iso).toLocaleTimeString("tr-TR",
      {hour:"2-digit", minute:"2-digit", timeZone:"Europe/Istanbul"});
  }catch(e){ return (iso||"").slice(11,16); }
}
async function bugunYukle(manuel){
  const kod = document.getElementById("ligSec").value;
  const durum = document.getElementById("bugunDurum");
  const govde = document.getElementById("bugunTablo");
  durum.textContent = "yükleniyor…";
  try{
    const d = await (await fetch(
      "https://site.api.espn.com/apis/site/v2/sports/soccer/"+kod+"/scoreboard")).json();
    const satirlar = [];
    for(const ev of (d.events||[])){
      try{
        const c = ev.competitions[0];
        const t = {};
        for(const k of (c.competitors||[])) t[k.homeAway]=k;
        const h=t.home||{}, a=t.away||{};
        const devam = (c.status&&c.status.type&&c.status.type.state)||"";
        satirlar.push("<tr><td class='b'>"+trSaat(ev.date)+"</td>"+
          "<td class='b'>"+(h.team?h.team.displayName:"?")+" — "+(a.team?a.team.displayName:"?")+"</td>"+
          "<td class='b'>"+((devam==="in"||devam==="post")?(h.score||0)+"-"+(a.score||0):"—")+"</td>"+
          "<td>"+((c.status&&c.status.type&&c.status.type.shortDetail)||"")+"</td>"+
          "<td class='mini'>"+((h.form||"")+" / "+(a.form||"")).trim()+"</td>"+
          "<td><button class='k' onclick=\"doldur('"+
          (h.team?h.team.displayName.replace(/'/g,""):"")+"','"+
          (a.team?a.team.displayName.replace(/'/g,""):"")+"')\">⚖️ kıyas</button></td></tr>");
      }catch(e){}
    }
    govde.innerHTML = satirlar.join("") ||
      "<tr><td colspan='6' class='mini'>bu ligde bugün maç yok</td></tr>";
    durum.textContent = new Date().toLocaleTimeString("tr-TR",
      {hour:"2-digit",minute:"2-digit"}) + " güncellendi · "+satirlar.length+" maç";
  }catch(e){
    durum.innerHTML = "<span class='hata'>ESPN'e ulaşılamadı (çevrimdışı olabilir)</span>";
  }
  x365Yukle();
}
let X365 = [];
async function x365Yukle(){
  const durum = document.getElementById("x365Durum");
  try{
    const d = await (await fetch(
      "https://webws.365scores.com/web/games/current/?appTypeId=5&langId=1&timezoneName=Europe/Istanbul&userCountryId=94&appVersion=12")).json();
    const komp = {};
    for(const c of (d.competitions||[]))
      komp[c.id] = ((c.countries&&c.countries[0]&&c.countries[0].name)||"")+" · "+(c.name||"");
    X365 = [];
    for(const g of (d.games||[])){
      if(g.sportId!==1 && g.sportId!=="1") continue;
      const h=g.homeCompetitor||{}, a=g.awayCompetitor||{};
      let oran = null;
      for(const aday of [g.odds, g.mainOdds, g.preGameOdds]){
        if(!aday) continue;
        const o = aday.odds || aday;
        const v = [o["1"], o.x, o["2"]];
        if(v.every(x=>x!==undefined&&x!==null&&!isNaN(parseFloat(x)))){
          oran = v.map(parseFloat); break;
        }
      }
      X365.push({saat:trSaat(g.startTime), ev:h.name||"?", dep:a.name||"?",
        skor:(h.score!==undefined?h.score+"-"+a.score:"—"),
        lig:komp[g.competitionId]||"", oran:oran, durum:g.statusText||""});
    }
    durum.textContent = "· "+X365.length+" maç";
  }catch(e){
    durum.innerHTML = "<span class='hata'>· ulaşılamadı</span>";
  }
  x365Ciz();
}
function x365Ciz(){
  const f = (document.getElementById("x365Filtre").value||"").toLowerCase();
  const govde = document.getElementById("x365Tablo");
  const liste = X365.filter(m => !f ||
    (m.ev+" "+m.dep+" "+m.lig).toLowerCase().includes(f)).slice(0,150);
  govde.innerHTML = liste.map(m =>
    "<tr><td class='b'>"+m.saat+"</td><td class='b'>"+m.ev+" — "+m.dep+"</td>"+
    "<td class='b'>"+m.skor+"</td><td>"+(m.oran?m.oran.map(x=>x.toFixed(2)).join(" / "):"—")+"</td>"+
    "<td class='mini'>"+m.lig+"</td>"+
    (m.oran ? "<td><button class='k' onclick='doldurOran(\""+m.ev.replace(/"/g,"")+"\",\""+
      m.dep.replace(/"/g,"")+"\","+m.oran.join(",")+")'>⚖️</button></td>" : "<td></td>")+
    "</tr>").join("") ||
    "<tr><td colspan='6' class='mini'>veri yok</td></tr>";
}

/* ------------------------------- PUAN DURUMU */
async function puanYukle(){
  const kod = document.getElementById("puanLig").value;
  const govde = document.getElementById("puanTablo");
  govde.innerHTML = "<tr><td colspan='9' class='mini'>yükleniyor…</td></tr>";
  try{
    const d = await (await fetch(
      "https://site.api.espn.com/apis/v2/sports/soccer/"+kod+"/standings")).json();
    const satirlar = [];
    for(const cocuk of (d.children||[]))
      for(const ent of ((cocuk.standings||{}).entries||[])){
        const s = {};
        for(const x of (ent.stats||[])){
          s[x.name]=x.displayValue; if(x.abbreviation) s[x.abbreviation]=x.displayValue;
        }
        satirlar.push("<tr><td class='b'>"+(s.rank||s.R||"")+"</td><td class='b'>"+
          ((ent.team||{}).displayName||"")+"</td><td>"+(s.GP||s.gamesPlayed||"")+
          "</td><td>"+(s.W||s.wins||"")+"</td><td>"+(s.D||s.ties||"")+"</td><td>"+
          (s.L||s.losses||"")+"</td><td>"+(s.GD||s.pointDifferential||"")+"</td><td class='b'>"+
          (s.P||s.points||"")+"</td><td class='mini'>"+(s.overall||"")+"</td></tr>");
      }
    govde.innerHTML = satirlar.join("") ||
      "<tr><td colspan='9' class='mini'>puan durumu yok</td></tr>";
  }catch(e){
    govde.innerHTML = "<tr><td colspan='9' class='hata'>ESPN'e ulaşılamadı</td></tr>";
  }
}

/* ------------------------------- KIYAS */
function kLigDoldur(){
  const s = document.getElementById("kLig");
  s.add(new Option("— kendi ligi analizi kapalı —", "-1"));
  const liste = PAKET.ligler.map((ad,i)=>({ad:i, etiket:ad}))
    .sort((a,b)=>b.etiket.localeCompare(a.etiket));
  for(const l of liste) s.add(new Option(l.etiket, String(l.ad)));
}
function doldur(ev, dep){
  document.getElementById("kEv").value = ev;
  document.getElementById("kDep").value = dep;
  sekme(2);
}
function doldurOran(ev, dep, o1, ox, o2){
  doldur(ev, dep);
  document.getElementById("k1").value = o1;
  document.getElementById("kX").value = ox;
  document.getElementById("k2").value = o2;
  kiyasCalistir();
}
function bar(d){
  return "<div class='bar'><div class='b1' style='width:"+d[0]+"%'></div>"+
    "<div class='bx' style='width:"+d[1]+"%'></div>"+
    "<div class='b2' style='width:"+d[2]+"%'></div></div>"+
    "<div class='mini'><span class='yuz'>1 → %"+d[0]+"</span> · "+
    "<span class='yuz'>X → %"+d[1]+"</span> · <span class='yuz'>2 → %"+d[2]+"</span></div>";
}
function blok(baslik, t, tol, ligEtiket){
  if(!t) return "";
  let h = "<div class='card'><h3>"+baslik+" — "+t.n+" maç (±%"+tol+")</h3>"+bar(t.dagilim)+
    "<div class='mini'>ort. gol "+t.ortGol+" · alt 2.5 %"+t.alt25+
    " · KG var %"+t.kg+" · en sık: "+
    t.skorlar.slice(0,3).map(s=>s[0]+" (%"+s[1]+")").join(", ")+"</div>";
  if(ligEtiket) h += "<div class='mini'>"+ligEtiket+"</div>";
  h += "<div class='sar'><table class='kt'><thead><tr><th>Tarih</th><th>Maç</th>"+
    "<th>MS</th><th>İY</th><th>Oran</th><th>Lig</th></tr></thead><tbody>"+
    t.ornek.map(z=>"<tr><td>"+z.t+"</td><td class='b'>"+z.ev+" — "+z.dep+
      "</td><td class='b'>"+z.ms+"</td><td class='b'>"+(z.iy||"–")+"</td><td>"+
      z.o.map(x=>x.toFixed(2)).join(" / ")+"</td><td class='mini'>"+z.lig+
      "</td></tr>").join("")+
    "</tbody></table></div></div>";
  return h;
}
function kiyasCalistir(){
  const o1=parseFloat(document.getElementById("k1").value);
  const ox=parseFloat(document.getElementById("kX").value);
  const o2=parseFloat(document.getElementById("k2").value);
  const sonuc = document.getElementById("kiyasSonuc");
  if(!(o1>1&&ox>1&&o2>1)){ sonuc.innerHTML=
    "<div class='card'><span class='hata'>Geçerli 1 / X / 2 oranları gir (1.01'den büyük)</span></div>"; return; }
  const ligIdx = parseInt(document.getElementById("kLig").value, 10);
  const r = kiyas(ARS, [o1,ox,o2], ligIdx>=0?ligIdx:null);
  const ev=document.getElementById("kEv").value, dep=document.getElementById("kDep").value;
  let h = "<div class='card'><div class='buyuk'>"+(ev||"?")+" — "+(dep||"?")+
    "</div><div class='mini'>hedef oran "+o1.toFixed(2)+" / "+ox.toFixed(2)+" / "+
    o2.toFixed(2)+" · gömülü arşiv: "+ARS.n.toLocaleString("tr-TR")+" maç</div></div>";
  h += blok("TÜM LİGLER", r.tum, Math.round(r.tol*100), null);
  if(ligIdx>=0) h += blok("KENDİ LİGİ — "+ARS.ligler[ligIdx], r.kendi,
    Math.round(r.tolg*100), null);
  sonuc.innerHTML = h;
}

/* ------------------------------- başlat */
ligDoldur(); kLigDoldur(); bugunYukle(); puanYukle();
setInterval(() => { if(document.getElementById("bolum1").style.display!=="none") bugunYukle(); }, 60000);
</script>
</body>
</html>
"""


def main():
    p = argparse.ArgumentParser(description="BULTEN_APP.html üret")
    p.add_argument("--cikti", default=os.path.join(KOK, "BULTEN_APP.html"))
    p.add_argument("--arsiv", default="")
    a = p.parse_args()

    ham = arsiv_yukle(a.arsiv or None)
    if not ham:
        return 1
    print("kodlanıyor…")
    buf, takimlar, ligler, atlanan = kodla(ham)
    b64 = base64.b64encode(buf).decode("ascii")
    print("  %d maç, %d bayt → base64 %.1f MB (atlanan: %d)"
          % (len(ham) - atlanan, len(buf), len(b64) / 1e6, atlanan))

    lig_say = {}
    paket = {"takimlar": takimlar, "ligler": ligler, "b64": b64}

    # JSON'u script etiketi içine gömerken "</script" dizisi geçmemeli
    pj = json.dumps(paket, ensure_ascii=False, separators=(",", ":"))
    assert "</script" not in pj.lower(), "paket içinde </script geçiyor!"

    espn_js = json.dumps(ESPN_LIGLER, ensure_ascii=False)
    html = (SABLON
            .replace("%%PAKET%%", pj)
            .replace("%%MAC%%", "{:,}".format(len(ham) - atlanan).replace(",", "."))
            .replace("%%URETIM%%", time.strftime("%d.%m.%Y %H:%M UTC", time.gmtime()))
            .replace("%%ARSKAYNAK%%", "betexplorer + football-data.co.uk + EPL aynası")
            .replace("%%ESPNLIGLER%%", espn_js))
    with open(a.cikti, "w", encoding="utf-8") as f:
        f.write(html)
    print("✔ %s (%.1f MB) — tarayıcıda aç, kurulum yok"
          % (a.cikti, os.path.getsize(a.cikti) / 1e6))
    return 0


if __name__ == "__main__":
    sys.exit(main())
