# Copyright 2018, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General 
# Public License

"""Sounds for PyScratch using simpleaudio or winsound.

See examples in the folder examples, or more info on github.com:
https://github.com/ericclack/geekclub/sound1.py

To install: pip3 install simpleaudio
Get free to use sounds here: https://freesound.org/

Authors: Eric Clack, eric@bn7.net
         Mark Gossage
"""


## Fallback sound class ---------------------------------------

class DummySoundLib():
    "No-op sound library if we can't load simpleaudio"
    WaveObject = None

    def __init__(self):
        print("Can't play sound!")
        print("You need to install simpleaudio with `pip3 install simpleaudio`")
        DummySoundLib.WaveObject = self

    def from_wave_file(self, file):
        return self

    def play(self):
        pass


## winsound ---------------------------------------------------
## note: you don't need the winsound imported if this code
## is never used - that suprised me

class WinSoundObj:
    "Winsound sound object"
    def __init__(self, file):
        self.file = file

    def play(self):
        winsound.PlaySound(self.file, winsound.SND_FILENAME)

class WinSoundLib():
    "Winsound wrapper to look like simpleaudio"
    WaveObject = None

    def __init__(self):
        print("simpleaudio not installed, fallback to winsound")
        WinSoundLib.WaveObject = self

    def from_wave_file(self, file):
        return WinSoundObj(file)


## import code ------------------------------------------------
## Try simpleaudio, then winsound, then fallback

try:
    # attempt 1: simple audio
    import simpleaudio as sa
except ImportError:
    try:
        # attempt 2: winsound
        import winsound
        sa = WinSoundLib()
    except ImportError:
        # attempt 3: dummy sound
        sa = DummySoundLib()


## rest of the code -------------------------------------------

import time

def load_sound(file):
    "Load a sound, tested with WAV files"
    return sa.WaveObject.from_wave_file(file)

def bpm_to_ms(bpm):
    return int((60 / bpm) * 1000)
