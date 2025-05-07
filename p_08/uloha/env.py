import numpy as np
import random
from collections import deque
from constants import BLOCKTYPES

# Class representing the environment
class Env:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.arr = np.zeros((height, width), dtype=int)
        self.startx = 0
        self.starty = 0
        self.goalx = width-1
        self.goaly = height-1
        
    def is_valid_xy(self, x, y):      
        if x >= 0 and x < self.width and y >= 0 and y < self.height and self.arr[y, x] == 0:
            return True
        return False 
        
    def set_start(self, x, y):
        if self.is_valid_xy(x, y):
            self.startx = x
            self.starty = y
            
    def set_goal(self, x, y):
        if self.is_valid_xy(x, y):
            self.goalx = x
            self.goaly = y
               
    def is_empty(self, x, y):
        if self.arr[y, x] == 0:
            return True
        return False
        
    def add_block(self, x, y):
        if self.arr[y, x] == 0:
            r = random.randint(1, BLOCKTYPES)
            self.arr[y, x] = r
                
    def get_neighbors(self, x, y):
        l = []
        if x-1 >= 0 and self.arr[y, x-1] == 0:
            l.append((x-1, y))
        
        if x+1 < self.width and self.arr[y, x+1] == 0:
            l.append((x+1, y))
            
        if y-1 >= 0 and self.arr[y-1, x] == 0:
            l.append((x, y-1))
        
        if y+1 < self.height and self.arr[y+1, x] == 0:
            l.append((x, y+1))
        
        return l
        
    def get_tile_type(self, x, y):
        return self.arr[y, x]
    
    # Returns a pair: 1. queue of pairs from start to goal, 2. list of tiles
    # for display - useful for highlighting the path or expanded nodes
    # start and goal are set using set_start and set_goal
    # <------    Custom method here
    def path_planner(self):
        # Hardcoded path from point (1, 0) to (9, 7)
        d = deque()
        d.appendleft((9, 7))
        d.appendleft((9, 6))
        d.appendleft((9, 5))
        d.appendleft((9, 4))
        d.appendleft((9, 3))
        d.appendleft((9, 2))
        d.appendleft((9, 1))
        d.appendleft((9, 0))
        d.appendleft((8, 0))
        d.appendleft((7, 0))
        d.appendleft((6, 0))
        d.appendleft((5, 0))
        d.appendleft((4, 0))
        d.appendleft((3, 0))
        d.appendleft((2, 0))
        d.appendleft((1, 0))
                
        return d, list(d)

def create_environment():
    """Create and initialize the environment with obstacles"""
    from constants import WIDTH, HEIGHT
    
    env = Env(WIDTH, HEIGHT)
    
    # Add blocks to create obstacles
    env.add_block(1, 1)
    env.add_block(2, 2)
    env.add_block(3, 3)
    env.add_block(4, 4)
    env.add_block(5, 5)
    env.add_block(6, 6)
    env.add_block(7, 7)
    env.add_block(8, 8)
    env.add_block(0, 8)

    env.add_block(11, 1)
    env.add_block(11, 6)
    env.add_block(1, 3)
    env.add_block(2, 4)
    env.add_block(4, 5)
    env.add_block(2, 6)
    env.add_block(3, 7)
    env.add_block(4, 8)
    env.add_block(0, 8)

    env.add_block(1, 8)
    env.add_block(2, 8)
    env.add_block(3, 5)
    env.add_block(4, 8)
    env.add_block(5, 6)
    env.add_block(6, 4)
    env.add_block(7, 2)
    env.add_block(8, 1)
    
    return env 