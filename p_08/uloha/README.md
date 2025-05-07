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

## Features

- 2D grid-based environment with various obstacle types
- UFO that can navigate using either reactive movement or path planning
- Path planning algorithm to find a route from start to goal
- Visual representation of the environment and UFO movement

## Requirements

- Python 3.x
- Pygame

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

## Customization

- You can modify the environment size, tile size, and FPS in `constants.py`
- To change the obstacle layout, modify the `create_environment()` function in `env.py`
- To implement a custom path planning algorithm, modify the `path_planner()` method in the `Env` class
- To implement a better reactive navigation, modify the `reactive_go()` method in the `Ufo` class 