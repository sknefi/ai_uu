"""
Graph search algorithms for path planning.

This module contains implementations of:
- Greedy Best-First Search
- Dijkstra's Algorithm
- A* Algorithm

=== ALGORITHM EXPLANATIONS ===

1. GREEDY BEST-FIRST SEARCH
--------------------------
Description:
    Greedy Best-First Search is a search algorithm that expands the node that appears closest to the goal according
    to a heuristic function. It always chooses the path that seems most promising at the moment.

How it works:
    1. Maintain a priority queue of nodes to visit (open set)
    2. Always select the node with the lowest heuristic value (estimated distance to goal)
    3. Expand this node by generating all its neighbors
    4. For each neighbor, calculate its heuristic value and add to the open set
    5. Continue until the goal is reached or the open set is empty

Advantages:
    - Very fast when the heuristic is accurate
    - Uses less memory than other algorithms because it doesn't track path costs
    - Often finds a solution quickly in simple environments

Disadvantages:
    - Does NOT guarantee the shortest path
    - Can get stuck in loops or suboptimal paths
    - Completely ignores the cost of the path taken so far

Visualization:
    Greedy search expands nodes in a direct line toward the goal, ignoring other potentially
    shorter paths. You'll see fewer expanded nodes compared to Dijkstra, but the final path
    may not be optimal.

2. DIJKSTRA'S ALGORITHM
---------------------
Description:
    Dijkstra's Algorithm is a classic graph search algorithm that finds the shortest path from a starting
    node to all other nodes in a weighted graph. In pathfinding, we typically stop once we reach the goal.

How it works:
    1. Maintain a priority queue of nodes to visit (open set), prioritized by total path cost
    2. Always select the node with the lowest total path cost so far
    3. Expand this node by generating all its neighbors
    4. For each neighbor, calculate the cost to reach it via the current node
    5. If this is a new node or the new cost is lower than previously found, update the cost
    6. Continue until the goal is reached or the open set is empty

Advantages:
    - Guarantees the shortest path
    - Works well in any graph with non-negative edge weights
    - Explores all possible paths systematically

Disadvantages:
    - Much slower than informed search algorithms
    - Expands nodes in all directions equally, including directions away from the goal
    - Requires more memory than greedy search

Visualization:
    Dijkstra's algorithm expands nodes in concentric "waves" outward from the start, exploring
    in all directions equally. You'll see many more expanded nodes than with other algorithms,
    but the final path will always be the shortest one.

3. A* ALGORITHM
------------
Description:
    A* (A-star) is an informed search algorithm that combines the advantages of Dijkstra's Algorithm
    and Greedy Best-First Search. It uses both the cost of the path so far and a heuristic estimate
    of the distance to the goal.

How it works:
    1. Maintain a priority queue of nodes to visit (open set)
    2. Prioritize nodes by f(n) = g(n) + h(n), where:
       - g(n) is the cost of the path from start to node n
       - h(n) is the heuristic estimate of the distance from n to the goal
    3. Always select the node with the lowest f(n) value
    4. Expand this node by generating all its neighbors
    5. For each neighbor, calculate its g and f values and add to the open set if beneficial
    6. Continue until the goal is reached or the open set is empty

Advantages:
    - Guarantees the shortest path if the heuristic is admissible (never overestimates)
    - More efficient than Dijkstra's Algorithm by using heuristic guidance
    - More accurate than Greedy Best-First Search by considering path costs

Disadvantages:
    - Requires a good heuristic function for optimal performance
    - Still requires significant memory for complex problems
    - The quality of the solution depends on the quality of the heuristic

Visualization:
    A* expands nodes in a directed manner toward the goal, but also considers the cost of the path
    taken so far. You'll see fewer expanded nodes than Dijkstra but more than Greedy search,
    and the final path will be optimal.

4. IMPLEMENTATION DETAILS
----------------------
- All algorithms use a priority queue (heap) for efficient node selection
- Manhattan distance is used as the heuristic function
- Path reconstruction works backwards from the goal using a "came_from" dictionary
- Expanded nodes are tracked for visualization
- All algorithms terminate when the goal is reached, not when the open set is empty

Time Complexity:
- Greedy Best-First Search: O(E) where E is the number of edges
- Dijkstra's Algorithm: O(E + V log V) where V is the number of vertices
- A* Algorithm: O(E) in the best case, but can be as bad as Dijkstra's Algorithm
"""

from collections import deque
import heapq

def heuristic(x, y, goal_x, goal_y):
    """
    Calculate Manhattan distance heuristic between two points.
    
    The Manhattan distance is the sum of the absolute differences of their Cartesian coordinates.
    In a grid-based environment, this represents the minimum number of steps needed to reach the goal
    if there were no obstacles.
    
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
    
    This algorithm always expands the node that appears to be closest to the goal,
    as determined by the heuristic function. It does not consider the cost of reaching
    the current node, only the estimated cost to the goal.
    
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
    expanded = []  # List to store expanded nodes for visualization
    came_from = {}  # Dictionary to store the path (maps node -> predecessor)
    
    # Priority queue with (heuristic, (x, y))
    # The first element of each tuple is the priority (lower is better)
    open_set = [(heuristic(start_x, start_y, goal_x, goal_y), (start_x, start_y))]
    
    while open_set:
        # Get the node with the lowest heuristic value
		# heapq.heappop returns the smallest element from the heap, 
		# thats how heapq works
        _, current = heapq.heappop(open_set)
        current_x, current_y = current
        
        # If we reached the goal, we can stop
        if current_x == goal_x and current_y == goal_y:
            break
        
        # Add to expanded nodes for visualization
        if current not in expanded:
            expanded.append(current)
        
        # Check all neighbors of the current node
        for neighbor in get_neighbors_fn(current_x, current_y):
            # Only consider neighbors we haven't processed yet
            if neighbor not in came_from:
                # Record how we reached this neighbor
                came_from[neighbor] = current
                
                # Calculate the heuristic for this neighbor
                h = heuristic(neighbor[0], neighbor[1], goal_x, goal_y)
                
                # Add to the open set with its heuristic as priority
                heapq.heappush(open_set, (h, neighbor))
    
    # Reconstruct the path from start to goal
    path = reconstruct_path(came_from, start_pos, goal_pos)
    return path, expanded

def dijkstra(start_pos, goal_pos, get_neighbors_fn):
    """
    Dijkstra's Algorithm for path finding.
    
    This algorithm systematically explores the graph by always expanding the node
    with the lowest cumulative path cost. It guarantees the shortest path but explores
    in all directions equally.
    
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
    expanded = []  # List to store expanded nodes for visualization
    came_from = {}  # Dictionary to store the path (maps node -> predecessor)
    
    # Priority queue with (cost, (x, y))
    # The first element of each tuple is the priority (lower is better)
    open_set = [(0, (start_x, start_y))]
    
    # Dictionary storing the cost of the best known path to each node
    cost_so_far = {(start_x, start_y): 0}
    
    while open_set:
        # Get the node with the lowest path cost
        _, current = heapq.heappop(open_set)
        current_x, current_y = current
        
        # If we reached the goal, we can stop
        if current_x == goal_x and current_y == goal_y:
            break
        
        # Add to expanded nodes for visualization
        if current not in expanded:
            expanded.append(current)
        
        # Check all neighbors of the current node
        for neighbor in get_neighbors_fn(current_x, current_y):
            # Calculate the cost to reach this neighbor via current node
            new_cost = cost_so_far[current] + 1  # Cost is 1 for each step in a grid
            
            # If this is a new node or we found a better path to it
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                # Update the cost to reach this neighbor
                cost_so_far[neighbor] = new_cost
                
                # Record how we reached this neighbor
                came_from[neighbor] = current
                
                # Add to the open set with its path cost as priority
                heapq.heappush(open_set, (new_cost, neighbor))
    
    # Reconstruct the path from start to goal
    path = reconstruct_path(came_from, start_pos, goal_pos)
    
    return path, expanded

def astar(start_pos, goal_pos, get_neighbors_fn):
    """
    A* Algorithm for path finding.
    
    This algorithm combines Dijkstra's approach with a heuristic. It prioritizes nodes
    by the sum of the path cost so far and the estimated distance to the goal.
    This makes it both optimal (like Dijkstra) and efficient (like Greedy Best-First).
    
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
    expanded = []  # List to store expanded nodes for visualization
    came_from = {}  # Dictionary to store the path (maps node -> predecessor)
    
    # Priority queue with (f_score, (x, y))
    # The first element of each tuple is the priority (lower is better)
    # Initial f_score is just the heuristic since g_score is 0
    open_set = [(heuristic(start_x, start_y, goal_x, goal_y), (start_x, start_y))]
    
    # Dictionary storing the cost of the best known path to each node
    cost_so_far = {(start_x, start_y): 0}
    
    while open_set:
        # Get the node with the lowest f_score (g_score + heuristic)
        _, current = heapq.heappop(open_set)
        current_x, current_y = current
        
        # If we reached the goal, we can stop
        if current_x == goal_x and current_y == goal_y:
            break
        
        # Add to expanded nodes for visualization
        if current not in expanded:
            expanded.append(current)
        
        # Check all neighbors of the current node
        for neighbor in get_neighbors_fn(current_x, current_y):
            # Calculate the cost to reach this neighbor via current node
            new_cost = cost_so_far[current] + 1  # Cost is 1 for each step in a grid
            
            # If this is a new node or we found a better path to it
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                # Update the cost to reach this neighbor
                cost_so_far[neighbor] = new_cost
                
                # Record how we reached this neighbor
                came_from[neighbor] = current
                
                # Calculate the f_score = g_score + heuristic
                # f() = g() + h()
                # g() is the cost of the path from start to the current node
                # h() is the heuristic estimate of the distance from the current node to the goal
                f_score = new_cost + heuristic(neighbor[0], neighbor[1], goal_x, goal_y)
                
                # Add to the open set with its f_score as priority
                heapq.heappush(open_set, (f_score, neighbor))
    
    # Reconstruct the path from start to goal
    path = reconstruct_path(came_from, start_pos, goal_pos)
    
    return path, expanded

def reconstruct_path(came_from, start_pos, goal_pos):
    """
    Reconstruct the path from start to goal using the came_from dictionary.
    
    This function works backwards from the goal to the start, following the
    predecessor links stored in the came_from dictionary.
    
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
        return path  # Return empty path if no path was found
    
    # Reconstruct path from goal to start
    while current != start_pos:
        path.appendleft(current)  # Add current position to the front of the path
        current = came_from.get(current, start_pos)  # Move to the predecessor
    
    # Add start position
    path.appendleft(start_pos)
    
    return path 