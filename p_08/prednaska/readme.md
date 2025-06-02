# Stromové prehledávání

Táto prednáška sa zaoberá problematikou **stromového prehledávania**, ktorá je kľúčová v oblasti umelej inteligencie. Zameriavame sa na hľadanie ciest nielen v geografickom zmysle, ale aj ako nájdenie optimálnej sekvencie akcií v definovanom prostredí.

---

## Definícia problému prehledávania

Problém prehledávania je definovaný šiestimi základnými časťami, pričom predpokladáme, že prostredie je plne pozorovateľné, známe a deterministické, a agent má k dispozícii konečný počet akcií.

1.  **Počiatočný stav**: Miesto, kde sa agent nachádza na začiatku (napr. poloha na mape, nastavenie Sudoku, rozloženie figúrok na šachovnici).
2.  **Stavový priestor**: Všetky možné stavy, do ktorých sa agent môže dostať (napr. všetky dosiahnuteľné miesta, všetky možné konfigurácie Sudoku alebo šachu).
3.  **Akcie**: Definované akcie, ktoré môže agent vykonať v danom stave (napr. presun do susedného mesta, zápis čísla do Sudoku, ťah figúrkou v šachu).
4.  **Prechody medzi stavmi**: Definícia stavu, do ktorého sa agent dostane po vykonaní akcie.
5.  **Test cieľa**: Funkcia, ktorá overí, či agent dosiahol cieľový stav (napr. dosiahnutie cieľového mesta, správne vyplnené Sudoku, šach-mat).
6.  **Cena cesty**: Ohodnotenie nákladov na danú sekvenciu stavov (napr. počet prejazdených kilometrov, počet ťahov v šachu). Predpokladá sa, že ceny nie sú negatívne.

Cieľom je nájsť cestu z počiatočného stavu do cieľa.

---

## Typy prehledávania

Existuje niekoľko typov prehledávania, ktoré sa líšia svojimi nárokmi a vlastnosťami:

* **Informované vs. Neinformované**:
    * **Neinformované** prohledávanie nevyužíva dodatočné, problémovo špecifické znalosti nad rámec definície problému.
    * **Informované** prohledávanie využíva heuristiky alebo iné pomocné informácie na usmernenie hľadania.
* **Úplné vs. Neúplné**:
    * **Úplné** algoritmy vždy nájdu riešenie, ak existuje.
    * **Neúplné** algoritmy nemusia nájsť riešenie, aj keď existuje (napr. zacyklenie, nedosiahnuteľnosť limitu).
* **Optimálne vs. Neoptimálne**:
    * **Optimálne** algoritmy nájdu najlepšie možné riešenie z hľadiska ceny cesty.
    * **Neoptimálne** algoritmy nemusia nájsť optimálne riešenie.
* **Statické vs. Dynamické**:
    * **Statické** prohledávanie predpokladá, že sa prostredie počas hľadania nemení.
    * **Dynamické** prohledávanie sa používa v prostrediach, ktoré sa menia.
* **Online vs. Offline**:
    * **Online** algoritmy sa musia rozhodovať v každom okamihu (akcia-po-akcii).
    * **Offline** algoritmy si môžu celý postup naplánovať vopred.

---

## Stromové prehledávanie

**Stromové prehledávanie** je základný koncept, pri ktorom expandovanie uzlov (stavov) vytvára strom možností.

* **Expandovanie uzla**: Proces vypísania všetkých dostupných možností (akcií) z daného uzla.
* **Ofina (fringe)**: Skupina potenciálnych uzlov (expandovaných uzlov), z ktorých sa vyberá ďalší nasledovník. Tieto uzly sa ukladajú do dátovej štruktúry (fronta, zásobník, prioritná fronta).

Opakované navštevovanie uzlov môže viesť k redundancii a neoptimálnym cestám. To sa dá ošetriť zapamätávaním si už navštívených uzlov.

---

## Neinformované prehledávanie

Neinformované prohledávanie nevyužíva žiadne dodatočné znalosti o probléme.

### BFS (Breadth-First Search - Prehledávanie do šířky)

* **Princíp**: Využíva **frontu** na výber nasledovníkov. Expanduje strom po vrstvách.
* **Vlastnosti**:
    * **Úplný**: Áno, vždy nájde riešenie, ak existuje.
    * **Optimálny**: Nie vždy, ale nájde najkratšiu cestu z hľadiska počtu vrcholov. Ak sú ceny všetkých akcií rovnaké, potom je optimálny.
* **Složitosť**: V najhoršom prípade exponenciálna $O(b^d)$, kde $b$ je faktor vetvenia a $d$ je hĺbka riešenia.

### DFS (Depth-First Search - Prehledávanie do hloubky)

* **Princíp**: Využíva **zásobník** na výber nasledovníkov. Prechádza vždy najhlbšie uzly v ofine.
* **Vlastnosti**:
    * **Úplný**: Nie, môže sa zacykliť alebo nedobehnúť pri veľkom množstve uzlov bez ošetrenia opakovaných návštev.
    * **Optimálny**: Nie.
* **Výhoda**: Potrebuje signifikantne menej pamäte ako BFS, pretože si pamätá len cestu z koreňa do listu a okolitých neexpandovaných súrodencov uzlov.

### DLS (Depth-Limited Search - Prehledávanie s hloubkovým limitem)

* **Princíp**: Modifikácia DFS, ktorá obmedzuje hĺbku prohledávania na maximálnu hĺbku $L$.
* **Vlastnosti**:
    * **Úplný**: Nie, ak riešenie leží v hĺbke > $L$.
    * **Optimálny**: Nie.

### IDS (Iterative-Deepening Search - Iteratívne prehlbovanie)

* **Princíp**: Opakované spúšťanie DLS s postupne sa zvyšujúcim hĺbkovým limitom.
* **Vlastnosti**:
    * **Úplný**: Áno.
    * **Optimálny**: Nie (bol by, keby sme obmedzovali cenu cesty, nie hĺbku).
* **Výhoda**: Preferovaný spôsob prehledávania, ak je stavový priestor obrovský a hĺbka riešenia nie je známa. Množstvo opakované práce je zanedbateľné v porovnaní s uzlami v hlbokých vrstvách.

---

## Informované prehledávanie

Informované prohledávanie dostáva viac informácií než len definíciu problému. Tieto informácie pomáhajú lepšie sa orientovať v úlohe a rýchlejšie sa dostať k cieľu.

* **Prioritná fronta**: Využíva sa na výber následovníkov, uzly sú ohodnocované pomocou funkcie $f(u)$.
* **Ohodnocovacia funkcia $f(u)$**:
    * $g(u)$ – doterajšia prejdená vzdialenosť zo štartu do uzla $u$.
    * $h(u)$ – heuristika/radca, odhadovaná vzdialenosť od uzla $u$ do cieľa.
* **Heuristika**: Radca, ktorý pomáha rýchlejšie nájsť cestu do cieľa, ale negarantuje optimálnosť.
* **Prípustná heuristika**: Odhad $h(u)$ nikdy nie je väčší ako skutočná vzdialenosť do cieľa (má tendenciu podhodnocovať, napr. vzdialenosť vzdušnou čiarou).

### Tri známe algoritmy informovaného prehledávania:

1.  **"Greedy" best-first search**: $f(u) = h(u)$
    * **Vlastnosti**: Úplný, ale nie optimálny.
2.  **Dijkstrov algoritmus**: $f(u) = g(u)$
    * **Vlastnosti**: Optimálny a úplný, ak sú váhy hrán pozitívne.
3.  **Algoritmus A***: $f(u) = g(u) + h(u)$
    * **Vlastnosti**: Úplný a optimálny pre prípustnú heuristiku. Vedie "rýchlejšie" k cieľu ako BFS.

---

## Online prehledávanie

Online prehledávanie sa vyznačuje tým, že agent sa musí rozhodovať v každom okamihu a nemá kompletnú informáciu o prostredí dopredu.

* **Náhodná prechádzka**: Agent náhodne vyberie následníka a "túla sa" stromom, kým nenájde riešenie. Môže trvať dlho a nemusí nájsť riešenie, ak sú akcie ireverzibilné.
* **DFS v online podobe**: Agent si pamätá cestu, ktorou sa dostal do uzla, a môže sa po nej vracať späť.
* **LRTA\***: Online varianta algoritmu A\*.

---

## Prehľad kapitoly

| Typ prohledávání         | Dátová struktura | Úplnosť | Optimálnosť | Vlastnosti                                            |
| :----------------------- | :--------------- | :------ | :---------- | :----------------------------------------------------- |
| **Neinformované** |                  |         |             |                                                        |
| BFS (do šírky)           | Fronta           | Áno     | Áno* | Nájde najkratšiu cestu v počte vrcholov. \*Optimálny, ak sú všetky ceny akcií rovnaké. |
| DFS (do hĺbky)           | Zásobník         | Nie     | Nie         | Vyžaduje málo pamäte. Môže sa zacykliť.               |
| DLS (s hĺbkovým limitom) | Zásobník         | Nie     | Nie         | DFS s obmedzenou hĺbkou.                               |
| IDS (iteratívne prehĺb.) | Zásobník         | Áno     | Nie         | Kombinácia DLS s rastúcim limitom. Efektívne pre veľké priestory s neznámou hĺbkou riešenia. |
| **Informované** |                  |         |             | Využíva dodatočné znalosti (heuristiky).             |
| "Greedy" best-first      | Prioritná fronta | Áno     | Nie         | Preferuje uzly najbližšie k cieľu (podľa heuristiky). |
| Dijkstrov algoritmus     | Prioritná fronta | Áno     | Áno         | Nájde najkratšiu cestu v grafe s nezápornými váhami.  |
| A\* algoritmus           | Prioritná fronta | Áno     | Áno         | Kombinuje skutočnú cenu a heuristický odhad. Vyžaduje prípustnú heuristiku. |
| IDA\* | Prioritná fronta | Áno     | Áno         | Kombinácia IDS a A\*.                                |
| **Online** |                  |         |             | Agent sa rozhoduje postupne, nemá kompletné info o prostredí. |
| Náhodná prechádzka       |                  | Nie     | Nie         | Jednoduchá, ale neefektívna. Môže viesť k zacykleniu.   |
| Online DFS               |                  | Áno     | Nie         | DFS s pamäťou cesty pre návrat.                      |
| LRTA\* |                  | Áno     | Áno         | Online varianta A\*.                                 |