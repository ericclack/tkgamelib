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

def costume_1(): sprite.switch_costume(1)
def costume_2(): sprite.switch_costume(2)
def costume_3(): sprite.switch_costume(3)

#forever(toggle, 500)
when_key_pressed('<space>', toggle)
when_key_pressed('1', costume_1)
when_key_pressed('2', costume_2)
when_key_pressed('3', costume_3)

banner("Press space to see next costume", 2000)
future_action( lambda: banner("...or keys 1,2,3", 2000),
               2000 )

mainloop()
