# Copyright 2018, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General
# Public License

"""Asteroids

DONE:
- 

TODO:
- Polygon ship
"""

import random, time, sys
sys.path.append('..')
from geekclub.pyscratch import *

create_canvas(background='black')

ship_points = [(-20,20), (20,0), (-20,-20), (-5,0), (-20,20)]
ship = PolygonSprite(ship_points, fill='yellow', outline='white')
ship.centre()
ship.speed = 0

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# World set up
#

world = Struct( level=1, status='play', asteroids = [])

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Events and actions
#

def turn_right():
    ship.turn(5)
    ship.rotate(5)

def turn_left():
    ship.turn(-5)
    ship.rotate(-5)

def thrust():
    ship.speed += 1

def move_asteroids():
    pass

def move_ship():
    ship.move_forward(ship.speed)
    ship.if_on_edge_wrap()
    

when_key_pressed('<Right>', turn_right)
when_key_pressed('<Left>', turn_left)
when_key_pressed('<Up>', thrust)

forever(move_asteroids, 50)
forever(move_ship, 50)
mainloop()
