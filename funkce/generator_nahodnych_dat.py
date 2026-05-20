import csv
import random
import os

class GeneratorDat:
    def __init__(self, slozka: str = "DATA"):
        self.slozka: str = slozka
        
        # Rovnou při vytvoření zkontrolujeme, jestli složka existuje
        if not os.path.exists(self.slozka):
            os.makedirs(self.slozka)

    def ziskej_datum(self, zaznam: list) -> str:
        return zaznam[0]

    def generuj_soubor(self, nazev_souboru: str, typ: str = "stabilni"):
        # Cesta k souboru
        cesta: str = os.path.join(self.slozka, nazev_souboru)
        zaznamy: list[list] = []
        
        # Náhodný výběr aktivních měsíců (4 až 8 měsíců)
        vsechny_mesice: list[int] = list(range(1, 10))
        pocet: int = random.randint(4, 8)
        vybrane_mesice: list[int] = sorted(random.sample(vsechny_mesice, pocet))
        
        for mesic in vybrane_mesice:
            # Jednoduché určení základu
            if typ == "rostouci": 
                zaklad: float = 40000 + (mesic * 10000)
            elif typ == "sezonni": 
                zaklad: float = 150000 if mesic in [6, 7, 8, 12] else 30000
            else: 
                zaklad: float = 100000

            # Generování příjmů
            for _ in range(random.randint(3, 5)):
                den: int = random.randint(1, 28)
                castka: float = round((zaklad / 4) * random.uniform(0.8, 1.2), 2)
                zaznamy.append([f"2026-{mesic:02d}-{den:02d}", "Prijem", castka])
                
            # Generování výdajů
            for _ in range(random.randint(4, 7)):
                den: int = random.randint(1, 28)
                castka: float = round((zaklad * 0.4 / 5) * random.uniform(0.7, 1.3), 2)
                zaznamy.append([f"2026-{mesic:02d}-{den:02d}", "Vydaj", castka])
                
            # Odvody
            zaznamy.append([f"2026-{mesic:02d}-15", "Odvod", round(7500 + (zaklad * 0.05), 2)])

        zaznamy.sort(key=self.ziskej_datum)

        with open(cesta, mode='w', encoding='utf-8', newline='') as file:
            writer: csv.writer = csv.writer(file)
            writer.writerow(["Datum", "Typ", "Castka"])
            writer.writerows(zaznamy)