# Block World

A simple 2D grid-based game where a UFO navigates through a world with obstacles to reach a goal.

## Project Structure

The project has been organized into the following files for better readability and maintainability:

- **block_world.py**: Main entry point that imports from the modular structure
- **main.py**: Contains the main game loop and initialization
- **env.py**: Contains the Environment class and related functions
- **ufo.py**: Contains the UFO class for navigation
- **renderer.py**: Contains the rendering functions
- **constants.py**: Contains all constants and configurations
- **graph_algorithms.py**: Contains implementations of path planning algorithms

## Features

- 2D grid-based environment with various obstacle types
- Multiple maps with different obstacle configurations
- UFO that can navigate using either reactive movement or path planning
- Path planning algorithms:
  - **Greedy Best-First Search**: Uses heuristic to guide search towards goal
  - **Dijkstra's Algorithm**: Finds shortest path by exploring all directions
  - **A* Algorithm**: Combines Dijkstra's and Greedy approaches for efficiency
- Visual comparison of expanded nodes for each algorithm
- Interactive controls for algorithm selection and visualization

## Requirements

- Python 3.x
- Pygame
- NumPy

## Installation

1. Install the required packages:
```bash
pip install pygame numpy
```

2. Ensure you have the required image files in the `imgs/` directory:
   - tile.jpg
   - markedtile.jpg
   - house1.jpg, house2.jpg, house3.jpg
   - tree1.jpg, tree2.jpg
   - ufo.jpg
   - flag.jpg

## How to Run

Simply run either the main entry point or the main file:

```bash
python block_world.py
```

or

```bash
python main.py
```

## Controls

- **SPACE**: Play/Pause the path execution
- **S**: Step mode (move one step at a time)
- **R**: Reset the UFO position and recalculate the path
- **TAB**: Switch between path planning algorithms
- **M**: Switch between different maps
- **0-8**: Directly select maps 0-8
- **ESC/Close Window**: Quit the application

## Maps

The application includes nine different maps to test the path planning algorithms:

### Map 0: Diagonal Obstacles
- Features diagonal obstacles with some gaps
- Good for testing basic pathfinding capabilities

### Map 1: Maze-like Environment
- Contains vertical and horizontal walls with strategic gaps
- Challenges algorithms to find paths through narrow passages

### Map 2: Open Center
- Has obstacles around the edges with an open center
- Tests algorithms' ability to navigate around the perimeter

### Map 3: Random Obstacles
- Contains randomly placed obstacles (about 30% of the grid)
- Good for testing algorithms on unpredictable terrain

### Map 4: Spiral Pattern
- Features obstacles arranged in a spiral pattern
- Forces algorithms to follow a long, winding path

### Map 5: Checkerboard Pattern
- Obstacles arranged in a checkerboard pattern
- Tests algorithms' ability to navigate through a regular grid of obstacles

### Map 6: Central Obstacle with Narrow Passages
- Large obstacle in the center with narrow passages
- Tests algorithms' ability to find and navigate through bottlenecks

### Map 7: Multiple Rooms with Doorways
- Environment divided into rooms connected by doorways
- Tests algorithms' ability to find paths through connected spaces

### Map 8: Concentric Obstacles
- Features concentric rectangles of obstacles with strategic openings
- Tests algorithms' ability to navigate through a maze-like structure

## Path Planning Algorithms

The path planning algorithms are implemented in the `graph_algorithms.py` file, making them reusable and modular:

### Greedy Best-First Search
- Uses a heuristic (Manhattan distance) to guide the search towards the goal
- Expands nodes that appear closest to the goal first
- Fast but doesn't guarantee the shortest path

### Dijkstra's Algorithm
- Explores all possible paths uniformly
- Guarantees the shortest path
- Typically expands more nodes than other algorithms

### A* Algorithm
- Combines Dijkstra's and Greedy approaches
- Uses both path cost and heuristic to guide the search
- Generally more efficient than Dijkstra's while still finding optimal paths

## Algorithm Comparison

The application displays statistics for each algorithm:
- **Path Length**: Number of steps in the found path
- **Expanded Nodes**: Number of nodes explored during the search
- **Visual Representation**: Expanded nodes are highlighted on the grid

This allows for easy comparison of the efficiency of different path planning approaches.

## Customization

- You can modify the environment size, tile size, and FPS in `constants.py`
- To change the obstacle layout, modify the `create_environment()` function in `env.py`
- To implement a custom path planning algorithm, add it to the `graph_algorithms.py` file
- To implement a better reactive navigation, modify the `reactive_go()` method in the `Ufo` class 