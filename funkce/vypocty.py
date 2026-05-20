import numpy as np

class Vypocty:
    def aktualni_dane(self, prijmi: float, vydaje: float) -> float:
        sazba_dane: float = 0.21     
        zaklad: float = prijmi - vydaje
        dan: float = zaklad * sazba_dane
        dan: float = np.round(dan, 2)
        return dan