from schelling import *

if __name__ == "__main__":
	grid = generate_agents(N)
	
	# calc EMPTY cells
	empty_cells1 = np.where(grid == EMPTY)
	empty_cells1 = list(zip(empty_cells1[0], empty_cells1[1]))
 
	updated_grid = grid.copy()
	updated_grid, sad_agents, null_agents = update_agents(updated_grid)
 
	happy_grid = updated_grid.copy()
	happy_grid = make_everyone_happy(happy_grid, sad_agents, null_agents)
 
	display_grid(updated_grid, happy_grid)

 	# calc empty cells
	empty_cells = np.where(happy_grid == EMPTY)
	empty_cells = list(zip(empty_cells[0], empty_cells[1]))
	happy_grid[empty_cells] = EMPTY
 
	print("empty cells: ", len(empty_cells1), " === ", len(empty_cells))