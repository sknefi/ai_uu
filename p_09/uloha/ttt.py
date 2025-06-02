import copy

Y = "\033[93m"
G = "\033[92m"
B = "\033[94m"
RED = "\033[91m"
R = "\033[0m"

# kreslí hru
def printgame(g):
	for r in g: 
		pr = ""
		for i in r:
			if i == 0:
				pr += "."
			elif i == 1:
				pr += "x"
			else:
				pr += "o"
		print(pr)
        

        
# říká kdo vyhrál 0=nikdo, 1, 2        
def whowon(g):

	# řádek
	if g[0][:] == [1, 1, 1] or g[1][:] == [1, 1, 1] or g[2][:] == [1, 1, 1]:
		return 1
			
	if g[0][:] == [2, 2, 2] or g[1][:] == [2, 2, 2] or g[2][:] == [2, 2, 2]:
		return 2

	# 1. sloupec
	if g[0][0] == g[1][0] == g[2][0] == 1:
		return 1

	if g[0][0] == g[1][0] == g[2][0] == 2:
		return 2

	# 2. sloupec
	if g[0][1] == g[1][1] == g[2][1] == 1:
		return 1

	if g[0][1] == g[1][1] == g[2][1] == 2:
		return 2


	# 3. sloupec
	if g[0][2] == g[1][2] == g[2][2] == 1:
		return 1

	if g[0][2] == g[1][2] == g[2][2] == 2:
		return 2


	# hlavní diagonála
	if g[0][0] == g[1][1] == g[2][2] == 1:
		return 1

	if g[0][0] == g[1][1] == g[2][2] == 2:
		return 2


	# hlavní anti-diagonála
	if g[0][2] == g[1][1] == g[2][0] == 1:
		return 1

	if g[0][2] == g[1][1] == g[2][0] == 2:
		return 2
		
	return 0
        
# vrací prázdná místa na šachovnici    
def emptyspots(g):
	emp = []
	for i in range(3):
		for j in range(3):
			if g[i][j] == 0:
				emp.append((i, j))
	return emp
    
def is_full(g):
	for i in range(3):
		for j in range(3):
			if g[i][j] == 0:
				return False
	return True

def winner(g):
	if whowon(g) == 1:
		print(f"\n{G}First player won{R}")
		return 1
	elif whowon(g) == 2:
		print(f"\n{G}Second player won{R}")
		return 2
	else:
		return 0

def ttt_move(game, myplayer, otherplayer):
	# Create a deep copy of the game to avoid modifying the original
	new_game = copy.deepcopy(game)

	# Get all empty spots
	empty = emptyspots(new_game)

	# If no empty spots, return the game as is
	if not empty:
		return new_game

	# Strategy 1: Check if we can win in one move
	for row, col in empty:
		# Try placing our piece
		new_game[row][col] = myplayer
		if whowon(new_game) == myplayer:
			return new_game  # We found a winning move
		# Undo the move
		new_game[row][col] = 0

	# Strategy 2: Check if we need to block opponent from winning
	for row, col in empty:
		# Try placing opponent's piece
		new_game[row][col] = otherplayer
		if whowon(new_game) == otherplayer:
			# Opponent would win, so we must block
			new_game[row][col] = myplayer
			return new_game
		# Undo the move
		new_game[row][col] = 0

	# Strategy 3: Make strategic moves
	# Priority order: center, corners, edges

	# Try center first
	if (1, 1) in empty:
		new_game[1][1] = myplayer
		return new_game

	# Try corners
	corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
	for corner in corners:
		if corner in empty:
			new_game[corner[0]][corner[1]] = myplayer
			return new_game

	# Try edges
	edges = [(0, 1), (1, 0), (1, 2), (2, 1)]
	for edge in edges:
		if edge in empty:
			new_game[edge[0]][edge[1]] = myplayer
			return new_game

	# Fallback: take the first available spot
	if empty:
		row, col = empty[0]
		new_game[row][col] = myplayer

	return new_game

def main():
	game = [[0, 0, 2], [0, 0, 2], [0, 0, 0]]
	itr = 1
	printgame(game)
	while not is_full(game):
		if winner(game):
			break
		print(f"\n{Y}Iteration {itr}{R}")
		print(f"\n{B}First player move{R}")
		
		# first player move
		game = ttt_move(game, 1, 2)
		printgame(game)
		print(f"\n{RED}Second player move{R}")
		
		# second player move
		game = ttt_move(game, 2, 1)
		printgame(game)
		
		itr += 1
if __name__ == "__main__":
    main()
