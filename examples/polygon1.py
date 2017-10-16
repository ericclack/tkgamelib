import sys; sys.path.append('..')
from geekclub.pyscratch import *
  
create_canvas()

p = PolygonSprite( [(0,0), (50,0), (50,50), (0,50), (25,25), (0,0)], fill='red', outline='black' )
p.centre()

def rotate():
    p.rotate(5)

forever(rotate, 50)
mainloop()
