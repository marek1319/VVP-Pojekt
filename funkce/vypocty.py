import numpy as np

class Vypocty:
    def aktualni_dane(self, prijmi, vydaje):
        sazba_dane = 0.21     
        zaklad = prijmi - vydaje
        dan = zaklad * sazba_dane
        dan = np.round(dan, 2)
        return dan