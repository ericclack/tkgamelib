# turtle_worms.py : Draws a worm moving from the centre of the screen
# https://github.com/ericclack/geekclub

from turtle import *
from random import *

speed('fastest')
width(5)

while True:
    penup()
    goto(0,0)
    pendown()
    setheading(randint(0,360))
    while abs(pos())<400:
        pencolor(random(),random(),random())
        forward(randint(10,50))
        left(randint(-50,50))
