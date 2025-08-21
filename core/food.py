import pygame, random

from settings import *


class Food:
    def __init__(self, screen_width, screen_height, size, color):
        self.size = size
        self.color = color
        self.x = random.randrange(MARGIN_X, screen_width - MARGIN_X, size)
        self.y = random.randrange(MARGIN_Y, screen_height - MARGIN_Y, size)

    def respawn(self, screen_width, screen_height):
        self.x = random.randrange(MARGIN_X, screen_width - MARGIN_X, self.size)
        self.y = random.randrange(MARGIN_Y, screen_height - MARGIN_Y, self.size)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.size, self.size), border_radius=5)
