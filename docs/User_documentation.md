## Základní popis
Program vyčísluje libovolné chemické rovnice. 
Chemické rovnice popisují průběh chemických dějů, při nichž ze vstupních látek vznikají látky nové. Obecně můžeme chemickou rovnici zapsat ve tvaru:

$$aA + bB \to cC + dD$$

Kde _A, B_ jsou reaktanty _C, D_ produkty a _a,b,c,d_ tzv. stechiometrické koeficienty. Vyčíslením rovnice rozumíme právě nalezení těchto stechiometrických koeficientů. Správné vyčíslení chemické rovnice vypadá tak, že během reakce v systému nevzniká ani nezaniká hmota.


## Spuštění programu
Pro spuštění programu je potřeba mít nainstalovanou aktuální verzi interpretu jazyka Python. Doporučuje se stáhnout a nainstalovat Python z oficiálních stránek [Python](https://www.python.org/downloads/). Pro správný běh programu je potřeba mít na svém zařízení také nainstalovanou knihovnu [SciPy](https://scipy.org/install/).
Po úspěšné instalaci knihoven lze spustit program ze souboru `main.py`

## Stručný popis řešení
Program načte vstupní rovnici, oddělí reaktanty a produkty, určí počet jednotlivých prvků v molekulách vstupujících a vystupujících z reakce. Z počtů prvků v jednotlivých molekulách je vytvořena soustava lineárních rovnic reprezentována maticí. Výpočtem jádra matice jsou získány poměry molekul vstupujících a vystupujících z reakce. Za stechiometrické koeficienty jsou označeny nejmenší nesoudělné poměry. Více informací o přesnějším algoritmickém řešení problému je dostupných v [Programátorské dokumentaci](Programmer_documentation.md).

## Popis vstupů a výstupů
Interakce s programem probíhá přes příkazový řádek. Vstupem programu je chemická rovnice, ve které jsou reaktanty od produktů odděleny znaménkem "=" a jednotlivé sloučeniny odděleny znaménkem "+".
Chemická sloučenina je zadávána ve standartní notaci - koeficienty udávající počet prvků se píší za značku prvku, nebo za závorku. Závorky ve sloučenině mohou být buď klasické `Ca(NO3)2` nebo hranaté `[Cu(NH3)]2`. V případě zadávání hydrátu použijeme znak hvězdičky `CuSO4 * 5H2O`. Program vrátí stejnou rovnici, ovšem doplněnou o stechiometrické koeficienty udávající poměr reagujících prvků. 

Příklad komunikace s programem: 
```
Enter a reaction:
IN:   N2 + H2 = NH3
OUT:  N2 + 3H2 = 2NH3
```