# turtle_mystify.py : Simulation of the win95 mystify screensaver
# https://github.com/ericclack/tkgamelib

from turtle import *
from random import *

def draw_poly(poly):
    penup()
    goto(poly[-1][0],poly[-1][1])
    pendown()
    for p in poly:
        goto(p[0],p[1])

speed('fastest')
tracer(4,0)

poly=[]
for i in range(4):
    poly.append([randint(-450,450),randint(-400,400),randint(-20,20),randint(-20,20)])

history=[poly]

while True:
    if len(history)>10:
        pencolor('white')
        draw_poly(history.pop(0))
    pencolor(random(),random(),random())
    poly=history[-1]
    draw_poly(poly)
    newpoly=[]
    for p in poly:
        t=[p[0]+p[2],p[1]+p[3],p[2],p[3]]
        if abs(t[0])>450:
            t[2]*=-1
        if abs(t[1])>400:
            t[3]*=-1
        newpoly.append(t)
    history.append(newpoly)
