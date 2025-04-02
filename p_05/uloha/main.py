
from tournament import *
from deap import base, creator
def main():
	creator.create("FitnessMax", base.Fitness, weights=(1.0,))
	creator.create("Individual", list, fitness=creator.FitnessMax)
	tournament()

if __name__ == "__main__":
    main()