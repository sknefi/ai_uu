import random
from utils import *

def count_conflicts(G, coloring):
    """
    Spočíta počet konfliktov – pre každú hranu, kde oba vrcholy majú rovnakú farbu.
    """
    conflicts = 0
    for u, v in G.edges():
        if coloring[u] == coloring[v]:
            conflicts += 1
    return conflicts

def local_conflict(G, coloring, vertex):
    """
    Vráti počet konfliktov, ktoré má daný vrchol so svojimi susedmi.
    """
    return sum(1 for u in G.neighbors(vertex) if coloring[u] == coloring[vertex])

def optimize_coloring(G, coloring):
    """
    Optimalizuje obarvenie grafu tak, aby sa použili najnižšie možné farby.
    Preusporiadava farby tak, aby každý vrchol mal najnižšiu možnú farbu,
    ktorá nespôsobuje konflikt so susedmi.
    
    Parametre:
      G       - Graf (NetworkX)
      coloring- Pôvodné obarvenie grafu
      
    Návrat:
      new_coloring - Optimalizované obarvenie s najnižšími možnými farbami
    """
    n = G.number_of_nodes()
    new_coloring = [-1] * n  # Začíname s neofarbeným grafom
    
    # Prechádzame vrcholy v poradí podľa stupňa (od najvyššieho)
    vertices_by_degree = sorted(range(n), key=lambda v: G.degree(v), reverse=True)
    
    for vertex in vertices_by_degree:
        # Zistíme, ktoré farby sú už použité susedmi
        neighbor_colors = {new_coloring[neighbor] for neighbor in G.neighbors(vertex) 
                          if new_coloring[neighbor] != -1}
        
        # Nájdeme najnižšiu dostupnú farbu
        color = 0
        while color in neighbor_colors:
            color += 1
        
        # Priradíme najnižšiu dostupnú farbu
        new_coloring[vertex] = color
    
    return new_coloring

def hill_climbing_random_walk(G, num_colors, max_iter=10000, random_walk_prob=0.1):
    """
    Hill climbing s optimalizáciou random walk – vylepšená verzia s lokálnym počítaním konfliktov.
    
    Parametre:
      G                - Graf (NetworkX)
      num_colors       - Počet dostupných farieb
      max_iter         - Maximálny počet iterácií
      random_walk_prob - Pravdepodobnosť vykonania náhodnej zmeny (random walk), ak nedôjde k zlepšeniu
      
    Návrat:
      coloring         - Najlepšie nájdené obarvenie (zoznam farebných indexov pre vrcholy)
      current_conflicts- Počet konfliktov pre najlepšie riešenie
    """
    n = G.number_of_nodes()
    # Inicializácia: náhodné obarvenie vrcholov
    coloring = [random.randint(0, num_colors - 1) for _ in range(n)]
    current_conflicts = count_conflicts(G, coloring)
    best_coloring = coloring.copy()
    best_conflicts = current_conflicts
    iterations_without_improvement = 0
    
    for iteration in range(max_iter):
        improved = False
        
        # Pre každý vrchol skúmame zmenu farby na základe lokálneho konfliktu
        for vertex in range(n):
            current_color = coloring[vertex]
            old_local = local_conflict(G, coloring, vertex)
            best_delta = 0  # rozdiel = new_local - old_local; ak je záporný, zlepšenie
            best_color = current_color
            
            # Skúšame farby od najnižšej po najvyššiu
            for color in range(num_colors):
                if color == current_color:
                    continue
                new_local = sum(1 for u in G.neighbors(vertex) if coloring[u] == color)
                delta = new_local - old_local
                
                # Ak je delta rovnaká, preferujeme nižšiu farbu
                if delta < best_delta or (delta == best_delta and color < best_color):
                    best_delta = delta
                    best_color = color
                    
            if best_color != current_color:
                # Zmena zlepšuje lokálny stav – vykonáme ju
                coloring[vertex] = best_color
                improved = True
        
        # Aktualizácia globálneho počtu konfliktov
        current_conflicts = count_conflicts(G, coloring)
        
        # Aktualizácia najlepšieho riešenia
        if current_conflicts < best_conflicts:
            best_conflicts = current_conflicts
            best_coloring = coloring.copy()
            iterations_without_improvement = 0
        else:
            iterations_without_improvement += 1
        
        # Ak sme dosiahli riešenie bez konfliktov, končíme
        if current_conflicts == 0:
            # Optimalizujeme farby pred vrátením výsledku
            if num_colors > 2:  # Ak máme viac ako 2 farby, skúsime optimalizovať
                coloring = optimize_coloring(G, coloring)
            return coloring, 0
        
        # Ak neboli vykonané žiadne zmeny, skúšame random walk
        if not improved:
            if random.random() < random_walk_prob:
                vertex = random.randrange(n)
                current_color = coloring[vertex]
                
                # Pri random walk preferujeme nižšie farby
                available_colors = list(range(num_colors))
                available_colors.remove(current_color)
                available_colors.sort()  # Zoradíme farby od najnižšej
                
                new_color = available_colors[0]  # Vyberieme najnižšiu dostupnú farbu
                coloring[vertex] = new_color
                current_conflicts = count_conflicts(G, coloring)
            else:
                # Ak dlho nedošlo k zlepšeniu, končíme
                if iterations_without_improvement >= 1000:
                    break
    
    # Optimalizujeme farby pred vrátením výsledku
    if best_conflicts == 0 and num_colors > 2:
        best_coloring = optimize_coloring(G, best_coloring)
    
    return best_coloring, best_conflicts

def find_minimum_colors(G, max_attempts=3):
    """
    Nájde minimálny počet farieb potrebný na obarvenie grafu pomocou binárneho vyhľadávania.
    
    Parametre:
      G           - Graf (NetworkX)
      max_attempts- Počet pokusov pre každý počet farieb
    
    Návrat:
      min_colors - Minimálny počet farieb potrebný na obarvenie grafu
      coloring   - Najlepšie nájdené obarvenie
    """
    # Začneme s hornou hranicou ako počet vrcholov a dolnou hranicou ako 2
    lower_bound = 2
    upper_bound = min(G.number_of_nodes(), 100)  # Rozumný horný limit
    best_valid_coloring = None
    min_colors = upper_bound
    
    while lower_bound <= upper_bound:
        num_colors = (lower_bound + upper_bound) // 2
        print(f"\nSkúšam ofarbiť graf použitím {num_colors} farieb...")
        
        # Vyskúšame niekoľko pokusov s daným počtom farieb
        best_conflicts = float('inf')
        for attempt in range(max_attempts):
            coloring, conflicts = hill_climbing_random_walk(G, num_colors)
            if conflicts < best_conflicts:
                best_conflicts = conflicts
                if conflicts == 0:
                    best_valid_coloring = coloring.copy()
                    break
        
        if best_conflicts == 0:
            # Našli sme platné obarvenie, skúsime menší počet farieb
            min_colors = num_colors
            upper_bound = num_colors - 1
            print(f"Úspešné obarvenie s {num_colors} farbami! Skúšam menej farieb...")
        else:
            # Nepodarilo sa nájsť platné obarvenie, potrebujeme viac farieb
            lower_bound = num_colors + 1
            print(f"Neúspešné obarvenie s {num_colors} farbami. Skúšam viac farieb...")
    
    return min_colors, best_valid_coloring