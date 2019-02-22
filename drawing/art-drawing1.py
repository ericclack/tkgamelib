from geekclub_packages import *

create_canvas()

pen = Sprite(canvas().create_oval(0,0,3,3))
pen2 = Sprite(canvas().create_oval(0,0,3,3))
pen3 = Sprite(canvas().create_oval(0,0,3,3))
pen2.pen_colour(0, 0, 30)
pen3.pen_colour(0, 0, 30)

def r(f=1): return random.randint(0,3) * f

def draw(event):
    pen.move_to(event.x, event.y)
    pen.pen_down()
    
    pen2.move_to(event.x+r(), event.y+r())
    pen2.pen_down()

    pen3.move_to(event.x+r(-1), event.y+r(-1))
    pen3.pen_down()

def stop_drawing(event):
    pen.pen_up()
    pen2.pen_up()
    pen3.pen_up()

def clear(event):
    clear_pen()

when_button1_dragged(draw)
when_button1_released(stop_drawing)
when_key_pressed('c', clear)

banner('Draw with the mouse', 2000)
future_action(lambda: banner('Press c to clear', 2000), 2000)

mainloop()
