import csv
import random
import os

class GeneratorDat:
    def __init__(self, slozka="DATA"):
        self.slozka = slozka
        
        # Rovnou při vytvoření zkontrolujeme, jestli složka existuje
        if not os.path.exists(self.slozka):
            os.makedirs(self.slozka)

    def ziskej_datum(self, zaznam):
        return zaznam[0]

    def generuj_soubor(self, nazev_souboru, typ="stabilni"):
        # Cesta k souboru
        cesta = os.path.join(self.slozka, nazev_souboru)
        zaznamy = []
        
        # Náhodný výběr aktivních měsíců (4 až 8 měsíců)
        vsechny_mesice = list(range(1, 10)) 
        pocet = random.randint(4, 8)
        vybrane_mesice = sorted(random.sample(vsechny_mesice, pocet))
        
        for mesic in vybrane_mesice:
            # Jednoduché určení základu
            if typ == "rostouci": 
                zaklad = 40000 + (mesic * 10000)
            elif typ == "sezonni": 
                zaklad = 150000 if mesic in [6, 7, 8, 12] else 30000
            else: 
                zaklad = 100000

            # Generování příjmů
            for _ in range(random.randint(3, 5)):
                den = random.randint(1, 28)
                castka = round((zaklad / 4) * random.uniform(0.8, 1.2), 2)
                zaznamy.append([f"2026-{mesic:02d}-{den:02d}", "Prijem", castka])
                
            # Generování výdajů
            for _ in range(random.randint(4, 7)):
                den = random.randint(1, 28)
                castka = round((zaklad * 0.4 / 5) * random.uniform(0.7, 1.3), 2)
                zaznamy.append([f"2026-{mesic:02d}-{den:02d}", "Vydaj", castka])
                
            # Odvody
            zaznamy.append([f"2026-{mesic:02d}-15", "Odvod", round(7500 + (zaklad * 0.05), 2)])

        zaznamy.sort(key=self.ziskej_datum)

        with open(cesta, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Datum", "Typ", "Castka"])
            writer.writerows(zaznamy)