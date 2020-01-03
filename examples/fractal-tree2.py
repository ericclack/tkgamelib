# Copyright 2016, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

import random
from packages import *

# How much to change the length on each recursion
LENGTH_DELTA=0.5
# How random to make the tree
RANDOMNESS=0.02

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

    if length < 5: return
    
    # Draw this branch
    length = random_change(length)
    angle = random_change(angle)
    x2, y2 = translate_point(x, y, length, angle)
    canvas().create_line(x,y, x2, y2, width=length/20)
    
    # Draw a smaller tree at the end of this branch
    for i in range(branches):
        tree(branches, branch_angle, x2, y2, 
             length * LENGTH_DELTA, 
             angle+(branch_angle*(i-(branches/2))))

for y in range(2):
    for x in range(2):
        v = (1+x)+y*2
        tree(3+v, 50 - (7*v), 200 + x*350, 380 + y*360, length=170, angle=270)

mainloop()
