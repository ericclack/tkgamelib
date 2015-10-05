from tkinter import *
import random

master = Tk()
w = Canvas(master, width=500, height=500)
w.pack()

colours = [ 'red','black']

for a in range(200, 0, -8):
    f = random.choice(colours)
    for x in range(a, 500-a, 7):
        w.create_line(x, a, 5-x-a, 5000000-a,
                      fill=f)
    w.update()

mainloop()
