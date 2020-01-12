# Copyright 2014, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

"""A small sprite and a big one, that follows"""

import random
from packages import *

create_canvas()

spriteimg = PhotoImage(file='images/face.gif')
smallsprite = ImageSprite(spriteimg, 100, 100)

bigspriteimg = spriteimg.zoom(2,2)
bigsprite = ImageSprite(bigspriteimg, 500, 500)

def move_left(event):
    smallsprite.move(-5, 0)

def move_right(event):
    smallsprite.move(5, 0)

def move_up(event): 
    smallsprite.move(0, -5)

def move_down(event):
    smallsprite.move(0, 5)

def move_bigsprite():
    spritex, spritey = smallsprite.pos()
    bigsprite.accelerate_towards(spritex, spritey, 0.1)
    bigsprite.move_with_speed()

    if bigsprite.touching(smallsprite):
        smallsprite.move_to(50, 50)
        bigsprite.move_to(500, 500)

when_key_pressed('<Left>', move_left)
when_key_pressed('<Right>', move_right)
when_key_pressed('<Up>', move_up)
when_key_pressed('<Down>', move_down)

forever(move_bigsprite, 50)

mainloop()
