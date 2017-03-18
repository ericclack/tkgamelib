import sys; sys.path.append('..')
from geekclub.pyscratch import *
  
create_canvas()
sprite = ImageSprite('my_images/face.gif')
sprite.pen_down()

def move_sprite(event):
    sprite.move(10,10)

when_key_pressed('<space>', move_sprite)
mainloop()
