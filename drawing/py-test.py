sfrom tkinter import *
import random

master = Tk()
w = Canvas(master, width=500, height=500)
w.pack()

w.create_oval(50,50, 200,200, )
mainloop()
