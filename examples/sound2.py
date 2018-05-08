import sys
sys.path.append('..')
from geekclub.pyscratch import *
import time

# Install simpleaudio with: pip3 install simpleaudio
import simpleaudio as sa

create_canvas()

# Not really necessary for this example, but why not:
sprite = ImageSprite('images/face.gif')
sprite.centre()

# Get free to use sounds here: https://freesound.org/
def load_sound(file):
    return sa.WaveObject.from_wave_file(file)

bpm = 3 * 60
def bps(): return bpm / 60
def beat_ms():
    return int(1000 / bps())

print(bpm, bps(), beat_ms())

def rest(beats):
    time.sleep(beat_ms() * beats / 1000)
               
laser = load_sound('sounds/laser.wav')
drum = load_sound('sounds/bass-drum.wav')
hh = load_sound('sounds/hh-cymbal.wav')

def lasers():
    laser.play()

def drums():
    drum.play()
    rest(.5)
    hh.play()

forever(lasers, beat_ms() * 3)
forever(drums, beat_ms())

mainloop()
