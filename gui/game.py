import pygame
import sys
import config
from player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
        pygame.display.set_caption("YeoJung")
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)
        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.player.update()

    def render(self):
        self.screen.fill(config.WHITE)
        self.player.draw(self.screen)
        pygame.display.flip()
