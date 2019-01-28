# Copyright 2019, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

from geekclub_packages import *

create_canvas()

# Not really necessary for this example, but why not:
sprite = ImageSprite('images/face.gif')
sprite.centre()

laser = load_sound('sounds/laser.wav')

def laser_sound():
    laser.play()

forever(laser_sound, 500)

mainloop()
