import numpy as np
import random
from collections import deque
import heapq
from constants import BLOCKTYPES
from graph_algorithms import *

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
    
    def clear(self):
        """Clear all blocks from the environment"""
        self.arr = np.zeros((self.height, self.width), dtype=int)
                
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
    def path_planner(self, algorithm="astar"):
        """
        Find a path from start to goal using the specified algorithm
        
        Parameters:
        - algorithm: String, one of "greedy", "dijkstra", or "astar"
        
        Returns:
        - path: deque of coordinates from start to goal
        - expanded: list of expanded nodes for visualization
        """
        start_pos = (self.startx, self.starty)
        goal_pos = (self.goalx, self.goaly)
        
        # Check if start and goal are valid
        if not self.is_valid_xy(self.startx, self.starty) or not self.is_valid_xy(self.goalx, self.goaly):
            return deque(), []
        
        # Use the appropriate algorithm from graph_algorithms module
        if algorithm == "greedy":
            return greedy_best_first_search(start_pos, goal_pos, self.get_neighbors)
        elif algorithm == "dijkstra":
            return dijkstra(start_pos, goal_pos, self.get_neighbors)
        else:  # Default to A*
            return astar(start_pos, goal_pos, self.get_neighbors)

def create_environment(map_index=0):
    """
    Create and initialize the environment with obstacles based on the map index
    
    Parameters:
    - map_index: Integer indicating which map to create (0-8)
    
    Returns:
    - env: Initialized environment with obstacles
    """
    from constants import WIDTH, HEIGHT
    
    env = Env(WIDTH, HEIGHT)
    
    # Map 0: Diagonal obstacles with some gaps
    if map_index == 0:
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
        
        # Default start and goal
        env.set_start(0, 0)
        env.set_goal(9, 7)
    
    # Map 1: Maze-like environment with narrow passages
    elif map_index == 1:
        # Create vertical walls with gaps
        for y in range(1, HEIGHT-1):
            if y != 2 and y != 6:
                env.add_block(3, y)
            
            if y != 4:
                env.add_block(6, y)
            
            if y != 1 and y != 7:
                env.add_block(9, y)
        
        # Create horizontal walls with gaps
        for x in range(1, WIDTH-1):
            if x != 2 and x != 7 and x != 10:
                env.add_block(x, 2)
            
            if x != 4 and x != 8:
                env.add_block(x, 5)
        
        # Add some random obstacles
        env.add_block(1, 1)
        env.add_block(2, 7)
        env.add_block(5, 3)
        env.add_block(8, 7)
        env.add_block(10, 3)
        
        # Set start and goal
        env.set_start(0, 0)
        env.set_goal(11, 8)
    
    # Map 2: Open center with obstacles around the edges
    elif map_index == 2:
        # Top and bottom walls with gaps
        for x in range(WIDTH):
            if x != 2 and x != 9:
                env.add_block(x, 1)
            if x != 3 and x != 8:
                env.add_block(x, HEIGHT-2)
        
        # Left and right walls with gaps
        for y in range(HEIGHT):
            if y != 2 and y != 7:
                env.add_block(1, y)
            if y != 3 and y != 6:
                env.add_block(WIDTH-2, y)
        
        # Some obstacles in the middle
        env.add_block(5, 4)
        env.add_block(6, 4)
        env.add_block(6, 5)
        
        # Set start and goal on opposite corners
        env.set_start(0, 0)
        env.set_goal(WIDTH-1, HEIGHT-1)
    
    # Map 3: Random obstacles
    elif map_index == 3:
        # Set a random seed for reproducibility
        random.seed(42)
        
        # Add random obstacles (about 30% of the grid)
        obstacle_count = int(WIDTH * HEIGHT * 0.3)
        for _ in range(obstacle_count):
            x = random.randint(0, WIDTH-1)
            y = random.randint(0, HEIGHT-1)
            # Don't block start and goal positions
            if (x, y) != (0, 0) and (x, y) != (WIDTH-1, HEIGHT-1):
                env.add_block(x, y)
        
        # Set start and goal
        env.set_start(0, 0)
        env.set_goal(WIDTH-1, HEIGHT-1)
    
    # Map 4: Spiral obstacle pattern
    elif map_index == 4:
        # Create a spiral pattern of obstacles
        # Start from outside and work inward
        
        # Top edge (right to left)
        for x in range(WIDTH-2, 2, -1):
            env.add_block(x, 1)
        
        # Left edge (top to bottom)
        for y in range(1, HEIGHT-2):
            env.add_block(2, y)
        
        # Bottom edge (left to right)
        for x in range(2, WIDTH-3):
            env.add_block(x, HEIGHT-2)
        
        # Right edge (bottom to top)
        for y in range(HEIGHT-2, 2, -1):
            env.add_block(WIDTH-3, y)
        
        # Inner spiral (continue pattern)
        for x in range(WIDTH-4, 4, -1):
            env.add_block(x, 3)
        
        for y in range(3, HEIGHT-3):
            env.add_block(4, y)
        
        # Set start and goal
        env.set_start(0, 0)
        env.set_goal(WIDTH-1, HEIGHT-1)
    
    # Map 5: Checkerboard pattern
    elif map_index == 5:
        # Create a checkerboard pattern of obstacles
        for x in range(WIDTH):
            for y in range(HEIGHT):
                if (x + y) % 2 == 0 and (x, y) != (0, 0) and (x, y) != (WIDTH-1, HEIGHT-1):
                    # Skip the start and goal positions
                    env.add_block(x, y)
        
        # Set start and goal on opposite corners
        env.set_start(0, 0)
        env.set_goal(WIDTH-1, HEIGHT-1)
    
    # Map 6: Central obstacle with narrow passages
    elif map_index == 6:
        # Create a large central obstacle with narrow passages
        center_x = WIDTH // 2
        center_y = HEIGHT // 2
        
        # Create a large rectangle in the center
        for x in range(center_x - 3, center_x + 3):
            for y in range(center_y - 2, center_y + 2):
                env.add_block(x, y)
        
        # Create narrow passages
        env.arr[center_y, center_x - 3] = 0  # Left passage
        env.arr[center_y, center_x + 2] = 0  # Right passage
        
        # Add some obstacles near the corners
        env.add_block(1, 1)
        env.add_block(2, 2)
        env.add_block(WIDTH-2, 1)
        env.add_block(WIDTH-3, 2)
        env.add_block(1, HEIGHT-2)
        env.add_block(2, HEIGHT-3)
        env.add_block(WIDTH-2, HEIGHT-2)
        env.add_block(WIDTH-3, HEIGHT-3)
        
        # Set start and goal on opposite corners
        env.set_start(0, 0)
        env.set_goal(WIDTH-1, HEIGHT-1)
    
    # Map 7: Multiple rooms with doorways
    elif map_index == 7:
        # Create vertical walls dividing the space into rooms
        for y in range(HEIGHT):
            if y != 2:  # Door in the first wall
                env.add_block(3, y)
            
            if y != HEIGHT-3:  # Door in the second wall
                env.add_block(7, y)
        
        # Create horizontal walls
        for x in range(WIDTH):
            if x < 3 or x > 7:  # Skip the middle section
                if x != 1:  # Door in the first section
                    env.add_block(x, 3)
                
                if x != WIDTH-2:  # Door in the last section
                    env.add_block(x, HEIGHT-4)
        
        # Set start and goal
        env.set_start(0, 0)
        env.set_goal(WIDTH-1, HEIGHT-1)
    
    # Map 8: Concentric obstacles
    elif map_index == 8:
        # Create concentric rectangles of obstacles
        
        # Outer rectangle
        for x in range(1, WIDTH-1):
            env.add_block(x, 1)
            env.add_block(x, HEIGHT-2)
        
        for y in range(1, HEIGHT-1):
            env.add_block(1, y)
            env.add_block(WIDTH-2, y)
        
        # Inner rectangle
        for x in range(3, WIDTH-3):
            env.add_block(x, 3)
            env.add_block(x, HEIGHT-4)
        
        for y in range(3, HEIGHT-3):
            env.add_block(3, y)
            env.add_block(WIDTH-4, y)
        
        # Create openings
        env.arr[1, 1] = 0  # Outer top-left
        env.arr[HEIGHT-2, WIDTH-2] = 0  # Outer bottom-right
        env.arr[3, 4] = 0  # Inner top
        env.arr[HEIGHT-4, WIDTH-5] = 0  # Inner bottom
        
        # Set start and goal
        env.set_start(0, 0)
        env.set_goal(WIDTH-1, HEIGHT-1)
    
    return env 