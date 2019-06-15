# Copyright 2019, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General
# Public License

from orbits_lib import *

"""Big Bang Fair demo - Orbits

"""

create_canvas("Orbits", 1000, 800, background="black")

# ---------------------------------------------------------
# Create your sprite objects

planets = [
    Sprite(canvas().create_oval(0,0, 300,300, fill="white")),
    Sprite(canvas().create_oval(0,0, 150,150, fill="gray")),
    ]

planets[0].move_to(200, 300)
planets[1].move_to(700, 200)

ship = Sprite(canvas().create_oval(0,0, 25,25, fill="red"))
ship.move_to(20, CANVAS_HEIGHT-40)

# ---------------------------------------------------------
# Define your functions to control the game and its sprites
# -- these must be defined before the event handlers

def gravity():
    for p in planets:
        d = max(p.width/2, ship.distance_between(p))
        f = p.width**2/d**2.5
        print(p.width, d, f)
        ship.accelerate_towards(p.centre_x, p.centre_y, f)

def move_ship():
    gravity()
    ship.move_with_speed()

def propel_ship(event):
    x, y = event.x, event.y
    ship.accelerate_towards(x,y, 5)
    

# ---------------------------------------------------------
# How will the user control the game? What will other
# sprites do? Add your event handlers here.

forever(move_ship, 25)
when_button1_clicked(propel_ship)

# ---------------------------------------------------------
# FINALLY
# Always call mainloop:

mainloop()
