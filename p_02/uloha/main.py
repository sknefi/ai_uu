from schelling import *

if __name__ == "__main__":
	grid = generate_agents(N)
	
	updated_grid = grid.copy()
	updated_grid, sad_agents, null_agents = update_agents(updated_grid)
 
	happy_grid = updated_grid.copy()
	happy_grid, num_happy_agents = make_everyone_happy(happy_grid, sad_agents, null_agents)
 
	display_grid(grid, updated_grid, happy_grid, num_happy_agents)
