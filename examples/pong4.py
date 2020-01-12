# Copyright 2014, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

"""A simple bat and ball game. 

TODO:
- Move bricks down as you play, if the bricks hit the bottom
  you lose a life.
- If you can get the ball to the top you go to the next level.
"""

import random, time
from packages import *

create_canvas()

bat_img = PhotoImage(file='images/bat.gif')
ball_img = PhotoImage(file='images/ball.gif')
brick_img = PhotoImage(file='images/small_brick.gif')

bat = ImageSprite(bat_img)

ball = ImageSprite(ball_img)
ball.speed_x = random.randint(-4,4) * 2
ball.speed_y = random.randint(-4,4) * 2
ball.max_speed = 10
ball.move_to(CANVAS_WIDTH/2, CANVAS_HEIGHT/2)

def make_bricks_for_level(level):
    bricks = []
    for y in range(0, 100*level, 28):
        for x in range(0, CANVAS_WIDTH, 101):
            brick = ImageSprite(brick_img)
            brick.move_to(x, y)
            bricks.append(brick)
    return bricks

def bat_follows_mouse():
    bat.move_to(mouse_x(), mouse_y())

def bounce_ball():
    if world.status != 'play': return
    
    ball.move_with_speed()
    ball.if_on_edge_bounce()
    if ball.touching(bat):
        ball.bounce_up()
        ball.accelerate(1.05)
        mid_bat_x = bat.x + (bat.width / 2)
        ball.speed_x = (ball.x - mid_bat_x) / 10

    if ball.y < 10:
        next_level()
        
    # Has the ball hit the bottom of the screen?
    if ball.y >= CANVAS_HEIGHT - ball.height:
        end_game()

    # Has the ball touched a brick?
    brick = ball.touching_any(world.bricks)
    if brick:
        if brick.below(ball):
            ball.bounce_up()
        else:
            ball.bounce_down()
        world.bricks.remove(brick)
        brick.delete()

def next_level():
    banner("Next level!")
    world.status = 'next'
    ball.move_to(CANVAS_WIDTH/2, CANVAS_HEIGHT/2)
    future_action(next_level2, 1000)

def next_level2():
    for b in world.bricks:
        b.delete()
    world.level += 1
    world.bricks = make_bricks_for_level(world.level)
    banner("Ready...?")
    future_action(next_level3, 1000)

def next_level3():
    clear_banner()
    world.status = 'play'

def move_bricks_down():
    if world.status != 'play': return
    for b in world.bricks:
        b.move(0, 5)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

world = Struct( level=1, status='play', bricks=make_bricks_for_level(1) )

forever(bat_follows_mouse, 20)
forever(bounce_ball, 20)
forever(move_bricks_down, 1000)
mainloop()
