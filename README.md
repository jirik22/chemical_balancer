### Základní popis
Chemical balancer je program vyčíslující libovolné chemické rovnice. Interakce s programem probíhá přes příkazový řádek. 

#### Popis vstupu

Vstupem programu je chemická rovnice, ve které jsou reaktanty od produktů odděleny znaménkem "=" a jednotlivé sloučeniny odděleny zanménkem "+"


- **Příklad vstupu:** `N2 + H2 = NH3`
- **Příklad výstupu:** `N2 + 3H2 = 2NH3`

### Podrobněji
1) Vstupní rovnice je rozdělena na reaktanty a produkty a dále pak na jednotlivé sloučeniny pomocí vestavěných funkcí v pythonu(split, replace...)

2) Každá sloučenina je zvlášť naparsována. String se sloučeninou je čten odzadu a postupně je měněna hodnota exp, která udává násobnost prvku který přijde. Na násobnost májí hodnotu jak koeficienty přímo za značkou prvku, tak koeficienty za závorkami. Zvlášť jsou ošetřeny hydráty sloučeniny typu (CuSO4 * 5H2O) ve kterých je při nalezení symbolu "*" hodnota exp nastavena na 1 a začíná se se čtením znovu

3) Výsledkem parsování je dictionary pro každou sloučeninu, udávající počet atomů ve sloučenině

`H2O = {"H": 2, "O":1}`

4) Z těchto slovníků je poměrně jednoduché sestavit soustavu rovnic reprezentovanou maticí, kde každý řádek matice odpovídá jednomu prvku a každý sloupec jedné sloučenině z rovnice. Přičemž hodnota na pozici i,j je definována jako počet prvků v danné sloučenině, hodnota je záporná pro produkty. Výpočtem jádra matice získáme stechiometrický poměr, ovšem ne celočíselný
