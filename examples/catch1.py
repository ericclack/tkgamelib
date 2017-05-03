import sys; sys.path.append('..')
from geekclub.pyscratch import *
  
create_canvas()

INIT_SPEED=-20
GRAVITY=0.2

def new_ball():
    oval = canvas().create_oval(0,0, 30,30, fill=hsv_to_hex(random.random(),1,1))
    ball = Sprite(oval)
    ball.move_to(random.randint(0, CANVAS_WIDTH), CANVAS_HEIGHT-10)
    ball.speed_y = random.randint(INIT_SPEED,INIT_SPEED/2)
    return ball

world = Struct(ball = new_ball())

def shoot_balls():
    b = world.ball
    b.speed_y += GRAVITY
    b.move_with_speed()
    if b.y > CANVAS_HEIGHT:
        b.delete()
        world.ball = new_ball()
    
forever(shoot_balls, 30)
mainloop()
