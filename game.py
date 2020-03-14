import pygame, sys, math

class GameObj:
    def __init__(self, env, path, pos, angle):
        self.env = env
        self.pos = pos.copy()
        self.surf = pygame.image.load(path)
        self.angle = angle
        self.surf = pygame.transform.rotate(self.surf, self.angle)
        self.path = path
        self.speed = 1
        self.omega = 1
        self.prop = 0

    def update(self):
        sr = self.surf.get_rect()
        sr.centerx = self.pos[0]
        sr.centery = self.pos[1]
        # screen.fill(BLACK)
        self.env.screen.blit(self.surf, sr)

    def move(self, direction):
        if not pygame.display.get_active():
            return
        ## Pause when the screen is not active
        self.pos[0] += direction[0] * self.speed
        self.pos[1] += direction[1] * self.speed
        if self.prop == 1 and (self.pos[0] <= 0 or self.pos[0] >= self.env.width or self.pos[1] <= 0 or self.pos[1] >= self.env.height):
            self.pos[0] -= direction[0] * self.speed
            self.pos[1] -= direction[1] * self.speed

    def rotateTo(self, angle):
        if not pygame.display.get_active():
            return
        ## Pause when the screen is not active
        self.angle = angle
        self.surf = pygame.image.load(self.path)
        self.surf = pygame.transform.rotate(self.surf, self.angle)
        self.update()

    def rotate(self, deltaAngle):
        if not pygame.display.get_active():
            return
        ## Pause when the screen is not active
        self.angle += deltaAngle
        self.surf = pygame.image.load(self.path)
        self.surf = pygame.transform.rotate(self.surf, self.angle)
        self.update()


class Tank(GameObj):
    width = 80
    height = 80

    def __init__(self, env, path, para_pos, para_angle):
        GameObj.__init__(self, env, path=path, pos=para_pos, angle=para_angle)
        self.prop = 1
    def shoot(self, ind):
        if not pygame.display.get_active():
            return
        ## Pause when the screen is not active
        bullet = Bullet(self.env, para_pos = self.pos, para_angle = self.angle, belong = ind)
        bullet.update()
        self.env.bulletQueue.append(bullet)
        effect = pygame.mixer.Sound('assets/boom.wav')
        effect.play()


class Bullet(GameObj):
    path = 'assets/shot.gif'
    speed = 3

    def __init__(self, env, para_pos, para_angle, belong):
        GameObj.__init__(self, env, path=self.path, pos=para_pos, angle=para_angle)
        self.surf = pygame.transform.rotate(self.surf, -90)
        self.belong = belong
        self.prop = 2

    def collapse(self):
        # self.rect = self.surf.get_rect()
        # print(self.rect.right, self.rect.left)
        if(self.pos[0] >= self.env.width or self.pos[0] <= 0 or self.pos[1] <= 0 or self.pos[1] >= self.env.height):
            # print("True")
            return True
        elif(self.belong == 2 and (abs(self.pos[0] - self.env.tank1.pos[0]) <= self.env.tank1.width / 2 and abs(self.pos[1] - self.env.tank1.pos[1]) < self.env.tank1.height / 2)):
            self.env.score2.inc()
            self.env.bulletQueue = []
            self.env.restart()
            return True
        elif(self.belong == 1 and (abs(self.pos[0] - self.env.tank2.pos[0]) <= self.env.tank2.width / 2 and abs(self.pos[1] - self.env.tank2.pos[1]) < self.env.tank2.height / 2)):
            self.env.score1.inc()
            self.env.bulletQueue = []
            self.env.restart()
            return True
        # print("False")
        return False
