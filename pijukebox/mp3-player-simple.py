# Copyright 2014, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

import os
import pibrella

PLAYER = "/usr/bin/mpc"

# Show we're loaded
pibrella.lights.pulse(0.2)

def mpc(command):
    os.system('mpc %s' % command)

def mpc_add_all_to_playlist():
    os.system('mpc ls | mpc add')

def set_up_playlist():
    mpc('clear')
    mpc_add_all_to_playlist()
    mpc('random on')
    mpc('repeat on')

def play_next_mp3(pin):
    pibrella.lights.fade(100, 0, 0.3)
    mpc('play')
    mpc('next')
    
set_up_playlist()
pibrella.button.released(play_next_mp3)
pibrella.pause()
