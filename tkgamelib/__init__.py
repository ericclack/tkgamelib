# Copyright 2014, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General 
# Public License

"""An attempt to make Scratch-style coding in Python easier.

See examples in the folder examples, or more info on github.com:
https://github.com/ericclack/geekclub

Author: Eric Clack, eric@bn7.net

To generate doc for this module run:
pydoc3 -w pyscratch
"""

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

def is_mac():
    return platform.system() == 'Darwin'

def hexs(v):
    """Return a number in range 0-255 as two hex digits 0-ff"""
    h = hex(int(v))[2:]
    if len(h) == 1: h = "0" + h
    return h

def hsv_to_hex(h, s, v):
    """Convert HSV values (0-1) to a hex string #000000-#ffffff.

    The first number is hue: red=0, green=0.333
    The second saturation (how much colour)
    And last brightness: black=0, brightest=1

    White:
    >>> hsv_to_hex(0, 0, 1)
    '#ffffff'

    Red:
    >>> hsv_to_hex(0, 1, 1)
    '#ff0000'
    """
    (r, g, b) = colorsys.hsv_to_rgb(h, s, v)
    return "#" + hexs(255*r) + hexs(255*g) + hexs(255*b)

def random_colour(s=1, v=1):
    """A random colour as a hex string, suitable for passing to canvas shapes.

    With optional saturation and value (brightness)."""
    return hsv_to_hex(random.random(), s, v)

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


def overlapping_rect(rect1, rect2):
    """Does rect1 overlap rect2, e.g. are they touching?
    If so, return the overlapping rectangle, otherwise None.
    
    >>> overlapping_rect((0,0,10,10), (20,20,30,30))
    >>> overlapping_rect((0,0,100,100), (20,20,30,30))
    (20, 20, 30, 30)
    >>> overlapping_rect((0,0,100,100), (60,60,130,130))
    (60, 60, 100, 100)
    >>> overlapping_rect((200,200,300,300), (20,20,210,210))
    (200, 200, 210, 210)
    >>> overlapping_rect((50,50,100,100), (0,75,400,75))
    (50, 75, 100, 75)
    """
    (ax1, ay1, ax2, ay2) = rect1
    (bx1, by1, bx2, by2) = rect2

    ox1 = max(ax1, bx1)
    oy1 = max(ay1,by1)
    ox2 = min(ax2, bx2)
    oy2 = min(ay2,by2)
    
    if ox1 <= ox2 and oy1 <= oy2:
        return (ox1, oy1, ox2, oy2)


def distance_between_points(x1,y1, x2,y2):
    """
    >>> distance_between_points(0,0, 100,0)
    100.0
    >>> distance_between_points(0,0, 0,50)
    50.0
    >>> distance_between_points(500,500, 200,100)
    500.0
    """
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    return math.sqrt(dx**2+dy**2)


def mouse_touching(sprite):
    return point_inside_box((mousex(), mousey()),
                            CANVAS.bbox(sprite.spriteid))


def mouse_touching_any(sprites):
    for s in sprites:
        if mouse_touching(s):
            return s


def mag_angle_to_xy(mag, angle):
    """Convert magnitude and angle to vector x, y
    >>> mag_angle_to_xy(1, 0)
    (1.0, 0.0)
    >>> x, y = mag_angle_to_xy(1, 30)
    >>> math.isclose(x, 0.866, abs_tol=0.001) and math.isclose(y, 0.5, abs_tol=0.001)
    True
    """
    x = math.cos(math.radians(angle))*mag
    y = math.sin(math.radians(angle))*mag
    return (x, y)


def translate_point(x, y, distance, angle):
    """Return a new point moving x,y by distance along angle"""
    x2, y2 = mag_angle_to_xy(distance, angle)
    return(x + x2, y + y2)


def xy_to_mag_angle(x, y):
    """Convert vector x, y to magnitude and angle
    >>> xy_to_mag_angle(3,4)[0]
    5.0
    >>> xy_to_mag_angle(1,1)[1]
    45.0
    >>> xy_to_mag_angle(-1,1)[1]
    -45.0
    """
    mag = math.sqrt(x**2 + y**2)
    angle = math.degrees(math.atan2(y, x))
    return (mag, angle)


def rotate_point(x, y, angle):
    """Rotate a point (x,y) around origin (0,0) by angle in degrees"""
    rad = math.radians(angle)
    return (x*math.cos(rad) - y*math.sin(rad),
            y*math.cos(rad) + x*math.sin(rad))


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
        

def create_canvas(window_title="Pyscratch Game", canvas_width=CANVAS_WIDTH, canvas_height=CANVAS_HEIGHT, **args):
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


def forever(fn, ms=100):
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
    
    
class Sprite:
    """A sprite that can be moved around the screen."""

    def __init__(self, spriteid):
        """spriteid can be a number or tag"""
        self.spriteid = spriteid
        self.pen = False
        self.pen_width = 1
        self.pen_colour_hex = "#000"
        self.speed_x = 0
        self.speed_y = 0
        self.max_speed = 5
        self.direction = 0

    def pos(self):
        """Return (x,y) of this sprite"""
        return CANVAS.bbox(self.spriteid)[0:2]

    @property
    def x(self): return self.pos()[0]

    @property
    def y(self): return self.pos()[1]

    @property
    def centre_x(self): return self.x + self.width/2

    @property
    def centre_y(self): return self.y + self.height/2
    
    @property
    def width(self):
        """The width in px of this sprite"""
        box = CANVAS.bbox(self.spriteid)
        return box[2]-box[0]

    @property
    def height(self):
        """The height in px of this sprite"""
        box = CANVAS.bbox(self.spriteid)
        return box[3]-box[1]


    def move(self, x, y):
        """Move by x and y pixels"""
        if self.pen:
            cx, cy = self.pos()
            CANVAS.create_line(cx,cy, cx+x,cy+y,
                               width=self.pen_width,
                               fill=self.pen_colour_hex,
                               tags="pen")
        CANVAS.move(self.spriteid, x, y)

    def delete(self):
        """Delete this sprite from the canvas"""
        CANVAS.delete(self.spriteid)

    def distance_between(self, sprite):
        """Distance between this sprite and another"""
        return distance_between_points(self.centre_x, self.centre_y,
                                       sprite.centre_x, sprite.centre_y)

    def move_towards(self, to_x, to_y, steps=1):
        """Move towards a point"""
        x, y = self.pos()
        dx = to_x - x
        dy = to_y - y
        distance = math.sqrt(dx**2+dy**2)
        if distance > 0.1:
            scale = steps/distance
            self.move(dx*scale, dy*scale)

    def move_to(self, x, y):
        """Move to a new x,y pos"""
        cx, cy = self.pos()
        self.move(x-cx, y-cy)

    def centre(self):
        self.move_to(CANVAS_WIDTH/2, CANVAS_HEIGHT/2)

    def offscreen(self):
        self.move_to(*offscreen(self.x, self.y))

    def turn(self, degrees):
        self.direction = (self.direction + degrees) % 360

    def turn_to(self, degrees):
        self.direction = degrees
        
    def move_forward(self, steps):
        x2, y2 = translate_point(self.x, self.y, steps, self.direction)
        self.move_to(x2, y2)
        
    def move_to_random_pos(self):
        """Move to a random pos on the canvas"""
        self.move_to(random.randint(1,CANVAS_WIDTH), random.randint(1,CANVAS_HEIGHT))

    def pen_down(self):
        """Start drawing when the sprite moves"""
        self.pen = True

    def pen_up(self):
        """Pick up the pen so that no lines are drawn"""
        self.pen = False

    def toggle_pen(self):
        self.pen = not(self.pen)

    def pen_colour(self, h, s=100, v=100):
        self.pen_colour_hex = hsv_to_hex(h/360.0, s/100.0, v/100.0)

    def touching(self, sprite):
        """Is this sprite touching another sprite?"""
        our_box = CANVAS.bbox(self.spriteid)
        their_box = CANVAS.bbox(sprite.spriteid)

        return overlapping_rect(our_box, their_box) is not None
    
    def touching_any(self, sprites):
        """Is this sprite touching any other sprite in the list?"""
        for s in sprites:
            if s == self: continue
            if self.touching(s):
                return s
        return False

    def above(self, sprite):
        """Is this sprite above another sprite"""
        (x1,y1,   x2,y2) = CANVAS.bbox(self.spriteid)
        (sx1,sy1, sx2,sy2) = CANVAS.bbox(sprite.spriteid)
        
        # Are we overlapped on x axis and above?
        return (x1 < sx2 and x2 > sx1) and (y1 < sy1)

    def below(self, sprite):
        """Is this sprite below another sprite"""
        (x1,y1,   x2,y2) = CANVAS.bbox(self.spriteid)
        (sx1,sy1, sx2,sy2) = CANVAS.bbox(sprite.spriteid)
        
        # Are we overlapped on x axis and below?
        return (x1 < sx2 and x2 > sx1) and (y2 > sy2)

    def left_of(self, sprite):
        """Is this sprite left of another sprite"""
        (x1,y1,   x2,y2) = CANVAS.bbox(self.spriteid)
        (sx1,sy1, sx2,sy2) = CANVAS.bbox(sprite.spriteid)
        
        # Are we overlapped on y axis and left?
        return (y1 < sy2 and y2 > sy1) and (x1 < sx1)
    
    def right_of(self, sprite):
        (x1,y1,   x2,y2) = CANVAS.bbox(self.spriteid)
        (sx1,sy1, sx2,sy2) = CANVAS.bbox(sprite.spriteid)
        
        # Are we overlapped on y axis and right?
        return (y1 < sy2 and y2 > sy1) and (x2 > sx2)
    

    def move_with_speed(self):
        self._limit_speed()
        self.move(self.speed_x, self.speed_y)

        
    def accelerate_towards(self, to_x, to_y, force=1):
        mag, angle = xy_to_mag_angle(to_x-self.centre_x, to_y-self.centre_y)
        dx, dy = mag_angle_to_xy(min(mag, force), angle)
        self.speed_x += dx
        self.speed_y += dy


    def accelerate(self, speed_up):
        self.speed_x *= speed_up
        self.speed_y *= speed_up
            

    def _limit_speed(self):
        """Check and reduce speed so it never exceeds +/- max_speed"""
        m, a = xy_to_mag_angle(self.speed_x, self.speed_y)
        if m > self.max_speed:
            self.speed_x, self.speed_y = mag_angle_to_xy(self.max_speed, a)


    def if_on_edge_bounce(self):
        x, y = self.pos()
        if x < 0: self.speed_x = abs(self.speed_x)
        if y < 0: self.speed_y = abs(self.speed_y)
        if x + self.width > CANVAS_WIDTH: self.speed_x = -abs(self.speed_x)
        if y + self.height > CANVAS_HEIGHT: self.speed_y = -abs(self.speed_y)

    def if_on_edge_wrap(self):
        x, y = x2, y2 = self.pos()
        if x + self.width < 0: x2 = CANVAS_WIDTH
        if y + self.height < 0: y2 = CANVAS_HEIGHT
        if x > CANVAS_WIDTH: x2 = 0
        if y > CANVAS_HEIGHT: y2 = 0
        self.move_to(x2, y2)
        
    def bounce_up(self):
        self.speed_y = -abs(self.speed_y)

    def bounce_down(self):
        self.speed_y = abs(self.speed_y)

    def bounce_off(self, sprite, slowdown=1):
        if self.below(sprite):
            self.speed_y = abs(self.speed_y * slowdown)
        if self.above(sprite):
            self.speed_y = -abs(self.speed_y * slowdown)
        if self.right_of(sprite):
            self.speed_x = abs(self.speed_x * slowdown)
        if self.left_of(sprite):
            self.speed_x = -abs(self.speed_x * slowdown)

    def replace_canvas_object(self, newobjid):
        self.delete()
        self.spriteid = newobjid
        

class ImageSprite(Sprite):
    """A sprite for a bitmap GIF image or sequence of image costumes.

    Create like this:
    > create_canvas()
    > s = ImageSprite('images/face.gif')
    Or:
    > image = PhotoImage(file='images/face.gif')
    > s = ImageSprite(image)

    Or for multiple sprites:
    > s = ImageSprite(['images/face1.gif', 'images/face2.gif'])

    Multiple images share the same tag and the image IDs
    are stored in the sprite object. All but the active image
    are stored offscreen. 
    """

    next_tag_id = 1

    @staticmethod
    def unique_tagname():
        id = ImageSprite.next_tag_id
        ImageSprite.next_tag_id += 1
        return "pyscratch-tag-%d" % id

    def __init__(self, imgs, x=100, y=100):
        self.costume_ids = []
        self.photo_images = []
        
        if isinstance(imgs, list):
            tag = ImageSprite.unique_tagname()
        else:
            imgs = [imgs]
            tag = None # Just one sprite
        
        for img in imgs:
            if isinstance(img, str):
                assert img.lower().endswith(".gif"), "Sorry, ImageSprite only works with GIFs"
                self.photo_images.append( PhotoImage(file=img) )
            else:
                self.photo_images.append( img )

            if self.costume_ids:
                # Successive sprites are hidden offscreen
                x, y = offscreen(x, y)
                
            spriteid = CANVAS.create_image(x,y, image=self.photo_images[-1], tag=tag)
            self.costume_ids.append(spriteid)
        
        super(ImageSprite, self).__init__(self.costume_ids[0])
        self.switch_costume(1)


    def _switch_to_costume_id(self, newid):
        """Put current costume offscreen and new one onscreen"""

        # Move current costume offscreen
        x, y = self.x, self.y
        self.move_to(*offscreen(x, y))

        # And then move the new costume back onscreen 
        self.spriteid = newid
        self.move_to(x, y)
            

    def next_costume(self):
        """Show next costume if this sprite is composed of multiple ones"""

        costumes = len(self.costume_ids)
        if costumes == 1: return # Only one sprite
        
        i = self.costume_ids.index(self.spriteid)
        i = (i + 1) % costumes
        self._switch_to_costume_id(self.costume_ids[i])        
        
        
    def switch_costume(self, number):
        "Show costume by number, 1 is the first one"
        switch_to_id = self.costume_ids[number-1]
        if self.spriteid == switch_to_id:
            return # nothing to do

        self._switch_to_costume_id(switch_to_id)
                

    def which_costume(self):
        "The costume number of the current costume, 1 is the first"
        return self.costume_ids.index(self.spriteid) + 1
        

class PolygonSprite(Sprite):
    """A multi-sided sprite that can be rotated and scaled."""

    def __init__(self, points, **attribs):
        """Points is a list of (x,y) tuples, with its centre at (0,0)"""
        assert isinstance(points[0][0] + points[0][1], int), "Points should be a list of (x,y) tuples"
        self.points = points
        self.attribs = attribs
        spriteid = CANVAS.create_polygon(points, attribs)
        super(PolygonSprite, self).__init__(spriteid)
        self.created_at_x, self.created_at_y = self.pos()

    def rotate(self, angle):
        """Rotate this polygon by an angle and redraw it"""
        # Capture where this sprite got to
        current_x, current_y = self.pos() 
        dx = current_x - self.created_at_x; dy = current_y - self.created_at_y
        
        self.points = [rotate_point(x, y, angle) for x,y in self.points]
        self.replace_canvas_object(CANVAS.create_polygon(self.points, self.attribs))
        self.created_at_x, self.created_at_y = self.pos()
        self.move(dx+1, dy+1) # Why is +1 needed?
        
        
class Struct:
    """A handy store for related variables."""
    def __init__(self, **entries): self.__dict__.update(entries)
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()


