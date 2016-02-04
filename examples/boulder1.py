# Copyright 2014, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

"""A Boulder Dash clone

TODO:
- Push boulders left or right
- Stop going off edge of screen
- Gems to collect
- Die if a boulder falls on you
- Aliens
"""

import random, time, sys
sys.path.append('..')
from geekclub.pyscratch import *

create_canvas()

earth_img = PhotoImage(file='images/earth.gif')
boulder_img = PhotoImage(file='images/ball.gif')
fred_img = PhotoImage(file='images/smallface.gif')
edge_img = PhotoImage(file='images/ball.gif')

BLOCK_SIZE=50

class MudSprite(ImageSprite):
    def __init__(self, x=0, y=0):
        super(MudSprite, self).__init__(earth_img, x, y)

class BoulderSprite(ImageSprite):
    def __init__(self, x=0, y=0):
        super(BoulderSprite, self).__init__(boulder_img, x, y)

class EdgeSprite(ImageSprite):
    def __init__(self, x=0, y=0):
        super(EdgeSprite, self).__init__(edge_img, x, y)

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

def is_mud(sprite):
    return isinstance(sprite, MudSprite)

def coords(sprite):
    cx, cy = sprite.pos()
    cx = int(cx/BLOCK_SIZE); cy = int(cy/BLOCK_SIZE)
    return (cx, cy)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

world = Struct( level=1, status='play', landscape=landscape, fred=fred )

def what_is_next_to(sprite, dx, dy):
    cx, cy = coords(sprite)
    if sprite != fred and (cx+dx, cy+dy) == coords(fred):
        return fred
    try:
        return landscape[cy+dy][cx+dx]    
    except IndexError:
        return EdgeSprite()

def can_move(dx, dy):
    what = what_is_next_to(fred, dx, dy)
    return what is None or is_mud(what)

def set_landscape(a_pair, what):
    x, y = a_pair
    landscape[y][x] = what

def delete_mud():
    x, y = coords(fred)
    mud = landscape[y][x]
    if mud:
        landscape[y][x] = None
        mud.delete()

def move(dx, dy):
    if can_move(dx, dy):
        fred.move(dx*BLOCK_SIZE, dy*BLOCK_SIZE)
        delete_mud()

def move_left(event):
    move(-1, 0)

def move_right(event):
    move(1, 0)

def move_up(event): 
    move(0, -1)

def move_down(event):
    move(0, 1)

def all_boulders():
    b = []
    for rows in landscape:
        for i in rows:
            if isinstance(i, BoulderSprite):
                b.append(i)
    return b

def boulders_fall():
    for b in all_boulders():
        if what_is_next_to(b, 0, 1) is None:
            set_landscape(coords(b), None)
            b.move(0, BLOCK_SIZE)
            set_landscape(coords(b), b)

when_key_pressed('<Left>', move_left)
when_key_pressed('<Right>', move_right)
when_key_pressed('<Up>', move_up)
when_key_pressed('<Down>', move_down)
forever(boulders_fall, 200)
mainloop()
