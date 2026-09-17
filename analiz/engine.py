# -*- coding: utf-8 -*-
"""
BULTEN 40-KATMANLI ANALIZ MOTORU  |  17.09.2026
Poisson + Dixon-Coles benzeri duzeltme, IY split, korner modeli, value/PME.
Girdi: takim bazli xG-temelli guc parametreleri (lig gucu normalize).
"""
import math
from itertools import product

def pois(k, l):
    return math.exp(-l) * l**k / math.factorial(k)

def score_matrix(lh, la, rho=-0.06, n=9):
    m = [[pois(i, lh)*pois(j, la) for j in range(n)] for i in range(n)]
    # Dixon-Coles dusuk skor duzeltmesi
    def tau(i,j):
        if i==0 and j==0: return 1-lh*la*rho
        if i==0 and j==1: return 1+lh*rho
        if i==1 and j==0: return 1+la*rho
        if i==1 and j==1: return 1-rho
        return 1.0
    for i in range(n):
        for j in range(n):
            m[i][j]*=tau(i,j)
    s=sum(map(sum,m))
    return [[v/s for v in r] for r in m]

def markets(lh, la, iy_pay_h, iy_pay_a):
    M = score_matrix(lh, la)
    n=len(M)
    ms1 = sum(M[i][j] for i in range(n) for j in range(n) if i>j)
    msx = sum(M[i][i] for i in range(n))
    ms2 = 1-ms1-msx
    kg  = sum(M[i][j] for i in range(1,n) for j in range(1,n))
    u25 = sum(M[i][j] for i in range(n) for j in range(n) if i+j>=3)
    u15 = sum(M[i][j] for i in range(n) for j in range(n) if i+j>=2)
    u35 = sum(M[i][j] for i in range(n) for j in range(n) if i+j>=4)
    # IY
    hh, ha = lh*iy_pay_h, la*iy_pay_a
    H = score_matrix(hh, ha, rho=-0.03)
    iy15 = sum(H[i][j] for i in range(n) for j in range(n) if i+j>=2)
    iy05 = 1-H[0][0]
    iykg = sum(H[i][j] for i in range(1,n) for j in range(1,n))
    iy1  = sum(H[i][j] for i in range(n) for j in range(n) if i>j)
    iyx  = sum(H[i][i] for i in range(n))
    return dict(MS1=ms1, MSX=msx, MS2=ms2, KG=kg, U15=u15, U25=u25, U35=u35,
                IY15=iy15, IY05=iy05, IYKG=iykg, IY1=iy1, IYX=iyx,
                lam=(lh,la), iylam=(hh,ha))

def corners(ch, ca, line_mac, line_iy, iy_pay=0.44):
    tot = ch+ca
    # negatif binom yaklasimi -> Poisson overdispersion duzeltmeli
    def over(lam, line, disp=1.18):
        l = lam
        k = math.floor(line)+1
        p = 1-sum(pois(i, l) for i in range(k))
        # overdispersion: ust kuyruk kalinlasir, cizgi ustundeyse hafif artir
        return min(0.97, p*(1+ (disp-1)*(0.5 if l>line else -0.35)))
    return dict(tot=tot, mac_ust=over(tot, line_mac), iy_tot=tot*iy_pay,
                iy_ust=over(tot*iy_pay, line_iy, 1.14))

def value(p, odd):
    return p*odd-1

def pme(p_model, p_piyasa):
    """Piyasa-Model Eslesme: pozitif = model piyasadan daha iyimser."""
    return (p_model-p_piyasa)*100
