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
3. Laser

"""

# Mouse or keyboard? (keyboard doesn't work well on Mac)
MOUSE_CONTROL = False

# ------------------------------------------------------------------
# Level layout

make_platforms([
    (50,150,  200,200, "white"),
    (380,500, 530,550, "yellow"),
    (700,300, 800,350, "green"),
    (0,CANVAS_HEIGHT-50, CANVAS_WIDTH,CANVAS_HEIGHT, "white")
])


# ---------------------------------------------------------
# Functions to control the game and its sprites

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
    if mousex() < sprite.centre_x - sprite.width:
        sprite.speed_x -= 1
    if mousex() > sprite.centre_x + sprite.width:
        sprite.speed_x += 1
    if mousey() < sprite.y:
        sprite.speed_y -= 1

    if old_speed_x == sprite.speed_x:
        sprite.speed_x *= 0.9
    else:
        set_sprite_costume()        
        
        
def fire():
    # Convert costume 1 or 2 into -1 or 1
    direction = sprite.which_costume()*2 - 3

    # Make a laser sprite
    x = sprite.centre_x
    y = sprite.centre_y
    length = 500
    fsprite = Sprite(canvas().create_rectangle(
        x + (direction * 30), y,
        x + (direction * length), y+3,
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


def move():
    move_sprite(world)
    move_aliens(world)
    move_rocket_parts(world)
    move_fuel(world)
    # Ready for take-off?
    rocket_takeoff(world)

    
# ---------------------------------------------------------
# Game controls

if MOUSE_CONTROL:
    forever(mouse_control, 25)
    when_button1_clicked(fire)
else:
    forever(key_control, 25)
    when_key_pressed('<Return>', fire)

forever(move, 25)
forever(update_score)


# ---------------------------------------------------------
# FINALLY - Always call mainloop:

mainloop()
