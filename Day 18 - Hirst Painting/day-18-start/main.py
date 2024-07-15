from turtle import Turtle, Screen
import random
# from turtle import * -> import everything
# import turtle as t -> rename to "t"


class World:
    tim = Turtle()
    screen = Screen()

    tim.shape("turtle")
    tim.color("purple")

    # draw a square
    # for steps in range(4):
    #     tim.forward(100)
    #     tim.left(90)

    # draw a dashed line
    # for steps in range(15):
    #     tim.forward(10)
    #     tim.penup()
    #     tim.forward(10)
    #     tim.pendown()

    # making a geometric pattern
    # for steps in range(100):
    #     for c in ('blue', 'red', 'green'):
    #         tim.color(c)
    #         tim.forward(steps)
    #         tim.right(30)

    # draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon

    colors = ["blue", "pink", "green", "red", "brown", "purple", "orange", "black"]


    def draw_shape(sides):
        angle = 360 / sides
        for steps in range(sides):
            tim.forward(100)
            tim.right(angle)


    for shape in range(3, 11):
        tim.color(random.choice(colors))
        draw_shape(shape)
