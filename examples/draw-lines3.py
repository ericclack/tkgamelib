# Copyright 2014, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

"""Click to draw, with timed deletion of lines."""

import random
from packages import *

create_canvas()

# What colour? 0=Red, 120=Green, 240=Blue
hue = 0

lines = []

def change_colour():
    global hue
    hue += 1
    if hue > 255: hue = 0

    
def draw(event):
    global hue
    x = event.x
    y = event.y
    lines.append(
        canvas().create_line(x,y, CANVAS_WIDTH-x,CANVAS_HEIGHT-y,
             fill=hsv_to_hex(hue / 255, 1, 1),
             width=2))
    change_colour()


def delete_lines():
    if len(lines) > 10:
        canvas().delete(lines.pop(0))
        

def clear(event):
    canvas().delete(ALL)

banner("Drag the mouse to draw lines", 2000)
    
when_button1_dragged(draw)
when_button2_clicked(clear)
forever(delete_lines, 50)

mainloop()
