import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# display two grids side by side
def display_grid(agents, updated_agents):
	cmap = mcolors.ListedColormap(['white', 'orange', 'blue', 'darkorange', 'darkblue'])
	bounds = [0, 1, 2, 3, 4, 5]
	norm = mcolors.BoundaryNorm(bounds, cmap.N)
	# display two grids side by side
	fig, axs = plt.subplots(1, 2, figsize=(10, 5))
	axs[0].imshow(agents, cmap=cmap, norm=norm)
	axs[1].imshow(updated_agents, cmap=cmap, norm=norm)
	plt.show()
