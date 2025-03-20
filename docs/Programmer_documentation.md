## Popis programu
Tento program vyčísluje chemické rovnice popisující chemické reakce tak, aby se během reakce neztrácela ani negenerovala hmota. Program používá externí funkci knihovny Scipy - [`scipy.linalg.null_space()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.null_space.html) k nalezení nulového prostoru matice koeficientů.

## Algoritmus programu
1. **Rozdělení rovnice na levou a pravou stranu**
   - Funkce `parse_eq_to_left_right()` odstraní mezery a rozdělí rovnici podle znaménka `=` na reaktanty a produkty.
   - Následně rozdělí rovnici na jednotlivé sloučeniny.

2. **Parsování chemických vzorců**
   - Funkce `comp_to_dict()` převede chemický vzorec na slovník obsahující prvky a jejich počty atomů. Např. `H2O = {"H": 2, "O":1}`
   - String hodnota sloučeniny je čtena postupně odzadu, přičemž se průběžně mění hodnota `exp`, která udává násobnost prvku který přijde. 
   - Na násobnost májí vliv jak koeficienty přímo za značkou prvku, tak koeficienty za závorkami. 
   - Zvlášť jsou ošetřeny hydráty (sloučeniny jako `CuSO4 * 5H2O`).
   - Při nalezení značky prvku se do slovníku uloží hodnota `exp` pod klíčem odpovídajícím této značce.
   - Funkce `split_equation()` postupně zavolá funkci `comp_to_dict()` na všechny reaktanty a produkty.
   - Následně zkontroluje, zda se na obou stranách vyskytují stejné prvky, pokud ne, rovnici nelze vyčíslit a program skončí s chybou `
     Equation is unbalancable`.

4. **Sestavení matice a nalezení jejího jádra**
   - Funkce `balance_equation()` sestaví soustavu rovnic reprezentovanou maticí, kde každý řádek matice odpovídá jednomu prvku a každý sloupec 
     jedné sloučenině z rovnice. 
   - Přičemž hodnota na pozici _(i,j)_ je definována jako počet prvků v dané sloučenině, přičemž hodnoty pro produkty reakce jsou záporné.
   - Například pro vstupní rovnici `N2 + H2 = NH3` bude sestavena matice

     $$ \begin{pmatrix} 0 & 2 & -3 \\ 
      2 & 0 & -1 \end{pmatrix} $$

   - Pomocí funkce [`scipy.linalg.null_space()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.null_space.html) je nalezeno jádro 
      matice.
   - Následně je zkontrolováno, zda jádro matice není prázdné, pokud prázdné je matici nelze vyčíslit a program skončí s chybou `Equation is 
     unbalancable`

5. **Nalezení nejmenšího celočíselného poměru**
   - Funkce `ratios.float_to_ratio()`převede jádro matice na celočíselný poměr.
   - Nejdříve jsou všechny prvky poměry vyděleny nejmenším prvkem.
   - Následně je každý prvek vynásoben hodnotou `10e5`.
   - Hodnoty jsou následně vyděleny svým největším společným dělitelem, který je nalezen pomocí Euklidova algoritmu.


6. **Sestavení vyčíslené rovnice**
   - Funkce `build_balanced_equation()` vytvoří finální textovou reprezentaci vyčíslené rovnice spojením naparsované vstupní rovnice s výslednými 
     koeficienty.
   - Koeficient `1` u vyčíslené rovnice se nezobrazuje.