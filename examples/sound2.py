# Copyright 2019, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

import sys
from geekclub_packages import *

create_canvas()

# Not really necessary for this example, but why not:
sprite = ImageSprite('images/face.gif')
sprite.centre()
   
laser = load_sound('sounds/laser.wav')
drum = load_sound('sounds/bass-drum.wav')
hh = load_sound('sounds/hh-cymbal.wav')

# Beats
world = Struct(bpm = 180, tick = 0)

def beat():
    # On even ticks play beat, on odd, off_beat
    if world.tick % 2 == 0:
        drum.play()
    else:
        hh.play()

    # Every third beat (so every 6 ticks), play this
    if world.tick % 6 == 0:
        laser.play()

    world.tick += 1
    

forever(beat, bpm_to_ms(world.bpm))
mainloop()
