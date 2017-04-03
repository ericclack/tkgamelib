import sys
sys.path.append('..')
from geekclub.pyscratch import *

create_canvas()

# Create a game from this template in 3 steps:
# 1. Create sprites
# 2. Add game controls
# 3. Write the control functions


# ---------------------------------------------------------
# STEP 1
# Find or draw your sprites and save them as GIFs to my_work/my_images
# Give them short names so that they are easy to enter here.

# Create your sprite objects, either images
sprite = ImageSprite('my_images/face.gif')
sprite.centre()

# Or you can use simple shapes
alien = Sprite(canvas().create_oval(10,10, 50,50, fill='red'))

# You can also make lists of sprites
gems = [] # An empty list
for i in range(10): # Make 10
    gem = Sprite(canvas().create_oval(10,10, 50,50, fill='blue'))
    gem.move_to_random_pos()
    gems.append(gem)  

    
# ---------------------------------------------------------
# STEP 3
# Define your functions to control the game and its sprites

def follow_mouse():
    sprite.move_towards(mousex(), mousey(), 20)
    if sprite.touching(alien):
        end_game()
        

def collect_gems():
    gem = sprite.touching_any(gems)
    if gem:
        # Remove gem from our list and from the screen
        gems.remove(gem)
        gem.delete()
        

def move_alien():
    alien.move_towards(sprite.x, sprite.y, 10)


# ---------------------------------------------------------
# STEP 2    
# How will the user control the game? Add event handlers here

forever(follow_mouse)
forever(collect_gems)
forever(move_alien)


# ---------------------------------------------------------
# FINALLY
# Always call mainloop:

mainloop()
