# Učenie s učiteľom (Supervised Learning)

## Úvod

Po inteligentných agentoch často chceme, aby sa vedeli učiť. Učenie môže mať viacero podôb, podľa toho, koľko informácií máme k dispozícii:

- **Bez informácií** – agent sa učí sám z prostredia
- **S evaluáciou** – dostáva spätnú väzbu, ako dobre sa rozhodol
- **S učiteľom** – dostáva vstupy a správne výstupy pre učenie

V tejto kapitole sa zameriame na **učenie s učiteľom**, najmä pomocou **neuronových sietí**.

---

## Vstupné dáta

Neuronová sieť je matematická funkcia, ktorá pre vstupy vracia výstupy. Pri učení s učiteľom používame **trénovaciu množinu dát**, ktorá obsahuje dvojice:

- `x` – vstup (napr. obraz)
- `y` – výstup (napr. identifikácia objektu)

Cieľom učenia je nájsť také váhy a prahy, aby výstupy siete čo najviac zodpovedali reálnym dátam. Zároveň nás zaujíma, ako dobre vie sieť **generalizovať** – teda ako si poradí s novými dátami, ktoré predtým nevidela.

---

## Chyba aproximácie

Pri učení chceme minimalizovať **chybu aproximácie** – rozdiel medzi výstupom siete a očakávaným výstupom.

Najčastejšie sa používa metrika **mean squared error** (MSE), teda priemer štvorcov rozdielov medzi výstupmi siete a požadovanými hodnotami.

---

## Algoritmus Backpropagation

Najznámejší algoritmus učenia viacvrstvových sietí je **backpropagation**, ktorý funguje nasledovne:

1. Spočítame výstupy siete a chybu na trénovacej množine.
2. Chyba je funkcia všetkých váh siete.
3. Spočítame **gradient** – smer najväčšieho klesania chyby.
4. Postupne upravujeme váhy v smere tohto gradientu.
5. Tento postup opakujeme, kým chyba neklesne dostatočne.

Cieľom je nájsť **globálne minimum** v krajine chybovej funkcie.

---

## Alternatívne algoritmy

Existuje mnoho alternatívnych algoritmov k backpropagation:

- **Silva-Almeida** – adaptívna učebná rýchlosť
- **Delta-bar-delta** – opatrnejšia zmena rýchlosti učenia
- **Rprop** – zameriava sa na rýchle prekonávanie plochých oblastí chyby
- **Quickprop** – berie do úvahy aj zakrivenie chyby (druhé derivácie)
- **QRprop** – kombinuje Rprop a Quickprop

---

## Aplikácie a limity neuronových sietí

Neuronové siete sú vhodné pre úlohy, kde potrebujeme **generalizáciu**. Sú však aj limitované:

✅ Vhodné na rozpoznávanie vzorov, predikcie, klasifikáciu

❌ Môžu sa **preučiť** (overfitting)

❌ Sú **náročné na dáta a výpočty**

❌ Sú **ťažko interpretovateľné** – čierna skrinka

---

## Nastavenie siete

Dôležité je zvoliť vhodnú **topológiu siete** – počet vrstiev a neurónov.

- Začni s 1 skrytou vrstvou
- Ak nefunguje dobre, pridaj neuróny alebo vrstvy
- Pri veľa neurónoch hrozí preučenie (overfitting)
- Váhy sa zvyčajne inicializujú náhodne z intervalu `[-a, a]`

---

## Ako zlepšiť učenie

- **Dobrá topológia siete**
- **Vhodná učebná rýchlosť**
- **Moment setrvačnosti** – pamätá si smer učenia
- **Náhodný šum** – znižuje riziko uviaznutia v lokálnom minime
- **Rozšírenie dát** – viac dát, lepšie učenie
- **Early stopping** – ukončenie učenia skôr, ako nastane overfitting

---

## Overfitting vs Underfitting

- **Overfitting** – sieť sa naučila presne trénovacie dáta, ale nefunguje na nové
- **Underfitting** – sieť sa nenaučila ani trénovacie dáta
- Riešením je **early stopping** a **testovacia množina**

---

## Regularizácia a Dropout

- **L1/L2 regularizácia** – trest za príliš veľké váhy
- **Dropout** – počas učenia náhodne vypíname niektoré neuróny

---

## Iné formy učenia s učiteľom

Okrem neuronových sietí existujú aj iné metódy:

- **Lineárna regresia**
- **Random Forests**
- **Support Vector Machines (SVM)**

---

Ak chceš k niektorej časti obrázok alebo doplniť kód, daj vedieť! 💡
