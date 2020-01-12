# Copyright 2014, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General 
# Public License

"""Canvas and events for TKGameLib

Author: Eric Clack, eric@bn7.net

To generate doc for this module run:
pydoc3 -w pyscratch

"""

import os
import random
import math
import colorsys
import time
import inspect
import platform

from tkinter import *
from tkinter import simpledialog
 
CANVAS = None
def canvas(): return CANVAS

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800

BANNER=None
VARIABLES={}
VAR_FONT_SIZE=30

# A dictionary of functions run with forever command
# used to pause or restart, especially in end game
# sequence
FOREVER_FNS={}

KEYS_DOWN = {}
KEYDOWN_DELAY = .1


def mouse_touching(sprite):
    return point_inside_box((mousex(), mousey()),
                            CANVAS.bbox(sprite.spriteid))


def mouse_touching_any(sprites):
    for s in sprites:
        if mouse_touching(s):
            return s


def _key_pressed(event):
    """Record time of last key down event"""
    KEYS_DOWN[event.char] = time.time()


def _key_released(event):
    if is_mac():
        # On Mac OS X, key_press and key_release events alternate when
        # a key is held down, we use the last time the key was pressed
        # and ignore event
        pass
    else:
        if event.char in KEYS_DOWN:
            del(KEYS_DOWN[event.char])

            
def is_key_down(key):
    """Experimental tracking of multiple key presses.

    Works well with ascii chars, including space, needs some
    work for arrow keys etc (with event.keysym prop?)."""
    if is_mac():
        return key in KEYS_DOWN and KEYS_DOWN[key] > (time.time() - KEYDOWN_DELAY)
    else:
        return key in KEYS_DOWN 
        

def create_canvas(window_title="TKGame", canvas_width=CANVAS_WIDTH, canvas_height=CANVAS_HEIGHT, **args):
    """Create the drawing / game area on the screen

    Ready for our sprites or drawing.
    """
    global CANVAS, CANVAS_WIDTH, CANVAS_HEIGHT
    CANVAS_WIDTH=canvas_width
    CANVAS_HEIGHT=canvas_height
    
    master = Tk()
    CANVAS = Canvas(master, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, **args)
    CANVAS.pack()
    if window_title:
        master.wm_title(window_title)

    CANVAS.focus_set()    
    CANVAS.bind('<KeyPress>', _key_pressed)
    CANVAS.bind('<KeyRelease>', _key_released)

    # Fix CWD for Mu editor so that relative links work
    caller_info = inspect.stack()[1]
    caller_path = os.path.split(caller_info[1])[0]
    if caller_path.startswith('/'): 
        if caller_path != os.getcwd():
            print("Fixed current working directory for Mu")
            os.chdir(caller_path)


def canvas_width(): return CANVAS_WIDTH
def canvas_height(): return CANVAS_HEIGHT


def offscreen(x,y):
    """Put x,y offscreen so that it can't be seen"""
    if x < CANVAS_WIDTH*5:
        x += CANVAS_WIDTH*5
    return x,y

def onscreen(x,y):
    """Put x,y onscreen"""
    if x > CANVAS_WIDTH*5:
        x -= CANVAS_WIDTH*5
    return x,y

def clear_canvas():
    """Remove everything from the canvas"""
    CANVAS.delete(ALL)

def clear_pen():
    """Clear pen drawings"""
    CANVAS.delete("pen")        

def banner(message, ms=None, **args):
    """Display a basic text banner in the middle of the screen.

    Clear it after a period if ms set"""
    global BANNER
    if BANNER: clear_banner()
    BANNER = CANVAS.create_text(CANVAS_WIDTH/2, CANVAS_HEIGHT/2,
                                font=("default", 50), text=message, **args)
    if ms:
        future_action(clear_banner, ms)

def show_variable(label, value, slot=0, **args):
    if slot in VARIABLES:
        CANVAS.delete(VARIABLES[slot])
    VARIABLES[slot] = CANVAS.create_text(15, 15 + VAR_FONT_SIZE*slot,
                                         font=("default", VAR_FONT_SIZE),
                                         text="%s: %s" % (label, value),
                                         anchor="nw", **args)

def show_variables(vars, **args):
    for i, (label, value) in enumerate(vars):
        show_variable(label, value, i, **args)
    
def askstring(title, prompt):
    return simpledialog.askstring(title, prompt, parent=CANVAS)

def askinteger(title, prompt):
    return simpledialog.askinteger(title, prompt, parent=CANVAS)

def clear_banner():
    """Clear any banner set by `banner` method."""
    CANVAS.delete(BANNER)

def _bind_fn(event, fn):
    """Bind an event to a function, including those with no args.

    Event callbacks must have one argument to receive the event, 
    but often this is not used. So for convenience we allow
    user to supply zero argument event callbacks."""
    
    arity = len(inspect.signature(fn).parameters)
    if arity == 1:
        CANVAS.bind(event, fn)
    elif arity == 0:
        # Wrap fn with a new fn that discards event arg
        CANVAS.bind(event, lambda event: fn())
    else:
        assert False, "Your event function must have zero or one argument"
    
def when_button1_clicked(fn):
    _bind_fn('<Button-1>', fn)

def when_button1_dragged(fn):
    _bind_fn('<B1-Motion>', fn)

def when_button1_released(fn):
    _bind_fn('<ButtonRelease-1>', fn)    

def when_mouse_enter(fn):
    _bind_fn('<Enter>', fn)

def when_mouse_motion(fn):
    _bind_fn('<Motion>', fn)        

def when_button2_clicked(fn):
    _bind_fn('<ButtonPress-2>', fn)

def when_key_pressed(key, fn):
    _bind_fn('%s' % key, fn)


def mousex(): return CANVAS.winfo_pointerx() - CANVAS.winfo_rootx()
def mousey(): return CANVAS.winfo_pointery() - CANVAS.winfo_rooty()


def forever(fn, ms=25):
    """Keep doing something forever, every ms milliseconds"""
    FOREVER_FNS[fn] = True
    def wrapper():
        if FOREVER_FNS.get(fn, False):
            fn()
        if fn in FOREVER_FNS:
            CANVAS.after(ms, wrapper)
    CANVAS.after(ms, wrapper)

def pause_forever(fn):
    FOREVER_FNS[fn] = False

def resume_forever(fn):
    FOREVER_FNS[fn] = True

def kill_forever(fn):
    del FOREVER_FNS[fn]

def future_action(fn, ms):
    """Do something in the future, in ms milliseconds"""
    CANVAS.after(ms, fn)

def _quit_game():
    canvas().quit()

def end_game(message='Game Over', fn=_quit_game, ms=5000, **args):
    for f in FOREVER_FNS:
        pause_forever(f)
    banner(message, ms, **args)
    future_action(fn, ms)

def restart_game():
    for f in FOREVER_FNS:
        resume_forever(f)
            

if __name__ == "__main__":
    import doctest
    doctest.testmod()


