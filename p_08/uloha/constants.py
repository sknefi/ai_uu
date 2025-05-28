import pygame
from colors import Colors
# Environment constants
WIDTH = 12
HEIGHT = 9
TILESIZE = 80
BLOCKTYPES = 5
FPS = 10

# Colors
WHITE = (255, 255, 255)

# Initialize pygame font
pygame.font.init()

# Algorithm colors
ALGO_COLORS = {
    "greedy": Colors.YELLOW,
    "dijkstra": Colors.CYAN,
    "astar": Colors.GREEN
}

# Fonts
BOOM_FONT = pygame.font.SysFont("comicsans", 100)
LEVEL_FONT = pygame.font.SysFont("comicsans", 20)

# Load images
TILE_IMAGE = pygame.image.load("./imgs/tile.jpg")
MTILE_IMAGE = pygame.image.load("./imgs/markedtile.jpg")
HOUSE1_IMAGE = pygame.image.load("./imgs/house1.jpg")
HOUSE2_IMAGE = pygame.image.load("./imgs/house2.jpg")
HOUSE3_IMAGE = pygame.image.load("./imgs/house3.jpg")
TREE1_IMAGE = pygame.image.load("./imgs/tree1.jpg")
TREE2_IMAGE = pygame.image.load("./imgs/tree2.jpg")
UFO_IMAGE = pygame.image.load("./imgs/ufo.jpg")
FLAG_IMAGE = pygame.image.load("./imgs/flag.jpg")

# Scale images
TILE = pygame.transform.scale(TILE_IMAGE, (TILESIZE, TILESIZE))
MTILE = pygame.transform.scale(MTILE_IMAGE, (TILESIZE, TILESIZE))
HOUSE1 = pygame.transform.scale(HOUSE1_IMAGE, (TILESIZE, TILESIZE))
HOUSE2 = pygame.transform.scale(HOUSE2_IMAGE, (TILESIZE, TILESIZE))
HOUSE3 = pygame.transform.scale(HOUSE3_IMAGE, (TILESIZE, TILESIZE))
TREE1 = pygame.transform.scale(TREE1_IMAGE, (TILESIZE, TILESIZE))
TREE2 = pygame.transform.scale(TREE2_IMAGE, (TILESIZE, TILESIZE))
UFO = pygame.transform.scale(UFO_IMAGE, (TILESIZE, TILESIZE))
FLAG = pygame.transform.scale(FLAG_IMAGE, (TILESIZE, TILESIZE)) 