import random
from constants import *
from utils import *

def count_conflicts(G, coloring):
	# Spočíta počet konfliktov – pre každú hranu, kde oba vrcholy majú rovnakú farbu.
	conflicts = 0
	for u, v in G.edges():
		if coloring[u] == coloring[v]:
			conflicts += 1
	return conflicts

def local_conflict(G, coloring, vertex):
	# Vráti počet konfliktov, ktoré má daný vrchol so svojimi susedmi.
	return sum(1 for u in G.neighbors(vertex) if coloring[u] == coloring[vertex])

def hill_climbing_random_walk(G, num_colors, max_iter, random_walk_prob):
	"""
	Hill climbing s optimalizáciou random walk – verzia, ktorá vždy uprednostní najnižšie
	číslovanú farbu v prípade rovnakého zlepšenia.
	"""
	n = G.number_of_nodes()

	# Inicializácia: náhodné obarvenie vrcholov
	coloring = [random.randint(0, num_colors - 1) for _ in range(n)]
	current_conflicts = count_conflicts(G, coloring)

	for iteration in range(max_iter):
		improved = False
		
		for vertex in range(n):
			current_color = coloring[vertex]
			old_local = local_conflict(G, coloring, vertex)
			
			# best_delta < 0 znamená zlepšenie (pretože delta = new_local - old_local)
			best_delta = 0
			best_color = current_color
			
			for color in range(num_colors):
				if color == current_color:
					continue
				# Koľko konfliktov by mal vrchol s touto novou farbou
				new_local = sum(1 for u in G.neighbors(vertex) if coloring[u] == color)
				delta = new_local - old_local
				
				# Podmienka: ak je delta menšia, je to lepšie;
				# ak je delta rovnaká a color < best_color, tiež to uprednostníme
				if delta < best_delta or (delta == best_delta and color < best_color):
					best_delta = delta
					best_color = color
			
			# Ak sme našli zlepšenie (best_delta < 0) alebo rovnocenné riešenie s menšou farbou
			if best_color != current_color:
				coloring[vertex] = best_color
				improved = True
		
		# Aktualizácia globálneho počtu konfliktov
		current_conflicts = count_conflicts(G, coloring)
		print(f"Iterácia {iteration}, konflikty: {current_conflicts}")
		
		# Ak sme dosiahli riešenie bez konfliktov, končíme
		if current_conflicts == 0:
			break
		
		# Ak neboli vykonané žiadne zmeny, skúšame random walk
		if not improved:
			if random.random() < random_walk_prob:
				vertex = random.randrange(n)
				current_color = coloring[vertex]
				available_colors = [c for c in range(num_colors) if c != current_color]
				new_color = random.choice(available_colors)
				coloring[vertex] = new_color
				print(f"Random walk: zmena vrcholu {vertex} na farbu {new_color}")
				current_conflicts = count_conflicts(G, coloring)
			# else:
			# 	print(ORANGE + "Žiadne zlepšenie a random walk nebola vykonaná. Ukončujem." + RESET)
			# 	break

	return coloring, current_conflicts


def is_coloring(G, col):
    # Overí, či je dané obarvenie korektné (žiadne dva susedné vrcholy nemajú rovnakú farbu)
    for u, v in G.edges():
        if col[u] == col[v]:
            print(RED + "Nevalidné obarvenie" + RESET)
            return False
    print(GREEN + "Validné obarvenie" + RESET)
    return True

