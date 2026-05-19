import numpy as np

class soucet:
    def secti_mesicni_transakce(self, vsechna_data):
        sumy_za_mesice = {}
        
        for firma in vsechna_data:
            nazev = firma["nazev"]
            
            # 1. Zjistíme, kolik měsíců budeme zpracovávat
            pocet_prijmu = len(firma["prijmy"])
            pocet_vydaju = len(firma["vydaje"])
            
            # 2. Vytvoříme rovnou NumPy pole o přesné velikosti (plné nul)
            prijmy_soucty = np.zeros(pocet_prijmu)
            vydaje_soucty = np.zeros(pocet_vydaju)
            
            # 3. Zápis částek rovnou na konkrétní index (odpadá append)
            for index, transakce_v_mesici in enumerate(firma["prijmy"].values()):
                prijmy_soucty[index] = np.sum(transakce_v_mesici)
                
            for index, transakce_v_mesici in enumerate(firma["vydaje"].values()):
                vydaje_soucty[index] = np.sum(transakce_v_mesici)
                
            sumy_za_mesice[nazev] = {
                "prijmy": prijmy_soucty,
                "vydaje": vydaje_soucty
            }
            
        return sumy_za_mesice