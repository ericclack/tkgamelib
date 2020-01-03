from packages import *
  
create_canvas()
bg = ImageSprite('my_images/space-bg.gif')
bg.move_to(0,0)
sprite = ImageSprite('my_images/face.gif')
sprite.pen_down()


def move_sprite(event):
    sprite.move(10,10)

when_key_pressed('<space>', move_sprite)
mainloop()
