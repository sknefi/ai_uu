# HEADER FILE FOR CONSTANTS

N = 100
TOL = .5
RADIUS = 1 # radius of the neighborhood
NUMBER_OF_AGENTS = N*N	# n*n torus grid

EMPTY = 0
ORANGE_SAD = 1
BLUE_SAD = 2
ORANGE_HAPPY = 3
BLUE_HAPPY = 4

ORANGE = [ORANGE_SAD, ORANGE_HAPPY]
BLUE = [BLUE_SAD, BLUE_HAPPY]

HAPPY = [ORANGE_HAPPY, BLUE_HAPPY]
SAD = [ORANGE_SAD, BLUE_SAD]