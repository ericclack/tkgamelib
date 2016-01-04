# Copyright 2014, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

"""A set of 10 sprites that follow each other."""

from tkinter import *
import random
from geekclub.pyscratch import *

create_canvas()

spriteimg = PhotoImage(file='images/face.gif')

sprites = []
for x in range(10):
    sprites.append( ImageSprite(spriteimg,
                        random.randint(1,1000),
                        random.randint(1,1000)) )


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

def randomise_sprites(event):
    sprite = random.choice(sprites)
    sprite.move_to( random.randint(1,1000), random.randint(1,1000) )


forever(follow_mouse, 10)
when_button1_clicked(randomise_sprites)
mainloop()
