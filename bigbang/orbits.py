# Copyright 2019, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General
# Public License

from orbits_lib import *

"""Big Bang Fair demo - Orbits

"""

create_canvas("Orbits", 1000, 800, background="black")

# Our own gravity constant
G = 0.0005

# ---------------------------------------------------------
# Create your sprite objects
 
clicks=[]
planets=[
    Sprite(canvas().create_oval(300,250, 650,600, fill="white")),
]
ship = Sprite(canvas().create_oval(0,0, 25,25, fill="red"))
ship.max_speed = 100 # Fast!


# ---------------------------------------------------------
# Define your functions to control the game and its sprites
# -- these must be defined before the event handlers

def gravity():
    for p in planets:
        d = max(p.width/5, ship.distance_between(p))
        f = G*(4*(p.width/2)**3/d**2)
        ship.accelerate_towards(p.centre_x, p.centre_y, f)

def move_ship():
    gravity()
    ship.move_with_speed()

def propel_ship(event):
    x, y = event.x, event.y
    # Show where we clicked
    clicks.append(
        Sprite(canvas().create_oval(x-15,y-15, x+15, y+15, fill=hsv_to_hex(0, 1, 0.5))))
    f = distance_between_points(ship.x, ship.y, x, y)**(1/3)
    ship.accelerate_towards(x,y, f)

def new_planet(event):
    x, y = event.x, event.y
    p = Sprite(canvas().create_oval(x-50,y-50, x+50,y+50, fill="gray"))
    canvas().tag_lower(p.spriteid)
    planets.append(p)
        

def restart():
    ship.move_to(80, CANVAS_HEIGHT-100)
    ship.speed_x = ship.speed_y = 0
    delete_all(clicks)

# ---------------------------------------------------------
# How will the user control the game? What will other
# sprites do? Add your event handlers here.

restart()

forever(move_ship, 25)
when_button1_clicked(propel_ship)
when_button2_clicked(new_planet)
when_key_pressed('r', restart)


# ---------------------------------------------------------
# FINALLY
# Always call mainloop:

mainloop()
