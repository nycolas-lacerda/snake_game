import os
import pygame
from settings import *

class Highscore:
    def __init__(self, filename="normal"):
        self.filename = f"scores/{filename}"
        self.highscore = self.load_highscore()
        self.font = pygame.font.SysFont("Arial", 25)

    def load_highscore(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                return int(f.read().strip() or 0)
        return 0

    def save_highscore(self, score):
        if score > self.highscore:
            self.highscore = score
            with open(self.filename, "w") as f:
                f.write(str(self.highscore))

    def draw(self, surface):
        text = self.font.render(f"Maior Pontuação: {self.highscore}", True, (255, 255, 255))
        surface.blit(text, (WIDTH - text.get_width(), 10))