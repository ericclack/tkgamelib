from geekclub_packages import *

create_canvas(background='black')

# Create a game from this template in 3 steps:
# 1. Create sprites
# 2. Add game controls (at the end of this file)
# 3. Write the control functions


# ---------------------------------------------------------
# STEP 1
# Find or draw your sprites and save them as GIFs to my_work/my_images
# Give them short names so that they are easy to enter here.

# Create your sprite objects
me = ImageSprite('images/me.gif')
me.centre()

# Add any variables you like
me.score = 0

# Or you can use simple shapes
aliens = []

# Platforms
platforms = [
    ImageSprite('images/platform.gif', x=150, y=150),
    ImageSprite('images/platform.gif', x=600, y=300),
    ImageSprite('images/platform.gif', x=400, y=300),
    ]

# Make ground
for i in range(5):
    platforms.append(ImageSprite('images/platform.gif', x=i*200, y=700))
    

    
# ---------------------------------------------------------
# STEP 3
# Define your functions to control the game and its sprites
# -- these must be defined before the event handlers

def gravity():
    me.speed_y += .1
    me.move_with_speed()
    if me.touching_any(platforms):
        me.move(0, -me.speed_y)
        me.speed_y = 0

def move_left():
    me.move(-2,0)

def move_right():
    me.move(2,0)

def thrust():
    me.speed_y -= 0.3

# ---------------------------------------------------------
# STEP 2    
# How will the user control the game? What will other
# sprites do? Add your event handlers here.

forever(gravity, 50)
when_key_pressed('z', move_left)
when_key_pressed('x', move_right)
when_key_pressed('<space>', thrust)


# ---------------------------------------------------------
# FINALLY
# Always call mainloop:

mainloop()
