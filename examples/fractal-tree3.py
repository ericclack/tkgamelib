# Copyright 2016, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

import random, sys
sys.path.append('..')
from geekclub.pyscratch import *

# How much to change the length on each recursion
LENGTH_DELTA=0.5
# How random to make the tree
RANDOMNESS=0.1
# Smallest branch to draw in pixels
SMALLEST_BRANCH=3

create_canvas()


def random_change(v):
    # This random number is small if RANDOMNESS is small
    r = random.random()*RANDOMNESS
    # Make v bigger or smaller?
    if random.random() < 0.5:
        return v * (1 - r)
    else:
        return v * (1 + r)


def tree(branches, branch_angle, x, y, length, angle):

    if length < SMALLEST_BRANCH: return
    
    # Draw this branch
    length = random_change(length)
    angle = random_change(angle)
    x2, y2 = translate_point(x, y, length, angle)
    canvas().create_line(x,y, x2, y2, width=length/20, fill=random_colour(1,.5))
    
    # Draw a smaller tree at the end of this branch
    for i in range(branches):
        tree(branches, branch_angle, x2, y2, 
             length * LENGTH_DELTA, 
             angle+(branch_angle*(i-(branches/2))))

def draw_trees(event):
    clear_canvas()
    for y in range(5):
        for x in range(5):
            v = (1+x)+y*5
            tree(2 + (v % 5), 120 - (7*v), 
                 100 + x*150, 150 + y*150, length=70, angle=270)

draw_trees(None)

when_key_pressed('<space>', draw_trees)

banner("Press space to see more trees", 2000)

mainloop()
