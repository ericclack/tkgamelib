import sys
sys.path.append('..')
from geekclub.pyscratch import *

create_canvas()

# Some backgrounds
background = ImageSprite(['images/bg-blue-white.gif', 'images/bg-black-white.gif'])
background.move_to(0,0)

# Three image costumes for the face sprite
sprite = ImageSprite(["images/face.gif", "images/face2.gif", "images/face3.gif"])
sprite.centre()


def toggle():
    sprite.next_costume()

def toggle_background():
    # BUG: this costume is now above all others!
    background.next_costume(method="lower")

def costume_1(): sprite.switch_costume(1)
def costume_2(): sprite.switch_costume(2)
def costume_3(): sprite.switch_costume(3)

#forever(toggle, 500)
when_key_pressed('<space>', toggle)
when_key_pressed('b', toggle_background)
when_key_pressed('1', costume_1)
when_key_pressed('2', costume_2)
when_key_pressed('3', costume_3)

banner("Press space or B to see next costume", 2000)
future_action( lambda: banner("...or keys 1,2,3", 2000),
               2000 )

mainloop()
