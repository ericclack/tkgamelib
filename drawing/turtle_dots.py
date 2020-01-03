# turtle_dots.py : A seemingly random set of dots which form a pattern
# https://github.com/ericclack/tkgamelib

from turtle import *
from random import *

speed('fastest')
tracer(10,0)

points=[[0,400],[400,-300],[-400,-300]]
p=list(points[0])
penup()

while True:
    c = choice(points)
    p[0]=(p[0]+c[0])/2
    p[1]=(p[1]+c[1])/2
    goto(p[0],p[1])
    dot(5,(random(),random(),random()))
