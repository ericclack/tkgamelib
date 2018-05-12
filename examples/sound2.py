import sys
sys.path.append('..')
from geekclub.pyscratch import *
from geekclub.sound import *

create_canvas()

# Not really necessary for this example, but why not:
sprite = ImageSprite('images/face.gif')
sprite.centre()
   
laser = load_sound('sounds/laser.wav')
drum = load_sound('sounds/bass-drum.wav')
hh = load_sound('sounds/hh-cymbal.wav')

def lasers():
    laser.play()

def on_beat():
    drum.play()

def off_beat():
    hh.play()

set_bpm(120)
every_beat(on_beat)
every_off_beat(off_beat)
every_n_beats(3, lasers)

mainloop()
