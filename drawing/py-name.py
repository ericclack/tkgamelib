from tkinter import *
import random

master = Tk()
w = Canvas(master, width=500, height=500)
w.pack()

def line(x1,y1, x2, y2):
    loops = 10.0
    dx = (x2-x1) / loops
    dy = (y2-y1) / loops
    x = x1
    y = y1
    for a in range(int(loops)):
        w.create_line(0, 0, x, y)
        x = x + dx
        y = y + dy
    w.create_line(x1, y1, x2, y2, width=2)
    

line(50,50, 100,50)
line(50,50, 50,200)
line(50,200, 100,200)
line(50,100, 100,100)

line(150,50, 200,50)
line(150,50, 150,200)
line(150,200, 200,200)
mainloop()
