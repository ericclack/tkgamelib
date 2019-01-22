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
sprite = ImageSprite('my_images/face.gif')
sprite.centre()
# Add any variables you like
sprite.score = 0

# Or you can use simple shapes
alien = Sprite(canvas().create_oval(10,10, 50,50, fill='red'))

# You can also make lists of sprites
gems = [] # An empty list
for i in range(30): # Make 30
    gem = Sprite(canvas().create_oval(10,10, 50,50, fill='blue'))
    gem.move_to_random_pos()
    gems.append(gem)  

    
# ---------------------------------------------------------
# STEP 3
# Define your functions to control the game and its sprites
# -- these must be defined before the event handlers

def follow_mouse():
    sprite.move_towards(mousex(), mousey(), 10)
    show_variables([
        ("Score", sprite.score),
        ("Gems left", len(gems))
    ])
    if sprite.touching(alien):
        end_game()
        

def collect_gem(gem):
    "Helper function to collect a gem"
    if gem:
        # Remove gem from our list and from the screen
        gems.remove(gem)
        gem.delete()    
        
def collect_gems():
    gem = sprite.touching_any(gems)
    if gem:
        sprite.score = sprite.score + 1
        collect_gem(gem)
        
    gem = alien.touching_any(gems)    
    if gem:
        sprite.score = sprite.score + 1
        collect_gem(gem)        
    

def move_alien():
    alien.move_towards(sprite.x, sprite.y, 5)


# ---------------------------------------------------------
# STEP 2    
# How will the user control the game? What will other
# sprites do? Add your event handlers here.

forever(follow_mouse)
forever(collect_gems)
forever(move_alien)


# ---------------------------------------------------------
# FINALLY
# Always call mainloop:

mainloop()
