# Copyright 2014, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

"""An oval that follows the mouse, but only when you move it."""

from tkinter import *
import random
from geekclub.pyscratch import *

create_canvas()

spriteid = canvas().create_oval(100,100, 150,150)

def direction(mouse, obj):
    if mouse > obj:
        return 1
    else:
        return -1

def move_towards_mouse(event):
    bbox = canvas().bbox(spriteid)
    x = direction(event.x, bbox[0])
    y = direction(event.y, bbox[1])
    canvas().move(spriteid, x, y)

def move_away_from_mouse(event):
    bbox = canvas().bbox(spriteid)
    x = direction(event.x, bbox[0])
    y = direction(event.y, bbox[1])
    canvas().move(spriteid, -x*15, -y*15)

def clear(event):
    canvas().delete(ALL)

when_mouse_motion(move_towards_mouse)
when_button1_clicked(move_away_from_mouse)
#when_key_pressed('C', clear)

mainloop()
