from geekclub_packages import *

create_canvas()

circles = []

for n in range(100):
    circle_shape = canvas().create_oval(0,0, 25,25, fill=random_colour())
    circle = Sprite(circle_shape)
    circle.move_to_random_pos()
    circles.append(circle)


def check_move_circle():
    hit = mouse_touching_any(circles)
    if hit:
        if not hit.speed_x:
            hit.speed_x = random.randint(-2,2)
            hit.speed_y = random.randint(-2,2)
            hit.max_speed = 5
        else:
            hit.accelerate(2.1)

def move_circles():
    for c in circles:
        c.move_with_speed()
    
forever(check_move_circle)
forever(move_circles)

mainloop()
