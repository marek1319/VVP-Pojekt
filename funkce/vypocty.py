import numpy as np

def aktualni_dane(prijmi, vydaje):
    sazba_dane = 0.21     
    zaklad = prijmi - vydaje
    dan = zaklad * sazba_dane
    dan = np.round(dan, 2)
    return dan