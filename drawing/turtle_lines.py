# turtle_lines.py : Draws a spiral of lines
# https://github.com/ericclack/geekclub

from turtle import *
from random import *

def draw_line(x1,y1,x2,y2):
    pencolor(random(),random(),random())
    penup()
    goto(x1,y1)
    pendown()
    goto(x2,y2)

w,h = 500,400
step = 10
speed('fastest')

for x in range(-w,w,step):
    draw_line(x,h,-x,-h)
for y in range(-h,h,step):
    draw_line(w,y,-w,-y)
