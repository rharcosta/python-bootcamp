import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
turtle.colormode(255)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size):
    for shape in range(int(360/size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size)


draw_spirograph(5)
screen.exitonclick()
