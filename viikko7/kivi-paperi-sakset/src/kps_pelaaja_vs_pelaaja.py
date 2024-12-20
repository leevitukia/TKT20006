from kps import KPS 

class KPSPelaajaVsPelaaja(KPS):
    def _toinen_siirto(self):
        toinen_siirto = input("Toisen pelaajan siirto: ")
        return toinen_siirto
    
    def aseta_siirto(self, siirto):
        super().aseta_siirto(siirto)
