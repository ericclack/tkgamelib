# Copyright 2014, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

"""An attempt to make Scratch style coding in Python easier.

See examples in the folder examples, or more info on github.com:
https://github.com/ericclack/geekclub

Author: Eric Clack, eric@bn7.net

To Do:
- When Key Pressed
- Moving in a direction (degrees)
"""

import colorsys
from tkinter import *
import random
 
CANVAS = None
def canvas(): return CANVAS

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800

BANNER=None


def hexs(v):
    """Return a number in range 0-255 as two hex digits 0-ff"""
    h = hex(int(v))[2:]
    if len(h) == 1: h = "0" + h
    return h

def hsv_to_hex(h, s, v):
    """Convert HSV values (0-1) to a hex string #000000-#ffffff"""
    (r, g, b) = colorsys.hsv_to_rgb(h, s, v)
    return "#" + hexs(255*r) + hexs(255*g) + hexs(255*b)

def direction(mousepos, objpos):
    if mousepos > objpos:
        return 1
    else:
        return -1

def sign(v):
    """Return -1 or 1 indicating the sign of v

    >>> sign(-10)
    -1
    >>> sign(15303)
    1
    >>> sign(0)
    1
    """
    if v < -1: return -1
    else: return 1
    

def point_inside_box(point, box):
    """Is point (x,y) inside box (x1, y1, x2, y2)?

    >>> point_inside_box((50,50), (25, 25, 100, 100))
    True
    >>> point_inside_box((50,50), (75, 75, 100, 100))
    False
    >>> point_inside_box((50,50), (25, 75, 100, 100))
    False
    >>> point_inside_box((50,50), (50, 50, 100, 100))
    True
    """
    x,y = point
    x1, y1, x2, y2 = box
    return (x2 >= x >= x1) and (y2 >= y >= y1)



def create_canvas(window_title="Pyscratch Game"):
    global CANVAS
    master = Tk()
    CANVAS = Canvas(master, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    CANVAS.pack()
    if window_title:
        master.wm_title(window_title)

def clear_canvas():
    CANVAS.delete(ALL)

def clear_pen():
    CANVAS.delete("pen")        

def banner(message):
    global BANNER
    if BANNER: clear_banner()
    BANNER = CANVAS.create_text(CANVAS_WIDTH/2, CANVAS_HEIGHT/2,
                             font=("default", 50), text=message)

def clear_banner():
    CANVAS.delete(BANNER)

def when_button1_clicked(fn):
    CANVAS.bind('<Button-1>', fn)

def when_button1_dragged(fn):
    CANVAS.bind('<B1-Motion>', fn)

def when_mouse_enter(fn):
    CANVAS.bind('<Enter>', fn)

def when_mouse_motion(fn):
    CANVAS.bind('<Motion>', fn)        

def when_button2_clicked(fn):
    CANVAS.bind('<ButtonPress-2>', fn)

def when_key_pressed(key, fn):
    CANVAS.focus_set()
    CANVAS.bind('%s' % key, fn)
#    CANVAS.bind('<KeyPress-%s>' % key, fn)
    

def mousex(): return CANVAS.winfo_pointerx() - CANVAS.winfo_rootx()
def mousey(): return CANVAS.winfo_pointery() - CANVAS.winfo_rooty()


def forever(fn, ms=100):
    def wrapper():
        fn()
        CANVAS.after(ms, wrapper)
    CANVAS.after(ms, wrapper)

def future(fn, ms):
    CANVAS.after(ms, fn)


class Sprite:

    def __init__(self, spriteid):
        self.spriteid = spriteid
        self.pen = False
        self.pen_width = 1
        self.pen_colour_hex = "#000"
        self.speed_x = 0
        self.speed_y = 0
        self.max_speed = 5

    def pos(self):
        """Return (x,y) of this sprite"""
        return CANVAS.bbox(self.spriteid)[0:2]

    def x(self): return self.pos()[0]
    def y(self): return self.pos()[1]

    def move(self, x, y):
        """Move by x and y"""
        if self.pen:
            cx, cy = self.pos()
            CANVAS.create_line(cx,cy, cx+x,cy+y,
                               width=self.pen_width,
                               fill=self.pen_colour_hex,
                               tags="pen")
        CANVAS.move(self.spriteid, x, y)

    def delete(self):
        CANVAS.delete(self.spriteid)

    def move_towards(self, to_x, to_y, steps=1):
        x, y = self.pos()
        dx = direction(to_x, x)
        dy = direction(to_y, y)
        self.move(dx*steps, dy*steps)

    def move_to(self, x, y):
        cx, cy = self.pos()
        self.move(x-cx, y-cy)

    def move_to_random_pos(self):
        self.move_to(random.randint(1,CANVAS_WIDTH), random.randint(1,CANVAS_HEIGHT))

    def pen_down(self):
        self.pen = True

    def pen_up(self):
        self.pen = False

    def toggle_pen(self):
        self.pen = not(self.pen)

    def pen_colour(self, h, s=100, v=100):
        self.pen_colour_hex = hsv_to_hex(h/360.0, s/100.0, v/100.0)

    def touching(self, sprite):
        """Is this sprite touching another sprite?"""
        our_box = CANVAS.bbox(self.spriteid)
        their_box = CANVAS.bbox(sprite.spriteid)

        # Check if any corner of our_box is inside the other_box
        # then check the reverse
        (c1x, c1y, c2x, c2y) = our_box
        our_corners = [ (c1x,c1y), (c2x,c1y), (c1x,c2y), (c2x,c2y) ]
        for cx, cy in our_corners:
            if point_inside_box((cx,cy), their_box):
                return True
            
        (c1x, c1y, c2x, c2y) = their_box
        their_corners = [ (c1x,c1y), (c2x,c1y), (c1x,c2y), (c2x,c2y) ]
        for cx, cy in their_corners:
            if point_inside_box((cx,cy), our_box):
                return True               

        return False

    def touching_any(self, sprites):
        """Is this sprite touching any other sprite in the list?"""
        for s in sprites:
            if s == self: continue
            if self.touching(s):
                return s
        return False

    def below(self, sprite):
        x,y = self.pos()
        sx, sy = sprite.pos()
        return (sy < y)

    def move_with_speed(self):
        self.move(self.speed_x, self.speed_y)

    def accelerate_towards(self, to_x, to_y, steps=1):
        x, y = self.pos()
        dx = direction(to_x, x)
        dy = direction(to_y, y)
        self.speed_x = self.accelerate_upto_max(self.speed_x, dx*steps)
        self.speed_y = self.accelerate_upto_max(self.speed_y, dy*steps)
        
    def accelerate_upto_max(self, speed, increase):
        speed += increase
        if abs(speed) > self.max_speed:
            speed = sign(speed)*self.max_speed
        return speed

    def accelerate(self, speed_up):
        if abs(self.speed_x) < self.max_speed:
            self.speed_x *= speed_up
        if abs(self.speed_y) < self.max_speed:
            self.speed_y *= speed_up

    def if_on_edge_bounce(self):
        x, y = self.pos()
        if x < 0: self.speed_x = abs(self.speed_x)
        if y < 0: self.speed_y = abs(self.speed_y)
        if x > CANVAS_WIDTH: self.speed_x = -abs(self.speed_x)
        if y > CANVAS_HEIGHT: self.speed_y = -abs(self.speed_y)

    def bounce_up(self):
        self.speed_y = -abs(self.speed_y)

    def bounce_down(self):
        self.speed_y = abs(self.speed_y)


class ImageSprite(Sprite):

    def __init__(self, img, x=100, y=100):
        spriteid = CANVAS.create_image(x,y, image=img)
        super(ImageSprite, self).__init__(spriteid)


class Struct:
    def __init__(self, **entries): self.__dict__.update(entries)
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()
