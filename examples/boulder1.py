# Copyright 2014, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

"""A Boulder Dash clone

TODO:
"""

import random, time, sys
from geekclub.pyscratch import *

create_canvas()

earth_img = PhotoImage(file='images/earth.gif')
boulder_img = PhotoImage(file='images/ball.gif')
fred_img = PhotoImage(file='images/smallface.gif')

BLOCK_SIZE=50

class MudSprite(ImageSprite):
    def __init__(self, x=0, y=0):
        super(MudSprite, self).__init__(earth_img, x, y)

class BoulderSprite(ImageSprite):
    def __init__(self, x=0, y=0):
        super(BoulderSprite, self).__init__(boulder_img, x, y)

class FredSprite(ImageSprite):
    def __init__(self, x=0, y=0):
        super(FredSprite, self).__init__(fred_img, x, y)

landscape = []
for y in range(20):
    landscape.append([])
    for x in range(20):
        if random.random() < 0.1:
            block = BoulderSprite()
        else:
            block = MudSprite()
        block.move_to(x*BLOCK_SIZE, y*BLOCK_SIZE)
        landscape[-1].append(block)

fred = FredSprite()
fred.move_to(0,0)


def move_left(event):
    fred.move(-BLOCK_SIZE, 0)

def move_right(event):
    fred.move(BLOCK_SIZE, 0)

def move_up(event): 
    fred.move(0, -BLOCK_SIZE)

def move_down(event):
    fred.move(0, BLOCK_SIZE)


world = Struct( level=1, status='play', landscape=landscape, fred=fred )

when_key_pressed('<Left>', move_left)
when_key_pressed('<Right>', move_right)
when_key_pressed('<Up>', move_up)
when_key_pressed('<Down>', move_down)
mainloop()
