import turtle

BRANCHES = 4

def tree(x, y, length, angle):

    if length < 5:
        return
    
    p = turtle.Pen()
    p.hideturtle()
    p.up()
    p.goto(x, y)
    p.setheading(angle)
    p.down()
    
    for i in range(5):
        p.forward(length / 5)
        p.right(5)

    a = angle - (30 * BRANCHES / 2)
    for i in range(BRANCHES):
        tree(p.xcor(), p.ycor(), length * 0.5, a)
        a += 30


turtle.tracer(8, 0) # Speed up the drawing
tree(x=0, y=-200, length=150, angle=90)
