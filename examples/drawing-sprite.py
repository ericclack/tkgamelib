# Copyright 2014, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

"""A drawing sprite, click to toggle the pen."""

import random
from packages import *

create_canvas()

spriteimg = PhotoImage(file='images/face.gif')

sprite = ImageSprite(spriteimg,
             random.randint(1,1000),
             random.randint(1,1000))
sprite.pen_down()
sprite.pen_width = 4


def follow_mouse():
    sprite.move_towards(mousex(), mousey(), 2)

def toggle_pen(event):
    sprite.toggle_pen()
    sprite.pen_colour(random.randint(1,360))

def clear(event):
    if messagebox.askokcancel("Clear canvas?", "Are you sure you want to clear the canvas?"):
        clear_pen()

forever(follow_mouse, 10)
when_button1_clicked(toggle_pen)
when_button2_clicked(clear)
mainloop()
