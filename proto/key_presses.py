from geekclub_packages import *

create_canvas()

# Create a game from this template in 3 steps:
# 1. Create sprites
# 2. Add game controls (at the end of this file)
# 3. Write the control functions


# ---------------------------------------------------------
# STEP 1
# Find or draw your sprites and save them as GIFs to my_work/my_images
# Give them short names so that they are easy to enter here.

# Create your sprite objects
sprite = Sprite(canvas().create_oval(10,10, 50,50, fill="yellow"))
sprite.centre()
# Add any variables you like
sprite.score = 0

    
# ---------------------------------------------------------
# STEP 3
# Define your functions to control the game and its sprites
# -- these must be defined before the event handlers

def follow_mouse():
    sprite.move_towards(mousex(), mousey(), 10)

def move_left():
    sprite.move(-2,0)

def move_right():
    sprite.move(2, 0)

def thrust():
    sprite.speed_y -= 2
        
# ---------------------------------------------------------
# STEP 2    
# How will the user control the game? What will other
# sprites do? Add your event handlers here.

#forever(follow_mouse, 25)
when_key_pressed('z', move_left)
when_key_pressed('x', move_right)
when_key_pressed('<Space>', thrust)



# ---------------------------------------------------------
# FINALLY
# Always call mainloop:

mainloop()
