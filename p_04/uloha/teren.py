import random
import numpy as np
import matplotlib.pyplot as plt
from deap import base, creator, tools, algorithms
from constants import *
from utils import plot_results

def evaluate(individual):
	# Terrain smoothness: smaller differences between adjacent points are better
	smoothness = sum(abs(individual[i] - individual[i + 1]) for i in range(len(individual) - 1))

	# Land ratio: we want approximately 60% of points above sea level
	land_ratio = sum(1 for x in individual if x > SEA_LEVEL) / len(individual)
	land_penalty = (land_ratio - 0.6) ** 2  # penalty if ratio differs from 0.6

	# Total fitness is the sum of smoothness and land ratio penalty
	total_fitness = smoothness + land_penalty
	return total_fitness,

def init_toolbox():
    # Define fitness and individuals
	creator.create("FitnessTerrain", base.Fitness, weights=(-1.0,))  # Minimalization problem
	creator.create("Individual", list, fitness=creator.FitnessTerrain)
 
	# Initialize toolbox
	toolbox = base.Toolbox()
	toolbox.register("attr_float", random.uniform, 0, 1)  # Terrain height between 0 and 1
	toolbox.register("individual", tools.initRepeat, creator.Individual,
					toolbox.attr_float, n=TERRAIN_LENGTH)
	toolbox.register("population", tools.initRepeat, list, toolbox.individual)
 
	# Register genetic operators
	toolbox.register("evaluate", evaluate)
	toolbox.register("mate", tools.cxBlend, alpha=0.5)  # Blend crossover for real numbers
	toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=0.1, indpb=0.1)
	toolbox.register("select", tools.selTournament, tournsize=2)
 
	return toolbox

def evolve_terrain(toolbox):
	"""
	Run the evolutionary algorithm to generate terrain.
	Args:
		toolbox: Toolbox with genetic operators
	Returns:
		pop: Final population
		logbook: Statistics of the evolution
		hof: Hall of Fame containing best individual
	"""
	pop = toolbox.population(n=POP_SIZE)

	# Setup statistics
	stats = tools.Statistics(lambda ind: ind.fitness.values)
	stats.register("avg", np.mean)
	stats.register("min", np.min)
	stats.register("max", np.max)

	# Create Hall of Fame to store best solution
	hof = tools.HallOfFame(1)

	# Run the algorithm
	pop, logbook = algorithms.eaSimple(pop, toolbox, cxpb=CXPB, mutpb=MUTPB,
										ngen=NGEN, stats=stats, halloffame=hof)

	return pop, logbook, hof


# Run the evolution process
if __name__ == "__main__":
	toolbox = init_toolbox()
	pop, logbook, hof = evolve_terrain(toolbox)
	plot_results(logbook, hof[0])
