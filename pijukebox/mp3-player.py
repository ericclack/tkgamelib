
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
time.sleep(0.5)
pibrella.light.yellow.pulse(0.5)
time.sleep(0.5)

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

def play_next_mp3(pin):
    pibrella.light.red.off()
    pibrella.light.green.pulse(0.5)
    mpc('play')
    mpc('next')
   
def toggle_play(pin):
    # Give the switch a chance to settle down
    time.sleep(0.1)
    if pin.read() == 1:
	mpc("pause")
	pibrella.light.red.pulse(0.5)
    else:
	pibrella.light.red.off()
	mpc("play")

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
pibrella.button.released(play_next_mp3)
pibrella.input.a.changed(toggle_play)
pibrella.input.d.pressed(check_halt)
pibrella.pause()
