
import os
import pibrella
import time


PLAYER = "/usr/bin/mpc"

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
    pibrella.light.green.pulse(0.5)
    mpc('play')
    mpc('next')
   
def toggle_play(pin):
    if pin.read() == 1:
	mpc("pause")
	pibrella.light.red.pulse(0.5)
    else:
	pibrella.light.red.off()
	mpc("play")

set_up_playlist()
pibrella.button.released(play_next_mp3)
pibrella.input.a.changed(toggle_play)
pibrella.pause()
