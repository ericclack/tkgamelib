# Copyright 2019, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

from packages import *
  
create_canvas()

world = Struct(balls = [], init_speed=-15, gravity=0.2, max_balls=2,
               size=50)

def new_ball():
    oval = canvas().create_oval(0,0, world.size, world.size,
                                fill=hsv_to_hex(random.random(),1,1))
    ball = Sprite(oval)
    ball.move_to(random.randint(0, CANVAS_WIDTH-world.size),
                 CANVAS_HEIGHT-10)
    ball.speed_y = random.randint(world.init_speed,
                                  int(world.init_speed/2))
    return ball

def shoot_balls():
    if len(world.balls) < world.max_balls:
        world.balls.append(new_ball())

    for b in world.balls:
        b.speed_y += world.gravity
        b.move_with_speed()
        if b.y > CANVAS_HEIGHT:
            end_game("You missed one!")

    ball = mouse_touching_any(world.balls)
    if ball:
        world.balls.remove(ball)
        ball.delete()

banner("Catch the balls with the mouse")
future_action(clear_banner, 2000)
forever(shoot_balls, 30)
mainloop()
