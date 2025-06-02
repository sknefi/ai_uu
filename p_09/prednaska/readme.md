# Prehľadávanie s protivníkom (Adversarial Search)

Táto prednáška sa zameriava na problematiku **prehľadávania s protivníkom** v oblasti umelej inteligencie, čo je kľúčové pre riešenie úloh v prostredí s viacerými agentmi, kde výsledok akcie agenta závisí aj od akcií ostatných, konkurenčných agentov.

---

## Motivácia

V mnohých úlohách umelej inteligencie, ako sú hry (šach, dáma, piškvorky, poker), sa agent ocitá v **multi-agentnom prostredí**. To znamená, že nie je v prostredí sám a výsledok jeho akcií je ovplyvnený aj akciami ostatných agentov, ktorí sú v tomto prípade **protivníci**. Ak tieto úlohy využívajú stromové prehľadávanie, hovoríme o **prehľadávaní s protivníkom** (adversarial search).

Pre naše účely sa zameriame na:
* **Hry dvoch hráčov**: Hráči sa pravidelne striedajú v ťahoch.
* **Hry s úplnou informáciou**: Vždy máme prehľad o celej hernej situácii (herný plán, dostupné ťahy, pravidlá, koniec hry). Príkladom sú šachy.
* **Deterministické hry**: Hry bez prvku náhody (napríklad hod kockou).
* **Hry s nulovým súčtom**: Výhra jedného hráča je prehra pre druhého. Skóre si stačí pamätať z pohľadu jedného hráča (napr. ak Max vyhrá $x$, Min prehrá $x$).

---

## Strom hry

Hru s nulovým súčtom možno efektívne reprezentovať pomocou **stromu**. Pre ilustráciu sa často používa jednoduchá hra **Tic-tac-toe** (piškvorky na mriežke 3x3).

### Príklad Tic-tac-toe:
* Začína hráč s krížikmi (Max), potom hráč s kolieskami (Min) a striedajú sa.
* Cieľom je získať 3 rovnaké útvary v rade (horizontálne, vertikálne, diagonálne).
* Hra môže skončiť aj remízou, ak obaja hráči hrajú optimálne.
* Ak sa na hru pozeráme z pohľadu Maxa: výhra je 1, prehra je -1, remíza je 0. Min má opačné hodnoty.
* Cieľom Maxa je voliť ťahy tak, aby sa dostal do koncového uzla s hodnotou 1, zatiaľ čo Min sa mu v tom snaží zabrániť.

Počet uzlov v hernom strome Tic-tac-toe je značný (odhadom až $9! = 362 880$), ale v reálnosti je nižší vďaka symetriám a skorým ukončeniam hier.

---

## Minimax prehľadávanie

**Minimax algoritmus** je základnou stratégiou pre prehľadávanie s protivníkom v deterministických hrách s úplnou informáciou a nulovým súčtom. Predpokladá, že protivník hrá optimálne a snaží sa minimalizovať zisk hráča.

### Princíp:
* Prehľadávanie sa vykonáva do hĺbky.
* Max (maximalizujúci hráč) si vyberá najväčšiu hodnotu z toho, čo mu vyberie Min (minimalizujúca hráčka) v nasledujúcom ťahu.
* Hodnota, ktorú Max získa v najhoršom prípade (pri optimálnej hre Min), sa nazýva **minimaxová hodnota**.

### Rekurzívna definícia minimaxovej hodnoty pre stav $s$:



kde $s \to a$ znamená stav, do ktorého prejdeme zo stavu $s$ pomocou akcie $a$.

Implementácia minimaxu je zo svojej podstaty **rekurzívna**.

---

## Alfa-beta prerezávanie

Minimax prehľadávanie môže byť pre veľké herné stromy (ako napríklad šachy s odhadom $10^{123}$ ciest) príliš náročné. **Alfa-beta prerezávanie** je optimalizácia minimaxu, ktorá výrazne znižuje počet preskúmaných uzlov v strome, pričom stále zaručuje rovnaký výsledok.

### Kľúčové hodnoty:
* **Alfa ($\alpha$)**: Najlepšia hodnota, ktorú sme doteraz našli na ceste z uzla pre maximalizujúceho hráča (Max). Na začiatku $-\infty$. Táto hodnota sa aktualizuje, keď je na ťahu Max.
* **Beta ($\beta$)**: Najlepšia hodnota, ktorú sme doteraz našli na ceste z uzla pre minimalizujúceho hráča (Min). Na začiatku $+\infty$. Táto hodnota sa aktualizuje, keď je na ťahu Min.

### Podmienka prerezávania:
Ak je $\beta(s) \le \alpha(s)$, môžeme zastaviť prehľadávanie následníkov uzla $s$, pretože optimálny ťah už bol nájdený v inej vetve a táto vetva neprinesie lepší výsledok.

---

## Vylepšenia prehľadávania

Pre ďalšie zvýšenie efektivity prehľadávania s protivníkom sa používajú rôzne techniky:

* **Poradie uzlov**: Prehľadávanie nádejnejších ciest skôr môže viesť k rýchlejšiemu prerezávaniu. Je možné použiť heuristiky (napr. materiálne hodnotenie v šachoch) alebo pamätať si úspešné ťahy z minulosti.
* **Evaluačná funkcia**: Ak je strom príliš hlboký na úplné prehľadanie, použije sa evaluačná funkcia na odhadnutie sľubnosti nekoncových uzlov. Mala by byť rýchlo vypočítateľná a presne odhadovať skutočné hodnoty uzlov.
* **Hĺbka prehľadávania**: Stanovenie vhodnej hĺbky, do ktorej sa strom prehľadáva, a použitie evaluačnej funkcie v tomto bode. Môže sa použiť aj iteratívne prehlbovanie. Problémom je **horizont pozorovania**, kedy sa dôležité udalosti môžu diať za hranicou prehľadanej hĺbky.
* **Ďalšie prerezávania**: Eliminácia nezmyselných alebo málo sľubných ťahov. Výber len niekoľkých najlepších ťahov na ďalšie prehľadávanie, čo drasticky znižuje zložitosť stromu, no môže viesť k premeškaniu dôležitých vetiev.
* **Slovník podhier**: Využívanie preddefinovaných stratégií pre známe podhry (napr. šachové koncovky).

---

## Zložitejšie hry

Predstavené metódy sú základom, ale reálne herné situácie môžu byť zložitejšie:

* **Hry s viacerými hráčmi**: Strom hry stále existuje, ale každé poschodie patrí inému hráčovi. Koncové uzly sú ohodnotené **vektorom čísel** (skóre pre každého hráča). Komplikáciou sú meniace sa aliancie, čo spadá do teórie hier.
* **Stochastické hry**: Obsahujú náhodu (napr. hody kockou). Strom hry má pridané poschodia pre náhodné ťahy. Uzly nemajú presné minimaxové, ale **očakávané hodnoty**. Možno použiť alfa-beta prerezávanie s odhadom očakávaných hodnôt, alebo **Monte Carlo simulácie**, kde program opakuje hry od daného uzla, aby odhadol jeho hodnotu.
* **Čiastočne pozorovateľné hry**: Hráč nemá úplnú informáciu o stave hry (napr. poker, lode). Stratégia zahŕňa spresňovanie stavu a hľadanie univerzálnej stratégie pre viacero možných stavov. Výhra môže byť len s určitou pravdepodobnosťou.

---

## State-of-the-art: Míľniky v súbojoch človeka a stroja

* **1997 - Šachy**: IBM Deep Blue porazil Garryho Kasparova. Využíval alfa-beta prerezávanie, obmedzenú hĺbku, rozsiahlu evaluačnú funkciu (8000 častí) a databázy otváracích pozícií a majstrovských hier.
* **2007 - Dáma**: Program Chinook dokázal hrať dámu perfektne (remíza pri optimálnej hre oboch strán). Spoliehal sa na alfa-beta prerezávanie a rozsiahle knižnice otváracích ťahov a koncoviek.
* **2007 - Scrabble**: Open-source program Quackle porazil svetového šampióna Davida Boysa.
* **2010 + 2015 - Go**:
    * 2010: MoGoTW porazil profesionálneho hráča pomocou Monte Carlo stromového prehľadávania.
    * 2015: AlphaGo porazil Lee Sedola (9. dan) so skóre 4:1. Kombinoval Monte Carlo prehľadávanie s hlbokými konvolučnými neurónovými sieťami, trénovanými posilňovaným učením (na ľudských hrách aj hraním samého so sebou).
* **2017 - Poker**: Program DeepStack porazil profesionálnych hráčov v No-Limit Texas Hold'em. Využíva hlboké učenie a hranie samého so sebou, rieši situácie lokálne a namiesto hlbokého prepočtu používa "intuitívnu aproximáciu" naučenú z náhodne generovaných situácií.
