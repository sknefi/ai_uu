from constants import *
import random
import pygame

# trida reprezentujici minu
class Mine:
    def __init__(self):

        # random x direction
        if random.random() > 0.5:
            self.dirx = 1
        else: 
            self.dirx = -1
            
        # random y direction    
        if random.random() > 0.5:
            self.diry = 1
        else: 
            self.diry = -1

        x = random.randint(200, WIDTH - ENEMY_SIZE) 
        y = random.randint(200, HEIGHT - ENEMY_SIZE) 
        self.rect = pygame.Rect(x, y, ENEMY_SIZE, ENEMY_SIZE)
        
        self.velocity = random.randint(1, MAX_MINE_VELOCITY)
        
  
    
  
# trida reprezentujici me, tedy meho agenta        
class Me:
    def __init__(self):
        self.rect = pygame.Rect(10, random.randint(1, 300), ME_SIZE, ME_SIZE)  
        self.alive = True
        self.won = False
        self.timealive = 0
        self.sequence = []
        self.fitness = 0
        self.dist = 0
    
    
# třída reprezentující cíl = praporek    
class Flag:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH - ME_SIZE, HEIGHT - ME_SIZE - 10, ME_SIZE, ME_SIZE)
        

# třída reprezentující nejlepšího jedince - hall of fame   
class Hof:
    def __init__(self):
        self.sequence = []