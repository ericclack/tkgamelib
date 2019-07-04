# turtle_web.py : Draws a pseudo spiders web
# https://github.com/ericclack/geekclub

from turtle import *
from random import *
from math import *

speed('fastest')

steps=10
sides=15

def web(anga,angb):
    ax,ay=350*sin(anga),350*cos(anga)
    bx,by=350*sin(angb),350*cos(angb)
    for i in range(0,steps+1):
        penup()
        goto(ax*i/steps,ay*i/steps)
        pendown()
        pencolor(random(),random(),random())
        goto(bx*(steps-i)/steps,by*(steps-i)/steps)

for i in range(sides):
    web(radians(360*i/sides),radians(360*(i+1)/sides))
