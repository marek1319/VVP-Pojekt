import os
from datetime import datetime
import csv

class NacitaniDat:
    """
    Třída zajišťující hromadné načítání a zpracování finančních dat.
    Prochází zadanou složku, čte CSV soubory a rozřazuje záznamy do měsíců 
    jako seznamy jednotlivých transakcí (nesčítá je).
    """
    
    def nacti(self, soubor_nazev: str) -> list[dict]: 
        vsechna_data: list[dict] = []
        # Procházení všech souborů v zadaném adresáři
        for nazev_souboru in os.listdir(soubor_nazev):
            # Filtrování pouze na soubory s příponou .csv
            if nazev_souboru.endswith(".csv"):
                cesta_k_souboru: str = os.path.join(soubor_nazev, nazev_souboru)
                
                # Inicializace slovníků pro ukládání seznamů transakcí za měsíc
                prijmy_transakce: dict[str, list[float]] = {}
                vydaje_transakce: dict[str, list[float]] = {}
                odvody_transakce: dict[str, list[float]] = {}
                
                # Otevření a čtení CSV souboru
                with open(cesta_k_souboru, mode="r", encoding="utf-8") as file:
                    reader: csv.DictReader = csv.DictReader(file)
                    # Zpracování souboru řádek po řádku
                    for row in reader:
                        # Převod textového data na datetime objekt a vytvoření klíče "RRRR-MM"
                        datum: datetime = datetime.strptime(row["Datum"], "%Y-%m-%d")
                        mesic_klic: str = datum.strftime("%Y-%m") 
                        # Získání finanční částky
                        castka = float(row["Castka"])
                        
                        # Pokud měsíc ještě není ve slovnících, vytvoříme pro něj prázdný seznam
                        if mesic_klic not in prijmy_transakce:
                            prijmy_transakce[mesic_klic] = []
                            vydaje_transakce[mesic_klic] = []
                            odvody_transakce[mesic_klic] = []
                      
                        # Přidání částky do seznamu v příslušné kategorii podle typu transakce
                        if row["Typ"] == "Prijem":
                            prijmy_transakce[mesic_klic].append(castka)
                        elif row["Typ"] == "Vydaj":
                            vydaje_transakce[mesic_klic].append(castka)
                        elif row["Typ"] == "Odvod":
                            odvody_transakce[mesic_klic].append(castka)

                # Zabalení dat aktuální firmy/subjektu do jednoho slovníku
                data_firmy = {
                    "nazev": nazev_souboru,
                    "prijmy": prijmy_transakce,
                    "vydaje": vydaje_transakce,
                    "odvody": odvody_transakce
                }
                # Přidání zpracovaných dat subjektu do celkového seznamu
                vsechna_data.append(data_firmy)
                
        # Navrácení kompletních rozřazených dat pro všechny zpracované soubory
        return vsechna_data