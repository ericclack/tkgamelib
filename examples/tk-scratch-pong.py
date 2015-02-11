# Copyright 2014, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

"""A set of 5 sprites that follow each other with acceleration and pens"""

from tkinter import *
import random
from geekclub.pyscratch import *

create_canvas()

ball_img = PhotoImage(file='geekclub/images/face.gif')
bat_img = PhotoImage(file='geekclub/images/bat.gif')

ball = Sprite(ball_img)
ball.speed_x = random.randint(-4,4) * 2
ball.speed_y = random.randint(-4,4) * 2

bat = Sprite(bat_img)

def bat_follows_mouse():
    bat.move_to(mousex(), mousey())

def bounce_ball():
    ball.move_with_speed()
    ball.if_on_edge_bounce()
    if ball.touching(bat):
        ball.speed_y = -abs(ball.speed_y)
    
forever(bat_follows_mouse, 20)
forever(bounce_ball, 20)
mainloop()
