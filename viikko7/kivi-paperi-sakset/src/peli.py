from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

def luo_peli(tyyppi):
    print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")
    if tyyppi == "a":
        return KPSPelaajaVsPelaaja()
    elif tyyppi == "b":
        return KPSTekoaly()
    elif tyyppi == "c":
        return KPSParempiTekoaly()
    return kps