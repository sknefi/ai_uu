from hill_climbing import *
from constants import *

def main():
	# Načítame graf
	G = readdimacs(PATH2)
	print("# vrcholov:", G.number_of_nodes(), ";", "# hran:", G.number_of_edges())

	best_coloring, conflicts = hill_climbing_random_walk(G, NUM_COLORS, MAX_ITER, RANDOM_WALK_PROB)
	print("Najdených konfliktov:", conflicts)
	print(best_coloring)
	plot(G, best_coloring)

if __name__ == '__main__':
    main()