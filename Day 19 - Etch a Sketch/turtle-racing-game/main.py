from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter a color"
                                   " (Blue, Red, Green, Pink, Orange, Purple): ")

colors = ["blue", "red", "green", "pink", "orange", "purple"]
all_turtles = []


def turtle_position(y_position):
    for turtle_index in range(6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(colors[turtle_index])
        new_turtle.goto(x=-230, y=y_position)
        y_position += 30
        all_turtles.append(new_turtle)


turtle_position(-70)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning = turtle.pencolor()
            if winning == user_bet:
                print(f"You've won! The {winning} turtle is the winner.")
            else:
                print(f"You've lost! The {winning} turtle is the winner.")
        distance = randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
