from hill_climbing import *
from constants import *

def main():
	# Načítame graf
	G = readdimacs(PATH)
	print("# vrcholov:", G.number_of_nodes(), ";", "# hran:", G.number_of_edges())

	coloring, conflicts = hill_climbing_random_walk(G, NUM_COLORS, MAX_ITER, RANDOM_WALK_PROB)
	
	print("Najdených konfliktov:", conflicts)
	is_coloring(G, coloring)
	plot(G, coloring)

if __name__ == '__main__':
    main()