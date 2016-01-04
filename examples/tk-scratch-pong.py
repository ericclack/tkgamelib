# Copyright 2014, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

"""A simple bat and ball game. """

from tkinter import *
import random
from geekclub.pyscratch import *

create_canvas()

ball_img = PhotoImage(file='images/face.gif')
bat_img = PhotoImage(file='images/bat.gif')

ball = ImageSprite(ball_img)
ball.speed_x = random.randint(-4,4) * 2
ball.speed_y = random.randint(-4,4) * 2

bat = ImageSprite(bat_img)

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
