import gui.util.config
import pygame


class Obstacle:
    def __init__(self):
        self.size = 30
        self.color = gui.util.config.GREEN
        self.x = 600
        self.y = gui.util.config.HEIGHT - self.size

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
