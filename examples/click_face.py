# 1, Import the library
import sys; sys.path.append('..')
from geekclub.pyscratch import *
import random
import winsound


create_canvas('click the face')

face = ImageSprite('my_images/face.gif')
face.speed_x = random.randint(-20,20)
face.speed_y = random.randint(-20,20)
face.max_speed = 100
world = Struct(score=0)
##show_variable("score",world.score)
        
##def bounce_on_edge(s):
##    if s.x<=0:
##        
##        face.if_on_edge_bounce = def

def move_face():
    face.move_with_speed()
    face.if_on_edge_bounce()
##    if face.x<=0:
##        face.
##        or face.x+face.width>=canvas().width:
##        face.bounce

def check_for_hit():
    if mouse_touching(face):
        face.move_to_random_pos()
        face.accelerate(1.1)
        world.score +=1     # add one to the score
        show_variable("score",world.score)  # show the score
        winsound.MessageBeep(-1)
        

forever(move_face)
when_button1_clicked(check_for_hit)

mainloop()
