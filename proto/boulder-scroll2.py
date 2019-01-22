# Copyright 2018-19, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

"""A Boulder Dash clone

DONE:
- Scrolling, with Fred always in the middle

TODO:
- Bigger landscape
"""

from geekclub_packages import *
import random, time

BLOCK_SIZE=50
SCREEN_SIZE=32
FRED_START=8 #(16,16)

create_canvas()

block_images = {
    'mud': PhotoImage(file='../examples/images/earth.gif'),
    'boulder': PhotoImage(file='../examples/images/ball.gif'),
    'wall': PhotoImage(file='../examples/images/wall.gif'),
    'gem': PhotoImage(file='../examples/images/gem.gif'),
}

fred_img = PhotoImage(file='../examples/images/smallface.gif')

class BlockSprite(ImageSprite):
    def __init__(self, what, x=0, y=0):
        self.landscape_x = x; self.landscape_y = y
        self.what = what
        self.falling = False
        image = block_images[what]
        super(BlockSprite, self).__init__(image)
        self.move_to(x*BLOCK_SIZE, y*BLOCK_SIZE)

    def is_a(self, what):
        return (self.what == what)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def block_choices():
    """More gems, boulders and walls the higher the level"""
    c1 = ['mud'] * 20
    c2 = ['wall', 'boulder', 'gem'] * world.level
    c1.extend(c2)
    return c1

def make_landscape():
    landscape = []
    for y in range(SCREEN_SIZE):
        landscape.append([])
        for x in range(SCREEN_SIZE):
            if x == FRED_START and y == FRED_START:
                # This is where fred starts
                what = None
            elif x in (0, (SCREEN_SIZE-1)) or y in (0, (SCREEN_SIZE-1)):
                what = 'wall'
            else:
                what = random.choice(block_choices())
                
            if what:
                block = BlockSprite(what, x, y)
                #block.move_to(x*BLOCK_SIZE, y*BLOCK_SIZE)
            else:
                block = None
            landscape[-1].append(block)
    return landscape

def clear_landscape():
    for row in world.landscape:
        for i in row:
            if i: i.delete()
    landscape = []

def coords(sprite):
    return (sprite.landscape_x, sprite.landscape_y)

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

def move_landscape(dx, dy):
    for rows in world.landscape:
        for i in rows:
            if i: i.move(dx*BLOCK_SIZE, dy*BLOCK_SIZE)

def move_fred(dx, dy):
    fred.landscape_x += dx; fred.landscape_y += dy
    move_landscape(-dx, -dy)

def move(dx, dy):
    if world.status != 'play': return

    if can_move(dx, dy):
        move_fred(dx, dy)        
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
            next_block.landscape_x += dx
            set_landscape(coords(next_block), next_block)
            # Now we can move too
            fred.landscape_x += dx
            move_landscape(-dx, 0)
        
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# World set up
#

world = Struct( level=1, status='play', fred=None, 
                landscape=None, gems_left=None )

# These require previous world things to be defined
world.landscape = make_landscape() 

fred = ImageSprite(fred_img)
# Fred is always in the centre
fred.landscape_x = fred.landscape_y = FRED_START
fred.move_to(FRED_START*BLOCK_SIZE, FRED_START*BLOCK_SIZE)
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

def boulders_fall():
    for b in all_boulders():
        what = what_is_next_to(b, 0, 1)
        if what is None:
            set_landscape(coords(b), None)
            b.move(0, BLOCK_SIZE)
            b.landscape_y += 1
            b.falling = True
            set_landscape(coords(b), b)
        else:
            if what is world.fred and b.falling:
                banner("Ouch!")
                world.status = 'end'
            else:
                b.falling = False

def start_level(event):
    """Start or restart a level"""
    world.status = 'building'
    clear_banner()
    clear_landscape()
    fred.move_to(FRED_START*BLOCK_SIZE,FRED_START*BLOCK_SIZE)
    fred.landscape_x = fred.landscape_y = FRED_START
    world.landscape = make_landscape() 
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

forever(boulders_fall, 200)
forever(check_status, 1000)
mainloop()
