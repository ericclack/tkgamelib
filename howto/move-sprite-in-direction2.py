from packages import *
  
create_canvas()
sprite = ImageSprite('images/face.gif')
sprite.pen_down()
sprite.turn_to(90)

def move_sprite():
    if is_key_down('a'):
        turn_left()
    if is_key_down('s'):
        turn_right()
    sprite.move_forward(5)
    
def turn_left():
    sprite.turn(-15)

def turn_right():
    sprite.turn(15)
        
forever(move_sprite, 25)
mainloop()
