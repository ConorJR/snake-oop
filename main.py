from turtle import *

t1= Turtle()
t2= Turtle()
t3= Turtle()
t4= Turtle()
t5= Turtle()
t6= Turtle()
t7= Turtle()
t8= Turtle()
t9= Turtle()
t10= Turtle()

t1.hideturtle()
t2.hideturtle()
t3.hideturtle()
t4.hideturtle()
t5.hideturtle()
t6.hideturtle()
t7.hideturtle()
t8.hideturtle()
t9.hideturtle()
t10.hideturtle()

t1.speed(0)
t2.speed(0)
t3.speed(0)
t4.speed(0)
t5.speed(0)
t6.speed(0)
t7.speed(0)
t8.speed(0)
t9.speed(0)
t10.speed(0)

t1.color('red')
t2.color('green')
t3.color('blue')
t4.color('red')
t5.color('green')
t6.color('blue')
t7.color('red')
t8.color('green')
t9.color('blue')
t10.color('red')
t1.left(0)
t2.left(36)
t3.left(72)
t4.left(108)
t5.left(144)
t6.left(180)
t7.left(216)
t8.left(252)
t9.left(288)
t10.left(324)

def printcircle():
    t1.begin_fill()
    t2.begin_fill()
    t3.begin_fill()
    t4.begin_fill()
    t5.begin_fill()
    t6.begin_fill()
    t7.begin_fill()
    t8.begin_fill()
    t9.begin_fill()
    t10.begin_fill()
    for i in range(22):
        t1.forward(10)
        t1.left(10)

        t2.forward(10)
        t2.left(10)

        t3.forward(10)
        t3.left(10)

        t4.forward(10)
        t4.left(10)

        t5.forward(10)
        t5.left(10)

        t6.forward(10)
        t6.left(10)

        t7.forward(10)
        t7.left(10)

        t8.forward(10)
        t8.left(10)

        t9.forward(10)
        t9.left(10)

        t10.forward(10)
        t10.left(10)

    t1.end_fill()
    t2.end_fill()
    t3.end_fill()
    t4.end_fill()
    t5.end_fill()
    t6.end_fill()
    t7.end_fill()
    t8.end_fill()
    t9.end_fill()
    t10.end_fill()

printcircle()

exitonclick()
