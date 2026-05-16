import numpy as np

def predikuj_pole(pole_dat):
    """
    Vezme pole (např. příjmy za 4 měsíce) a pomocí lineární regrese 
    ho prodlouží na celých 12 měsíců.
    """
    pocet_mesicu = len(pole_dat)

    if pocet_mesicu >= 12:
        return pole_dat[:12]
        
    if pocet_mesicu == 1:
        return np.repeat(pole_dat[0], 12)

    osa_x_zname = np.arange(1, pocet_mesicu + 1) 
    
    k, q = np.polyfit(osa_x_zname, pole_dat, 1)

    osa_x_budouci = np.arange(pocet_mesicu + 1, 13)
    
    budouci_hodnoty = np.polyval([k, q], osa_x_budouci)
    
    budouci_hodnoty = np.maximum(budouci_hodnoty, 0)
    
    return np.concatenate((pole_dat, budouci_hodnoty))