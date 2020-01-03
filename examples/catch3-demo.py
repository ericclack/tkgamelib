# Copyright 2018, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

from packages import *
  
create_canvas()

world = Struct(balls = [], init_speed=-10,
               gravity=0.1, max_balls=10, size=200)

def new_ball():
    oval = canvas().create_oval(0,0, world.size,world.size,
                                fill=random_colour())
    ball = Sprite(oval)
    ball.move_to(random.randint(0, CANVAS_WIDTH-30), CANVAS_HEIGHT-100)
    ball.speed_y = random.randint(world.init_speed,world.init_speed/2)
    return ball

def delete_ball(b):
    world.balls.remove(b)
    b.delete()

def shoot_balls():
    show_variable("Level", world.max_balls)
    
    if len(world.balls) < world.max_balls:
        world.balls.append(new_ball())

    for b in world.balls:
        b.speed_y += world.gravity
        b.move_with_speed()
        if b.y > CANVAS_HEIGHT:
            #end_game("You missed one!")
            banner("You missed one!",300)
            delete_ball(b)

    ball = mouse_touching_any(world.balls)
    if ball:
        delete_ball(ball)

def make_harder():
    banner("Getting harder!", 500)
    world.max_balls += 1
    world.size *= 0.8

banner("Catch the balls with the mouse", 2000)
forever(shoot_balls, 30)
forever(make_harder, 60*1000)
mainloop()
