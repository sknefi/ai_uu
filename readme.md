# Umelá inteligencia (AI)

Tento repozitár obsahuje projekty a cvičenia pre univerzitný predmet zameraný na umelú inteligenciu. Počas kurzu sú skúmané rôzne techniky a frameworky umelej inteligencie.

## Nastavenie prostredia pre TensorFlow

Tento projekt používa TensorFlow, ktorý vyžaduje Python verzie 3.11 (TensorFlow nie je kompatibilný s Pythonom 3.13). Bol vytvorený virtuálny environment s názvom `tf_env`, ktorý obsahuje správnu verziu Pythonu a nainštalovaný TensorFlow.

### Používanie TensorFlow prostredia

Na aktiváciu TensorFlow prostredia spustite:

```bash
source tf_env/bin/activate
```

Po aktivácii by sa na začiatku riadku v termináli malo zobraziť `(tf_env)`, čo signalizuje, že prostredie je aktívne.

Na spustenie TensorFlow skriptu použite:

```bash
python3 your_script.py
```

Na deaktiváciu prostredia po dokončení práce:

```bash
deactivate
```

### Kontrola verzií

Na zobrazenie verzie Pythonu v systéme a v tf_env prostredí:

```bash
# Systémová verzia
python --version

# tf_env verzia
source tf_env/bin/activate && python --version && deactivate
```

Na zobrazenie verzie TensorFlow:

```bash
source tf_env/bin/activate && python -c "import tensorflow as tf; print(f'TensorFlow version: {tf.__version__}')" && deactivate
```

### Detaily prostredia
- Verzia Pythonu: 3.11
- Verzia TensorFlow: 2.19.0
- Umiestnenie virtuálneho prostredia: ./tf_env/