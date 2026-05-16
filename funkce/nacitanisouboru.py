import os
from datetime import datetime
import csv
import numpy as np

def nacti(soubor_nazev): 
    vsechna_data = []
    for nazev_souboru in os.listdir(soubor_nazev):
        if nazev_souboru.endswith(".csv"):
            cesta_k_souboru = os.path.join(soubor_nazev, nazev_souboru)
            
            prijmy_agregace = {}
            vydaje_agregace = {}
            odvody_agregace = {}
            
            with open(cesta_k_souboru, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    datum = datetime.strptime(row["Datum"], "%Y-%m-%d")
                    mesic_klic = datum.strftime("%Y-%m") 
                    castka = float(row["Castka"])
                    
                    if mesic_klic not in prijmy_agregace:
                        prijmy_agregace[mesic_klic] = 0
                        vydaje_agregace[mesic_klic] = 0
                        odvody_agregace[mesic_klic] = 0

                    if row["Typ"] == "Prijem":
                        prijmy_agregace[mesic_klic] += castka
                    elif row["Typ"] == "Vydaj":
                        vydaje_agregace[mesic_klic] += castka
                    elif row["Typ"] == "Odvod":
                        odvody_agregace[mesic_klic] += castka

            mesicni_prijmy_pole = np.array(list(prijmy_agregace.values()))
            mesicni_vydaje_pole = np.array(list(vydaje_agregace.values()))
            mesicni_odvody_pole = np.array(list(odvody_agregace.values()))
            
            data_firmy = {
                "nazev": nazev_souboru,
                "prijmy": mesicni_prijmy_pole,
                "vydaje": mesicni_vydaje_pole,
                "odvody": mesicni_odvody_pole
            }
            
            vsechna_data.append(data_firmy)

    return vsechna_data