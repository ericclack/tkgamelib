# Copyright 2014, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

"""A Boulder Dash clone

DONE:
- Push boulders left or right
- Stop going off edge of screen
- Gems to collect
- r to restart
- Die if a boulder falls on you
- Some way to save and reload one level
- Boulder on boulder falls into gap (either side)

TODO:
- Some way to load multiple levels
- Aliens
"""

import random, time
from geekclub_packages import *

BLOCK_SIZE=50
SCREEN_SIZE=16

create_canvas()

block_images = {
    'mud': PhotoImage(file='images/earth.gif'),
    'boulder': PhotoImage(file='images/ball.gif'),
    'wall': PhotoImage(file='images/wall.gif'),
    'gem': PhotoImage(file='images/gem.gif'),
}

fred_img = PhotoImage(file='images/smallface.gif')

class BlockSprite(ImageSprite):
    def __init__(self, what, x=0, y=0):
        self.what = what
        self.falling = False
        image = block_images[what]
        super(BlockSprite, self).__init__(image, x, y)

    def is_a(self, what):
        return (self.what == what)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def block_choices():
    """More gems, boulders and walls the higher the level"""
    c1 = ['mud'] * 20
    c2 = ['wall', 'boulder', 'gem'] * world.level
    c1.extend(c2)
    return c1

def block_at_xy(x, y, landscape_data=None):
    if landscape_data:
        what = landscape_data[y][x]
        return what if what != 'None' else None
    if x == 2 and y == 2:
        # This is where fred starts
        what = None
    elif x in (0, (SCREEN_SIZE-1)) or y in (0, (SCREEN_SIZE-1)):
        what = 'wall'
    else:
        what = random.choice(block_choices())
    return what

def make_landscape(landscape_data=None):
    """Generate or load a landscape"""
    landscape = []
    for y in range(SCREEN_SIZE):
        landscape.append([])
        for x in range(SCREEN_SIZE):
            what = block_at_xy(x, y, landscape_data)
            if what:
                block = BlockSprite(what)
                block.move_to(x*BLOCK_SIZE, y*BLOCK_SIZE)
            else:
                block = None
            landscape[-1].append(block)
    return landscape

def dump_landscape():
    """Output landscape in a way that can be reloaded"""
    print('level', world.level)
    for row in world.landscape:
        srow = [r.what if r else 'None' for r in row]
        print(','.join(srow))

def clear_landscape():
    for row in world.landscape:
        for i in row:
            if i: i.delete()
    landscape = []

def coords(sprite):
    cx, cy = sprite.pos()
    cx = int(cx/BLOCK_SIZE); cy = int(cy/BLOCK_SIZE)
    return (cx, cy)

def all_blocks_of(what):
    b = []
    for rows in world.landscape:
        for i in rows:
            if i and i.is_a(what):
                b.append(i)
    return b

def all_boulders():
    return all_blocks_of('boulder')

def all_gems():
    return all_blocks_of('gem')

def what_is_next_to(sprite, dx, dy):
    cx, cy = coords(sprite)
    if sprite != fred and (cx+dx, cy+dy) == coords(fred):
        return fred
    try:
        return world.landscape[cy+dy][cx+dx]    
    except IndexError:
        return None

def what_is_below(sprite): return what_is_next_to(sprite, 0, 1)
def what_is_left_of(sprite): return what_is_next_to(sprite, -1, 0)
def what_is_right_of(sprite): return what_is_next_to(sprite, 1, 0)
def nothing_left_and_lbelow(sprite):
    return (what_is_left_of(sprite) is None 
            and what_is_next_to(sprite, -1, 1) is None)
def nothing_right_and_rbelow(sprite):
    return (what_is_right_of(sprite) is None 
            and what_is_next_to(sprite, 1, 1) is None)

def can_move(dx, dy):
    sprite = what_is_next_to(fred, dx, dy)
    return sprite is None or sprite.is_a('mud') or sprite.is_a('gem')

def set_landscape(a_pair, what):
    x, y = a_pair
    world.landscape[y][x] = what

def clear_block():
    """Clear the block that fred just landed on"""
    x, y = coords(fred)
    block = world.landscape[y][x]
    if block:
        world.landscape[y][x] = None
        if block.is_a('gem'): world.gems_left -= 1
        block.delete()

def move(dx, dy):
    if world.status != 'play': return

    if can_move(dx, dy):
        fred.move(dx*BLOCK_SIZE, dy*BLOCK_SIZE)
        clear_block()
        if world.gems_left <= 0:
            banner("Well done!")
            world.status = 'next_level'
    elif dy == 0:
        next_block = what_is_next_to(fred, dx, 0)
        next_next_block = what_is_next_to(fred, dx*2, 0)
        if next_block.is_a('boulder') and next_next_block is None:
            # We can move a boulder
            set_landscape(coords(next_block), None)
            next_block.move(dx*BLOCK_SIZE, 0)
            set_landscape(coords(next_block), next_block)
            # Now we can move too
            fred.move(dx*BLOCK_SIZE, 0)
        
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# World set up
#

world = Struct( level=1, status='play', fred=None, 
                landscape=None, gems_left=None )

# These require previous world things to be defined
world.landscape = make_landscape() 
dump_landscape()

fred = ImageSprite(fred_img)
fred.move_to(2*BLOCK_SIZE,2*BLOCK_SIZE)
world.fred = fred

world.gems_left = len(all_gems())

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Events and actions
#

def move_left(event):
    move(-1, 0)

def move_right(event):
    move(1, 0)

def move_up(event): 
    move(0, -1)

def move_down(event):
    move(0, 1)

def boulder_fall_down(b, left_right=0):
    set_landscape(coords(b), None)
    b.move(left_right*BLOCK_SIZE, BLOCK_SIZE)
    b.falling = True
    set_landscape(coords(b), b)

def boulders_fall():
    if world.status != 'play': return

    for b in all_boulders():
        below = what_is_below(b)
        if below is None:
            boulder_fall_down(b)
        elif below == world.fred:
            if b.falling:
                banner("Ouch!")
                world.status = 'end'
        elif below.what in ('boulder', 'gem'):
            if nothing_left_and_lbelow(b) and nothing_right_and_rbelow(b):
                boulder_fall_down(b, left_right=random.choice([-1,1]))
            elif nothing_left_and_lbelow(b):
                boulder_fall_down(b, left_right=-1)
            elif nothing_right_and_rbelow(b):
                boulder_fall_down(b, left_right=1)
        else:
            b.falling = False
        
def start_level(event):
    """Start or restart a level"""
    world.status = 'building'
    clear_banner()
    clear_landscape()
    world.landscape = make_landscape() 
    fred.move_to(2*BLOCK_SIZE,2*BLOCK_SIZE)
    world.gems_left = len(all_gems())
    world.status = 'play'
    dump_landscape()

def load_level(event):
    level = askstring("What level to load?", "Level")

    file = open("boulder-levels/level-%s.txt" % level)
    landscape_data = [l.strip().split(',') for l in file.readlines()]
    file.close()

    world.status = 'loading'
    clear_banner()
    clear_landscape()
    world.landscape = make_landscape(landscape_data)
    fred.move_to(2*BLOCK_SIZE,2*BLOCK_SIZE)
    world.gems_left = len(all_gems())
    world.status = 'play'

def check_status():
    if world.status == 'next_level':
        world.level += 1
        start_level(None)
    if world.status == 'end':
        end_game()
        

when_key_pressed('<Left>', move_left)
when_key_pressed('<Right>', move_right)
when_key_pressed('<Up>', move_up)
when_key_pressed('<Down>', move_down)
when_key_pressed('r', start_level)
when_key_pressed('l', load_level)

forever(boulders_fall, 200)
forever(check_status, 1000)
mainloop()
