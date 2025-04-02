import random
import numpy as np
import matplotlib.pyplot as plt
from deap import base, creator, tools, algorithms
from constants import *
from utils import plot_results

def evaluate(individual):
	# Calculate terrain smoothness by summing differences between adjacent points
	# Smaller differences indicate smoother terrain
	smoothness = sum(abs(individual[i] - individual[i + 1]) for i in range(len(individual) - 1))

	# Calculate the ratio of land above sea level
	# Target is approximately 60% of points above sea level
	land_ratio = sum(1 for x in individual if x > SEA_LEVEL) / len(individual)
	# Apply penalty if the ratio deviates from the target of 0.6
	land_penalty = (land_ratio - 0.6) ** 2

	# Combine smoothness and land ratio penalty for total fitness
	# Lower fitness is better (minimization problem)
	total_fitness = smoothness + land_penalty
	return total_fitness,

def init_toolbox():
	# Define fitness and individuals
	creator.create("FitnessTerrain", base.Fitness, weights=(-1.0,))  # Minimization problem
	creator.create("Individual", list, fitness=creator.FitnessTerrain)
 
	# Initialize toolbox with genetic operators
	toolbox = base.Toolbox()
	# Generate random terrain heights between 0 and 1
	toolbox.register("attr_float", random.uniform, 0, 1)
	# Create individuals with specified terrain length
	toolbox.register("individual", tools.initRepeat, creator.Individual,
					toolbox.attr_float, n=TERRAIN_LENGTH)
	# Create population of individuals
	toolbox.register("population", tools.initRepeat, list, toolbox.individual)
 
	# Register genetic operators
	toolbox.register("evaluate", evaluate)
	# Blend crossover for real numbers with alpha=0.5
	toolbox.register("mate", tools.cxBlend, alpha=0.5)
	# Gaussian mutation with mean=0, std=0.1, and 10% probability per attribute
	toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=0.1, indpb=0.1)
	# Tournament selection with size 2
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
	# Initialize population
	pop = toolbox.population(n=POP_SIZE)
	
	# Setup statistics tracking
	stats = tools.Statistics(lambda ind: ind.fitness.values)
	stats.register("avg", np.mean)
	stats.register("min", np.min)
	stats.register("max", np.max)

	# Create Hall of Fame to store best solution
	hof = tools.HallOfFame(1)

	# Run the evolutionary algorithm
	pop, logbook = algorithms.eaSimple(pop, toolbox, cxpb=CXPB, mutpb=MUTPB,
										ngen=NGEN, stats=stats, halloffame=hof)

	return pop, logbook, hof
