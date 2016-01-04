geekclub
========

Code and examples for Plumpton Geek Club.

An attempt to make Scratch style programming in Python possible -- in
response to the question: "What shall I try after Scratch". Inspired by MIT Scratch: http://scratch.mit.edu/

I'm aiming for a suite of libraries that:

* Makes it easy to get visual or audio effects
* Gives immediate results (like Scratch does), type some commands, press run, see results
* Runs easily on the Pi (of course)
* Has depth with plenty to explore.

Prerequesites
-------------

* Python 3
* A working tkinter library

Examples
--------

Start up `idle3` from the geekclub directory and run...

    >>> from pyscratch import *
    >>> create_canvas()
    >>> spriteimg = PhotoImage(file='images/face.gif')
    >>> sprite = ImageSprite(spriteimg)
    >>> sprite.move(100,0)
    >>> sprite.move(0,100)
    >>> sprite.move(-100,0)
    >>> sprite.move(0,-1000)

Check out the examples directory. The symbolic link (up one directory) makes it 
possible to run the code from there, but ordinarily you'd write code and put
the geekclub checkout in the same directory as your code.



