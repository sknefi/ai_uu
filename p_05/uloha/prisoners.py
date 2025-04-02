import random
from deap import base, creator, tools, algorithms
from constants import * 

def fk_solution(my_history, opponent_history):
	BETRAY_ROUND = 8 # Each 8th round betray
 
 	# Start with cooperation
	if not opponent_history:
		return 0
		
	# Betray on specific rounds
	if (len(my_history) + 1) % BETRAY_ROUND == 0:
		return 1
		
	# Count opponent's last 3 moves
	last_moves = opponent_history[-3:] if len(opponent_history) >= 3 else opponent_history
	betray_count = last_moves.count(1)
	
	# If opponent betrayed in majority of last moves, betray
	if betray_count >= len(last_moves) / 2:
		return 1
		
	# If opponent cooperated in majority, cooperate
	return 0

def sneaky_bastard(my_history, opponent_history):
	rounds = len(my_history) + 1

	if not opponent_history:
		return 0

	# Betray on specific rounds
	if rounds % BETRAY_ROUND == 0:
		return 1

	# Occasionally cooperate when opponent betrays
	if opponent_history[-1] == 1:
		if random.random() < 0.1:
			return 0

	return opponent_history[-1]

def random_strategy(my_history, opponent_history):
	# Randomly choose between cooperation (0) and betrayal (1)
	return random.choice([0, 1])

def tit_for_tat(my_history, opponent_history):
	# Start with cooperation
	if not opponent_history:
		return 0

	# Copy opponent's last move
	return opponent_history[-1]

def pavlov(my_history, opponent_history):
	# Start with cooperation
	if not opponent_history:
		return 0
	# If both players made the same move, repeat it
	if my_history[-1] == opponent_history[-1]:
		return my_history[-1]
	# Otherwise, change the move
	else:
		return 1 - my_history[-1]

def adaptive(my_history, opponent_history, cooperation_threshold=0.5):
	# Start with cooperation
	if not opponent_history:
		return 0
	# Calculate opponent's cooperation rate
	cooperation_rate = opponent_history.count(0) / len(opponent_history)
	# Cooperate if opponent cooperates frequently
	if cooperation_rate > cooperation_threshold:
		return 0
	# Betray if opponent betrays frequently
	else:
		return 1

