# Copyright 2018, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General
# Public License

"""Asteroids"""

import random, time, sys
sys.path.append('..')
from geekclub.pyscratch import *

create_canvas(background='black')

NUM_ASTEROIDS = 5
ASTEROID_SIZE = 100

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# World set up
#

ship_points = [(-20,20), (20,0), (-20,-20), (-5,0), (-20,20)]
ship = PolygonSprite(ship_points, fill='yellow', outline='white')
ship.centre()
ship.speed = 0

asteroids = []
for i in range(NUM_ASTEROIDS):
    x, y = random.randint(0, CANVAS_WIDTH//3), random.randint(0, CANVAS_HEIGHT//3)
    o = canvas().create_oval(x,y,
                             x+ASTEROID_SIZE, y+ASTEROID_SIZE,
                             fill='gray')
    a = Sprite(o)
    a.speed_x = random.randint(-3, 3)
    a.speed_y = random.randint(-3, 3)
    asteroids.append( a )


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
    for a in asteroids:
        a.move_with_speed()
        a.if_on_edge_wrap()
        
def move_ship():
    ship.move_forward(ship.speed)
    ship.if_on_edge_wrap()
    

when_key_pressed('<Right>', turn_right)
when_key_pressed('<Left>', turn_left)
when_key_pressed('<Up>', thrust)

forever(move_asteroids, 50)
forever(move_ship, 50)
mainloop()
