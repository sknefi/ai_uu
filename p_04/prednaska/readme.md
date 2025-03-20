# Umelá evolúcia a evolučné algoritmy

Táto prednáška predstavuje základné princípy umelej evolúcie a evolučných algoritmov, ktoré využívajú inšpiráciu z prírodného evolučného procesu (napr. Darwinovej teórie) na riešenie zložitých optimalizačných úloh. Evolučné algoritmy sú mimoriadne užitočné, najmä keď nevieme presne, ako má ideálne riešenie vyzerať, ale poznáme požadované vlastnosti.

## Základné princípy umelej evolúcie

- **Inšpirácia z biológie:**  
  Evolučné algoritmy čerpajú zo základných princípov prírodnej evolúcie: 
  - **Dedičnosť:** Jedinci môžu zdediť vlastnosti od svojich rodičov.
  - **Variabilita:** V populácii existujú rozdiely, ktoré umožňujú vznik nových riešení.
  - **Prírodný výber:** Jedinci s lepšími vlastnosťami majú väčšiu šancu prežiť, rozmnožiť sa a odovzdať svoje vlastnosti ďalej.

- **Náhodná inicializácia:**  
  Na začiatku generujeme populáciu jedincov (riešení) náhodne, čo znamená, že prvotné riešenia môžu byť neplatné alebo nekvalitné, ale obsahujú základnú genetickú informáciu.

## Evolučný proces a kľúčové komponenty

Evolučné algoritmy pracujú na základe opakovaných generácií, kde sa populácia jedincov postupne zlepšuje. Hlavné kroky sú:

### 1. Kódovanie jedincov

Každý jedinec predstavuje riešenie úlohy a môže byť zakódovaný rôznymi spôsobmi:
- **Binárne kódovanie:**  
  Jedinec je reťazec 0 a 1, čo je pôvodný spôsob, ktorý používal Holland.
- **Stromové kódovanie:**  
  Používa sa pre zložitejšie štruktúry (napr. rozhodovacie stromy, programy).
- **N-tice alebo tabuľkové kódovanie:**  
  Vhodné pre reprezentáciu posloupností alebo akčných plánov.

### 2. Fitness funkcia

Fitness funkcia hodnotí, ako dobré je riešenie reprezentované jedincami. Príklady:
- **Optimalizácia funkcie:** Fitness je hodnota funkcie v danom bode.
- **Hľadanie stratégie:** Fitness môže byť počet výhier získaných opakovaným spustením stratégie.
- **SAT problém:** Fitness je počet splnených klauzúl.
- **Optimalizácia dizajnu:** Napríklad optimalizácia tvaru křídla, kde fitness vychádza z fyzikálnych simulácií.

### 3. Selekcia

Na základe fitness sa vyberajú jedinci, ktorí sa stanú rodičmi novej generácie. Medzi bežne používané metódy patria:
- **Ruletová selekcia:** Výber jedincov úmerne k ich fitness.
- **Stochastic Universal Sampling (SUS):** Rovnomernejší výber jedincov.
- **Elitizmus:** Najlepší jedinci sa automaticky prenášajú do ďalšej generácie.
- **Turnajová selekcia:** Náhodne sa vyberú skupiny jedincov a silnejší jedinec má väčšiu šancu vyhrať.

### 4. Genetické operátory

Pre vytvorenie novej generácie sa využívajú genetické operátory:
- **Crossover:**  
  Kombinácia genetickej informácie dvoch rodičov, ktorá môže prebiehať jednobodovo, dvoubodovo alebo viacbodovo.
- **Mutácia:**  
  Náhodná zmena v jedincovi, ktorá prináša novú genetickú informáciu a pomáha pri preskúmavaní vyhľadávacieho priestoru.

### 5. Evolučný cyklus

Celý evolučný algoritmus prebieha v nasledujúcich fázach:
- **Inicializácia:**  
  Generácia populácie jedincov (náhodné riešenia).
- **Hodnotenie:**  
  Každý jedinec je ohodnotený fitness funkciou.
- **Selektívna reprodukcia a genetické operátory:**  
  Na základe fitness sa vytvára nová generácia.
- **Opakovanie:**  
  Tento proces sa opakuje, kým sa nedosiahne uspokojivé riešenie alebo preddefinovaný počet generácií.

## Hollandove genetické algoritmy

John Holland predstavil svoje genetické algoritmy v knihe *Adaptation in Natural and Artificial Systems* (1975). Jeho prístup sa stal základom pre evolučné algoritmy, pričom poskytuje univerzálny rámec:
- **Definovať kódovanie jedincov**
- **Nastaviť mechanizmus selekcie**
- **Navrhnúť genetické operátory (crossover, mutácia)**
- **Stanoviť fitness funkciu**

Tento rámec môže byť aplikovaný na riešenie rôznych problémov, od grafového obarvenia po optimalizáciu dizajnu či evolučné programovanie.

## Aplikácie evolučných algoritmov

Evolučné algoritmy našli svoje uplatnenie v mnohých oblastiach:
- **Optimalizácia dizajnu:**  
  Napríklad u Boeingu 777, kde evolučná optimalizácia lopatiek motorov viedla k významnej úspore paliva.
- **Návrh antén:**  
  NASA použila evolučné algoritmy na návrh antény s netradičným tvarom, ktorý by ľudský dizajnér ťažko navrhol.
- **Forenzná identifikácia:**  
  Evolučné algoritmy môžu pomôcť zostaviť identiku pachateľa zo sádia jednotlivých častí tváre.
- **Generatívne umenie:**  
  Evolučné metódy sa používajú na tvorbu umeleckých diel, kde sa umelecké riešenia evolvujú a hodnotia.
- **Hľadanie architektúry neurónových sietí:**  
  Automatické vyhľadávanie optimálnej štruktúry neurónových sietí využíva evolučné algoritmy.

## Záver

Evolučné algoritmy poskytujú flexibilný a univerzálny rámec pre riešenie optimalizačných úloh, najmä keď presná podoba riešenia nie je vopred známa. Vďaka princípom evolúcie, ako je selekcia, crossover a mutácia, dokážu tieto algoritmy postupne zlepšovať populáciu riešení a hľadať optimálne alebo aspoň veľmi kvalitné riešenia aj pre náročné problémy. Úspech evolučných algoritmov závisí na správnom nastavení parametrov, voľbe vhodného kódovania jedincov a definovaní efektívnej fitness funkcie.

Experimentujte s rôznymi evolučnými stratégiami a aplikujte ich na riešenie konkrétnych problémov – od grafového obarvenia až po komplexné inžinierske optimalizácie. Evolučné algoritmy dokazujú svoju univerzálnosť a efektívnosť v mnohých reálnych aplikáciách, čo ich robí dôležitým nástrojom aj v modernej umelej inteligencii.
