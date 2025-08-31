import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {
            "eat": pygame.mixer.Sound("assets/food.mp3"),
            "gameover": pygame.mixer.Sound("assets/gameover.wav"),
            "move": pygame.mixer.Sound("assets/move.mp3"),
        }

        pygame.mixer.music.load("assets/music.mp3")
        pygame.mixer.music.set_volume(0.5)

    def play_music(self):
        pygame.mixer.music.play(-1)  # loop infinito

    def stop_music(self):
        pygame.mixer.music.stop()

    def play_sound(self, name):
        if name in self.sounds:
            self.sounds[name].play()