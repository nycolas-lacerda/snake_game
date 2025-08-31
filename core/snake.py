from time import sleep

import pygame
from pygame.examples.audiocapture import sound

from settings import *
from core.sound_manager import SoundManager


class Snake:
    def __init__(self, x, y, size, color, difficulty="normal"):
        self.body = [[x, y]]
        self.size = size
        self.color = color
        self.x_vel = 0
        self.y_vel = 0
        self.growing = False
        self.direction = "RIGHT"
        self.difficulty = difficulty
        self.sound = SoundManager()

    def move(self):
        head = self.body[-1].copy()
        head[0] += self.x_vel
        head[1] += self.y_vel
        if self.difficulty == "normal":
            head[0] = ((head[0] - MARGIN_X) % PLAY_WIDTH) + MARGIN_X
            head[1] = ((head[1] - MARGIN_Y) % PLAY_HEIGHT) + MARGIN_Y
        elif self.difficulty == "hard":
            # colisão com parede
            if (
                head[0] < MARGIN_X or head[0] >= PLAY_WIDTH + MARGIN_X or
                head[1] < MARGIN_Y or head[1] >= PLAY_HEIGHT + MARGIN_Y
            ):
                return False

        self.body.append(head)

        if not self.growing:
            self.body.pop(0)
        else:
            self.growing = False
        return True

    def grow(self):
        self.growing = True
        self.sound.play_sound('eat')

    def check_self_collision(self):
        if len(self.body) < 4:
            return False
        head = self.body[-1]
        for part in self.body[:-1]:
            if part == head:
                return True
        return False

    def set_direction(self, direction):
        self.sound.play_sound('move')
        if (direction == "UP" and self.direction != "DOWN") or \
                (direction == "DOWN" and self.direction != "UP") or \
                (direction == "LEFT" and self.direction != "RIGHT") or \
                (direction == "RIGHT" and self.direction != "LEFT"):
            self.direction = direction
            if direction == "UP":
                self.x_vel, self.y_vel = 0, -CELL_SIZE

            elif direction == "DOWN":
                self.x_vel, self.y_vel = 0, CELL_SIZE
            elif direction == "LEFT":
                self.x_vel, self.y_vel = -CELL_SIZE, 0
            elif direction == "RIGHT":
                self.x_vel, self.y_vel = CELL_SIZE, 0

    def draw(self, surface):
        # Corpo
        for part in self.body[:-1]:
            pygame.draw.rect(surface, (0, 180, 0), (part[0], part[1], CELL_SIZE, CELL_SIZE), border_radius=6)

        head_x, head_y = self.body[-1]
        head_rect = pygame.Rect(head_x, head_y, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(surface, (0, 255, 0), head_rect, border_radius=5)
        eyes = []
        eye_radius = 3
        offset = 4

        if self.direction == "UP":
            eyes = [
                (head_x + offset, head_y + offset),  # canto superior esquerdo
                (head_x + CELL_SIZE - offset, head_y + offset)  # canto superior direito
            ]
        elif self.direction == "DOWN":
            eyes = [
                (head_x + offset, head_y + CELL_SIZE - offset),  # canto inferior esquerdo
                (head_x + CELL_SIZE - offset, head_y + CELL_SIZE - offset)  # canto inferior direito
            ]
        elif self.direction == "LEFT":
            eyes = [
                (head_x + offset, head_y + offset),  # canto superior esquerdo
                (head_x + offset, head_y + CELL_SIZE - offset)  # canto inferior esquerdo
            ]
        elif self.direction == "RIGHT":
            eyes = [
                (head_x + CELL_SIZE - offset, head_y + offset),  # canto superior direito
                (head_x + CELL_SIZE - offset, head_y + CELL_SIZE - offset)  # canto inferior direito
            ]

        self.draw_eyes(surface, eyes, eye_radius)

    def draw_eyes(self, surface, eyes, eye_radius):
        for ex, ey in eyes:
            pygame.draw.circle(surface, (255, 255, 255), (ex, ey), eye_radius)
            pygame.draw.circle(surface, (0, 0, 0), (ex, ey), 1)
