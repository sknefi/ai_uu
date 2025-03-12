import numpy as np
import random as rd
from graphic import *
from constants import *

def generate_agents(N):
	## generate 2D NxN grid with random agents 0 1 2 3 4
 
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
	# calc ratio of neighbors with same color
	# formula: same_color_neighbors / all_neighbors
	same_color_neighbors = 0
	all_neighbors = 0
	current_agent = agents[x, y]

	# Check all neighbors in the radius
	for i in range(x-RADIUS, x+RADIUS+1):
		i = i % N
		for j in range(y-RADIUS, y+RADIUS+1):
			j = j % N
			if i == x and j == y:  # skip current agent
				continue
			if agents[i, j] != EMPTY:  # skip empty cells
				all_neighbors += 1
				if is_same_color(agents[i, j], current_agent):
					same_color_neighbors += 1

	if all_neighbors == 0:
		return 0

	return same_color_neighbors / all_neighbors

def update_agents(agents): # tento nazov je kktsky prepisat
    # agent is sad when rat < TOL
	# set agent happy or sad based on rat
	null_agents = []
	sad_agents = []
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

def change_agent_mood(agents, agent, sad_agents):
	x, y = agent
	if agents[x, y] != EMPTY:
		rat = calc_rat(agents, x, y)
		if rat < TOL:
			if agents[x, y] in ORANGE:
				agents[x, y] = ORANGE_SAD
			else:
				agents[x, y] = BLUE_SAD
			if [x, y] not in sad_agents:
				sad_agents.append([x, y])
		else:
			if agents[x, y] in ORANGE:
				agents[x, y] = ORANGE_HAPPY
			else:
				agents[x, y] = BLUE_HAPPY
			if [x, y] in sad_agents:
				sad_agents.remove([x, y])

def update_one_agent(agents, agent, sad_agents):
	x, y = agent
 
	# First check the agent at the position itself
	change_agent_mood(agents, agent, sad_agents)

	# Check all neighbors and based on their color change the mood of the agent
	for i in range(x-RADIUS, x+RADIUS+1):
		i = i % N
		for j in range(y-RADIUS, y+RADIUS+1):
			j = j % N
			if i == x and j == y:  # skip center agent
				continue
			change_agent_mood(agents, [i, j], sad_agents)
	return agents

def update_agents_in_radius(agents, sad_agents, x, y):
	for i in range(x-RADIUS, x+RADIUS+1):
		i = i % N
		for j in range(y-RADIUS, y+RADIUS+1):
			j = j % N
			if agents[i, j] != EMPTY:
				update_one_agent(agents, [i, j], sad_agents)
	return agents

def make_everyone_happy(agents, sad_agents, null_agents):
	# Choose random sad agent and move him to random null cell
	num_happy_agents = []
	while (len(sad_agents) > 0 and len(null_agents) > 0):
		random_sad_agent = rd.choice(sad_agents)
		random_null_agent = rd.choice(null_agents)
		
		# Move sad agent to random null cell
		agents[random_null_agent[0], random_null_agent[1]] = agents[random_sad_agent[0], random_sad_agent[1]]
		
		# Set the old sad agent position to empty
		agents[random_sad_agent[0], random_sad_agent[1]] = EMPTY
		null_agents.append(random_sad_agent)

		# update agents in radius of the random sad agent and the random null agent
		update_agents_in_radius(agents, sad_agents, random_sad_agent[0], random_sad_agent[1])
		update_agents_in_radius(agents, sad_agents, random_null_agent[0], random_null_agent[1])
		
		# Remove the random sad agent and null agent from the lists
		null_agents.remove(random_null_agent)
		sad_agents.remove(random_sad_agent)
  
		# Keep track of the number of happy agents for graph
		num_happy_agents.append(NUMBER_OF_AGENTS - len(sad_agents) - len(null_agents))
  
		print(len(sad_agents))
  
	return agents, num_happy_agents
