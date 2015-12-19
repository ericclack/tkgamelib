from tkinter import *
import random

master = Tk()
w = Canvas(master, width=500, height=500)
w.pack()

colours = [ 'red', 'green', 'blue']

for x in range(0, 500, 20):
    f = random.choice(colours)
    for y in range(0, 500, 20):
        w.create_oval(x,y, x-25,y-25,
                      fill=f)
    w.update()

mainloop()
