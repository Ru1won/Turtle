from turtle import *
from random import randint

title('Turtle Racing')

speed(5)
penup()

for step in range(6):
    goto(-200, 240-(40*(step)))
    down()
    forward(400)
    penup()

hideturtle()

dimsum = Turtle()
dimsum.color('blue')
dimsum.shape('turtle')

dimsum.penup()
dimsum.goto(-200, 220)
dimsum.pendown()

jerry = Turtle()
jerry.color('dark orchid')
jerry.shape('turtle')

jerry.penup()
jerry.goto(-200, 180)
jerry.pendown()

timothy = Turtle()
timothy.color('green')
timothy.shape('turtle')

timothy.penup()
timothy.goto(-200, 140)
timothy.pendown()

diesel = Turtle()
diesel.color('black')
diesel.shape('turtle')

diesel.penup()
diesel.goto(-200, 100)
diesel.pendown()

idk = Turtle()
idk.color('brown')
idk.shape('turtle')

idk.penup()
idk.goto(-200, 60)
idk.pendown()

for turn in range(120):
    dimsum.forward(randint(1, 5))
    jerry.forward(randint(1, 5))
    timothy.forward(randint(1, 5))
    diesel.forward(randint(1, 5))
    idk.forward(randint(1, 5))

distance = (dimsum.xcor(), jerry.xcor(), diesel.xcor(), idk.xcor(), timothy.xcor())

windistance = max(distance)

if windistance == dimsum.xcor():
    winner = 'dimsum wins!(the blue turtle)'
elif windistance == jerry.xcor():
    winner = 'jerry wins!(the purple turtle)'
elif windistance == idk.xcor():
    winner = 'idk wins!(the brown turtle)'
elif windistance == timothy.xcor():
    winner = 'timothy wins!(the green turtle)'
elif windistance == diesel.xcor():
    winner = 'diesel wins!(the black turtle)'

goto(0, 240)
write(winner, align = 'center', font = ('Times New Roman', 14, 'normal'))
exitonclick()
