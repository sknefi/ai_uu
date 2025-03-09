import numpy as np
import random as rd
import matplotlib.pyplot as plt
from graphic import *
from constants import *

def generate_agents(N):
	## generate 2D 20x20 grid with random agents 0 1 2 3 5
	## generate grid with 0 1 2
	agents = np.random.randint(0, 3, (N, N))
	return agents

def is_same_color(agent1, agent2):
    if agent1 in ORANGE:
        return agent2 in ORANGE
    elif agent1 in BLUE:
        return agent2 in BLUE
    else:
        return 0

def calc_rat(agents, x, y):
	# 1 2 3
	# 4 x 5
	# 6 7 8
	# calc ratio of neighbors with same color
	# formula: same_color_neighbors / all_neighbors
	rat = 0
	same_color_neighbors = 0
	all_neighbors = 0
	current_agent = agents[x, y]
	for i in range(x-RADIUS, x+RADIUS):
		i = i % N
		for j in range(y-RADIUS, y+RADIUS):
			j = j % N
			if i == x and j == y: # skip current agent
				continue
			if agents[i, j] != EMPTY: # skip empty cells
				all_neighbors += 1
				same_color_neighbors += is_same_color(agents[i, j], current_agent)
	if all_neighbors == 0:
		return 0
	rat = same_color_neighbors / all_neighbors
	return rat

def update_agents(agents):
    # agent is sad when rat < TOL
	# set agent happy or sad based on rat
	sad_agents = []
	null_agents = []
	for i in range(N):
		for j in range(N):
			current_agent = agents[i, j]
			if current_agent != EMPTY:
				if calc_rat(agents, i, j) < TOL:
					if current_agent in ORANGE:
						agents[i, j] = ORANGE_SAD
					else:
						agents[i, j] = BLUE_SAD
					sad_agents.append([i, j])
				else:
					if current_agent in ORANGE:
						agents[i, j] = ORANGE_HAPPY
					else:
						agents[i, j] = BLUE_HAPPY
			else:
				null_agents.append([i, j])
	return (agents, sad_agents, null_agents)


def make_everyone_happy(agents, sad_agents, null_agents):
	# choose random sad agent and move him to random null cell
	while (len(sad_agents) > 0 and len(null_agents) > 0):
		random_sad_agent = rd.choice(sad_agents)
		random_null_agent = rd.choice(null_agents)
		
		# move sad agent to random null cell
		agents[random_null_agent[0], random_null_agent[1]] = agents[random_sad_agent[0], random_sad_agent[1]]
		
		# Set the old position to empty
		agents[random_sad_agent[0], random_sad_agent[1]] = EMPTY
		
		# set all neighbors of sad agent to empty
		random_null_agent, random_sad_agent = random_sad_agent, random_null_agent
		for i in range(random_sad_agent[0] - RADIUS, random_sad_agent[0] + RADIUS):
			i = i % N
			for j in range(random_sad_agent[1] - RADIUS, random_sad_agent[1] + RADIUS):
				j = j % N
				if i == random_sad_agent[0] and j == random_sad_agent[1]:
					continue
				current_agent = agents[i, j]


		sad_agents.remove(random_sad_agent)
		null_agents.remove(random_null_agent)

	return agents