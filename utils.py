import math

def iterateQueue(game):
    for bullet in game.bulletQueue:
        bullet.move(angleToDirection(game, bullet.angle))
        bullet.update()
        if bullet.collapse():
            game.bulletQueue.remove(bullet)

def angleToDirection(game, angle):
    return [game.tank1.speed * math.cos(math.radians(angle)), -game.tank1.speed * math.sin(math.radians(angle))]

def Add(game, event):
    for e in game.uevent:
        if(e == event):
            return
    game.uevent.append(event)

def checkCollapse(game):
    if(abs(game.tank1.pos[0] - game.tank2.pos[0]) < game.tank1.width / 2 and abs(game.tank2.pos[1] - game.tank1.pos[1]) < game.tank1.height / 2):
        game.restart()
