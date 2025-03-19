import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def readdimacs(filename):
	"""
	Načíta graf zo súboru vo formáte DIMACS.
	Každý riadok začínajúci "e" definuje hranu.
	"""
	with open(filename, 'r') as f:
		lines = f.readlines()

	Gd = nx.Graph()
	for line in lines:
		if line.startswith("e"):
			vs = [int(s) for s in line.split() if s.isdigit()]
			# 0-indexovanie: odpočítame 1
			Gd.add_edge(vs[0]-1, vs[1]-1)
	return Gd
 
# bere na vstupu pole barev vrcholu poporade, cislum priradi nahodne barvy a vykresli graf
def plot(G, cols):
	rng = np.random.default_rng(12345)  # seed
	k = np.max(cols)
	symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
	colmap = ["#"+''.join(rng.choice(symbols, 6)) for i in range(k+1)]
							
	colors = [colmap[c] for c in cols]

	# Zobrazí legendu s farbami
	plt.legend(handles=[plt.scatter([], [], c=colmap[i], label=f'Color {i}') for i in range(k+1)])

	# Vykreslí graf s obarvenými vrcholmi
	nx.draw(G, node_color=colors, with_labels=True)

	# Zobrazí text s počtom použitých farieb
	num_used_colors = len(set(cols))
	plt.title(f"Počet použitých farieb: {num_used_colors}")

	plt.show()

def init_graph(path):
	G = readdimacs(path)
	print("#vrcholov:", G.number_of_nodes(), ";", "#hran:", G.number_of_edges())
	return G