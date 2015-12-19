# Copyright 2014, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

"""Test out of python for Racket stars game"""

import random, time
from geekclub.pyscratch import *

create_canvas()


stars = []
for i in range(200):
    x, y = random.randint(0, CANVAS_WIDTH), random.randint(0, CANVAS_HEIGHT)
    stars.append(canvas().create_oval(x, y, x+5, y+5))
    


def move_stars():
    for starid in stars:
        bbox = canvas().bbox(starid)
        x, y = bbox[0], bbox[1]
        if x < 0 or x > CANVAS_WIDTH or y < 0 or y > CANVAS_HEIGHT:
            canvas().move(starid, ndom.randint(0, CANVAS_WIDTH), random.randint(0, CANVAS_HEIGHT))
        else:            
            dx = (x - CANVAS_WIDTH/2) / (CANVAS_WIDTH/50)
            dy = (y - CANVAS_HEIGHT/2) / (CANVAS_HEIGHT/50)
            canvas().move(starid, dx, dy)
        
forever(move_stars)
mainloop()
