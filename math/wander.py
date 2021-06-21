import turtle
from turtle import *
from random import randint


shape('turtle')
speed(0)


def wander():
    square_length = 200
    while True:
        forward(3)
        if xcor() >= square_length or xcor() <= -square_length or ycor() >= square_length or ycor() <= -square_length:
            lt(randint(90, 180))


wander()
turtle.Screen().exitonclick()
