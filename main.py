import pygame
from defs import *
from fruit import Fruit
from snake import Snake

class Game:
    def __init__(self) -> None:
        self.fruit = Fruit()
        self.snake = Snake()


    def update(self) -> None:
        GAME_SCREEN.fill(BLACK)

        if(self.snake.isDead() == True):
            self.snake.resetSnake()
            self.fruit.randomize()
            self.snake.draw_body()
            pygame.time.delay(1500)

        # Other Game Objects Printed Here
        self.fruit.drawFruit()
        self.snake.next_tick()
        
        if self.fruit.get_pos() == self.snake.getHead():
            self.fruit.randomize()
            self.snake.increaseLength()
            print("Yummy")            

        # Renders to screen
        pygame.display.flip()


    def main(self) -> None:
        Game.update(self)
        


# pygame setup
pygame.init()
clock = pygame.time.Clock()
running = True
game = Game()


if __name__ == "__main__":
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game.main()

        clock.tick(FPS) 


pygame.quit()