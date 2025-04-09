import random
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

