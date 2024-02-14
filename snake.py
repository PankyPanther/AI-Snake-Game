from defs import *
import pygame
from pygame.math import Vector2

class Snake:
    def __init__(self) -> None:
        Snake.resetSnake(self)


    def draw_body(self):
        sizeChecker = 0
        newBody = []
        for segment in self.body:
            if sizeChecker < self.size:
                if segment == self.body[0]:
                    pygame.draw.rect(GAME_SCREEN, DARK_GREEN, (segment.x, segment.y, CELL_SIZE, CELL_SIZE))
                else:
                    pygame.draw.rect(GAME_SCREEN, GREEN, (segment.x, segment.y, CELL_SIZE, CELL_SIZE))
                newBody.append(segment)
                sizeChecker += 1
            else:
                self.body = newBody
                break


    def move_snake(self):
        # Movement GLitches
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w] and self.direction != Vector2(0, -1):
            self.direction = Vector2(0, 1)
        if keys[pygame.K_s] and self.direction != Vector2(0, 1):
            self.direction = Vector2(0, -1)
        if keys[pygame.K_a] and self.direction != Vector2(1, 0):
            self.direction = Vector2(-1, 0)
        if keys[pygame.K_d] and self.direction != Vector2(-1, 0):
            self.direction = Vector2(1, 0)
        
        if self.direction == Vector2(0, -1):
            self.body.insert(0, Vector2(self.body[0].x, self.body[0].y + CELL_SIZE))
        if self.direction == Vector2(0, 1):
            self.body.insert(0, Vector2(self.body[0].x, self.body[0].y - CELL_SIZE))
        if self.direction == Vector2(-1, 0):
            self.body.insert(0, Vector2(self.body[0].x - CELL_SIZE, self.body[0].y))
        if self.direction == Vector2(1, 0):
            self.body.insert(0, Vector2(self.body[0].x + CELL_SIZE, self.body[0].y))


    def next_tick(self):
        Snake.draw_body(self)
        Snake.move_snake(self)
        

    def increaseLength(self):
        self.size += 1


    def isDead(self):
        for segment in self.body[3:]:
            if segment == self.body[0]:
                return True
        
        # I need to reowrk this
        if(self.body[0].x > GAME_WIDTH or self.body[0].x < 0 - CELL_SIZE or self.body[0].y < 0 - CELL_SIZE or self.body[0].y > GAME_HEIGHT):
            return True
        
        return False


    def resetSnake(self):
        self.body = STARTING_BODY
        self.direction = STARTING_DIRECTION
        self.size = STARTING_SIZE


    def getHead(self):
        return self.body[0]

    