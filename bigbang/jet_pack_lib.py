from geekclub_packages import *

def make_platforms(rectangles):
    return [Sprite(canvas().create_rectangle(x1,y1, x2,y2, fill=c))
                for x1, y1, x2, y2, c in rectangles]  

def new_rocket_part(w):
    r = ImageSprite('images/rocket%s.gif' % (len(w.rocket_parts) + 1))
    r.move_to(random.randint(0, CANVAS_WIDTH-100), 0)
    r.speed_x = 0
    r.speed_y = 1
    r.in_place = False
    r.landing = False
    return r
