# turtle_triangles.py : Draws recursive subdivision of triangles
# https://github.com/ericclack/geekclub

from turtle import *
from random import *

def mid(a,b):
    return ((a[0]+b[0])/2,(a[1]+b[1])/2)

def triangles(a,b,c):
    if abs(b[0]-c[0])+abs(b[1]-c[1])<10: return
    pencolor(random(),random(),random())
    penup()
    goto(c[0],c[1])
    pendown()
    goto(a[0],a[1])
    goto(b[0],b[1])
    goto(c[0],c[1])
    m0=mid(a,b)
    m1=mid(b,c)
    m2=mid(c,a)
    triangles(a,m0,m2)
    triangles(b,m0,m1)
    triangles(c,m1,m2)

speed('fastest')
points=[(0,400),(400,-300),(-400,-300)]
triangles(points[0],points[1],points[2])
