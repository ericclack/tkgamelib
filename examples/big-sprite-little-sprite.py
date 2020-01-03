# Copyright 2014, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

"""A small sprite and a big one, that follows"""

import random
from packages import *

create_canvas()

spriteimg = PhotoImage(file='images/face.gif')
smallsprite = ImageSprite(spriteimg, 100, 100)

bigspriteimg = spriteimg.zoom(2,2)
bigsprite = ImageSprite(bigspriteimg, 100, 100)


def move_towards_mouse():
    smallsprite.move_towards(mousex(), mousey(), 5)
    if smallsprite.touching(bigsprite):
        smallsprite.move_to_random_pos()

def move_bigsprite():
    spritex, spritey = smallsprite.pos()
    bigsprite.move_towards(spritex, spritey)
    

forever(move_towards_mouse, 25)
forever(move_bigsprite, 50)

mainloop()
