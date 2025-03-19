from hill_climbing import *
from constants import *

def main():
	# Zvolíme si graf 0-6
	path, num_colors = choose_graph(int(input("Zvolte číslo simulácie [0, 8]> ")))

	# Načítame si graf
	G = init_graph(path)

	# is_coloring(G, VALID_125_1)

	# Spustíme hill climbing random walk
	coloring = hill_climbing(G, num_colors) # funkcia step zo zadania

	# Zistíme, či je obarvenie správne
	is_coloring(G, coloring)

	# Vypíšeme obarvenie a vykreslíme graf
	print(coloring)
	plot(G, coloring)

if __name__ == '__main__':
    main()