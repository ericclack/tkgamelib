from packages import *

create_canvas()

# Some backgrounds
background = ImageSprite(['../examples/images/bg-blue-white.gif',
                          '../examples/images/bg-black-white.gif'])
background.move_to(0,0)

# Three image costumes for the face sprite
sprite = ImageSprite(["../examples/images/face.gif",
                      "../examples/images/face2.gif",
                      "../examples/images/face3.gif"])
sprite.centre()


def toggle():
    sprite.next_costume()

def toggle_background():
    background.next_costume()

def costume_1(): sprite.switch_costume(1)
def costume_2(): sprite.switch_costume(2)
def costume_3(): sprite.switch_costume(3)

#forever(toggle, 500)
when_key_pressed('<space>', toggle)
when_key_pressed('b', toggle_background)
when_key_pressed('1', costume_1)
when_key_pressed('2', costume_2)
when_key_pressed('3', costume_3)

banner("Press space or B to see next costume", 2000)
future_action( lambda: banner("...or keys 1,2,3", 2000),
               2000 )

mainloop()
