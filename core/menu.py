import pygame
from core.highscore import Highscore

class BaseScreen:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", 24)
        self.big_font = pygame.font.SysFont("arial", 40)

    @property
    def WIDTH(self):
        return self.screen.get_width()

    @property
    def HEIGHT(self):
        return self.screen.get_height()


class Menu(BaseScreen):
    def __init__(self, screen, options=None):
        super().__init__(screen)
        self.options = options or ["Jogar", "High Score", "Dificuldade", "Sair"]
        self.selected = 0
        self.difficulty = "normal"

    def run(self):
        while True:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_UP, pygame.K_w):
                        self.selected = (self.selected - 1) % len(self.options)
                    elif event.key in (pygame.K_DOWN, pygame.K_s):
                        self.selected = (self.selected + 1) % len(self.options)
                    elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                        choice = self.options[self.selected]
                        if choice == "Jogar":
                            return "play"
                        if choice == "High Score":
                            return "highscore"
                        if choice == "Dificuldade":
                            self.difficulty = "hard" if self.difficulty == "normal" else "normal"
                        if choice == "Sair":
                            return "quit"
            self.clock.tick(15)

    def draw(self):
        self.screen.fill((0, 0, 0))
        for i, option in enumerate(self.options):
            selected = (i == self.selected)
            color = (0, 255, 0) if selected else (255, 255, 255)

            if option == "Dificuldade":
                text = f"{option}: {self.difficulty.capitalize()}"
            else:
                text = option
            render = self.big_font.render(
                f"> {text} <" if selected else text, True, color
            )
            rect = render.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2 + i * 50))
            self.screen.blit(render, rect)
        pygame.display.flip()

class HighScoreView(BaseScreen):
    def run(self, difficulty):
        highscore = Highscore(difficulty).load_highscore()
        while True:
            self.screen.fill((20, 20, 20))
            title = self.big_font.render("High Score", True, (255, 255, 0))
            value = self.big_font.render(str(highscore), True, (255, 255, 255))
            hint = self.font.render("ENTER para voltar", True, (200, 200, 200))

            self.screen.blit(title, (self.WIDTH//2 - title.get_width()//2, self.HEIGHT//3))
            self.screen.blit(value, (self.WIDTH//2 - value.get_width()//2, self.HEIGHT//2))
            self.screen.blit(hint,  (self.WIDTH//2 - hint.get_width()//2,  self.HEIGHT - 50))

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                if event.type == pygame.KEYDOWN and event.key in (pygame.K_RETURN, pygame.K_ESCAPE):
                    return "menu"
            self.clock.tick(15)


class GameOverView(BaseScreen):
    def __init__(self, screen, score):
        super().__init__(screen)
        self.score = score

    def run(self, difficulty):
        highscore = Highscore(difficulty).load_highscore()
        while True:
            self.screen.fill((50, 0, 0))
            title = self.big_font.render("GAME OVER", True, (255, 60, 60))
            score_t = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
            high_t  = self.font.render(f"Highscore: {highscore}", True, (255, 255, 0))
            hint    = self.font.render("ENTER para voltar ao menu", True, (220, 220, 220))

            self.screen.blit(title,  (self.WIDTH//2 - title.get_width()//2,  self.HEIGHT//3))
            self.screen.blit(score_t,(self.WIDTH//2 - score_t.get_width()//2, self.HEIGHT//2))
            self.screen.blit(high_t, (self.WIDTH//2 - high_t.get_width()//2,  self.HEIGHT//2 + 28))
            self.screen.blit(hint,   (self.WIDTH//2 - hint.get_width()//2,    self.HEIGHT - 50))

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                if event.type == pygame.KEYDOWN and event.key in (pygame.K_RETURN, pygame.K_ESCAPE):
                    return "menu"
            self.clock.tick(15)
