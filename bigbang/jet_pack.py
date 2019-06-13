# Copyright 2019, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General
# Public License

from jet_pack_lib import *

"""Big Bang Fair demo - Jet Pack

This code contains some bugs and bad design decisions that
make the game almost unplayable. So:

- Test the game out and identify the bugs
- Explore and fix each bug
- See if you can get the highest score. 

Hints: look in these areas:

1. Layout of the screen
2. Controls
3. Too many aliens

"""

create_canvas(background="black")

# Mouse or keyboard (keyboard doesn't work well on Mac)
MOUSE_CONTROL = True

# ---------------------------------------------------------
# Create your sprite objects

sprite = ImageSprite(['images/jet_pack_left.gif', 'images/jet_pack_right.gif'])
sprite.centre()
sprite.max_speed = 7
sprite.in_rocket = False

platform_rectangles = [(50,150, 200,200, "white"),
                       (380, 500, 530,550, "yellow"),
                       (700,300, 800,350, "green"),
                       #(160,200, 700,250, "blue"),
                       (0,CANVAS_HEIGHT-50, CANVAS_WIDTH,CANVAS_HEIGHT, "white")]

# Our world contains everything the game needs
world = Struct(lives=5, score=0, level=1, status='play',
               sprite = sprite,
               platforms = make_platforms(platform_rectangles),
               rocket_parts = [],
               aliens = [],
               fuel = [],
               flames = []
               )

# Variables and constants
MAX_FUEL = 3
DROP_SPEED = 5
MAX_FLAMES = 5
MAX_ALIENS = 1

# How likely is next rocket part or fuel to appear each tick?
PROB_NEXT_PART = 0.5

# ---------------------------------------------------------
# Define your functions to control the game and its sprites
# -- these must be defined before the event handlers

def set_sprite_costume():
    # Left or right?
    if sprite.speed_x < 0:
        sprite.switch_costume(1)
    else:
        sprite.switch_costume(2)    

def key_control():
    old_speed_x = sprite.speed_x
    if is_key_down('z'):
        sprite.speed_x -= 1
    if is_key_down('x'):
        sprite.speed_x += 1
    if is_key_down(' '):
        sprite.speed_y -= 1

    if old_speed_x == sprite.speed_x:
        sprite.speed_x *= 0.9
    else:
        set_sprite_costume()
        
def mouse_control():
    old_speed_x = sprite.speed_x
    if mousex() < sprite.x - sprite.width:
        sprite.speed_x -= 1
    if mousex() > sprite.x + 2 * sprite.width:
        sprite.speed_x += 1
    if mousey() < sprite.y:
        sprite.speed_y -= 1

    if old_speed_x == sprite.speed_x:
        sprite.speed_x *= 0.9
    else:
        set_sprite_costume()        

def move_sprite():
    # Gravity
    sprite.speed_y += 0.5

    # Platforms
    p = sprite.touching_any(world.platforms)
    if p:
        sprite.bounce_off(p)

    # Move
    sprite._limit_speed()
    sprite.move_with_speed()
    sprite.if_on_edge_wrap()

    # Hit an alien?
    if sprite.touching_any(world.aliens):
        banner("You hit an alien!", 2000, fill="white")
        world.lives -= 1
        if world.lives == 0:
            end_game("Game over!", fill="white")
        start_level(world, delete_rocket_parts=False, level_up=0)

def fire():
    direction = sign(sprite.speed_x) or 1
    x = sprite.x + sprite.width / 2
    y = sprite.y + sprite.height / 2
    fsprite = Sprite(canvas().create_rectangle(
                        x + (direction * 30), y, x + (direction*500), y+3,
                        fill="yellow", outline=None))
    # Has the laser hit any aliens?
    a = fsprite.touching_any(world.aliens)
    while a:
        a.delete()
        world.aliens.remove(a)
        world.score += 10
        # Has the laser hit any other aliens?
        a = fsprite.touching_any(world.aliens)

    # Delete the laser in 1/10th second
    future_action(lambda: fsprite.delete(), 100)

def move_aliens():
    if len(world.aliens) < MAX_ALIENS and random.random() < 0.05:
        world.aliens.append(new_alien(world))

    for a in world.aliens:
        a.accelerate_towards(sprite.x, sprite.y, steps=world.level**2/20)

        a.move_with_speed()
        if a.y > CANVAS_HEIGHT or a.touching_any(world.platforms):
            a.delete()
            world.aliens.remove(a)
        else:
            a.if_on_edge_wrap()

def move_rocket_parts():
    if ready_for_next_rocket_part(world) and random.random() < PROB_NEXT_PART:
        world.rocket_parts.append(new_rocket_part(world))

    if world.rocket_parts:
        r = world.rocket_parts[-1]
        if not r.in_place:
            if r.touching(sprite) and not r.landing:
                r.move_to(sprite.x, sprite.y)
                if in_landing_zone(r.x):
                    world.score += 50
                    r.move_to(LANDING_ZONE, r.y)
                    r.landing = True
                    r.speed_y = DROP_SPEED
            elif r.landing and (r.touching_any(world.platforms)
                                or r.touching_any(world.rocket_parts[:-1])):
                r.in_place = True
                r.landing = False
            elif not r.touching_any(world.platforms):
                r.move_with_speed()

def move_fuel():
    if ready_for_next_fuel(world) and random.random() < PROB_NEXT_PART:
        world.fuel.append(new_fuel(world))

    if world.fuel:
        f = world.fuel[-1]
        if not f.in_place:
            if f.touching(sprite) and not f.landing:
                f.move_to(sprite.x, sprite.y)
                if in_landing_zone(f.x):
                    world.score += 50
                    f.move_to(LANDING_ZONE, f.y)
                    f.landing = True
                    f.speed_y = DROP_SPEED
            elif f.landing and (f.touching_any(world.platforms)
                                or f.touching_any(world.fuel[:-1])):
                f.in_place = True
                f.landing = False
                world.rocket_parts[len(world.fuel)-1].next_costume()
                # Hide fuel
                f.move_to(-100,-100)
            elif not f.touching_any(world.platforms):
                f.move_with_speed()

def rocket_takeoff():
    if world.status not in ['readyfortakeoff', 'takeoff'] and ready_for_takeoff(world):
        banner("Ready for take off!", 1000, fill="white")
        world.status = 'readyfortakeoff'
        world.score += 100

    if world.status == 'readyfortakeoff':
        if sprite.touching_any(world.rocket_parts):
            sprite.in_rocket = True

        if len(world.flames) == MAX_FLAMES:
            world.status = 'takeoff'
            if sprite.in_rocket:
                banner("Take off!", 1000, fill="white")
            else:
                banner("You missed the rocket!", 1000, fill="white")
                world.lives -= 1
                start_level(world, level_up=0)

        elif random.random() < 0.02:
            world.flames.append(new_flame(world))

    if world.status == 'takeoff':
        for p in world.rocket_parts + world.fuel + world.flames:
            p.move(0, -5)
        if world.rocket_parts[0].y < 0:
            start_level(world)

    if sprite.in_rocket:
        r = world.rocket_parts[0]
        sprite.move_to(r.x + r.width, r.y)

def update_score():
    show_variables([["Lives", world.lives],
                    ["Score", world.score],
                    ["Level", world.level]],
                   fill="white")


# ---------------------------------------------------------
# How will the user control the game? What will other
# sprites do? Add your event handlers here.

if MOUSE_CONTROL:
    forever(mouse_control, 25)
    when_button1_clicked(fire)
else:
    forever(key_control, 25)
    when_key_pressed('<Return>', fire)

forever(move_sprite, 25)
forever(move_aliens, 25)
forever(move_rocket_parts, 25)
forever(move_fuel, 25)
forever(rocket_takeoff, 25)
forever(update_score)

# ---------------------------------------------------------
# FINALLY
# Always call mainloop:

mainloop()
