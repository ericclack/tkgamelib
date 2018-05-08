# Copyright 2018, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General 
# Public License

"""Sounds for PyScratch using simpleaudio.

See examples in the folder examples, or more info on github.com:
https://github.com/ericclack/geekclub/sound1.py

To install: pip install simpleaudio
Get free to use sounds here: https://freesound.org/

Author: Eric Clack, eric@bn7.net
"""

import simpleaudio as sa
import time

BPM = 1 * 60

def load_sound(file):
    "Load a sound, tested with WAV files"
    return sa.WaveObject.from_wave_file(file)

def set_bpm(b):
    global BPM
    BPM = b

def bps():
    "Beats per second"
    return BPM / 60

def beat_ms():
    "The length of a beat in miliseconds"
    return int(1000 / bps())

def rest(beats):
    "Rest for this many beats, e.g. 0.5"
    time.sleep(beat_ms() * beats / 1000)
    

