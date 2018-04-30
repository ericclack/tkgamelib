import sys
sys.path.append('..')
from geekclub.pyscratch import *

create_canvas()

# Two image costumes for the face sprite
img1 = PhotoImage(file="images/face.gif")
img2 = PhotoImage(file="images/face2.gif")
img3 = PhotoImage(file="images/face3.gif")

sprite = ImageSprite([img1, img2, img3])

sprite.centre()

def toggle():
    sprite.next_costume()

#forever(toggle, 500)
when_key_pressed('<space>', toggle)

mainloop()
