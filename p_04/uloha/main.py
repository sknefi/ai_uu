from teren import *

# Run the evolution process
if __name__ == "__main__":
	toolbox = init_toolbox()
	pop, logbook, hof = evolve_terrain(toolbox)
	plot_results(logbook, hof[0])