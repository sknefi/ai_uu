"""
Graph search algorithms for path planning.

This module contains implementations of:
- Greedy Best-First Search
- Dijkstra's Algorithm
- A* Algorithm
"""

from collections import deque
import heapq

def heuristic(x, y, goal_x, goal_y):
    """
    Calculate Manhattan distance heuristic between two points.
    
    Args:
        x, y: Coordinates of the current position
        goal_x, goal_y: Coordinates of the goal position
        
    Returns:
        Manhattan distance (sum of horizontal and vertical distances)
    """
    return abs(x - goal_x) + abs(y - goal_y)

def greedy_best_first_search(start_pos, goal_pos, get_neighbors_fn):
    """
    Greedy Best-First Search algorithm.
    
    Args:
        start_pos: Starting position as (x, y)
        goal_pos: Goal position as (x, y)
        get_neighbors_fn: Function that returns valid neighbors for a position
        
    Returns:
        Tuple of (path, expanded_nodes)
    """
    start_x, start_y = start_pos
    goal_x, goal_y = goal_pos
    
    # Initialize data structures
    expanded = []  # List to store expanded nodes
    came_from = {}  # Dictionary to store the path
    
    # Priority queue with (heuristic, (x, y))
    open_set = [(heuristic(start_x, start_y, goal_x, goal_y), (start_x, start_y))]
    
    while open_set:
        _, current = heapq.heappop(open_set)
        current_x, current_y = current
        
        # If we reached the goal
        if current_x == goal_x and current_y == goal_y:
            break
        
        # Add to expanded nodes
        if current not in expanded:
            expanded.append(current)
        
        # Check neighbors
        for neighbor in get_neighbors_fn(current_x, current_y):
            if neighbor not in came_from:
                came_from[neighbor] = current
                h = heuristic(neighbor[0], neighbor[1], goal_x, goal_y)
                heapq.heappush(open_set, (h, neighbor))
    
    # Reconstruct path
    path = reconstruct_path(came_from, start_pos, goal_pos)
    
    return path, expanded

def dijkstra(start_pos, goal_pos, get_neighbors_fn):
    """
    Dijkstra's Algorithm for path finding.
    
    Args:
        start_pos: Starting position as (x, y)
        goal_pos: Goal position as (x, y)
        get_neighbors_fn: Function that returns valid neighbors for a position
        
    Returns:
        Tuple of (path, expanded_nodes)
    """
    start_x, start_y = start_pos
    goal_x, goal_y = goal_pos
    
    # Initialize data structures
    expanded = []  # List to store expanded nodes
    came_from = {}  # Dictionary to store the path
    
    # Priority queue with (cost, (x, y))
    open_set = [(0, (start_x, start_y))]
    cost_so_far = {(start_x, start_y): 0}
    
    while open_set:
        _, current = heapq.heappop(open_set)
        current_x, current_y = current
        
        # If we reached the goal
        if current_x == goal_x and current_y == goal_y:
            break
        
        # Add to expanded nodes
        if current not in expanded:
            expanded.append(current)
        
        # Check neighbors
        for neighbor in get_neighbors_fn(current_x, current_y):
            new_cost = cost_so_far[current] + 1  # Cost is 1 for each step
            
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                came_from[neighbor] = current
                heapq.heappush(open_set, (new_cost, neighbor))
    
    # Reconstruct path
    path = reconstruct_path(came_from, start_pos, goal_pos)
    
    return path, expanded

def astar(start_pos, goal_pos, get_neighbors_fn):
    """
    A* Algorithm for path finding.
    
    Args:
        start_pos: Starting position as (x, y)
        goal_pos: Goal position as (x, y)
        get_neighbors_fn: Function that returns valid neighbors for a position
        
    Returns:
        Tuple of (path, expanded_nodes)
    """
    start_x, start_y = start_pos
    goal_x, goal_y = goal_pos
    
    # Initialize data structures
    expanded = []  # List to store expanded nodes
    came_from = {}  # Dictionary to store the path
    
    # Priority queue with (f_score, (x, y))
    open_set = [(heuristic(start_x, start_y, goal_x, goal_y), (start_x, start_y))]
    cost_so_far = {(start_x, start_y): 0}
    
    while open_set:
        _, current = heapq.heappop(open_set)
        current_x, current_y = current
        
        # If we reached the goal
        if current_x == goal_x and current_y == goal_y:
            break
        
        # Add to expanded nodes
        if current not in expanded:
            expanded.append(current)
        
        # Check neighbors
        for neighbor in get_neighbors_fn(current_x, current_y):
            new_cost = cost_so_far[current] + 1  # Cost is 1 for each step
            
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                came_from[neighbor] = current
                f_score = new_cost + heuristic(neighbor[0], neighbor[1], goal_x, goal_y)
                heapq.heappush(open_set, (f_score, neighbor))
    
    # Reconstruct path
    path = reconstruct_path(came_from, start_pos, goal_pos)
    
    return path, expanded

def reconstruct_path(came_from, start_pos, goal_pos):
    """
    Reconstruct the path from start to goal using the came_from dictionary.
    
    Args:
        came_from: Dictionary mapping positions to their predecessors
        start_pos: Starting position as (x, y)
        goal_pos: Goal position as (x, y)
        
    Returns:
        Deque containing the path from start to goal
    """
    path = deque()
    current = goal_pos
    
    # Check if a path was found
    if current not in came_from and goal_pos != start_pos:
        return path
    
    # Reconstruct path from goal to start
    while current != start_pos:
        path.appendleft(current)
        current = came_from.get(current, start_pos)
    
    # Add start position
    path.appendleft(start_pos)
    
    return path 