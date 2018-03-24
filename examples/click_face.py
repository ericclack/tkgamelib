# 1, Import the library
import sys; sys.path.append('..')
from geekclub.pyscratch import *
import random

# 2, the canvas
create_canvas('click the face')
world = Struct(score=0)	# set score to zero

# 3, the face
face = ImageSprite('images/face.gif')
face.speed_x = random.randint(-20,20)
face.speed_y = random.randint(-20,20)
face.max_speed = 100

# 4, setup the movement function
def move_face():
    face.move_with_speed()
    face.if_on_edge_bounce()

# 5, click hits the face
def check_for_hit():
    if mouse_touching(face):
        face.move_to_random_pos()
        face.accelerate(1.1)
        world.score +=1     # add one to the score
        show_variable("score",world.score)  # show the score
        
# 6, off we go
when_button1_clicked(check_for_hit)
forever(move_face)
mainloop()
