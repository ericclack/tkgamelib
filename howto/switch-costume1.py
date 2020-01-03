from packages import *

create_canvas()

# Three image costumes for the face sprite
img1 = PhotoImage(file="../examples/images/face.gif")
img2 = PhotoImage(file="../examples/images/face2.gif")
img3 = PhotoImage(file="../examples/images/face3.gif")

sprite = ImageSprite([img1, img2, img3])

sprite.centre()

def toggle():
    sprite.next_costume()

#forever(toggle, 500)
when_key_pressed('<space>', toggle)

banner("Press space to see next costume", 2000)

mainloop()
