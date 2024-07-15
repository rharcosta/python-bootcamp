from turtle import Turtle
POSITION = (0, -280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("coral")
        self.penup()
        self.left(90)
        self.goto(POSITION)

    def up(self):
        self.forward(20)

    def reset_position(self):
        self.goto(POSITION)
