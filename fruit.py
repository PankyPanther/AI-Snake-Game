from defs import *
import pygame
from random import randint
from pygame.math import Vector2

class Fruit:
    def __init__(self):
        Fruit.randomize(self)


    def randomize(self):
        self.x = randint(0, (GAME_WIDTH / CELL_SIZE) - 1 )  * CELL_SIZE
        self.y = randint(0, (GAME_HEIGHT / CELL_SIZE) - 1)  * CELL_SIZE

        self.pos = Vector2(self.x, self.y)

        print(self.pos)


    def drawFruit(self):
        pygame.draw.rect(GAME_SCREEN, RED, (self.pos.x, self.pos.y, CELL_SIZE, CELL_SIZE))


    def get_pos(self) -> Vector2:
        return self.pos
