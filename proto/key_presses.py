from geekclub_packages import *

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
    ]
    
# ---------------------------------------------------------
# STEP 3
# Define your functions to control the game and its sprites
# -- these must be defined before the event handlers

def follow_mouse():
    sprite.move_towards(mousex(), mousey(), 10)

def move_sprite():
    # Keys
    old_speed_x = sprite.speed_x
    if is_key_down('z'):
        sprite.speed_x -= 1
    if is_key_down('x'):
        sprite.speed_x += 1
    if is_key_down(' '):
        sprite.speed_y -= 1
    if old_speed_x == sprite.speed_x:
        sprite.speed_x *= 0.9

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
        
        
# ---------------------------------------------------------
# STEP 2    
# How will the user control the game? What will other
# sprites do? Add your event handlers here.

#forever(check_keys, 25)
forever(move_sprite, 25)


# ---------------------------------------------------------
# FINALLY
# Always call mainloop:

mainloop()
