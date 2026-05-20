import numpy as np

class soucet:
    def secti_mesicni_transakce(self, vsechna_data: list[dict]) -> dict[str, dict[str, np.ndarray]]:
        sumy_za_mesice = {}
        
        for firma in vsechna_data:
            nazev: str = firma["nazev"]
            
            # Zjistím, kolik měsíců budeme zpracovávat
            pocet_prijmu: int = len(firma["prijmy"])
            pocet_vydaju: int = len(firma["vydaje"])
            
            # Vytvořím rovnou NumPy pole o přesné velikosti (plné nul)
            prijmy_soucty: np.ndarray = np.zeros(pocet_prijmu)
            vydaje_soucty: np.ndarray = np.zeros(pocet_vydaju)
            
            # Zápis částek rovnou na konkrétní index
            for index, transakce_v_mesici in enumerate(firma["prijmy"].values()):
                prijmy_soucty[index] = np.sum(transakce_v_mesici)
                
            for index, transakce_v_mesici in enumerate(firma["vydaje"].values()):
                vydaje_soucty[index] = np.sum(transakce_v_mesici)
                
            sumy_za_mesice[nazev] = {
                "prijmy": prijmy_soucty,
                "vydaje": vydaje_soucty
            }
            
        return sumy_za_mesice