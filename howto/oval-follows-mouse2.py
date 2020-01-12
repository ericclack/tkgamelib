# Copyright 2014, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

"""An oval that follows the mouse."""

import random
from packages import *

create_canvas()

oval = canvas().create_oval(100,100, 150,150)
sprite = Sprite(oval)
sprite.pen_down()

def move_towards_mouse():
    dx = (mouse_x() - sprite.x)
    dy = (mouse_y() - sprite.y)
    scale = 1+ abs(dx + dy)
    sprite.move(2 * dx / scale, 2 * dy / scale)


def move_here(event):
    sprite.move_to(event.x, event.y)


forever(move_towards_mouse, 50)
when_button1_clicked(move_here)

mainloop()
