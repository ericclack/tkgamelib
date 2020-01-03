# Copyright 2014, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

"""A set of 5 sprites that follow each other with acceleration and pens"""

import random
from packages import *

create_canvas()

img = PhotoImage(file='images/face.gif')

sprites = []
m = 10
for x in range(5):
    sprite = ImageSprite(img)
    sprite.move_to_random_pos()
    sprite.max_speed = m
    sprite.pen_width = 4
    sprite.pen_down()
    
    sprites.append(sprite)
    # Each sprite gets a bit slower than the last one
    m = m * 0.9


def follow_mouse():
    """The first sprite follows the mouse, the others follow each other"""
    
    firstsprite = sprites[0]
    firstsprite.accelerate_towards(mousex(), mousey(), 0.5)
    
    followsprite = firstsprite
    for sprite in sprites[1:]:
        fx, fy = followsprite.pos()
        sprite.accelerate_towards(fx, fy, 0.5)
        followsprite = sprite

    for sprite in sprites:
        sprite.move_with_speed()

def toggle_pens(event):
    for sprite in sprites:
        sprite.toggle_pen()

def clear(event):
    if messagebox.askokcancel("Clear canvas?", "Are you sure you want to clear the canvas?"):
        clear_pen()


forever(follow_mouse, 10)
when_button1_clicked(toggle_pens)
when_button2_clicked(clear)
mainloop()
