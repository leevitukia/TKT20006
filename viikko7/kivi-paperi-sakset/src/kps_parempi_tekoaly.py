from kps import KPS

class KPSParempiTekoaly(KPS):
    def __init__(self, muistin_koko = 10):
        self._muisti = [None] * muistin_koko
        self._vapaa_muisti_indeksi = 0

    def _toinen_siirto(self):
        
        if self._vapaa_muisti_indeksi == 0 or self._vapaa_muisti_indeksi == 1:
            siirto = "k"
        else:
            viimeisin_siirto = self._muisti[self._vapaa_muisti_indeksi - 1]

            k = 0
            p = 0
            s = 0

            for i in range(0, self._vapaa_muisti_indeksi - 1):
                if viimeisin_siirto == self._muisti[i]:
                    seuraava = self._muisti[i + 1]

                    if seuraava == "k":
                        k = k + 1
                    elif seuraava == "p":
                        p = p + 1
                    else:
                        s = s + 1

            # Tehdään siirron valinta esimerkiksi seuraavasti;
            # - jos kiviä eniten, annetaan aina paperi
            # - jos papereita eniten, annetaan aina sakset
            # muulloin annetaan aina kivi
            if k > p or k > s:
                siirto = "p"
            elif p > k or p > s:
                siirto = "s"
            else:
                siirto = "k"
        print(f"Tietokone valitsi: {siirto}")
        return siirto
        # Tehokkaampiakin tapoja löytyy, mutta niistä lisää
        # Johdatus Tekoälyyn kurssilla!
    
    def aseta_siirto(self, siirto):
        if self._vapaa_muisti_indeksi == len(self._muisti):
            for i in range(1, len(self._muisti)):
                self._muisti[i - 1] = self._muisti[i]

            self._vapaa_muisti_indeksi = self._vapaa_muisti_indeksi - 1

        self._muisti[self._vapaa_muisti_indeksi] = siirto
        self._vapaa_muisti_indeksi = self._vapaa_muisti_indeksi + 1

