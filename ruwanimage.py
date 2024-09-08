import turtle as t
from turtle import *
def rectangle(horizontal, vertical, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for counter in range(1, 3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()
t.penup()
t.speed('fast')
t.bgcolor('maroon')
#for feet
t.goto(-100, -150)
rectangle(50, 20, 'orange')
t.goto(-30, -150)
rectangle(50, 20, 'orange')
#for shoe-lining
t.goto(-100, -170)
rectangle(50, 3, 'grey')
t.goto(-30, -170)
rectangle(50, 3, 'grey')
#for legs
t.goto(-25, -50)
rectangle(20, 100, 'black')
t.goto(-55, -50)
rectangle(-20, 100, 'black')
#for body
t.goto(-90, 100)
rectangle(105, 155, 'dark blue')
#for jacket-pockets
t.goto(-15, -5)
rectangle(1, 19, 'black')
t.goto(-65, -5)
rectangle(1, 19, 'black')
t.goto(-14, -6)
rectangle(1, 17, 'black')
t.goto(-66, -6)
rectangle(1, 17, 'black')
#for left arm
t.goto(-91, 100)
rectangle(-19, 18, 'navy')
t.goto(-110, 81)
rectangle(18, 80, 'navy')
t.goto(-110, 2)
rectangle(18, 18, 'peach puff')
#for right arm
t.goto(16, 100)
rectangle(19, 18, 'navy')
t.goto(35, 81)
rectangle(-18, 80, 'navy')
t.goto(17, 2)
rectangle(18, 18, 'peach puff')
t.goto(-200, -199)
#for neck
t.goto(-47, 116)
rectangle(19, 15, 'peach puff')
#for head
t.goto(-64, 169)
rectangle(52, 54, 'peach puff')
#for hair
t.goto(-64, 169)
rectangle(52, 6, 'black')
#for eye 1
t.goto(-49, 145)
rectangle(-2, 2, 'dark gray')
t.goto(-48, 145)
rectangle(2, 2, 'dark gray')
t.goto(-49, 144)
rectangle(-2, 2, 'white')
t.goto(-48, 144)
rectangle(2, 2, 'dark gray')
#for eye 2
t.goto(-28, 145)
rectangle(-2, 2, 'dark gray')
t.goto(-27, 145)
rectangle(2, 2, 'dark gray')
t.goto(-28, 144)
rectangle(-2, 2, 'white')
t.goto(-27, 144)
rectangle(2, 2, 'dark gray')
#for mouth
t.goto(-49, 130)
rectangle(1, 2, 'black')
t.goto(-47, 127)
rectangle(1, 1, 'black')
t.goto(-45, 125)
rectangle(14, 1, 'black')
t.goto(-30, 127)
rectangle(1, 1, 'black')
t.goto(-28, 130)
rectangle(1, 2, 'black')
#to make turtle invisible
t.hideturtle()
#to keep the image there
exitonclick()
#the end
