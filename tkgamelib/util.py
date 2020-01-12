# Copyright 2014, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General 
# Public License

"""Utils for TKGameLib - things with few dependencies, except 
to the standard libraries. 

Author: Eric Clack, eric@bn7.net

To generate doc for this module run:
pydoc3 -w pyscratch

"""

import random
import math
import colorsys
import platform


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

                    
class Struct:
    """A handy store for related variables."""
    def __init__(self, **entries): self.__dict__.update(entries)
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()
