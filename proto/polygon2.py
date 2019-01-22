# Copyright 2019, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

from geekclub_packages import *
  
create_canvas()

# Make a composite shape...

p1 = PolygonSprite( [(-100,-100), (100,-100), (100,100), (-100,100), (0,0), (-100,-100)],
                    fill='red', outline='black' )
p1.centre()
p2 = PolygonSprite( [(-90,-90), (-90,-80), (-80,-80), (-80,-90)],
                    fill='yellow', outline='black' )
p2.centre()
p2.move(50,20)

def move(event):
    p1.move_forward(5)
    p2.move_forward(5)
    
def rotate_left(event):
    p1.rotate(-5)
    p1.turn(-5)
    p2.rotate(-5)
    p2.turn(-5)
    
def rotate_right(event):
    p1.rotate(5)
    p1.turn(5)
    p2.rotate(5)
    p2.turn(5)

when_key_pressed('<Left>', rotate_left)
when_key_pressed('<Right>', rotate_right)
when_key_pressed('<space>', move)

mainloop()
