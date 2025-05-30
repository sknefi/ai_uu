import pygame
import time
from constants import *
from env import Env, create_environment
from ufo import Ufo
from renderer import init_window, draw_window
from utils import print_stats, select_map

def print_map_info(map_index, algorithm, path, expanded):
	print("\n" + "="*50)
	print_stats(map_index, algorithm, len(path), len(expanded))
	print("="*50) 

def main():
    # Initialize pygame
    pygame.init()
    
    # Initialize map and algorithm selection
    map_index = 0
    total_maps = 9  # Updated to include all maps (0-8)
    algorithms = ["greedy", "dijkstra", "astar"]
    current_algo_index = 0
    algorithm = algorithms[current_algo_index]
    
    # Create environment and set start and goal
    env = create_environment(map_index)
    
    # Create UFO at start position
    ufo = Ufo(env.startx, env.starty)
    
    # Initialize window
    win = init_window(WIDTH, HEIGHT, TILESIZE)
    
    # Run the current algorithm
    path, expanded = env.path_planner(algorithm)
    ufo.set_path(path, expanded)
    
    print_stats(map_index, algorithm, len(path), len(expanded))
    
    # Game loop
    clock = pygame.time.Clock()
    run = True
    paused = True
    step_mode = False
    
    while run:
        clock.tick(FPS)
        
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Toggle pause
                    paused = not paused
                elif event.key == pygame.K_s:
                    # Step mode (move one step at a time)
                    step_mode = True
                    paused = False
                elif event.key == pygame.K_r:
                    # Reset UFO position and path
                    ufo.x = env.startx
                    ufo.y = env.starty
                    path, expanded = env.path_planner(algorithm)
                    ufo.set_path(path, expanded)
                elif event.key == pygame.K_TAB:
                    # Switch algorithm
                    current_algo_index = (current_algo_index + 1) % len(algorithms)
                    algorithm = algorithms[current_algo_index]
                    
                    # Reset UFO position
                    ufo.x = env.startx
                    ufo.y = env.starty
                    
                    # Run the new algorithm
                    start_time = time.time()
                    path, expanded = env.path_planner(algorithm)
                    end_time = time.time()
                    
                    ufo.set_path(path, expanded)
                    
                    # Print algorithm statistics
                    print("\n" + "="*50)
                    print_stats(map_index, algorithm, len(path), len(expanded), end_time - start_time)
                    print("="*50)
                elif event.key == pygame.K_m:
                    # Switch map
                    map_index = (map_index + 1) % total_maps
                    
                    # Create new environment
                    env = create_environment(map_index)
                    
                    # Reset UFO position
                    ufo = Ufo(env.startx, env.starty)
                    
                    # Run the current algorithm on the new map
                    start_time = time.time()
                    path, expanded = env.path_planner(algorithm)
                    end_time = time.time()
                    
                    ufo.set_path(path, expanded)
                    
                    # Print map and algorithm statistics
                    print("\n" + "="*50)
                    print_stats(map_index, algorithm, len(path), len(expanded), end_time - start_time)
                    print("="*50)
                # Handle direct map selection with number keys
                elif pygame.K_1 <= event.key <= pygame.K_9:
                    # Map keys 1-9 correspond to map indices 0-8
                    selected_map = event.key - pygame.K_1
                    
                    # Make sure the map index is valid
                    if 0 <= selected_map < total_maps:
                        map_index = selected_map
                        
                        # Create new environment and UFO
                        env = create_environment(map_index)
                        ufo = Ufo(env.startx, env.starty)
                        
                        # Run algorithm on the selected map
                        path, expanded = env.path_planner(algorithm)
                        ufo.set_path(path, expanded)
                        
                        # Print map info
                        print_map_info(map_index, algorithm, path, expanded)
        
        # Move UFO if not paused
        if not paused and (ufo.x != env.goalx or ufo.y != env.goaly) and path:
            # Use path following
            x, y = ufo.execute_path()
            
            if env.is_valid_xy(x, y):
                ufo.move(x, y)
            
            # If in step mode, pause after each step
            if step_mode:
                paused = True
                step_mode = False
        
        # Draw the game state
        draw_window(win, ufo, env)
        
        # Add text overlay for current algorithm and map
        font = pygame.font.SysFont("Arial", 32)  # Increased font size
        small_font = pygame.font.SysFont("Arial", 24)  # Added smaller font for help text
        
        map_text = font.render(f"Map: {map_index}", True, (255, 255, 255))
        algo_text = font.render(f"Algorithm: {algorithm.upper()}", True, (255, 255, 255))
        stats_text = font.render(f"Path: {len(path)} | Expanded: {len(expanded)}", True, (255, 255, 255))
        help_text = small_font.render("SPACE: Play/Pause | S: Step | R: Reset | TAB: Switch Algo | M: Switch Map | 1-9: Select Map", True, (255, 255, 255))
        
        win.blit(map_text, (20, 20))  # Added map text
        win.blit(algo_text, (20, 60))  # Adjusted position
        win.blit(stats_text, (20, 100))  # Adjusted position
        win.blit(help_text, (20, HEIGHT * TILESIZE - 40))  # Adjusted vertical position
        
        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    main() 