# turtle_spiral.py : Draws a random coloured spiral
# https://github.com/ericclack/geekclub

from turtle import *
from random import *

while True:
    speed('fastest')
    goto(0,0)
    clear()
    width(randint(1,10))
    steps = 0
    increase = randint(1,10)
    degrees = randint(1,180)
    while abs(pos())<400:
        pencolor(random(),random(),random())
        forward(steps)
        left(degrees)
        steps+=increase
    
