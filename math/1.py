import turtle
from turtle import *

shape('turtle')
speed(100)


def square(side_length=100):
    for i in range(4):
        forward(side_length)
        right(90)


def triangle(side_length=100):
    for i in range(3):
        forward(100)
        right(120)


def polygon(num_side=4, side_length=100):
    for i in range(num_side):
        forward(side_length)
        right(360/num_side)


def star(side_length):
    for i in range(5):
        forward(side_length)
        angle = 720/5
        right(angle)


def star_spiral():
    length = 5
    for i in range(60):
        star(length)
        length += 5
        right(5)


star_spiral()

turtle.Screen().exitonclick()
