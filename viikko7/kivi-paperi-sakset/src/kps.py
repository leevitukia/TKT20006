from tuomari import Tuomari

class KPS:
    def __init__(self):
        pass

    def pelaa(self):
        tuomari = Tuomari()

        ensimmainen_siirto = self._ensimmainen_siirto()
        toinen_siirto = self._toinen_siirto()

        while self._onko_ok_siirto(ensimmainen_siirto) and self._onko_ok_siirto(toinen_siirto):
            tuomari.kirjaa_siirto(ensimmainen_siirto, toinen_siirto)
            print(tuomari)

            ensimmainen_siirto = self._ensimmainen_siirto()
            toinen_siirto = self._toinen_siirto()
            self.aseta_siirto(ensimmainen_siirto)

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s" 

    def _ensimmainen_siirto(self):
        siirto = input("Ensimmäisen pelaajan siirto: ")
        return siirto 
    def _toinen_siirto(self):
        pass
    def aseta_siirto(self, siirto):
        pass