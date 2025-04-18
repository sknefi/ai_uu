# Neurónové siete

Tento dokument poskytuje prehľad základných konceptov umelej neurónovej siete, od modelu jednotlivého neurónu až po moderné architektúry ako CNN a RNN.

![Intro image](../../imgs_for_readme/neuron/intro.png) 

## Model umelého neurónu (Perceptron)
- **Biologický paralel:** Neurón má dendrity (vstupy) a axón (výstup). Signály sa sčítavajú a ak prekročia prah, neurón „odpáli“ signál.

- **Perceptron (1958):**  
  - Vstupy: \(x_1, x_2, ..., x_n\)  
  - Váhy: \(w_1, w_2, ..., w_n\)  
  - Práh: \(Θ -> théta)  
  - Výstup \(y\):
    ```math
    y =
      \begin{cases}
        1, & \text{ak } \sum_i w_i x_i \ge \theta,\\
        0, & \text{inak.}
      \end{cases}
    ```

  ![Perceptron](../../imgs_for_readme/neuron/neuronimg.jpeg)

- **Lineárna separabilita:** Perceptron rozdeľuje priestor nadrovinou. Rozlíši len lineárne separabilné problémy (napr. AND, OR), no nie XOR ani NXOR.

  ![AND OR](../../imgs_for_readme/neuron/and_or.jpeg) 
  
  ![Polrovina](../../imgs_for_readme/neuron/polrovina.png) 

- **Tabulka všetkých možných 16 logických funkcí o dvou vstupech** 
  
  ![Tabulka x1 x2](../../imgs_for_readme/neuron/tablex1x2.jpeg)  

## Dopredná neurónová sieť (Feedforward)
- Vrstvy neurónov bez spätných cyklov:
  1. **Vstupná vrstva** (I)  
  2. **Skryté vrstvy** (N)  
  3. **Výstupná vrstva** (O)  
- Signál prechádza len jedným smerom (bez cyklov). 
  
  ![Dopredná sieť](../../imgs_for_readme/neuron/dopredna_siet.jpeg) 
  
- **Príklad XOR:** Potrebujeme dva perceptrony v prvej vrstve + jeden OR-perceptron v druhej vrstve, aby sieť dokázala reprezentovať XOR.
  
  ![XOR](../../imgs_for_readme/neuron/xor.jpeg) 

- **V priestore n:** budeme k separácii potrebovať n+1 neurónov pre vymedzenie množiny bodov a jeden AND neuron, ktorý nám povie či všetky body z množiny splňujú polohu polrovin.

	![n+1 linea](../../imgs_for_readme/neuron/n+1.jpeg)  

## Aktivačné funkcie
- **Skoková (Heaviside):**  
	Jednoduchá, ale nediferencovateľná v prahu.
	![n+1 linea](../../imgs_for_readme/neuron/fskok.jpeg)  

- **Lineárna:**  
	Priame prevedenie signálu. 
	![Linear function](../../imgs_for_readme/neuron/flin.jpeg) 
- **ReLU:**  
	Rýchla konvergencia, rieši negatívne hodnoty. 
	![ReLu function](../../imgs_for_readme/neuron/frelu.jpeg) 
- **Sigmoida (logistická):**  
	Výstup v (0,1), hladká.  
	![Sigmoid function](../../imgs_for_readme/neuron/fsigmoid.jpeg)
- **Tanh (hyperbolický):**  
	Výstup v (−1,1), centrálny okolo 0.
	![Hyperbolický tangens](../../imgs_for_readme/neuron/fhtan.jpeg)

## Neurónová sieť ako funkcia
- Sieť predstavuje zloženú funkciu \(f:\mathbb{R}^n\to\mathbb{R}^m\).  
- Rieši úlohy ako klasifikácia, predikcia či riadenie.  
- Problém učenia: správne nastaviť váhy a prahy, aby sieť vracala očakávané výstupy.

## Typy neurónových sietí

### 1. Dopredné siete (Feed forward Neural Networks)
- Vrstvy: vstupná → skryté → výstupné.  
- Žiadne cykly, signál prudí iba jedným smerom.

	![UU FFNN](../../imgs_for_readme/neuron/uuffnn.jpeg)

### 2. Hlboké siete (DNN - Deep Neural Networks)
- Viacero skrytých vrstiev (dve a viac).  
- Automatická extrakcia vlastností (feature learning). 
- Problémy: vanishing gradient — riešenie: dropout, batch norm, reziduálne vrstvy.

	![UU DNN](../../imgs_for_readme/neuron/uudnn.jpeg)

	- Dvojvrstvová - rieši napr. XOR
  
		![Deep neural network 2 layers](../../imgs_for_readme/neuron/deepneuralnetwork.png) 

	- Trojvrstvová - rieši napr. kategorizáciu obrázkov
	
		![Deep neural network 3 layers](../../imgs_for_readme/neuron/deepneuralnetwork3.png) 

### 3. Rekurentné siete (RNN - Recurent Neural Networks)
- Majú spätné spojenia, modelujú časové závislosti.  
- Použitie: text, časové rady, reč.  
- Pokročilé jednotky: LSTM, GRU — riešia dlhodobé závislosti.

	![UU RNN](../../imgs_for_readme/neuron/uurnn.jpeg)

#### Sekvenčné spracovanie a skrytý stav

- Na rozdiel od CNN, ktoré sa orientujú na priestorové vzory, RNN pracujú so sekvenčnými dátami (časové rady, text, reč).

- Každý krok do seba vstup (napr. jeden znak alebo jeden časový údaj) a tiež prevezme skrytý stav z predchádzajúceho kroku, ten funguje ako krátkodobá pamäť pre predošlé informácie.
  
	![Recurent Neural Network](../../imgs_for_readme/neuron/rnn.png)

### 4. Konvolučné siete (CNN - Convolutional Neural Network)
- Určené najmä pre obrazové dáta.  
- **Konvolučné vrstvy:** Filtre extrahujú lokálne vzory (hrany, textúry, tvary).  
- Aplikácie: detekcia objektov, rozpoznávanie tvárí, segmentácia.
	![UU CNN](../../imgs_for_readme/neuron/uucnn.jpeg)

#### Hierarchická extrakcia rysov

- Na najnižších úrovniach sa filtrami zachytávajú základné elementy obrazu (hrany, rohy, plochy).

- V stredných vrstvách sa už spoja do zložitejších štruktúr (textúry, menšie tvary).

- V hlbších vrstvách vznikajú semantické celky (uši, oči, objekty).

#### Lokálna i translácia invariantná detekcia

- Každý filter pracuje iba na malej lokálnej oblasti (receptívne pole), čo umožňuje učiť sa miestne vzory.

- Keďže ten istý filter sa „posúva“ (sliduje) cez celý obraz, je schopný detegovať rovnaký vzor kdekoľvek – výsledok je translácia‑invariantný.
  - Filter obrázku:
  
	![Filter CNN](../../imgs_for_readme/neuron/uumatrix.jpeg)

  - Process CNN
  
	![CNN process](../../imgs_for_readme/neuron/zebra.png)

## Aplikácie
- **Klasifikácia obrazu:** Rozpoznávanie objektov.  
- **Predikcia časových radov:** Ekonomické dáta, senzory.  
- **NLP:** Strojový preklad, sentiment analýza.  
- **Reinforcement Learning:** AlphaGo, DeepMind Atari agent. 


| Typ siete                                 | Aplikácie                                                        |
|-------------------------------------------|------------------------------------------------------------------|
| **Feedforward Neural Network**            | Klasifikácia a regresia na tabulárnych dátach                    |
| **Deep Neural Network (DNN)**             | Extrakcia vlastností (feature learning), obrazová klasifikácia   |
| **Recurrent Neural Network (RNN)**        | Predikcia časových radov, spracovanie prirodzeného jazyka, reč    |
| **Convolutional Neural Network (CNN)**    | Rozpoznávanie a detekcia objektov, segmentácia obrazov, FaceID   |
