import numpy as np
#Lineární regrese
class Predikce:
    def predikuj_pole(self, pole_dat: np.ndarray) -> np.ndarray:
        """
        Vezme pole (např. příjmy za 4 měsíce) a pomocí lineární regrese 
        ho prodlouží na celých 12 měsíců.
        """
        pocet_mesicu: int = len(pole_dat)

        # Pokud už máme data za celý rok (nebo víc), vrátíme jen prvních 12 měsíců
        if pocet_mesicu >= 12:
            return pole_dat[:12]
        
        # Pokud máme data jen za 1 měsíc, nelze udělat regresi (jedním bodem přímku neproložíš).
        # Hodnotu proto jako nejlepší odhad zkopírujeme na celý rok.
        if pocet_mesicu == 1:
            return np.repeat(pole_dat[0], 12)

        # Vytvoření osy X pro známá data (např. pole [1, 2, 3, 4] pro 4 měsíce)
        osa_x_zname: np.ndarray = np.arange(1, pocet_mesicu + 1) 

        # Výpočet koeficientů lineární regrese (rovnice přímky y = k*x + q)
        # k = směrnice (trend růstu nebo poklesu), q = průsečík s osou y        
        k: float
        q: float
        k, q = np.polyfit(osa_x_zname, pole_dat, 1)

        # Vytvoření osy X pro chybějící budoucí měsíce (např. od 5 do 12)
        osa_x_budouci: np.ndarray = np.arange(pocet_mesicu + 1, 13)
        
        # Výpočet budoucích hodnot pro tyto měsíce dosazením do nalezené přímky
        budouci_hodnoty: np.ndarray = np.polyval([k, q], osa_x_budouci)
        
        # Ošetření extrémních propadů - finanční hodnoty nenecháme padnout do mínusu
        budouci_hodnoty: np.ndarray = np.maximum(budouci_hodnoty, 0)
        
        # Spojení původních (známých) a budoucích (predikovaných) dat do jednoho uceleného pole
        return np.concatenate((pole_dat, budouci_hodnoty))