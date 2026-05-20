## Predikce daňové povinnosti malého podnikatele

Autor: Marek Slavík

Studenské čislo : SLA0395

## Textový popis
Tento projekt se zabývá řešením (výpočtem a predikcí daňové povinnosti) a také základním generováním testovacích finančních dat pro malé podnikatele. Základním vstupem bude časová řada příjmů a výdajů v průběhu roku. Cílem projektu je implementovat algoritmy pro načítání těchto záznamů, matematický výpočet aktuální/budoucí daně a generování vzorových finančních toků.

Na začátku bude implementována funkce pro načítání transakcí z CSV souboru. Tato funkce bude umět načítat libovolně velký dataset (datum, částka, typ transakce) a uložit ho do paměti v podobě vhodných datových struktur (např. NumPy pole nebo Pandas DataFrame). Poté bude implementován algoritmus pro výpočet základu daně a predikci budoucího vývoje do konce roku (např. pomocí lineární regrese nebo klouzavých průměrů). Poslední částí bude vytvoření generátoru transakcí za použití šablon typických podnikatelů.

Výstup bude formou grafického obrázku (vizualizace historie příjmů a výdajů s vyznačeným trendem predikce a odhadovanou výší daně).

## Funcionality
Implementovat načítání finančních dat z CSV souboru (evidence příjmů, výdajů a základních mzdových odvodů).

Implementovat algoritmus pro hledání trendu a predikci za použití zvoleného matematického modelu, který bude pracovat v následujících dvou krocích:

1. Zpracování dat a výpočet aktuální daňové povinnosti (zjednodušený model dle platné legislativy).

2. Odhad příjmů a výdajů do konce roku (např. pomocí lineární regrese) a následná simulace celkové roční daně.

Zapsat historická data a nalezenou predikci do grafického výstupu (obrázku), kde historická data budou např. modře a predikovaná část a daňová zátěž bude vyznačena červeně.

Vytvořit funkci pro generování testovacích finančních dat, aby bylo možné aplikaci spolehlivě testovat (tj. aby vygenerovala data za určité měsíce s realistickým rozložením).

Funkce začne s nějakou šablonou (předdefinované v kódu) a poté bude generovat transakce s určitou mírou náhodnosti.

Šablon bude více (např. stabilní příjmy – pravidelné měsíční fakturace, sezónní podnikání – výkyvy v určitých měsících, rostoucí trend – postupně se zvyšující zisky).

## Rozcestník 

Složka DATA -> Obsahuje csv soubry přijmu a vydaju 

Složka funkce -> Obsahuje classy a funkce použité v tomto projektu 

1. generator_nahodnych_dat.py -> Tento soubor má za učel vytvařet jiné soubory na predikci dat, nově vytvořené soubory se ukladají do složky data 
2. nacitanisouboru.py -> Tento soubor má za učel rozebrat testovací data ze složky data do slovníku aby se s tím dále dalo pracovat 
3. predikce_prijmu_a_vydaju.py -> Tento soubor ma za učel pomocí linearní regrese predikci dat 
4. ransac_robust.py -> Tento soubor ma za uřel pomocí robustní regrese udělat odhad pohybu cen (zde využívám ransac)
5. soucet_jednotlivych_mesicu.py -> Tento soubor ma za učel sečíst jednotlivé častky v měsících tak aby jsme s nima mohly pracovat 
6. vypocty.py -> Tento soubor ma za učel vypočitat daň za jednotlivé měsíce 

examples.ipynb -> Tento soubor ma za učel propojit jednotlivé  funkce a zobrazit vystupy 

## Zdůvodnění zvoleného způsobu 
### Využití Linearní regrese 

Linearní regresy jsem využil protože za mě je to asi ten nejlepší zpusob když mame sumy dat za měsíc (to znamná max 12 bodů) které se daji lehce spojit a na zakladě toho odhadnout průběh 

### Využití Robustní regrese 

Něco k robustní regresy 
1. Důvod využití 
využívám ji protože jsem se chtěl podivat na předpověď cen v jednotlyvých měsicí a chtěl jsem pravě pracovat se všemy daty (ano mohl jsem na to využit linearni regresy nebo připadně zvolit polynomyalní) ale za mě robustní je docela elegantní pro tyhle ty data protože ignoruje výkyvy připadně chyby které vybočují uplně z mého data setu (to znamená že nedochází ke zkreslení ) 

2. Ruzné druhy robustní regrese 
Mamé více druhů robustní regrese konkretně 
RANSAC — vezme dva nahodné body data setu a mezi nima uděla přimku a pak nasledně mení sklon na zakladě okolí dat s tím že ignoruje data která jsou mimo dané okolí 
Huber — neodstraňuje outliers(neboli data která jsou bokem), ale zmenšuje jejich vliv. Blízké body trestá kvadraticky , vzdálené lineárně. Nejběžnější volba v běžné praxi (to jsem se aspoň dočetl).
Theil-Sen — vezme medián sklonů všech možných dvojic bodů. Velmi odolný, ale pomalý na velkých datech.

3. Proč jsem zvolil RANSAC 
protože jsem se k němu dostal jako k prvnímu a protože my přišel docela vhodný na moje konkretní data i když po bližším zjišťování jsem zjistil že by možná na moje malé datasety byl mnohem efektivnější Huber ale již ponechám Ransac