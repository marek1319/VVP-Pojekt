import csv
import random
import os

def generuj_data_s_mezerami(nazev_souboru, sablona="stabilni"):
    """
    Vygeneruje finanční data pro 1. až 9. měsíc, ale náhodně některé měsíce vynechá 
    """
    def ziskej_zaklad_prijmu(mesic, typ_sablony):
        if typ_sablony == "stabilni": return 100000
        elif typ_sablony == "rostouci": return 40000 + (mesic * 10000)
        elif typ_sablony == "sezonni": return 150000 if mesic in [6, 7, 8, 12] else 30000
        else: return 100000

    zaznamy = []
    
    vsechny_mesice = list(range(1, 10)) 
    
    pocet_aktivnich_mesicu = random.randint(4, 8)
    
    vybrane_mesice = sorted(random.sample(vsechny_mesice, pocet_aktivnich_mesicu))
    
    for mesic in vybrane_mesice:
        zakladni_prijem = ziskej_zaklad_prijmu(mesic, sablona)

        pocet_prijmu = random.randint(3, 5)
        for _ in range(pocet_prijmu):
            den = random.randint(1, 28)
            castka = round((zakladni_prijem / pocet_prijmu) * random.uniform(0.8, 1.2), 2)
            zaznamy.append([f"2026-{mesic:02d}-{den:02d}", "Prijem", castka])
            
        pocet_vydaju = random.randint(4, 7)
        for _ in range(pocet_vydaju):
            den = random.randint(1, 28)
            castka = round((zakladni_prijem * 0.4 / pocet_vydaju) * random.uniform(0.7, 1.3), 2)
            zaznamy.append([f"2026-{mesic:02d}-{den:02d}", "Vydaj", castka])
            
        odvod_castka = round(7500 + (zakladni_prijem * 0.05), 2)
        zaznamy.append([f"2026-{mesic:02d}-15", "Odvod", odvod_castka])

    zaznamy.sort(key=lambda x: x[0])

    with open(nazev_souboru, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Datum", "Typ", "Castka"])
        writer.writerows(zaznamy)
        
    print(f"Vygenerováno: {nazev_souboru} | Aktivní měsíce: {vybrane_mesice}")

if not os.path.exists("DATA"):
    os.makedirs("DATA")