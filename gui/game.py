import pygame
import requests
import config
from player import Player
from obstacle import Obstacle

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
        pygame.display.set_caption("YeoJung")
        self.font = pygame.font.SysFont(None, 36)
        self.button_rect = pygame.Rect(config.BUTTON_X, config.BUTTON_Y, config.BUTTON_WIDTH, config.BUTTON_HEIGHT)
        self.button_text = self.font.render("API", True, config.BLACK)
        self.api_result = ""
        self.player = Player()
        self.obstacle=Obstacle()
        self.clock = pygame.time.Clock()
        self.running = True

    def fetch_api_data(self):
        try:
            response = requests.post("http://localhost:8080/test")
            if response.status_code == 200:
                return response.text
            else:
                return f"Error: {response.status_code}"
        except Exception as e:
            return f"Exception: {str(e)}"

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.button_rect.collidepoint(event.pos):
                    self.api_result = self.fetch_api_data()

    def update(self):
        self.player.update()

    def render(self):
        self.screen.fill(config.WHITE)
        pygame.draw.rect(self.screen, config.GRAY, self.button_rect)
        self.screen.blit(self.button_text, (self.button_rect.x + 20, self.button_rect.y + 10))
        result_render = self.font.render(self.api_result, True, config.DARK_GRAY)
        self.screen.blit(result_render, (50, 400))
        self.player.draw(self.screen)
        self.obstacle.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)

        pygame.quit()