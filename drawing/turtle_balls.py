# turtle_balls.py : Draws trajectory of balls with gravity and bouncing
# https://github.com/ericclack/geekclub

from turtle import *
from random import *

speed('fastest')

gravity=-1
while True:
    penup()
    x,y=0,0
    vx=randint(-10,10)
    vy=randint(5,30)
    goto(x,y)
    pencolor(random(),random(),random())
    pendown()
    while True:
        x+=vx
        y+=vy
        vy+=gravity
        if y<-380:
            y=-380
            vy=abs(vy*0.5)
            if vy<5: break
        if x>450:
            vx=-abs(vx)
        if x<-450:
            vx=abs(vx)
        goto(x,y)
