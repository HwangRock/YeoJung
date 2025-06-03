from gui.object.enemy import Enemy
from gui.object.ground import Ground
from gui.object.obstacle import Obstacle
from gui.object.player import Player
from .stageInterface import Stage
import gui.util.config


class Stage1(Stage):
    def __init__(self):
        super().__init__()

    def load(self):
        self.obstacles = [Obstacle()]
        self.enemies = [Enemy(400, gui.util.config.HEIGHT - gui.util.config.ENEMY_SIZE)]
        self.grounds = [Ground(300, 200, 500, 20)]
        self.player = Player(500, 0)
