from hill_climbing import *
from constants import *

def main():
	# Zvolíme si graf 0-6
	path, num_colors = choose_graph(int(input()))

	# Načítame si graf
	G = readdimacs(path)
	print("# vrcholov:", G.number_of_nodes(), ";", "# hran:", G.number_of_edges())

	# Spustíme hill climbing random walk
	coloring, conflicts = hill_climbing(G, num_colors, MAX_ITER) # funkcia step zo zadania

	# Vypíšeme počet konfliktov a zistíme, či je obarvenie správne
	print("Najdených konfliktov:", conflicts)
	is_coloring(G, coloring)

	# Vypíšeme obarvenie a vykreslíme graf
	print(coloring)
	plot(G, coloring)

if __name__ == '__main__':
    main()