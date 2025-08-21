import pygame

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont("Arial", 25)

    def add_points(self, points):
        self.score += points

    def draw(self, surface):
        text = self.font.render(f"Pontos: {self.score}", True, (255, 255, 255))
        surface.blit(text, (10, 10))