from kps import KPS

class KPSTekoaly(KPS):
    def __init__(self):
        self._siirto = 0

    def _toinen_siirto(self):
        
        self._siirto = self._siirto + 1
        self._siirto = self._siirto % 3
        siirto = ""
        if self._siirto == 0:
            siirto = "k"
        elif self._siirto == 1:
            siirto = "p"
        else:
            siirto = "s"
        
        print(f"Tietokone valitsi: {siirto}")
        return siirto
    
