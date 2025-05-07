import pygame
from constants import WIDTH, HEIGHT, TILESIZE, FPS
from env import Env, create_environment
from ufo import Ufo
from renderer import init_window, draw_window

def main():
    # Initialize pygame
    pygame.init()
    
    # Create environment and set start and goal
    env = create_environment()
    env.set_start(0, 0)
    env.set_goal(9, 7)
    
    # Create UFO at start position
    ufo = Ufo(env.startx, env.starty)
    
    # Initialize window
    win = init_window(WIDTH, HEIGHT, TILESIZE)
    
    # Optional: Use path planner for movement
    # p, t = env.path_planner()
    # ufo.set_path(p, t)
    
    # Game loop
    clock = pygame.time.Clock()
    run = True
    
    while run:
        clock.tick(FPS)
        
        # Reactive movement until reaching the goal
        if (ufo.x != env.goalx) or (ufo.y != env.goaly):
            # Option 1: Reactive movement
            x, y = ufo.reactive_go(env)
            
            # Option 2: Path following
            # x, y = ufo.execute_path()
            
            if env.is_valid_xy(x, y):
                ufo.move(x, y)
            else:
                print('[', x, ',', y, ']', "wrong coordinate!")
        
        # Draw the game state
        draw_window(win, ufo, env)
        
        # Check for exit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
    pygame.quit()

if __name__ == "__main__":
    main() 