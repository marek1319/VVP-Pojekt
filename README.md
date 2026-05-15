## Predikce daňové povinnosti malého podnikatele

Autor: Marek Slavík
Studenské čislo : SLA0395

## Textový popis
•	Tento projekt se zabývá řešením (výpočtem a predikcí daňové povinnosti) a také základním generováním testovacích finančních dat pro malé podnikatele. Základním vstupem bude časová řada příjmů a výdajů v průběhu roku. Cílem projektu je implementovat algoritmy pro načítání těchto záznamů, matematický výpočet aktuální/budoucí daně a generování vzorových finančních toků.
•	Na začátku bude implementována funkce pro načítání transakcí z CSV souboru. Tato funkce bude umět načítat libovolně velký dataset (datum, částka, typ transakce) a uložit ho do paměti v podobě vhodných datových struktur (např. NumPy pole nebo Pandas DataFrame). Poté bude implementován algoritmus pro výpočet základu daně a predikci budoucího vývoje do konce roku (např. pomocí lineární regrese nebo klouzavých průměrů). Poslední částí bude vytvoření generátoru transakcí za použití šablon typických podnikatelů.
•	Výstup bude formou grafického obrázku (vizualizace historie příjmů a výdajů s vyznačeným trendem predikce a odhadovanou výší daně).

## Funcionality
•	Implementovat načítání finančních dat z CSV souboru (evidence příjmů, výdajů a základních mzdových odvodů).
•	Implementovat algoritmus pro hledání trendu a predikci za použití zvoleného matematického modelu, který bude pracovat v následujících dvou krocích:
•	Zpracování dat a výpočet aktuální daňové povinnosti (zjednodušený model dle platné legislativy).
•	Odhad příjmů a výdajů do konce roku (např. pomocí lineární regrese) a následná simulace celkové roční daně.
•	Zapsat historická data a nalezenou predikci do grafického výstupu (obrázku), kde historická data budou např. modře a predikovaná část a daňová zátěž bude vyznačena červeně.
•	Vytvořit funkci pro generování testovacích finančních dat, aby bylo možné aplikaci spolehlivě testovat (tj. aby vygenerovala data za určité měsíce s realistickým rozložením).
•	Funkce začne s nějakou šablonou (předdefinované v kódu) a poté bude generovat transakce s určitou mírou náhodnosti.
•	Šablon bude více (např. stabilní příjmy – pravidelné měsíční fakturace, sezónní podnikání – výkyvy v určitých měsících, rostoucí trend – postupně se zvyšující zisky).