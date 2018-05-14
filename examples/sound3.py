import sys
sys.path.append('..')
from geekclub.pyscratch import *
from geekclub.sound import *

create_canvas()

# Move the sprite to change the BPMs
sprite = ImageSprite('images/face.gif')
sprite.centre()
   
laser = load_sound('sounds/laser.wav')
drum = load_sound('sounds/bass-drum.wav')
hh = load_sound('sounds/hh-cymbal.wav')

world = Struct(bpm = 180, tick = 0)

def beat():
    world.tick += 1

    # On even ticks play beat, on odd, off_beat
    if world.tick % 2 == 0:
        drum.play()
    else:
        hh.play()

    # Every third beat (so every 6 ticks), play this
    if world.tick % 6 == 0:
        laser.play()

    # Next beat based on BPM
    future_action(beat, bpm_to_ms(world.bpm))

    
def follow_mouse():
    "Vary BPM based on mouse position"
    sprite.move_to(sprite.x, mousey())
    new_bpm = 60 + sprite.y
    if new_bpm != world.bpm:
        print("New BPM: ", world.bpm)
        world.bpm = new_bpm

    
forever(follow_mouse)
beat() # This fn takes care of repeating itself

mainloop()
