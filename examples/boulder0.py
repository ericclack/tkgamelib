# Copyright 2014, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

"""A Boulder Dash clone

TODO:
- Everything!
"""

import random, time, sys
sys.path.append('..')
from geekclub.pyscratch import *

create_canvas()

fred_img = PhotoImage(file='images/smallface.gif')

BLOCK_SIZE=50

class FredSprite(ImageSprite):
    def __init__(self, x=0, y=0):
        super(FredSprite, self).__init__(fred_img, x, y)

fred = FredSprite()
fred.move_to(0,0)

def move(dx, dy):
    fred.move(dx*BLOCK_SIZE, dy*BLOCK_SIZE)

def move_right(event):
    move(1, 0)

def move_down(event):
    move(0, 1)

when_key_pressed('<Right>', move_right)
when_key_pressed('<Down>', move_down)
mainloop()
