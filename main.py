from turtle import *
from random import randint

colors = ["red", "green", "yellow", "blue", "pink", "orange", "aqua", "lightgreen"]

t = Turtle()
t.width(6)
t.speed(0)


for i in range(36):
    t.color(colors[randint(0, len(colors)-1)])
    t.circle(80)
    t.left(10)

done()