from turtle import *
from random import randint, choice

window = Screen()
window.bgcolor("black")
window.title("Ping Pong")
window.setup(width=1.0, height=1.0)
window.tracer(2)


border = Turtle()
border.speed(0)
border.color("green")
border.goto(-500, -300)
border.begin_fill()
for i in range(2):
    border.forward(1000)
    border.left(90)
    border.forward(600)
    border.left(90)
border.end_fill()

border.goto(0, 300)
border.right(90)
border.color("white")
border.width(4)
for i in range(25):
    if i % 2 == 0:
        border.forward(24)
    else:
        border.up()
        border.forward(24)
        border.down()
border.hideturtle()

rocket_A = Turtle()
rocket_A.color("white")
rocket_A.up()
rocket_A.shape("square")
rocket_A.shapesize(5, 1)
rocket_A.goto(-450, 0)

rocket_B = Turtle()
rocket_B.color("white")
rocket_B.up()
rocket_B.shape("square")
rocket_B.shapesize(5, 1)
rocket_B.goto(450, 0)

def up_a():
    new_y = rocket_A.ycor() + 10
    if new_y > 250:
        new_y = 250
    rocket_A.sety(new_y)

def down_a():
    new_y = rocket_A.ycor() - 10
    if new_y < -250:
        new_y = -250
    rocket_A.sety(new_y)

def up_b():
    new_y = rocket_B.ycor() + 10
    if new_y > 250:
        new_y = 250
    rocket_B.sety(new_y)

def down_b():
    new_y = rocket_B.ycor() - 10
    if new_y < -250:
        new_y = -250
    rocket_B.sety(new_y)


window.listen()
window.onkeypress(up_a, "w")
window.onkeypress(down_a, "s")
window.onkeypress(up_b, "Up")
window.onkeypress(down_b, "Down")

ball = Turtle()
ball.color("red")
ball.shape("circle")
ball.up()
ball.speed(0)
ball.bx = 1
ball.by = 1

FONT = ("Arial", 44)
score_A = 0
sA = Turtle()
sA.hideturtle()
sA.color("white")
sA.penup()
sA.goto(-200, 300)
sA.write(score_A, font=FONT)

score_B = 0
sB = Turtle()
sB.hideturtle()
sB.color("white")
sB.penup()
sB.goto(200, 300)
sB.write(score_B, font=FONT)

while True:
    window.update()

    ball.setx(ball.xcor() + ball.bx)
    ball.sety(ball.ycor() + ball.by)

    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.by = -ball.by

    if ball.xcor() >= 490: 
        score_B += 1
        sB.clear()
        sB.write(score_B, font=FONT)
        ball.goto(0, randint(-250, 250))
        ball.dx = choice([1, 2, -1, -2])
        ball.dy = choice([1, 2, -1, -2])
    
    if ball.xcor() <= -490:
        score_A += 1
        sA.clear()
        sA.write(score_A, font=FONT)
        ball.goto(0, randint(-250, 250))
        ball.dx = choice([1, 2, -1, -2])
        ball.dy = choice([1, 2, -1, -2])
    

    if ball.xcor() >= rocket_B.xcor() - 10 and ball.xcor() <= rocket_B.xcor() + 10 and ball.ycor() >= rocket_B.ycor() - 50 and ball.ycor() <= rocket_B.ycor() + 50:
        ball.bx = - ball.bx

    if ball.xcor() >= rocket_A.xcor() - 10 and ball.xcor() <= rocket_A.xcor() + 10  and ball.ycor() >= rocket_A.ycor() - 50 and ball.ycor() <= rocket_A.ycor() + 50:
        ball.bx = - ball.bx

    

window.mainloop()