# turtle_stars.py : Draws random stats on the screen
# https://github.com/ericclack/geekclub

from turtle import *
from random import *

speed('fastest')

while True:
    sides=1+2*randint(1,8)
    mult=randint(2,5)
    if sides%mult==0: continue
    angle=mult*360/sides
    length=100
    penup()
    goto(randint(-500,500),randint(-400,400))
    pendown()
    for i in range(sides):
        pencolor(random(),random(),random())
        forward(length)
        left(angle)
