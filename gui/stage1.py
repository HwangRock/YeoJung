from stageInterface import Stage
from obstacle import Obstacle
from enemy import Enemy
from ground import Ground
from player import Player
import config


class Stage1(Stage):
    def __init__(self):
        super().__init__()

    def load(self):
        self.obstacles = [Obstacle()]
        self.enemies = [Enemy(400, config.HEIGHT - config.ENEMY_SIZE)]
        self.grounds = [Ground(300, 200, 500, 20)]
        self.player = Player(500, 0)
