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

def draw_colored_graph(G, coloring, color_names):
	"""
	Vykreslí graf s farebným obarvením.

	Parametre:
		G           - Graf (NetworkX)
		coloring    - Pole farebných indexov (dĺžka rovnaká ako počet vrcholov)
		color_names - Zoznam názvov farieb, napr. ['red', 'green', 'blue', ...]
	"""
	node_colors = [color_names[coloring[node]] for node in G.nodes()]
	pos = nx.spring_layout(G)
	nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color='gray')
	plt.show()
 
# bere na vstupu pole barev vrcholu poporade, cislum priradi nahodne barvy a vykresli graf
def plot(G, cols):
	rng = np.random.default_rng(12345)  # seed
	k = np.max(cols)
	symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
	colmap = ["#"+''.join(rng.choice(symbols, 6)) for i in range(k+1)]
							
	colors = [colmap[c] for c in cols]

	nx.draw(G, node_color=colors, with_labels=True)
	plt.show()