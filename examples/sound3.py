import sys
sys.path.append('..')
from geekclub.pyscratch import *
from geekclub.sound import *

create_canvas()

# Not really necessary for this example, but why not:
sprite = ImageSprite('images/face.gif')
sprite.centre()
   
set_bpm(180)
laser = load_sound('sounds/laser.wav')
drum = load_sound('sounds/bass-drum.wav')
hh = load_sound('sounds/hh-cymbal.wav')

def lasers():
    laser.play()

def drums():
    drum.play()
    rest(.5)
    hh.play()

def follow_mouse():
    "Vary BPM based on mouse position"
    sprite.move_to(sprite.x, mousey())
    set_bpm(60 + sprite.y)
    print(bpm())
    
forever(lasers, beat_ms() * 3)
forever(drums, beat_ms()) # how can this work with varying BPM?
forever(follow_mouse)

mainloop()
