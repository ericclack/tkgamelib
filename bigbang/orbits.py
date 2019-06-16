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
    Sprite(canvas().create_oval(0,0, 80,80, fill="gray")),
    Sprite(canvas().create_oval(0,0, 300,300, fill="white")),
    ]

planets[0].move_to(200, 200)
planets[1].move_to(550, 300)

ship = Sprite(canvas().create_oval(0,0, 25,25, fill="red"))
ship.move_to(20, CANVAS_HEIGHT-40)

world = Struct(clicks=[])


# ---------------------------------------------------------
# Define your functions to control the game and its sprites
# -- these must be defined before the event handlers

def gravity():
    for p in planets:
        d = max(p.width/3, ship.distance_between(p))
        f = p.width**2/d**2.5
        ship.accelerate_towards(p.centre_x, p.centre_y, f)

def move_ship():
    gravity()
    ship.move_with_speed()

def propel_ship(event):
    x, y = event.x, event.y
    world.clicks.append(
        Sprite(canvas().create_oval(x-15,y-15, x+15, y+15, fill=hsv_to_hex(0, 1, 0.5))))
    ship.accelerate_towards(x,y, 3)

def restart():
    ship.move_to(20, CANVAS_HEIGHT-40)
    ship.speed_x = ship.speed_y = 0
    delete_all(world.clicks)

# ---------------------------------------------------------
# How will the user control the game? What will other
# sprites do? Add your event handlers here.

forever(move_ship, 25)
when_button1_clicked(propel_ship)
when_key_pressed('r', restart)


# ---------------------------------------------------------
# FINALLY
# Always call mainloop:

mainloop()
