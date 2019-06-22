# Copyright 2019, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General
# Public License

from geekclub_packages import *

MAX_ROCKET_PARTS = 4
LANDING_ZONE = 550
MAX_ALIENS = 1

# How likely is next rocket part or fuel to appear each tick?
PROB_NEXT_PART = 0.5

# Variables and constants
DROP_SPEED = 5



def make_platforms(rectangles):
    return [Sprite(canvas().create_rectangle(x1,y1, x2,y2, fill=c))
                for x1, y1, x2, y2, c in rectangles]  

def in_landing_zone(x):
    return (LANDING_ZONE-5) < x < (LANDING_ZONE+5)

def say(s, *args, **kwargs):
    banner(s, *args, fill="white", **kwargs)

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

def move_sprite(world):
    sprite = world.sprite
    if sprite.in_rocket: return
    
    # Gravity
    sprite.speed_y += 0.5

    # Platforms
    p = sprite.touching_any(world.platforms)
    if p:
        sprite.bounce_off(p)

    # Move
    sprite.move_with_speed()
    sprite.if_on_edge_wrap()

    # Hit an alien?
    if sprite.touching_any(world.aliens):
        say("You hit an alien!", 2000)
        world.lives -= 1
        if world.lives == 0:
            print("Score", world.score, "Level", world.level)
            end_game("Game over!", fill="white")
        start_level(world, delete_rocket_parts=False, level_up=0)



def move_aliens(world):
    sprite = world.sprite
    
    if len(world.aliens) < MAX_ALIENS and random.random() < 0.05:
        world.aliens.append(new_alien(world))

    for a in world.aliens:
        if world.level > 0:
            a.accelerate_towards(sprite.x, sprite.y, (world.level+1)**2/20)

        a.move_with_speed()
        if a.y > CANVAS_HEIGHT or a.touching_any(world.platforms):
            a.delete()
            world.aliens.remove(a)
        else:
            a.if_on_edge_wrap()

            
def move_rocket_parts(world):
    sprite = world.sprite
    
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

                
def move_fuel(world):
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

                
def rocket_takeoff(world):
    if world.status not in ['countdown', 'takeoff'] and ready_for_takeoff(world):
        say("Ready for take off!", 1000)
        world.status = 'countdown'
        world.score += 100
        world.takeoff_countdown = 400
        world.flames.append( new_flame(world) )

    if world.status == 'countdown':
        world.flames[0].next_costume()
        world.takeoff_countdown -= 1
        if world.takeoff_countdown < 300:
            say(world.takeoff_countdown // 40)
        
        if sprite.touching_any(world.rocket_parts):
            sprite.in_rocket = True
            sprite.offscreen()

        if world.takeoff_countdown <= 0:
            world.status = 'takeoff'
            if sprite.in_rocket:
                say("Take off!", 1000)
            else:
                say("You missed the rocket!", 1000)
                world.lives -= 1
                
    if world.status == 'takeoff':
        for p in world.rocket_parts + world.flames:
            world.flames[0].next_costume()
            p.move(0, -5)
            
        if world.rocket_parts[0].y < -world.rocket_parts[0].height*2:
            start_level(world, level_up=1 if sprite.in_rocket else 0)        

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
