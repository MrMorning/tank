from utils import *
import pygame, sys, math
from bg import *
from game import *

game = TankGame()

game.tank1.update()
game.tank2.update()
keySet1 = {pygame.K_s, pygame.K_w, pygame.K_d, pygame.K_a}
keySet2 = {pygame.K_DOWN, pygame.K_UP, pygame.K_RIGHT, pygame.K_LEFT}
game.titleStart()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                Add(game, pygame.event.Event(pygame.KEYDOWN, {"unicode": 123, "key": pygame.K_a}))
                game.tank1.rotate(game.tank1.omega)
                game.tank1.update()
            elif event.key == pygame.K_d:
                Add(game, pygame.event.Event(pygame.KEYDOWN, {"unicode": 123, "key": pygame.K_d}))
                game.tank1.rotate(-game.tank1.omega)
                game.tank1.update()
            elif event.key == pygame.K_s:
                Add(game, pygame.event.Event(pygame.KEYDOWN, {"unicode": 123, "key": pygame.K_s}))
                game.tank1.move(angleToDirection(game, game.tank1.angle + 180))
                game.tank1.update()
            elif event.key == pygame.K_w:
                Add(game, pygame.event.Event(pygame.KEYDOWN, {"unicode": 123, "key": pygame.K_w}))
                game.tank1.move(angleToDirection(game, game.tank1.angle))
                game.tank1.update()
            elif event.key == pygame.K_LEFT:
                Add(game, pygame.event.Event(pygame.KEYDOWN, {"unicode": 123, "key": pygame.K_LEFT}))
                game.tank2.rotate(game.tank2.omega)
                game.tank2.update()
            elif event.key == pygame.K_RIGHT:
                Add(game, pygame.event.Event(pygame.KEYDOWN, {"unicode": 123, "key": pygame.K_RIGHT}))
                game.tank2.rotate(-game.tank2.omega)
                game.tank2.update()
            elif event.key == pygame.K_DOWN:
                Add(game, pygame.event.Event(pygame.KEYDOWN, {"unicode": 123, "key": pygame.K_DOWN}))
                game.tank2.move(angleToDirection(game, game.tank2.angle + 180))
                game.tank2.update()
            elif event.key == pygame.K_UP:
                Add(game, pygame.event.Event(pygame.KEYDOWN, {"unicode": 123, "key": pygame.K_UP}))
                game.tank2.move(angleToDirection(game, game.tank2.angle))
                game.tank2.update()
            elif event.key == pygame.K_g:
                game.tank1.shoot(1)
            elif event.key == pygame.K_SLASH:
                game.tank2.shoot(2)
            elif event.key == pygame.K_1:
                game.startFlag = 1
            elif event.key == pygame.K_2:
                game.startFlag = 2
            elif event.key == pygame.K_ESCAPE:
                game.startFlag = 0
                game.titleStart()

        elif event.type == pygame.KEYUP:
            newEvent = pygame.event.Event(pygame.KEYDOWN, {"unicode": 123, "key": event.key})
            flag = 0
            for e in game.uevent:
                if(e.key == newEvent.key):
                    flag = 1
            if(flag):
                game.uevent.remove(newEvent)
    #
    if(game.startFlag == 2):
        # print(len(game.uevent))
        for event in game.uevent:
            pygame.event.post(event)
        # print("he")
        # print(len(bulletQueue))
        game.screen.fill(BLACK)
        # print(tank1.pos)
        iterateQueue(game)
        checkCollapse(game)
        game.update()
    pygame.display.update()
    game.fclock.tick(game.fps)
