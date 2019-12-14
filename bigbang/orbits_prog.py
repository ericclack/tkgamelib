# Copyright 2019, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General
# Public License

from orbits_lib import *
from functools import partial

"""Big Bang Fair demo - Orbits

Program a list of force vectors to get the ship in orbit. 
"""

create_canvas("Orbits", 1000, 900, background="black")

# Our own gravity constant
G = 0.0005

# Does the game end if we hit a planet?
COLLISIONS = True

# Timed directional forces applied to the ship. Format:
# seconds: (x, y) vector

FORCES = {
    0: (50,20),
    2: (-300,50),
    4: (0,50),
    }


# ---------------------------------------------------------
# Create your sprite objects
 
clicks=[]
mx, my = canvas_width()/2,canvas_height()/2

planets=[
    Sprite(canvas().create_oval(mx-150, my-150, mx+150, my+150,
                                fill="white")),
]
ship = Sprite(canvas().create_oval(0,0, 25,25, fill="red"))
ship.max_speed = 100 # Fast!

ship.start_time = time.time()

timer = Sprite(canvas().create_text(15, 15*3, font=("default", 30),
                                    text="0 sec", fill="white",
                                    anchor="nw"))


# ---------------------------------------------------------
# Functions to control the game and its sprites

def gravity():
    for p in planets:
        d = ship.distance_between(p)
        if COLLISIONS and d < p.width/2:
            end_game("You hit a planet!", fn=restart, ms=2000, fill="red")
        f = G*(4*(p.width/2)**3/d**2)
        ship.accelerate_towards(p.centre_x, p.centre_y, f)

        
def move_ship():
    gravity()
    ship.move_with_speed()
    if COLLISIONS and not (0 < ship.x < canvas_width()) or not (0 < ship.y < canvas_height()):
        end_game("You left the solar system!", fn=restart, ms=2000, fill="red")

            
def apply_vector(x, y):
    print("Ship at", (ship.x, ship.y),
          "Applying vector", (x, y),
          "Accellerating towards", ship.x+x, ship.y+y)
    f = distance_between_points(0, 0, x, y)**(1/2)
    print(f)
    ship.accelerate_towards(ship.x+x, ship.y+y, f)    

    
def new_planet(event):
    x, y = event.x, event.y
    p = Sprite(canvas().create_oval(x-50,y-50, x+50,y+50, fill="gray"))
    canvas().tag_lower(p.spriteid)
    planets.append(p)

    
def delete_planet(event):
    # Check all but the first planet
    for i, p in enumerate(planets[1:]):
        if mouse_touching(p):
            planets.pop(i+1).delete()
    

def vector_action_fn(vx, vy):
    def _vector_action():
        show_variable("Last vector", (vx, vy), fill="white")
        apply_vector(vx, vy)
    return _vector_action
    

def make_vector_actions():
    for sec, (vx, vy) in FORCES.items():
        future_action(vector_action_fn(vx, vy), sec*1000)
        
        
def restart():
    ship.move_to(80, CANVAS_HEIGHT-100)
    ship.speed_x = ship.speed_y = 0
    ship.start_time = time.time()
    delete_all(clicks)
    make_vector_actions()
    restart_game()


def update_timer():
    t = time.time() - ship.start_time 
    canvas().dchars(timer.spriteid, 0, 100)
    canvas().insert(timer.spriteid, 0, "%s sec" % round(t, 1))

    
# ---------------------------------------------------------
# Event handlers here.

restart()

forever(move_ship, 25)
forever(update_timer, 100)
when_button1_clicked(new_planet)
when_button2_clicked(delete_planet)


# ---------------------------------------------------------
# FINALLY
# Always call mainloop:

mainloop()
