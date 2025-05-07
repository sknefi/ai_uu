from colors import Colors
from constants import ALGO_COLORS
from env import create_environment
from ufo import Ufo

def colored_algorithm(algorithm):
    """Return the algorithm name with its associated color"""
    return f"{ALGO_COLORS.get(algorithm, Colors.WHITE)}{algorithm.upper()}{Colors.RESET}"

def print_stats(map_index, algorithm, path_length, expanded_nodes, time_taken=None):
    """Print statistics with colors"""
    map_color = Colors.MAGENTA
    path_color = Colors.BLUE
    expanded_color = Colors.RED
    time_color = Colors.GREEN
    
    print(f"{map_color}Map: {map_index}{Colors.RESET}")
    print(f"Algorithm: {colored_algorithm(algorithm)}")
    print(f"{path_color}Path length: {path_length}{Colors.RESET}")
    print(f"{expanded_color}Expanded nodes: {expanded_nodes}{Colors.RESET}")
    if time_taken is not None:
        print(f"{time_color}Time taken: {time_taken:.6f} seconds{Colors.RESET}")

def select_map(map_index, env, ufo, algorithm):
    """Helper function to select a map and update environment and UFO"""
    env = create_environment(map_index)
    ufo = Ufo(env.startx, env.starty)
    return env, ufo