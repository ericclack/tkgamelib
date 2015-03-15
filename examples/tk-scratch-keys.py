# Copyright 2014, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

"""A small sprite and a big one, that follows"""

from tkinter import *
import random
from geekclub.pyscratch import *

create_canvas()

spriteimg = PhotoImage(file='../images/face.gif')
smallsprite = Sprite(spriteimg, 100, 100)

bigspriteimg = spriteimg.zoom(2,2)
bigsprite = Sprite(bigspriteimg, 500, 500)


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
    bigsprite.move_towards(spritex, spritey)

when_key_pressed('<Left>', move_left)
when_key_pressed('<Right>', move_right)
when_key_pressed('<Up>', move_up)
when_key_pressed('<Down>', move_down)

forever(move_bigsprite, 50)

mainloop()
