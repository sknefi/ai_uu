# Game of Life - 1D

DEL = "  "
DEAD = "*"
ALIVE = "~"

RED = "\033[1;31m"
BLUE = "\033[1;34m"

# pretty print the row
def pretty_print(row):
	for x in row:
		if x == ALIVE:
			print(RED + ALIVE, end=DEL)
		else:
			print(BLUE + DEAD, end=DEL)
	print()

# neigbours are **i** 
# handling overflow by using modulo - circular array
def nu_alive_cells(row, i):
	sum_of_neighbours = 0

	for x in range(i-2, i+3):
		if x == i:		# skip the cell itself
			continue	# COMMENT THIS PART FOR DIFFERENT PATTERN
		i_modulo = x % len(row)
		if (row[i_modulo] == ALIVE):
			sum_of_neighbours += 1
	return sum_of_neighbours

# neigbours are **i**
# doesnt handle overflow, checks only the valid indexes
def nu_alive_cells_v2(row, i):
	sum_of_neighbours = 0

	for x in range(i-2, i+3):
		if x == i:		# skip the cell itself
			continue	# COMMENT THIS PART FOR DIFFERENT PATTERN
		if 0 <= x and x < len(row):
			if (row[x] == ALIVE):
				sum_of_neighbours += 1
	return sum_of_neighbours


# if number of neigbours is 2 or 4 then cell survives
# if number of neigbours is 2 or 3 then cell is born	
def step(row, itr):
	row_new = row.copy()
	
	pretty_print(row) 
	if itr == 0:
		return
	for i in range(len(row)):
		nu_neighbours = nu_alive_cells_v2(row, i)
		if row[i] == ALIVE:
			if nu_neighbours == 2 or nu_neighbours == 4:
				row_new[i] = ALIVE
			else:
				row_new[i] = DEAD
		else: # DEAD
			if nu_neighbours == 2 or nu_neighbours == 3:
				row_new[i] = ALIVE
			else:
				row_new[i] = DEAD
	step(row_new, itr-1)

def main():
	test_cases = [
		 [DEAD, ALIVE, DEAD, ALIVE, ALIVE, DEAD, DEAD, DEAD, DEAD, DEAD, ALIVE, ALIVE, DEAD, ALIVE, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
		 [DEAD, ALIVE, DEAD, ALIVE, ALIVE, DEAD, DEAD, DEAD, DEAD, DEAD, ALIVE, ALIVE, DEAD, ALIVE, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
		 [ALIVE, ALIVE, DEAD, ALIVE, ALIVE, DEAD, DEAD, DEAD, DEAD, DEAD, ALIVE, ALIVE, DEAD, ALIVE, DEAD, DEAD, DEAD, DEAD, DEAD, DEAD],
		 [ALIVE, DEAD, ALIVE, DEAD, ALIVE],
		 [ALIVE, DEAD, ALIVE, DEAD, DEAD],
		 [ALIVE, ALIVE, DEAD, DEAD],
		[DEAD, ALIVE, DEAD, ALIVE, ALIVE, DEAD, DEAD, DEAD, ALIVE, DEAD, DEAD],
		[DEAD, ALIVE, DEAD, ALIVE, ALIVE, DEAD, DEAD, ALIVE]
	]

	for arr in test_cases:
		print("Initial State")
		step(arr, 20)
 
if __name__ == "__main__":
	main()