import pygame
from pygame.math import Vector2

# Pygame Setup
GAME_WIDTH, GAME_HEIGHT =  800, 800
GAME_SCREEN = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
FPS = 10

# Game Colors
BLACK = (0, 0, 0)
RED = ( 238, 75, 43 )
GREEN = (0, 255, 0)
DARK_GREEN = (1, 50, 32)

# Game Settings
CELL_SIZE = 40
STARTING_DIRECTION = Vector2(0, -1)
STARTING_BODY = [Vector2(0, 80), Vector2(0, 40), Vector2(0, 0)]
STARTING_SIZE = 3