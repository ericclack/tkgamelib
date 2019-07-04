# Copyright 2019, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General
# Public License

from geekclub_packages import *

create_canvas(background="black")

MAX_ROCKET_PARTS = 4
LANDING_ZONE = 550

# ---------------------------------------------------------
# Create sprite objects

sprite = ImageSprite(['images/jet_pack_left.gif', 'images/jet_pack_right.gif'])
sprite.centre()
sprite.max_speed = 7
sprite.in_rocket = False

platform_rectangles = [(50,150, 200,200, "white"),
                       (380, 500, 530,550, "yellow"),
                       (700,300, 800,350, "green"),
                       #(160,200, 700,250, "blue"),
                       (0,CANVAS_HEIGHT-50, CANVAS_WIDTH,CANVAS_HEIGHT, "white")]

def make_platforms(rectangles):
    return [Sprite(canvas().create_rectangle(x1,y1, x2,y2, fill=c))
                for x1, y1, x2, y2, c in rectangles]  

# Our world contains everything the game needs
world = Struct(lives=5, score=0, level=1, status='play',
               sprite = sprite,
               platforms = make_platforms(platform_rectangles),
               rocket_parts = [],
               aliens = [],
               fuel = [],
               flames = [],
               takeoff_countdown = 0
               )

# Variables and constants
DROP_SPEED = 5
MAX_ALIENS = 5

# How likely is next rocket part or fuel to appear each tick?
PROB_NEXT_PART = 0.5

# ------------------------------------------------------------------

def in_landing_zone(x):
    return (LANDING_ZONE-5) < x < (LANDING_ZONE+5)

def say(s, *args, **kwargs):
    banner(s, *args, fill="white", **kwargs)

def set_sprite_costume():
    # Left or right?
    if sprite.speed_x < 0:
        sprite.switch_costume(1)
    else:
        sprite.switch_costume(2)    

# ------------------------------------------------------------------

def new_rocket_part(w):
    i = (len(w.rocket_parts) + 1)
    r = ImageSprite(['images/rocket%s.gif' % i, 'images/rocket%s_fuelled.gif' % i])
    r.move_to(random.randint(0, CANVAS_WIDTH-100), 0)
    r.speed_x = 0
    r.speed_y = 1
    r.in_place = False
    r.landing = False
    return r

def new_alien(w):
    a = Sprite(canvas().create_oval(0,0, 35,35, fill="red"))
    a.max_speed = 3

    if random.random() < 0.5:
        # Along top
        a.move_to(random.randint(0, CANVAS_WIDTH * .9), 0)
    else:
        # Along right hand side
        a.move_to(CANVAS_WIDTH, random.randint(0, CANVAS_HEIGHT *.6))
        
    a.speed_x = -random.randint(1,3)
    a.speed_y = 1.5
    return a

def new_fuel(w):
    f = ImageSprite('images/fuel.gif')
    f.move_to(random.randint(0, CANVAS_WIDTH), 0)
    f.speed_x = 0
    f.speed_y = 1
    f.in_place = False
    f.landing = False
    return f

def new_flame(w):
    r = w.rocket_parts[0] # The base of the rocket
    flame = ImageSprite(['images/flame1.gif',
                         'images/flame2.gif',
                         'images/flame3.gif'])
    x = (r.x + r.width / 2) - (flame.width / 2)
    y = r.y + r.height
    flame.move_to(x, y)
    return flame

def delete_all(spritelist):
    while spritelist:
        spritelist.pop().delete()

def start_level(w, delete_rocket_parts=True, level_up=1):
    delete_all(w.aliens)
    if delete_rocket_parts:
        delete_all(w.rocket_parts)
        delete_all(w.fuel)
        delete_all(w.flames)
    w.level += level_up
    w.sprite.in_rocket = False
    w.sprite.centre()
    w.status = 'play'

# ------------------------------------------------------------------

def parts_in_place(parts):
    return all([r.in_place for r in parts])

def parts_left(parts):
    return MAX_ROCKET_PARTS - len(parts)

def parts_complete(parts):
    return parts_left(parts) == 0 and parts_in_place(parts)

# ------------------------------------------------------------------

def ready_for_next_rocket_part(w):
    return parts_left(w.rocket_parts) and parts_in_place(w.rocket_parts)

def ready_for_next_fuel(w):
    return parts_complete(w.rocket_parts) and parts_left(w.fuel) \
           and parts_in_place(w.fuel)

def ready_for_takeoff(w):
    return parts_complete(w.fuel) and parts_complete(w.rocket_parts)
