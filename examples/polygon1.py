import sys; sys.path.append('..')
from geekclub.pyscratch import *
  
create_canvas()

p = PolygonSprite( [(-100,-100), (100,-100), (100,100), (-100,100), (0,0), (-100,-100)], fill='red', outline='black' )
p.centre()

def move(event):
    p.move_forward(5)

def rotate_left(event):
    p.rotate(-5)
    p.turn(-5)

def rotate_right(event):
    p.rotate(5)
    p.turn(5)

when_key_pressed('<Left>', rotate_left)
when_key_pressed('<Right>', rotate_right)
when_key_pressed('<space>', move)

mainloop()
