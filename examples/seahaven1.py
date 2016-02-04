# Copyright 2016, Eric Clack, eric@bn7.net 

# This program is distributed under the terms of the GNU General
# Public License

import random, sys
sys.path.append('..')
from geekclub.pyscratch import *

create_canvas()

spriteimg = PhotoImage(file='images/face.gif')
sprite = ImageSprite(spriteimg)
sprite.pen_down()
sprite.pen_width = 4

def follow_mouse():
    sprite.move_towards(mousex(), mousey(), 10)

def toggle_pen(event):
    sprite.toggle_pen()
    sprite.pen_colour(random.randint(1,360))

def thicker_pen(event):
    sprite.pen_width += 1

def thinner_pen(event):
    sprite.pen_width -= 1

forever(follow_mouse, 10)

when_key_pressed('<space>', toggle_pen)
when_key_pressed('<Up>', thicker_pen)
when_key_pressed('<Down>', thinner_pen)

mainloop()
