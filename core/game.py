import pygame

from core.snake import Snake
from core.food import Food
from core.scoreboard import Scoreboard
from core.highscore import Highscore
from settings import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()

        self.snake = Snake(MARGIN_X, MARGIN_Y, CELL_SIZE, GREEN)
        self.food = Food(WIDTH, HEIGHT, CELL_SIZE, RED)
        self.scoreboard = Scoreboard()
        self.highscore_manager = Highscore()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_UP if self.snake.y_vel == 0:
                            # self.snake.x_vel, self.snake.y_vel = 0, -CELL_SIZE
                            self.snake.set_direction('UP')
                        case pygame.K_DOWN if self.snake.y_vel == 0:
                            # self.snake.x_vel, self.snake.y_vel = 0, CELL_SIZE
                            self.snake.set_direction('DOWN')
                        case pygame.K_LEFT if self.snake.x_vel == 0:
                            # self.snake.x_vel, self.snake.y_vel = -CELL_SIZE, 0
                            self.snake.set_direction('LEFT')
                        case pygame.K_RIGHT if self.snake.x_vel == 0:
                            # self.snake.x_vel, self.snake.y_vel = CELL_SIZE, 0
                            self.snake.set_direction('RIGHT')

            self.snake.move()

            head_x, head_y = self.snake.body[-1]
            if (head_x < MARGIN_X or head_x == MARGIN_X + PLAY_WIDTH
                    or head_y < MARGIN_Y or head_y == MARGIN_Y + PLAY_HEIGHT):
                running = False

            if self.snake.check_self_collision():
                running = False

            if (self.snake.body[-1][0] == self.food.x
                    and self.snake.body[-1][1] == self.food.y):
                self.snake.grow()
                self.food.respawn(WIDTH, HEIGHT)
                self.scoreboard.add_points(1)
                self.highscore_manager.save_highscore(self.scoreboard.score)

            self.screen.fill(BLACK)
            pygame.draw.rect(self.screen, WHITE,(MARGIN_X, MARGIN_Y, PLAY_WIDTH, PLAY_HEIGHT), BORDER_SIZE)
            self.snake.draw(self.screen)
            self.food.draw(self.screen)
            self.scoreboard.draw(self.screen)
            self.highscore_manager.draw(self.screen)

            # pygame.display.update()

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
