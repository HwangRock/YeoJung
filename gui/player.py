import pygame
import config

class Player:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.speed = 5
        self.color = config.BLUE
        self.size = 50

        self.isJumping = False
        self.velocity_y = 0
        self.gravity = 1
        self.jump_strength = -15

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and 0<self.x<=config.WIDTH:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and 0<=self.x<config.WIDTH-self.size:
            self.x += self.speed
        if keys[pygame.K_UP] and 0<self.y<=config.HEIGHT and not self.isJumping:
            self.velocity_y=self.jump_strength
            self.isJumping=True

    def update(self):
        self.handle_input()

        self.velocity_y += self.gravity
        self.y += self.velocity_y

        if self.y >= config.HEIGHT - self.size:
            self.y = config.HEIGHT - self.size
            self.velocity_y = 0
            self.isJumping = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))
