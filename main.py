# Created by Chen Geng
# 2020/03/14

# Descpription: this file is main flow of the game
# IMPORTANT: more comment are contained in class and method specifications!
# If you use PyCharm, you can use Ctrl + Q to check documentation of a class or method.
# If you have more problems, please contact gengchen AT zju DOT edu DOT cn
# or contact unrealgengchen AT gmail DOT com
# This project will be open sourced on Github after being handed in.
# So please give it a STAR if possible!
# My github homepage is: http://github.com/MrMorning
from utils import *
import pygame, sys, math
from bg import *
from game import *

game = TankGame()
## Init game from TankGame class(in bg.py)


game.tank1.update()
game.tank2.update()
game.titleStart()
## start from title
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                Add(game, pygame.event.Event(pygame.KEYDOWN, {"unicode": 123, "key": pygame.K_a}))
                # make pressing for a long time possible
                # Add() is a function declared in utils.py,
                # which maintain a queue of events.
                # every time the screen get flushed, we will scan this queue
                # and add events in this queue to the Pygame Event Queue
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
            elif event.key == pygame.K_LEFT and game.startFlag == 2:
                Add(game, pygame.event.Event(pygame.KEYDOWN, {"unicode": 123, "key": pygame.K_LEFT}))
                game.tank2.rotate(game.tank2.omega)
                game.tank2.update()
            elif event.key == pygame.K_RIGHT and game.startFlag == 2:
                Add(game, pygame.event.Event(pygame.KEYDOWN, {"unicode": 123, "key": pygame.K_RIGHT}))
                game.tank2.rotate(-game.tank2.omega)
                game.tank2.update()
            elif event.key == pygame.K_DOWN and game.startFlag == 2:
                Add(game, pygame.event.Event(pygame.KEYDOWN, {"unicode": 123, "key": pygame.K_DOWN}))
                game.tank2.move(angleToDirection(game, game.tank2.angle + 180))
                game.tank2.update()
            elif event.key == pygame.K_UP and game.startFlag == 2:
                Add(game, pygame.event.Event(pygame.KEYDOWN, {"unicode": 123, "key": pygame.K_UP}))
                game.tank2.move(angleToDirection(game, game.tank2.angle))
                game.tank2.update()
            elif event.key == pygame.K_g:
                game.tank1.shoot(1)
            elif event.key == pygame.K_SLASH and game.startFlag == 2:
                game.tank2.shoot(2)
            elif event.key == pygame.K_1:
                game.startFlag = 1
            elif event.key == pygame.K_2:
                game.startFlag = 2
            elif event.key == pygame.K_ESCAPE:
                game.startFlag = 0
                game.titleStart()

        elif event.type == pygame.KEYUP:
            # if key up, we will remove the event from the queue
            # so the event will not be added to event queue any more
            newEvent = pygame.event.Event(pygame.KEYDOWN, {"unicode": 123, "key": event.key})
            flag = 0
            for e in game.uevent:
                if (e.key == newEvent.key):
                    flag = 1
            # to see if this event is in the queue
            if flag:
                game.uevent.remove(newEvent)
    #
    if (game.startFlag == 2):
        # game.startFlag means which type
        # 1 means single player
        # 2 means double player
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
    elif (game.startFlag == 1):
        game.tank2.speed = 0.2
        # slow down the ai, because the ai is so niubi
        game.tank2.move(angleToDirection(game, getAttackAngle(game)))
        game.tank2.rotateTo(getAttackAngle(game))
        if game.clock % 300 == 150:
            game.tank2.shoot(2)
        # shoot every 1 second
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
    game.clock += 1
    game.fclock.tick(game.fps)
