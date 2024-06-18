from turtle import Turtle, Screen
import random
import turtle

tim = Turtle()
screen = Screen()
turtle.colormode(255)

directions = [0, 90, 180, 270]
tim.pensize(20)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


for shape in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen.exitonclick()
