import sys
sys.path.append('..')
from geekclub.pyscratch import *
from geekclub.sound import *

create_canvas()

# Not really necessary for this example, but why not:
sprite = ImageSprite('images/face.gif')
sprite.centre()

laser = load_sound('sounds/laser.wav')

def laser_sound():
    laser.play()

forever(laser_sound, 500)

mainloop()
