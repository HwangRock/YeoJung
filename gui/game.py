import pygame
import requests
import config
from player import Player
from obstacle import Obstacle
from enemy import Enemy
from ground import Ground
from api import fetch_test
from stage1 import Stage1


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
        pygame.display.set_caption("YeoJung")
        self.font = pygame.font.SysFont(None, 36)
        self.button_rect = pygame.Rect(config.BUTTON_X, config.BUTTON_Y, config.BUTTON_WIDTH, config.BUTTON_HEIGHT)
        self.button_text = self.font.render("API", True, config.BLACK)
        self.api_result = ""
        self.player = Player(500, 100)
        self.obstacles = [Obstacle()]
        self.enemies = [
            Enemy(900, config.HEIGHT - config.ENEMY_SIZE)
        ]
        self.grounds = [
            Ground(300, 500, 500, 20)
        ]
        self.clock = pygame.time.Clock()
        self.running = True
        background_img = pygame.image.load("./image/morning.png")
        self.image = pygame.transform.scale(background_img, (config.WIDTH, config.HEIGHT))
        self.stages = [None, Stage1()]
        self.current_stage_index = 0
        self.load_stage()

    def load_stage(self):
        if self.current_stage_index == 0:
            self.obstacles = [Obstacle()]
            self.enemies = [Enemy(900, config.HEIGHT - config.ENEMY_SIZE)]
            self.grounds = [Ground(300, 500, 500, 20)]
            self.player = self.player
        else:
            stage = self.stages[self.current_stage_index]
            stage.load()
            self.obstacles = stage.obstacles
            self.enemies = stage.enemies
            self.grounds = stage.grounds
            self.player = stage.player

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.button_rect.collidepoint(event.pos):
                    self.api_result = fetch_test()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.next_stage()

    def update(self):
        self.player.update()
        onPlatform = False

        playerRect = pygame.Rect(self.player.x, self.player.y, self.player.size, self.player.size)
        for o in self.obstacles:
            obstacleRect = pygame.Rect(o.x - o.size, o.y - o.size, 2 * o.size, 2 * o.size)
            if playerRect.colliderect(obstacleRect):
                print("gameover : obstacle")

        for e in self.enemies[:]:
            e.update()
            enemyRect = pygame.Rect(e.x, e.y, e.size, e.size)
            if playerRect.colliderect(enemyRect):
                if self.player.color == config.BLACK:
                    print("gameover : enemy")
                else:
                    self.enemies.remove(e)

        for p in self.grounds:
            plat_rect = pygame.Rect(p.x, p.y, p.w, p.h)

            if playerRect.colliderect(plat_rect) and self.player.velocity_y >= 0:
                if self.player.y + self.player.size <= p.y + self.player.velocity_y:
                    self.player.land_on(p.y)
                    onPlatform = True
                    break
        if not onPlatform:
            self.player.land_off()

    def next_stage(self):
        if self.current_stage_index + 1 < len(self.stages):
            self.current_stage_index += 1
            self.load_stage()

    def render(self):
        self.screen.blit(self.image, (0, 0))
        pygame.draw.rect(self.screen, config.GRAY, self.button_rect)
        self.screen.blit(self.button_text, (self.button_rect.x + 20, self.button_rect.y + 10))
        result_render = self.font.render(self.api_result, True, config.DARK_GRAY)
        self.screen.blit(result_render, (50, 400))
        self.player.draw(self.screen)

        for o in self.obstacles:
            o.draw(self.screen)
        for e in self.enemies:
            e.draw(self.screen)
        for g in self.grounds:
            g.draw(self.screen)

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)

        pygame.quit()
