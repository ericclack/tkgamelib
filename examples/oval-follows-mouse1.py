# Copyright 2014, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

"""An oval that follows the mouse, but only when you move it."""

import random, sys
sys.path.append('..')
from geekclub.pyscratch import *

create_canvas()

oval = canvas().create_oval(100,100, 150,150)
sprite = Sprite(oval)

def move_towards_mouse(event):
    x = sign(event.x - sprite.x)
    y = sign(event.y - sprite.y)
    sprite.move(x, y)

def move_away_from_mouse(event):
    x = sign(event.x - sprite.x)
    y = sign(event.y - sprite.y)
    sprite.move(-x*15, -y*15)

when_mouse_motion(move_towards_mouse)
when_button1_clicked(move_away_from_mouse)

mainloop()
