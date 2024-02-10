from turtle import *


t1 = Turtle()
t2 = Turtle()
t3 = Turtle()

t1.color('red')
t2.color('green')
t3.color('blue')
t2.left(120)
t3.left(240)

for i in range(36):
    t1.forward(10)
    t1.left(10)

    t2.forward(10)
    t2.left(10)

    t3.forward(10)
    t3.left(10)

