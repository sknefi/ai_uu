import pygame
from constants import (
    TILE, MTILE, HOUSE1, HOUSE2, HOUSE3, 
    TREE1, TREE2, FLAG, UFO, TILESIZE
)

# Initialize the pygame window
def init_window(width, height, tilesize):
    win = pygame.display.set_mode((width * tilesize, height * tilesize))
    pygame.display.set_caption("Block world")
    return win

# Draw the game window
def draw_window(win, ufo, env):
    for i in range(env.width):
        for j in range(env.height):
            t = env.get_tile_type(i, j)
            if t == 1:
                win.blit(TREE1, (i*TILESIZE, j*TILESIZE))
            elif t == 2:
                win.blit(HOUSE1, (i*TILESIZE, j*TILESIZE))
            elif t == 3:
                win.blit(HOUSE2, (i*TILESIZE, j*TILESIZE))
            elif t == 4:
                win.blit(HOUSE3, (i*TILESIZE, j*TILESIZE))  
            elif t == 5:
                win.blit(TREE2, (i*TILESIZE, j*TILESIZE))     
            else:
                win.blit(TILE, (i*TILESIZE, j*TILESIZE))
    
    for (x, y) in ufo.tiles:
        win.blit(MTILE, (x*TILESIZE, y*TILESIZE))
    
    win.blit(FLAG, (env.goalx * TILESIZE, env.goaly * TILESIZE))        
    win.blit(UFO, (ufo.x * TILESIZE, ufo.y * TILESIZE))
        
    pygame.display.update() 