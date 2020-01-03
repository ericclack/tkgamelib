# Copyright 2018, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General
# Public License

"""Asteroids"""

import random, time
from packages import *

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

b = canvas().create_oval(0,0, 5, 5, fill='white')
bullet = Sprite(b)
bullet.live = False

def hide_bullet():
    bullet.move_to(-5, -5)

hide_bullet()

    
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

def shoot():
    x, y = ship.pos()
    bullet.move_to(x + ship.width/2, y + ship.height / 2)
    bullet.turn_to(ship.direction)
    bullet.move_forward(ship.width)
    bullet.speed = ship.speed + 5
    bullet.live = True

def move_bullet():
    if bullet.live:
        bullet.move_forward(bullet.speed)
        a = bullet.touching_any(asteroids)
        if a:
            asteroids.remove(a)
            a.delete()
            bullet.live = False
            hide_bullet()

when_key_pressed('<Right>', turn_right)
when_key_pressed('<Left>', turn_left)
when_key_pressed('<Up>', thrust)
when_key_pressed('<space>', shoot)

forever(move_asteroids, 50)
forever(move_ship, 50)
forever(move_bullet, 50)
mainloop()
