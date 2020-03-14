# Tank
> a game written for acee

## Description
In the game, there are two tanks, and tank1 is in the left-top corner, the tank2 is in the right-bottom corner.

you can use `W` to let tank1 move forward and `D` to let it move backward. use `A` to let tank1 rotate left and `D` to the right side.

similarly, you can use `UP` `DOWN` `RIGHT` `LEFT` to control tank2, following the similar rule.

When you enter the welcome page, you can press `1` to enter single player mode and `2` to enter double player mode.

When you want to return to title page, please press `ESC`.

In single player mode, you will meet a powerful AI tank! Try your best to beat it !

## How can you play it
The only requirements of this game is `pygame` library, which you can install by:
```bash
pip install pygame
```
then, just simply run
```bash
python main.py
```
Enjoy yourself !

## Features of this game
* smoothly move and rotate, just like in the reality
* control two car at the same time
* move and rotate simutaneously
* pressing a button for a long time is supported
* we have an AI :-)
* game is paused when the window is not active


## description on files
* `main.py` main program, controling pygame running frame.
* `game.py` define `GameObject` class and its subclass `Tank` and `Bullet`
* `bg.py` define `TankGame` class containing global config and variables of this game.
* `utils.py` includes multiple miscellous functions
* `assets` include assets we use in this game

## PR, stars and issues are welcomed!