# Copyright 2016, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

import random, sys
sys.path.append('..')
from geekclub.pyscratch import *

BRANCHES = 6
BRANCH_ANGLE=30
LENGTH_DELTA=0.5
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


def tree(x, y, length, angle):

    if length < 5: return
        
    length = random_change(length)
    angle = random_change(angle)
    x2, y2 = translate_point(x, y, length, angle)
    canvas().create_line(x,y, x2, y2, width=length/20)
    
    for i in range(BRANCHES):
        tree(x2, y2, length * LENGTH_DELTA, 
             angle+(BRANCH_ANGLE*(i-(BRANCHES/2))))

for y in range(2):
    for x in range(2):
        tree(200 + x*350, 380 + y*350, length=180, angle=270)

mainloop()
