geekclub
========

Code and examples for Plumpton Geek Club.

An attempt to make Scratch style programming in Python possible -- in
response to the question: "What shall I try after Scratch". Inspired by MIT Scratch: http://scratch.mit.edu/

I'm aiming for a suite of libraries that:

* Makes it easy to get visual or audio effects
* Gives immediate results (like Scratch does), type some commands, press run, see results
* Runs easily on the Raspberry Pi
* Runs easily on Windows PCs in schools, to support my STEM Ambassador work
* Has depth with plenty to explore.

Prerequesites
-------------

* Python 3
* A working tkinter library

Examples
--------

Start up `idle3` and run...

    >>> from geekclub.pyscratch import *
    >>> create_canvas()
    >>> spriteimg = PhotoImage(file='examples/images/face.gif')
    >>> sprite = ImageSprite(spriteimg)
    >>> sprite.move(100,0)
    >>> sprite.move(0,100)
    >>> sprite.move(-100,0)
    >>> sprite.move(0,-1000)

Check out the examples directory. You should be able to run the code straight
from that directory. 

![boulder screen shot](/images/boulder.png)



