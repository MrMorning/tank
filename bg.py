import pygame, sys, math
from game import Tank, Bullet
BLACK = 0, 0, 0
class TankGame:
    def __init__(self):
        pygame.init()
        self.size = self.width, self.height = 600, 400
        self.speed = [1, 1]
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("tank")
        self.fps = 300
        self.fclock = pygame.time.Clock()
        self.uevent = []
        self.tank1 = Tank(env=self, path="assets/tank1.png", pos=[70, 70], angle=0)
        self.tank2 = Tank(env=self, path="assets/tank2.png", pos=[300, 300], angle=180)
        self.bulletQueue = []