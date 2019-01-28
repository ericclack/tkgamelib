# Copyright 2014, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

"""Animate a star field"""

import random, time
from geekclub_packages import *

create_canvas()

STARS = []
MAX_STARS = askinteger("Question", "How many stars?") or 100


def new_star():
    x, y = random.randint(0, CANVAS_WIDTH), random.randint(0, CANVAS_HEIGHT)
    star = Sprite(canvas().create_oval(x, y, x+5, y+5))
    return star

def star_out_of_view(star):
    x, y = star.x, star.y
    return (x < 0 or x > CANVAS_WIDTH or y < 0 or y > CANVAS_HEIGHT)

def fly_forwards():
    global STARS
    STARS = move_stars(STARS)

def move_stars(stars):
    """Make a new list of stars that have been moved and refreshed"""
    stars2 = []
    for star in stars:
        if star_out_of_view(star):
            star.delete()
            stars2.append(new_star())
        else:            
            dx = (star.x - CANVAS_WIDTH/2) / (CANVAS_WIDTH/50)
            dy = (star.y - CANVAS_HEIGHT/2) / (CANVAS_HEIGHT/50)
            star.move(dx, dy)
            stars2.append(star)
    return stars2

for i in range(MAX_STARS):
    STARS.append(new_star())
        
forever(fly_forwards, 50)
mainloop()
