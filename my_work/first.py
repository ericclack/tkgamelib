# 1, Import the library
import sys; sys.path.append('..')
from geekclub.pyscratch import *

# 2, Create the canvas  
create_canvas()

# Your own program code here
sprite = ImageSprite('my_images/face.gif')
sprite.pen_down()

def move_sprite():
    sprite.move(10,10)

when_key_pressed('<space>', move_sprite)

# 3, Finally, the main program loop
mainloop()
