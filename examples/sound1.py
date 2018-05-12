import sys
sys.path.append('..')
from geekclub.pyscratch import *

# Install simpleaudio with: pip3 install simpleaudio
# You might need to upgrade pip3 first
import simpleaudio as sa

create_canvas()

# Not really necessary for this example, but why not:
sprite = ImageSprite('images/face.gif')
sprite.centre()

laser = sa.WaveObject.from_wave_file('sounds/laser.wav')

def laser_sound():
    laser.play()

forever(laser_sound, 500)

mainloop()
