import sys; sys.path.append('..')
from geekclub.pyscratch import *
  
create_canvas()

circles = []

for n in range(1000):
    circle_shape = canvas().create_oval(0,0, 15,15, fill=random_colour())
    circle = Sprite(circle_shape)
    circle.move_to_random_pos()
    circles.append(circle)


def check_move_circle():
    hit = mouse_touching_any(circles)
    if hit:
        hit.move(1,0)
    
forever(check_move_circle)

mainloop()
