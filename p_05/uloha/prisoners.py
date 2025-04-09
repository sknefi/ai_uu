import random
from deap import base, creator, tools, algorithms
from constants import * 

# Create genetic algorithm classes only once
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

def evaluate_strategy(ind, opponent_history):
	# ind[0] = betray threshold (0-1)
	# ind[1] = lookback period (0-1)
	# ind[2] = forgiveness factor (0-1)
	# Calculate lookback period (2-5 moves)
	lookback = int(2 + ind[1] * 3)
	last_moves = opponent_history[-lookback:] if len(opponent_history) >= lookback else opponent_history
	
	# Count betrayals and calculate betrayal rate
	betray_count = last_moves.count(1)
	betrayal_rate = betray_count / len(last_moves)
	
	# Apply forgiveness factor
	adjusted_rate = betrayal_rate * (1 - ind[2])
	
	# Make decision based on evolved parameters
	if adjusted_rate >= ind[0]:
		return 1  # Betray
	return 0  # Cooperate

def init_genetic_algorithm():
	toolbox = base.Toolbox()
	toolbox.register("attr_float", random.uniform, 0, 1)
	toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, 3)
	toolbox.register("population", tools.initRepeat, list, toolbox.individual)
	return toolbox 

def fk_solution(my_history, opponent_history): 
	# Start with cooperation
	if not opponent_history:
		return 0
		
	# Betray on specific rounds
	if (len(my_history) + 1) % BETRAY_ROUND == 0:
		return 1
	
	toolbox = init_genetic_algorithm()
	
	def evaluate(ind):
		# Evaluate how well the strategy predicts opponent's moves
		correct = 0
		for i in range(1, len(opponent_history)):
			# Use the strategy to make a prediction using history up to current point
			pred = evaluate_strategy(ind, opponent_history[:i])
			if pred == opponent_history[i]:
				correct += 1
		return (correct,)  # Return as tuple for fitness
	
	# Register genetic operators
	toolbox.register("evaluate", evaluate)
	toolbox.register("mate", tools.cxTwoPoint)
	toolbox.register("mutate", tools.mutGaussian, mu=0.5, sigma=MUT_SIGMA, indpb=MUT_IND_PB)
	toolbox.register("select", tools.selTournament, tournsize=TOURNAMENT_SIZE)
	
	# Create and evolve population
	pop = toolbox.population(n=POP_SIZE)
	algorithms.eaSimple(pop, toolbox, cxpb=CX_PROB, mutpb=MUT_PROB, ngen=NGEN, verbose=False)
	
	# Get best strategy
	best = tools.selBest(pop, k=1)[0]
	
	# Use best strategy to make decision
	return evaluate_strategy(best, opponent_history)
