# Copyright 2019, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General
# Public License

"""Big Bang Fair demo - Jet Pack

This lib file contains most of the game logic, 
the logic that we don't need to show the students
so that their debugging is a bit easier
"""

from geekclub_packages import *

create_canvas(background="black")

MAX_ROCKET_PARTS = 4
LANDING_ZONE = 550
MAX_ALIENS = 5

# How likely is next rocket part or fuel to appear each tick?
PROB_NEXT_PART = 0.5

# Variables and constants
DROP_SPEED = 5


# ---------------------------------------------------------
# Create sprite objects

sprite = ImageSprite(['images/jet_pack_left.gif', 'images/jet_pack_right.gif'])
sprite.centre()
sprite.max_speed = 7
sprite.in_rocket = False

# Our world contains everything the game needs
world = Struct(lives=5, score=0, level=1, status='play',
               sprite = sprite,
               platforms = [],
               rocket_parts = [],
               aliens = [],
               fuel = [],
               flames = [],
               takeoff_countdown = 0
               )

def make_platforms(rectangles):
    world.platforms = [
        Sprite(canvas().create_rectangle(x1,y1, x2,y2, fill=c))
        for x1, y1, x2, y2, c in rectangles ]  

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
    r.carried = False
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
    f.carried = False
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
    else:
        # Drop anything we're carrying
        for p in w.rocket_parts + w.fuel:
            if p.carried: p.carried = False
            
    w.level += level_up
    w.sprite.in_rocket = False
    w.sprite.centre()
    w.status = 'play'

# ------------------------------------------------------------------

def move_sprite(w):
    if w.sprite.in_rocket: return
    
    # Gravity
    w.sprite.speed_y += 0.5

    # Platforms
    p = w.sprite.touching_any(w.platforms)
    if p:
        w.sprite.bounce_off(p)

    # Move
    w.sprite.move_with_speed()
    w.sprite.if_on_edge_wrap()

    # Hit an alien?
    if w.sprite.touching_any(w.aliens):
        say("You hit an alien!", 2000)
        w.lives -= 1
        if w.lives == 0:
            print("Score", w.score, "Level", w.level)
            end_game("Game over!", fill="white")
        start_level(w, delete_rocket_parts=False, level_up=0)


def move_aliens(w):
    if len(w.aliens) < MAX_ALIENS and random.random() < 0.05:
        w.aliens.append(new_alien(w))

    for a in w.aliens:
        if w.level > 1:
            a.accelerate_towards(w.sprite.x, w.sprite.y,
                                 ((w.level+1)**2)/200)

        a.move_with_speed()
        if a.y > CANVAS_HEIGHT or a.touching_any(w.platforms):
            a.delete()
            w.aliens.remove(a)
        else:
            a.if_on_edge_wrap()

            
def move_rocket_parts(w):
    if ready_for_next_rocket_part(w) and random.random() < PROB_NEXT_PART:
        w.rocket_parts.append(new_rocket_part(w))

    if w.rocket_parts:
        r = w.rocket_parts[-1]
        if not r.in_place:
            if r.touching(w.sprite) and not r.landing:
                r.carried = True

            if r.carried:
                r.move_to(w.sprite.x, w.sprite.y)
                if in_landing_zone(r.x):
                    w.score += 50
                    r.move_to(LANDING_ZONE, r.y)
                    r.landing = True
                    r.carried = False
                    r.speed_y = DROP_SPEED
            elif r.landing and (r.touching_any(w.platforms)
                                or r.touching_any(w.rocket_parts[:-1])):
                r.in_place = True
                r.landing = False
            elif not r.touching_any(w.platforms):
                r.move_with_speed()

                
def move_fuel(w):
    if ready_for_next_fuel(w) and random.random() < PROB_NEXT_PART:
        w.fuel.append(new_fuel(w))

    if w.fuel:
        f = w.fuel[-1]
        if not f.in_place:
            if f.touching(w.sprite) and not f.landing:
                f.carried = True

            if f.carried:
                f.move_to(w.sprite.x, w.sprite.y)
                if in_landing_zone(f.x):
                    w.score += 50
                    f.move_to(LANDING_ZONE, f.y)
                    f.landing = True
                    f.carried = False
                    f.speed_y = DROP_SPEED
            elif f.landing and (f.touching_any(w.platforms)
                                or f.touching_any(w.fuel[:-1])):
                f.in_place = True
                f.landing = False
                w.rocket_parts[len(w.fuel)-1].next_costume()
                # Hide fuel
                f.move_to(-100,-100)
            elif not f.touching_any(w.platforms):
                f.move_with_speed()

                
def rocket_takeoff(w):
    if w.status not in ['countdown', 'takeoff'] and ready_for_takeoff(w):
        say("Ready for take off!", 1000)
        w.status = 'countdown'
        w.score += 100
        w.takeoff_countdown = 400
        w.flames.append( new_flame(w) )

    if w.status == 'countdown':
        w.flames[0].next_costume()
        w.takeoff_countdown -= 1
        if w.takeoff_countdown < 300:
            say(w.takeoff_countdown // 40)
        
        if w.sprite.touching_any(w.rocket_parts):
            w.sprite.in_rocket = True
            w.sprite.offscreen()

        if w.takeoff_countdown <= 0:
            w.status = 'takeoff'
            if w.sprite.in_rocket:
                say("Take off!", 1000)
            else:
                say("You missed the rocket!", 1000)
                w.lives -= 1
                
    if w.status == 'takeoff':
        for p in w.rocket_parts + w.flames:
            w.flames[0].next_costume()
            p.move(0, -5)
            
        if w.rocket_parts[0].y < -w.rocket_parts[0].height*2:
            start_level(w, level_up=1 if w.sprite.in_rocket else 0)        

# ------------------------------------------------------------------

def parts_in_place(parts):
    return all([r.in_place for r in parts])

def parts_left(parts):
    return MAX_ROCKET_PARTS - len(parts)

def parts_complete(parts):
    return parts_left(parts) == 0 and parts_in_place(parts)

def update_score():
    show_variables([["Lives", world.lives],
                    ["Score", world.score],
                    ["Level", world.level]],
                   fill="white")

# ------------------------------------------------------------------

def ready_for_next_rocket_part(w):
    return parts_left(w.rocket_parts) and parts_in_place(w.rocket_parts)

def ready_for_next_fuel(w):
    return parts_complete(w.rocket_parts) and parts_left(w.fuel) \
           and parts_in_place(w.fuel)

def ready_for_takeoff(w):
    return parts_complete(w.fuel) and parts_complete(w.rocket_parts)
