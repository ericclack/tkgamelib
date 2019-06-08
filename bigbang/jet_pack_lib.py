from geekclub_packages import *

MAX_ROCKET_PARTS = 7
LANDING_ZONE = 550

def make_platforms(rectangles):
    return [Sprite(canvas().create_rectangle(x1,y1, x2,y2, fill=c))
                for x1, y1, x2, y2, c in rectangles]  

def in_landing_zone(x):
    return (LANDING_ZONE-5) < x < (LANDING_ZONE+5)

# ------------------------------------------------------------------

def new_rocket_part(w):
    r = ImageSprite('images/rocket%s.gif' % (len(w.rocket_parts) + 1))
    r.move_to(random.randint(0, CANVAS_WIDTH-100), 0)
    r.speed_x = 0
    r.speed_y = 1
    r.in_place = False
    r.landing = False
    return r

def new_alien(w):
    a = Sprite(canvas().create_oval(0,0, 50,50, fill="red"))
    a.max_speed = 3
    
    if random.random() < 0.5:
        a.move_to(random.randint(0, CANVAS_WIDTH * .9), 0)
    else:
        a.move_to(CANVAS_WIDTH, random.randint(0, CANVAS_HEIGHT *.6))
        
    a.speed_x = -random.randint(3,8)
    a.speed_y = 2
    return a

def new_fuel(w):
    f = Sprite(canvas().create_rectangle(0,0, 100,40, fill="purple"))
    f.move_to(random.randint(0, CANVAS_WIDTH), 0)
    f.speed_x = 0
    f.speed_y = 1
    f.in_place = False
    f.landing = False
    return f

def new_flame(w):
    r = w.rocket_parts[0] # The base of the rocket
    size = 30 - len(w.flames) * 2
    x = LANDING_ZONE + r.width / 2 - size / 2
    y = r.y + r.height + len(w.flames) * size * .9
    return Sprite(canvas().create_oval(x,y, x+size,y+size,
                                       fill="red"))    


def restart_level(w):
    for a in w.aliens:
        a.delete()
    w.aliens.clear()
    w.sprite.centre()

# ------------------------------------------------------------------

def parts_in_place(parts):
    return all([r.in_place for r in parts])

def parts_left(parts):
    return MAX_ROCKET_PARTS - len(parts)

def parts_complete(parts):
    return parts_left(parts) == 0 and parts_in_place(parts)

def ready_for_next_rocket_part(w):
    return parts_left(w.rocket_parts) and parts_in_place(w.rocket_parts)

def ready_for_next_fuel(w):
    return parts_complete(w.rocket_parts) and parts_left(w.fuel) \
           and parts_in_place(w.fuel)

def ready_for_takeoff(w):
    return parts_complete(w.fuel) and parts_complete(w.rocket_parts)
