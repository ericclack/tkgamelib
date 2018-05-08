import sys
sys.path.append('..')
from geekclub.pyscratch import *

import simpleaudio as sa

create_canvas()

sprite = ImageSprite('images/face.gif')
sprite.centre()

laser = sa.WaveObject.from_wave_file('sounds/laser.wav')

def laser_sound():
    laser.play()

forever(laser_sound, 1000)

mainloop()
