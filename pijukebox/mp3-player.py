# Copyright 2014, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

import os
import pibrella
import time
import sys

# Halt or just quit this program?
REALLY_HALT = True
if 'SUDO_UID' in os.environ or 'TERM' in os.environ:
    print "Won't really halt -- running as sudo / from term"
    REALLY_HALT = False

# Show we're loaded
pibrella.buzzer.buzz(500)
time.sleep(0.5)
pibrella.buzzer.off()
time.sleep(0.5)
pibrella.buzzer.buzz(250)
time.sleep(0.5)
pibrella.buzzer.off()
time.sleep(0.5)
pibrella.buzzer.buzz(125)
time.sleep(0.5)
pibrella.buzzer.off()
time.sleep(0.5)

pibrella.light.green.pulse(0.5)

def mpc(command):
    os.system('mpc %s' % command)

def mpc_add_all_to_playlist():
    os.system('mpc ls | mpc add')

def set_up_playlist():
    mpc('update')
    mpc('clear')
    mpc_add_all_to_playlist()
    mpc('random on')
    mpc('repeat on')

def anti_bounce():
    time.sleep(0.05)

def really_pressed(pin):
    """Deal with switch bounce"""
    anti_bounce()
    return pin.read()

def next_prev_mp3(pin):
    """A quick click is next, longer hold are back"""
    if not(really_pressed(pin)): return

    pibrella.light.red.off()
    time.sleep(0.5)
    mpc('play')
    if pin.read() == 1:
        print "Prev"
        mpc('prev')
    else:
        print "Next"
        mpc('next')
   
def toggle_play(pin):
    anti_bounce()
    if pin.read() == 1:
	mpc("pause")
	pibrella.light.red.pulse(0.5)
    else:
	pibrella.light.red.off()
	mpc("play")

def toggle_random(pin):
    anti_bounce()
    if pin.read() == 1:
        mpc("random on")
	pibrella.light.yellow.pulse(0.5)
    else:
        mpc("random off")
	pibrella.light.yellow.off()

def check_halt(pin):
    print "Checking whether to halt..."
    print "keep button pressed for 5 seconds to halt"
    time.sleep(5)
    if pin.read() == 1:
        print "Halting!"
        mpc("pause")
        if REALLY_HALT:
            os.system('/sbin/halt')
            time.sleep(5)
        sys.exit()


set_up_playlist()
pibrella.button.changed(next_prev_mp3)
pibrella.input.a.changed(toggle_play)
pibrella.input.b.changed(toggle_random)
pibrella.input.d.pressed(check_halt)
pibrella.pause()
