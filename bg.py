import pygame

from game import Tank

BLACK = 0, 0, 0
WHITE = 255, 255, 255


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
        self.score1 = Score(self, 0, [500, 100])
        self.score2 = Score(self, 0, [500, 200])
        self.text1 = Text(self, "assets/comic.ttf", 36, WHITE, "Tank1:", [400, 100])
        self.text2 = Text(self, "assets/comic.ttf", 36, WHITE, "Tank2:", [400, 200])
        self.startFlag = 0

    def restart(self):
        self.tank1 = Tank(env=self, path="assets/tank1.png", pos=[70, 70], angle=0)
        self.tank2 = Tank(env=self, path="assets/tank2.png", pos=[300, 300], angle=180)

    def update(self):
        self.tank1.update()
        self.tank2.update()
        self.text1.update()
        self.text2.update()
        self.score1.update()
        self.score2.update()

class Text:
    def __init__(self, game, font, size, color, str, pos):
        self.content = str
        self.env = game
        self.fontObj = pygame.font.Font(font, size)
        self.color = color
        self.surf = self.fontObj.render(self.content, True, color)
        self.pos = pos

    def reRender(self):
        self.surf = self.fontObj.render(self.content, True, self.color)

    def update(self):
        self.rect = self.surf.get_rect()
        self.rect.centerx = self.pos[0]
        self.rect.centery = self.pos[1]
        self.env.screen.blit(self.surf, self.rect)

    def get(self):
        return self.content

class Score(Text):
    def __init__(self, game, score, pos):
        Text.__init__(self, game, "assets/comic.ttf", 36, WHITE, str(score), pos)
        self.val = score

    def add(self, val):
        self.val += val
        self.content = str(self.val)
        self.reRender()
        self.update()

    def inc(self):
        self.add(1)

    def getScore(self):
        return self.val
