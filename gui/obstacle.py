import config
import pygame

class Obstacle:
    def __init__(self):
        self.size = 30
        self.color = config.GREEN
        self.x=600
        self.y=config.HEIGHT - self.size


    def draw(self,screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.size)