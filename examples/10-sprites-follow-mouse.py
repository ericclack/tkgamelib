# Copyright 2014, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

"""A list of 10 sprites that follow each other, and the mouse."""

import random
from geekclub_packages import *

create_canvas()

spriteimg = PhotoImage(file='images/face.gif')

sprites = []
for x in range(10):
    i = ImageSprite(spriteimg)
    i.move_to_random_pos()
    i.pen_width = 2
    i.pen_down()
    sprites.append(i)

def follow_mouse():
    """The first sprite follows the mouse, the others follow each other"""
    
    steps = len(sprites)/2
    firstsprite = sprites[0]
    firstsprite.move_towards(mousex(), mousey(), steps)
    
    followsprite = firstsprite
    for sprite in sprites[1:]:
        steps = steps - 0.5
        fx, fy = followsprite.pos()
        sprite.move_towards(fx, fy, steps)
        followsprite = sprite

def clear(event):
    clear_pen()

forever(follow_mouse, 10)
when_button1_clicked(clear)
mainloop()
