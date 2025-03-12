import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from constants import *

# display 4 grids side by side
def display_grid(initial_agents, updated_agents, happy_agents, num_happy_agents):
	#cmap = mcolors.ListedColormap(['white', 'orange', 'blue', 'darkorange', 'darkblue'])
	cmap = mcolors.ListedColormap(['white', 'yellow', 'green', 'darkorange', 'darkblue'])
	bounds = [0, 1, 2, 3, 4, 5]
	norm = mcolors.BoundaryNorm(bounds, cmap.N)
	
	# display grids and graph side by side
	fig, axs = plt.subplots(1, 4, figsize=(20, 5))
	
	# Display initial grid
	axs[0].imshow(initial_agents, cmap=cmap, norm=norm)
	axs[0].set_title('Initial State')
	
	# Display updated grid
	axs[1].imshow(updated_agents, cmap=cmap, norm=norm)
	axs[1].set_title('Realization of agents neighborhood')
	
	# Display happy grid
	axs[2].imshow(happy_agents, cmap=cmap, norm=norm)
	axs[2].set_title('Happy State')
	
	# Display graph of happy agents over time
	axs[3].plot(range(len(num_happy_agents)), num_happy_agents)
	axs[3].set_title('Happy Agents Over Time')
	axs[3].set_xlabel('Iterations')
	axs[3].set_ylabel('Number of Happy Agents')
	axs[3].grid(True)
	
	plt.tight_layout()
	plt.show()
