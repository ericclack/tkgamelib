from geekclub_packages import *

MAX_ROCKET_PARTS = 7

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

def restart_level(w):
    for a in w.aliens:
        a.delete()
    w.aliens.clear()
    w.sprite.centre()

def parts_in_place(parts):
    return all([r.in_place for r in parts])

def parts_left(parts):
    return MAX_ROCKET_PARTS - len(parts)

def parts_complete(parts):
    return parts_left(parts) == 0 and parts_in_place(parts)

def ready_for_next_rocket_part(w):
    return parts_left(w.rocket_parts) and parts_in_place(w.rocket_parts)
