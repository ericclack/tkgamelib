TKGameLib: Step up from Scratch to Python
==========================================

Inspired by MIT Scratch and PygameZero, answers the question "what should I try after Scratch?"

PygameZero is really cool, but it requires extra libraries to be installed so isn't an option in some organisations such as schools. TKGameLib works on the default Python, it uses TKinter for graphics, sprites etc, and is designed to encourage exploration of everything. 

Project aims:

* Makes it easy to get visual or audio effects
* Gives immediate results (like Scratch does), type some commands, press run, see results
* Runs easily on the Raspberry Pi
* Runs easily on Windows PCs in schools, to support my STEM Ambassador work
* Has depth with plenty to explore.

Screen shots
------------

![boulder screen shot](/images/boulder.png)

![pong screen shot](/images/pong.png)

![fractal trees screen shot](/images/fractal-trees.png)


Prerequesites
-------------

* Python 3
* A working tkinter library

Get the code
------------

You can use `git` or download a [zip file of the code](https://github.com/ericclack/tkgamelib/archive/master.zip):

    git clone https://github.com/ericclack/tkgamelib.git


Examples
--------

Start up IDLE3 and create a new file, save it to the directory `my_work`, then add the following code...

```
from packages import *
  
create_canvas()
sprite = ImageSprite('my_images/face.gif')
sprite.pen_down()

def move_sprite(event):
    sprite.move(10,10)

when_key_pressed('<space>', move_sprite)
mainloop()
```

Documentation
-------------

Check out the [examples](https://github.com/ericclack/tkgamelib/blob/master/examples/) directory. You should be able to run the code straight
from that directory.

Have a look at the [wiki](https://github.com/ericclack/tkgamelib/wiki) to get started. Or you can [view the source code](https://github.com/ericclack/tkgamelib/blob/master/tkgamelib/) of the library.

