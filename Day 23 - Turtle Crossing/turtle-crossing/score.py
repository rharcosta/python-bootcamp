from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.point = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.point += 1
        self.goto(-200, 250)
        self.write(f"Level: {self.point}", align="center", font=("Courier", 24, "bold"))

    def finish_game(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center",  font=("Courier", 24, "bold"))
