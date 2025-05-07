"""
Block World - Main Entry Point

This file now serves as a simple entry point that imports from the modular structure.
The code has been refactored into separate files for better readability:

- constants.py: Contains all constants and configurations
- env.py: Contains the Environment class and related functions
- ufo.py: Contains the UFO class
- renderer.py: Contains the rendering functions
- main.py: Contains the main game loop

To run the game, simply execute this file or main.py directly.
"""

# Import and run the main function
from main import main

if __name__ == "__main__":
    main()