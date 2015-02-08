# Copyright 2014, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

"""A set of 5 sprites that follow each other with acceleration and pens"""

import random, time
from geekclub.pyscratch import *

create_canvas()

bat_img = PhotoImage(file='geekclub/images/bat.gif')
ball_img = PhotoImage(file='geekclub/images/ball.gif')
brick_img = PhotoImage(file='geekclub/images/small_brick.gif')

bat = Sprite(bat_img)

ball = Sprite(ball_img)
ball.speed_x = random.randint(-4,4) * 2
ball.speed_y = random.randint(-4,4) * 2
ball.max_speed = 10
ball.move_to(CANVAS_WIDTH/2, CANVAS_HEIGHT/2)

bricks = []
for y in range(0, 400, 30):
    for x in range(0, CANVAS_WIDTH, 110):
        brick = Sprite(brick_img)
        brick.move_to(x, y)
        bricks.append(brick)
    

def bat_follows_mouse():
    bat.move_to(mousex(), mousey())

def bounce_ball():
    ball.move_with_speed()
    ball.if_on_edge_bounce()
    if ball.touching(bat):
        ball.speed_y = -abs(ball.speed_y)
        ball.accelerate(1.05)

    # Has the ball hit the bottom of the screen?
    if ball.y() > CANVAS_HEIGHT - 10:
        # Not sure how to quit!
        time.sleep(10)

    # Has the ball touched a brick?
    brick = ball.touching_any(bricks)
    if brick:
        if brick.below(ball):
            ball.speed_y = abs(ball.speed_y)            
        else:
            ball.speed_y = -abs(ball.speed_y)
        bricks.remove(brick)
        brick.delete()

    
forever(bat_follows_mouse, 20)
forever(bounce_ball, 20)
mainloop()
