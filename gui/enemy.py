import config
import pygame


class Enemy:
    def __init__(self, x, y):
        self.color = config.RED
        self.x = x
        self.y = y
        self.startX = x
        self.startY = y
        self.speed = 3
        self.size = config.ENEMY_SIZE
        self.limit = 100
        self.direct = True

    def update(self):
        if self.direct:
            self.x += self.speed
            if self.x >= self.startX + self.limit:
                self.direct = False
        else:
            self.x -= self.speed
            if self.x <= self.startX - self.limit:
                self.direct = True

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))
