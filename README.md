## Predikce daňové povinnosti malého podnikatele

Autor: Marek Slavík

Studenské čislo : SLA0395

## Textový popis
Tento projekt se zabývá řešením (výpočtem a predikcí daňové povinnosti) a také základním generováním testovacích finančních dat pro malé podnikatele. Základním vstupem bude časová řada příjmů a výdajů v průběhu roku. Cílem projektu je implementovat algoritmy pro načítání těchto záznamů, matematický výpočet aktuální/budoucí daně a generování vzorových finančních toků.

Na začátku bude implementována funkce pro načítání transakcí z CSV souboru. Tato funkce bude umět načítat libovolně velký dataset (datum, částka, typ transakce) a uložit ho do paměti v podobě vhodných datových struktur (např. NumPy pole nebo Pandas DataFrame). Poté bude implementován algoritmus pro výpočet základu daně a predikci budoucího vývoje do konce roku (např. pomocí lineární regrese nebo klouzavých průměrů). Poslední částí bude vytvoření generátoru transakcí za použití šablon typických podnikatelů.

Výstup bude formou grafického obrázku (vizualizace historie příjmů a výdajů s vyznačeným trendem predikce a odhadovanou výší daně).

## Funkcionality
Implementovat načítání finančních dat z CSV souboru (evidence příjmů, výdajů a základních mzdových odvodů).

Implementovat algoritmus pro hledání trendu a predikci za použití zvoleného matematického modelu, který bude pracovat v následujících dvou krocích:

1. Zpracování dat a výpočet aktuální daňové povinnosti (zjednodušený model dle platné legislativy).

2. Odhad příjmů a výdajů do konce roku (např. pomocí lineární regrese) a následná simulace celkové roční daně.

Zapsat historická data a nalezenou predikci do grafického výstupu (obrázku), kde historická data budou např. modře a predikovaná část a daňová zátěž bude vyznačena červeně.

Vytvořit funkci pro generování testovacích finančních dat, aby bylo možné aplikaci spolehlivě testovat (tj. aby vygenerovala data za určité měsíce s realistickým rozložením).

Funkce začne s nějakou šablonou (předdefinované v kódu) a poté bude generovat transakce s určitou mírou náhodnosti.

Šablon bude více (např. stabilní příjmy – pravidelné měsíční fakturace, sezónní podnikání – výkyvy v určitých měsících, rostoucí trend – postupně se zvyšující zisky).

## Rozcestník 

Složka DATA -> Obsahuje CSV soubory příjmů a výdajů. 

Složka funkce -> Obsahuje classy a funkce použité v tomto projektu.

1. generator_nahodnych_dat.py -> Tento soubor má za účel vytvářet jiné soubory na predikci dat, nově vytvořené soubory se ukládají do složky DATA. 
2. nacitanisouboru.py -> Tento soubor má za účel rozebrat testovací data ze složky DATA do slovníku, aby se s tím dále dalo pracovat. 
3. predikce_prijmu_a_vydaju.py -> Tento soubor má za účel pomocí lineární regrese predikci dat.
4. ransac_robust.py -> Tento soubor má za účel pomocí robustní regrese udělat odhad pohybu cen (zde využívám RANSAC).
5. soucet_jednotlivych_mesicu.py -> Tento soubor má za účel sečíst jednotlivé částky v měsících, tak aby jsme s nimi mohli pracovat.
6. vypocty.py -> Tento soubor má za účel vypočítat daň za jednotlivé měsíce.

examples.ipynb -> Tento soubor má za účel propojit jednotlivé funkce a zobrazit výstupy.

## Zdůvodnění zvoleného způsobu 
### Využití lineární regrese 

Lineární regresi jsem využil, protože za mě je to asi ten nejlepší způsob, když máme sumy dat za měsíc (to znamená max. 12 bodů), které se dají lehce spojit a na základě toho odhadnout průběh.

### Využití robustní regrese

Něco k robustní regresi:

1. Důvod využití

Využívám ji, protože jsem se chtěl podívat na předpověď cen v jednotlivých měsících a chtěl jsem právě pracovat se všemi daty (ano, mohl jsem na to využít lineární regresi nebo případně zvolit polynomiální), ale za mě robustní je docela elegantní pro tyhle ty data, protože ignoruje výkyvy, případně chyby, které vybočují úplně z mého datasetu (to znamená, že nedochází ke zkreslení).

2. Různé druhy robustní regrese

Máme více druhů robustní regrese, konkrétně:

RANSAC — vezme dva náhodné body datasetu a mezi nimi udělá přímku a pak následně mění sklon na základě okolí dat s tím, že ignoruje data, která jsou mimo dané okolí.

Huber — neodstraňuje outliers (neboli data, která jsou bokem), ale zmenšuje jejich vliv. Blízké body trestá kvadraticky, vzdálené lineárně. Nejběžnější volba v běžné praxi (to jsem se aspoň dočetl).

Theil-Sen — vezme medián sklonů všech možných dvojic bodů. Velmi odolný, ale pomalý na velkých datech.

3. Proč jsem zvolil RANSAC

Protože jsem se k němu dostal jako k prvnímu a protože mi přišel docela vhodný na moje konkrétní data, i když po bližším zjišťování jsem zjistil, že by možná na moje malé datasety byl mnohem efektivnější Huber, ale již ponechám RANSAC.
