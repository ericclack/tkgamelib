# Copyright 2014, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

"""Click to draw lines"""

import random, sys
sys.path.append('..')
from geekclub.pyscratch import *

create_canvas()

def draw(event):
    x = event.x
    y = event.y
    canvas().create_line(x,y, CANVAS_WIDTH-x,CANVAS_HEIGHT-y,
                  fill=random.choice(['red', 'green', 'blue', 'yellow']))

def clear(event):
    clear_canvas

when_button1_dragged(draw)
when_button2_clicked(clear)

mainloop()
