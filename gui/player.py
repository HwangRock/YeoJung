import config
import pygame


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.color = config.BLACK
        self.size = 50

        self.isJumping = False
        self.velocity_y = 0
        self.gravity = 1
        self.jump_strength = -15

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < config.WIDTH - self.size:
            self.x += self.speed
        if keys[pygame.K_UP] and not self.isJumping:
            self.velocity_y = self.jump_strength
            self.isJumping = True

        self.color = config.BLACK
        if keys[pygame.K_q]:
            self.color = config.RED
        if keys[pygame.K_w]:
            self.color = config.BLUE
        if keys[pygame.K_e]:
            self.color = config.GREEN
        if keys[pygame.K_r]:
            self.color = config.GRAY

    def land_on(self, y):
        self.y = y - self.size
        self.velocity_y = 0
        self.isJumping = False

    def land_off(self):
        self.isJumping = True

    def update(self):
        self.handle_input()
        self.velocity_y += self.gravity
        self.y += self.velocity_y

        if self.y >= config.HEIGHT - self.size:
            self.y = config.HEIGHT - self.size
            self.velocity_y = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))
