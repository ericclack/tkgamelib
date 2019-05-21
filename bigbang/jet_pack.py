from geekclub_packages import *

"""Big Bang Fair demo - Thrust

TO DO:
- Place platforms in better places
- Aliens kill you
- Can fire at aliens
- Aliens appear at RHS of screen too
- Rocket takes off

Then:
- Introduce bugs or remove features

"""

create_canvas(background="black")

# ---------------------------------------------------------
# STEP 1
# Find or draw your sprites and save them as GIFs to my_work/my_images
# Give them short names so that they are easy to enter here.

# Create your sprite objects
sprite = Sprite(canvas().create_oval(10,10, 50,50, fill="yellow"))
sprite.centre()
sprite.max_speed = 5

platforms = [
    Sprite(canvas().create_rectangle(50,100, 200,150, fill="white")),
    Sprite(canvas().create_rectangle(0,500, 500,550, fill="white")),
    Sprite(canvas().create_rectangle(0,CANVAS_HEIGHT-50,
                                     CANVAS_WIDTH,CANVAS_HEIGHT, fill="white")),
    ]

rocket_parts = []
MAX_ROCKET_PARTS = 5
LANDING_ZONE = 650

aliens = []
MAX_ALIENS = 5

# ---------------------------------------------------------
# STEP 3
# Define your functions to control the game and its sprites
# -- these must be defined before the event handlers

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

def move_sprite():
    # Gravity
    sprite.speed_y += 0.5

    # Platforms
    p = sprite.touching_any(platforms)
    if p:
        sprite.bounce_off(p)

    # Move
    sprite._limit_speed()
    sprite.move_with_speed()
    sprite.if_on_edge_wrap()

def new_alien():
    a = Sprite(canvas().create_oval(0,0, 50,50, fill="red"))
    a.move_to(random.randint(0, CANVAS_WIDTH), 0)
    a.speed_x = -random.randint(1,3)
    a.speed_y = 2
    return a

def move_aliens():
    if len(aliens) < MAX_ALIENS and random.random() < 0.05:
        aliens.append(new_alien())
        
    for a in aliens:
        a.move_with_speed()
        if a.y > CANVAS_HEIGHT or a.touching_any(platforms):
            a.delete()
            aliens.remove(a)
        else:
            a.if_on_edge_wrap()

def new_rocket_part():
    r = Sprite(canvas().create_rectangle(0,0, 100,40, fill="gray"))
    r.move_to(random.randint(0, CANVAS_WIDTH), 0)
    r.speed_x = 0
    r.speed_y = 1
    r.in_place = False
    r.landing = False
    return r

def ready_for_next_rocket_part():
    """Either none yet, or most recent one is in place"""
    return rocket_parts == [] or (len(rocket_parts) < MAX_ROCKET_PARTS
                                 and rocket_parts[-1].in_place)
     
def in_landing_zone(x):
    return (LANDING_ZONE-5) < x < (LANDING_ZONE+5)

def move_rocket_parts():
    if ready_for_next_rocket_part() and random.random() < 0.01:
        rocket_parts.append(new_rocket_part())

    if rocket_parts:
        r = rocket_parts[-1]
        if not r.in_place:
            if r.touching(sprite) and not r.landing:
                r.move_to(sprite.x, sprite.y)
                if in_landing_zone(r.x):
                    r.move_to(LANDING_ZONE, r.y)
                    r.landing = True
                    r.speed_y = 2
            elif r.landing and (r.touching_any(platforms)
                                or r.touching_any(rocket_parts[:-1])):
                r.in_place = True
                r.landing = False
            elif not r.touching_any(platforms):
                r.move_with_speed()

        
# ---------------------------------------------------------
# STEP 2    
# How will the user control the game? What will other
# sprites do? Add your event handlers here.

forever(key_control, 25)
#forever(mouse_control, 25)

forever(move_sprite, 25)
forever(move_aliens, 25)
forever(move_rocket_parts, 25)

# ---------------------------------------------------------
# FINALLY
# Always call mainloop:

mainloop()
