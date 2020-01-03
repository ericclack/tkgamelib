# turtle_string.py : Draws strings wound between pins on a circle
# https://github.com/ericclack/tkgamelib

from turtle import *
from random import *
from math import *

speed('fastest')

sides=17
points=[]

for i in range(sides+1):
    a=radians((360*i)/sides)
    p=(350*sin(a),350*cos(a))
    points.append(p)

penup()
goto(points[0][0],points[0][1])
pendown()

for i in range(1,sides//2):
    pencolor(random(),random(),random())
    for j in range(sides+1):
        p=points[(i*j)%sides]
        goto(p[0],p[1])
