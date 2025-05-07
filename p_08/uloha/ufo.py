from collections import deque
import random

# Class representing the UFO
class Ufo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.path = deque()
        self.tiles = []
    
    # Moves the UFO to the given position - it's good to check with the environment first
    # whether the position is valid
    def move(self, x, y):
        self.x = x
        self.y = y
   
    # Reactive navigation <------------------------ !!!!!!!!!!!! TO BE IMPLEMENTED
    def reactive_go(self, env):
        r = random.random()
        
        dx = 0
        dy = 0
        
        if r > 0.5: 
            r = random.random()
            if r < 0.5:
                dx = -1
            else:
                dx = 1
            
        else:
            r = random.random()
            if r < 0.5:
                dy = -1
            else:
                dy = 1
        
        return (self.x + dx, self.y + dy)
    
    # Sets the path to execute
    def set_path(self, p, t=[]):
        self.path = p
        self.tiles = t
   
    # Executes the planned path, at each moment when called, returns the next
    # waypoint
    def execute_path(self):
        if self.path:
            return self.path.popleft()
        return (-1, -1) 