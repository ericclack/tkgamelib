# Copyright 2014, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General 
# Public License

"""Sprites for TKGameLib: moveable objects on the canvas.

Dependent on canvas module.

Author: Eric Clack, eric@bn7.net
"""

from tkgamelib.canvas import *
from tkgamelib.util import *


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
        self.max_speed = 20
        self.direction = 0

    def pos(self):
        """Return (x,y) of this sprite"""
        return canvas().bbox(self.spriteid)[0:2]

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
        box = canvas().bbox(self.spriteid)
        return box[2]-box[0]

    @property
    def height(self):
        """The height in px of this sprite"""
        box = canvas().bbox(self.spriteid)
        return box[3]-box[1]


    def move(self, x, y):
        """Move by x and y pixels"""
        if self.pen:
            cx, cy = self.pos()
            canvas().create_line(cx,cy, cx+x,cy+y,
                               width=self.pen_width,
                               fill=self.pen_colour_hex,
                               tags="pen")
        canvas().move(self.spriteid, x, y)

    def delete(self):
        """Delete this sprite from the canvas"""
        canvas().delete(self.spriteid)

    def distance_between(self, sprite):
        """Distance between this sprite and another"""
        return distance_between_points(self.centre_x, self.centre_y,
                                       sprite.centre_x, sprite.centre_y)

    def move_towards(self, thing, steps=1):
        """Move towards a sprite or point by steps, 
        an approimation of pixels."""
        x, y = self.pos()
        to_x, to_y = Sprite._xy(thing)
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
        """Move some steps in direction set by turn or turn_to."""
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
        our_box = canvas().bbox(self.spriteid)
        their_box = canvas().bbox(sprite.spriteid)

        return overlapping_rect(our_box, their_box) is not None
    
    def touching_any(self, sprites):
        """Is this sprite touching any other sprite in the list?"""
        for s in sprites:
            if s == self: continue
            if self.touching(s):
                return s
        return False

    def above(self, sprite):
        """Is this sprite above another sprite (further up the screen)?"""
        (x1,y1,   x2,y2) = canvas().bbox(self.spriteid)
        (sx1,sy1, sx2,sy2) = canvas().bbox(sprite.spriteid)
        
        # Are we overlapped on x axis and above?
        return (x1 < sx2 and x2 > sx1) and (y1 < sy1)

    def below(self, sprite):
        """Is this sprite below another sprite (further down the screen)"""
        (x1,y1,   x2,y2) = canvas().bbox(self.spriteid)
        (sx1,sy1, sx2,sy2) = canvas().bbox(sprite.spriteid)
        
        # Are we overlapped on x axis and below?
        return (x1 < sx2 and x2 > sx1) and (y2 > sy2)

    def left_of(self, sprite):
        """Is this sprite left of another sprite"""
        (x1,y1,   x2,y2) = canvas().bbox(self.spriteid)
        (sx1,sy1, sx2,sy2) = canvas().bbox(sprite.spriteid)
        
        # Are we overlapped on y axis and left?
        return (y1 < sy2 and y2 > sy1) and (x1 < sx1)
    
    def right_of(self, sprite):
        (x1,y1,   x2,y2) = canvas().bbox(self.spriteid)
        (sx1,sy1, sx2,sy2) = canvas().bbox(sprite.spriteid)
        
        # Are we overlapped on y axis and right?
        return (y1 < sy2 and y2 > sy1) and (x2 > sx2)
    

    def move_with_speed(self):
        self._limit_speed()
        self.move(self.speed_x, self.speed_y)

        
    def accelerate_towards(self, thing, force=1):
        "Accelerate towards a sprite or point"""
        to_x, to_y = Sprite._xy(thing)
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
        """E.g. go off the right and reappear on the left"""
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

    # - - - -

    @staticmethod
    def _xy(thing):
        """Get x, y from a tuple or a sprite."""
        return thing if isinstance(thing, tuple) else (thing.x, thing.y) 


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
                
            spriteid = canvas().create_image(x,y, image=self.photo_images[-1], tag=tag)
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
        spriteid = canvas().create_polygon(points, attribs)
        super(PolygonSprite, self).__init__(spriteid)
        self.created_at_x, self.created_at_y = self.pos()

    def rotate(self, angle):
        """Rotate this polygon by an angle and redraw it"""
        # Capture where this sprite got to
        current_x, current_y = self.pos() 
        dx = current_x - self.created_at_x; dy = current_y - self.created_at_y
        
        self.points = [rotate_point(x, y, angle) for x,y in self.points]
        self.replace_canvas_object(canvas().create_polygon(self.points, self.attribs))
        self.created_at_x, self.created_at_y = self.pos()
        self.move(dx+1, dy+1) # Why is +1 needed?
        
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()


