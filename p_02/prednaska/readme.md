# Inteligentný agent (AI prednáška č. 2)

## 🔸 Čo je agent?
- Vníma prostredie pomocou **senzorov** (napr. kamera, mikrofón)
- Vykonáva **akcie** na základe vnímania (napr. pohyb, signalizácia)
- Agent = **vnímanie → rozhodovanie → akcia**

## 🔸 Racionálny agent
- Vyberá najlepšie možné akcie na základe dostupných informácií
- Cieľom je **maximalizácia užitku** (zisk, efektívnosť)

## 🔸 Typy prostredí

### Pozorovateľnosť
- **Plne pozorovateľné:** Agent vidí všetko, nepotrebuje pamäť
  - *(Príklad: Šach)*
- **Čiastočne pozorovateľné:** Obmedzené informácie
  - *(Príklad: Poker, jazda autom v hmle)*

### Počet agentov
- **Jedno-agentné:** V prostredí je jediný agent (napr. sudoku)
- **Multi-agentné:** Viacero agentov, spolupráca alebo súťaž
  - *(Príklad: Fortnite)*

### Determinizmus
- **Deterministické:** Ďalší stav jasne určený aktuálnym stavom
- **Stochastické:** Obsahujú náhodné prvky
  - *(Príklad: náhodné predmety v hrách)*

### Epizodické vs. Sekvenčné
- **Epizodické:** Akcia v jednej epizóde neovplyvní ďalšie epizódy
  - *(Príklad: triedenie balíkov)*
- **Sekvenčné:** Akcie ovplyvňujú budúcnosť
  - *(Príklad: hranie šachu)*

### Statické vs. Dynamické
- **Statické:** Svet čaká na rozhodnutie agenta
  - *(Príklad: šach bez časového limitu)*
- **Dynamické:** Svet sa mení počas rozhodovania
  - *(Príklad: jazda autom v premávke)*

### Diskrétne vs. Spojité
- **Diskrétne:** Obmedzený počet akcií/stavov
- **Spojité:** Nekonečne veľa možných stavov alebo akcií

### Známe vs. Neznáme
- **Známe:** Agent pozná následky svojich akcií vopred
- **Neznáme:** Agent sa učí následky za chodu
  - *(Príklad: kartové hry)*

## 🔸 Typy agentov podľa štruktúry

### 1. Jednoduchý (reflexný) agent
- Reaguje okamžite podľa pravidiel (if-then)
- Neuvažuje nad minulosťou ani budúcnosťou
- *(Príklad: automatické dvere, detektor dymu)*

### 2. Reflexný agent s modelom
- Má **model sveta** (pamätá si históriu)
- Využíva model pri rozhodovaní
- *(Príklad: termostat)*

### 3. Cieľovo orientovaný agent
- Má jasný cieľ, plánuje kroky na jeho dosiahnutie
- *(Príklad: navigácia GPS)*

### 4. Užitkovo orientovaný agent
- Hodnotí aj kvalitu cesty k cieľu (bezpečnosť, cena, čas)
- Využíva **očakávaný užitok**
- *(Príklad: autonómne vozidlo)*

### 5. Učiaci sa agent
- Zlepšuje svoje rozhodovanie učením sa zo skúseností
- Potrebuje **spätnú väzbu**
- *(Príklad: chatbot, robotické učenie)*

## 🔸 Základná rovnica agentov
```
Agent = Architektúra + Program
```
- **Architektúra:** telo agenta, hardware, senzory
- **Program:** softvér určujúci správanie a akcie

## 🔸 Príklady prostredí pre rôznych agentov

| Prostredie | Pozorovateľnosť | Dynamika | Sekvenčnosť | Determinizmus | Počet agentov | Spojitosť | Známe/Neznáme |
|------------|-----------------|----------|-------------|---------------|---------------|------------|---------------|
| Šach       | Plná            | Statické | Sekvenčné   | Deterministické | Jedno-agentné | Diskrétne  | Známe        |
| Poker      | Čiastočná       | Statické | Sekvenčné   | Stochastické  | Multiagentné  | Diskrétne  | Neznáme      |
| Fortnite   | Čiastočne       | Dynamické| Sekvenčné   | Stochastické  | Multiagentné  | Spojité    | Neznáme      |
| Sudoku     | Plne            | Statické | Sekvenčné   | Deterministické| Jedno-agentné | Diskrétne  | Známe        |
| Kontrola kvality výrobkov | Plne | Statické | Epizodické | Deterministické | Jedno-agentné | Diskrétne  | Známe        |
| Autonómne vozidlo | Čiastočne | Dynamické | Sekvenčné | Stochastické | Multiagentné | Spojité    | Neznáme      |
