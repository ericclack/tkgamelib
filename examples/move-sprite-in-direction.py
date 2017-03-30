import sys; sys.path.append('..')
from geekclub.pyscratch import *
  
create_canvas()
sprite = ImageSprite('images/face.gif')
sprite.pen_down()
sprite.turn_to(90)

def move_sprite(event):
    sprite.move_forward(5)
    
def turn_left(event):
    sprite.turn(-5)

def turn_right(event):
    sprite.turn(5)
        
when_key_pressed('<space>', move_sprite)
when_key_pressed('<Left>', turn_left)
when_key_pressed('<Right>', turn_right)

mainloop()
