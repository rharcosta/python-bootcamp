import turtle
from color import color_list
import random

circle = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)

circle.penup()  # to don't show the line
circle.hideturtle()  # to hide the turtle

circle.speed("fastest")
screen.title("Rubia Painting =D")

circle.setheading(225)  # height
circle.forward(300)
circle.setheading(0)  # the started line
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    circle.dot(20, random.choice(color_list))
    circle.forward(50)

    if dot_count % 10 == 0:
        circle.setheading(90)
        circle.forward(50)
        circle.setheading(180)
        circle.forward(500)
        circle.setheading(0)

screen.exitonclick()
