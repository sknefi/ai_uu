# Schelling's Segregation Model Simulation

This project implements a simulation of Schelling's segregation model. The model demonstrates how individual preferences can lead to overall segregation, even when the individual bias is small. Agents are placed on a grid and update their "mood" (happy or sad) depending on the similarity of their neighbors. Unhappy (sad) agents then move to empty cells until everyone is content with their surroundings.

## Overview

- **Grid Initialization:**  
  The simulation starts by generating a 2D grid with random agents using the `generate_agents()` function. The grid represents a torus (edges wrap around) where each cell can be occupied by an agent or be empty.

- **Agent Mood Determination:**  
  Each agent's satisfaction is determined by comparing the number of neighboring agents of the same type to the total number of neighbors. If the ratio of similar neighbors falls below a set tolerance threshold (`TOL`), the agent becomes sad; otherwise, the agent is happy.

- **Agent Relocation:**  
  The simulation uses the `make_everyone_happy()` function to iteratively move unhappy agents to empty cells. This process continues until no more moves are necessary, and all agents are happy.

- **Visualization:**  
  A custom display function shows four panels:
  1. **Initial State:** The original grid of agents.
  2. **Neighborhood Realization:** The grid after the initial evaluation of each agent’s neighborhood.
  3. **Final (Happy) State:** The grid after all unhappy agents have been moved.
  4. **Happy Agents Over Time:** A graph plotting the number of happy agents versus the number of iterations.

## Code Structure

- **`constants.py`**  
  Contains the simulation parameters:
  - `N`: Grid size (NxN).
  - `TOL`: Tolerance threshold for agent satisfaction.
  - `RADIUS`: The neighborhood radius for checking neighbors.
  - Agent state definitions (e.g., `EMPTY`, `ORANGE_SAD`, `BLUE_HAPPY`, etc.).

- **`schelling.py`**  
  Implements the core simulation functions:
  - `generate_agents(N)`: Creates the initial random grid.
  - `calc_rat()`: Calculates the ratio of like-colored neighbors.
  - `update_agents()`, `change_agent_mood()`, and `update_one_agent()`: Update each agent’s state.
  - `make_everyone_happy()`: Moves sad agents to empty cells until all are happy, while tracking the number of happy agents over iterations.

- **`graphic.py`**  
  Contains the `display_grid()` function which uses Matplotlib to display:
  - The initial grid.
  - The updated grid after the agents’ neighborhood evaluation.
  - The final happy grid.
  - A plot of the number of happy agents over time.

- **`main.py`** (or similar)  
  Serves as the entry point of the simulation:
  ```python
  from schelling import *

  if __name__ == "__main__":
      grid = generate_agents(N)
      
      updated_grid = grid.copy()
      updated_grid, sad_agents, null_agents = update_agents(updated_grid)
   
      happy_grid = updated_grid.copy()
      happy_grid, num_happy_agents = make_everyone_happy(happy_grid, sad_agents, null_agents)
   
      display_grid(grid, updated_grid, happy_grid, num_happy_agents)
