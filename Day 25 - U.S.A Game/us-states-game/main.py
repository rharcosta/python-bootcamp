from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle = Turtle(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []
total = len(states)

while len(guessed_states) < total:
    answer = screen.textinput(title=f"{len(guessed_states)}/{total} Number of States",
                              prompt="Guess a State name:").title()
    if answer == "Exit":
        missing_states = [row for row in states if row not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer in states:
        state = Turtle()
        state.hideturtle()
        state.penup()
        state_data = data[data.state == answer]
        state.goto(int(state_data.x), int(state_data.y))
        state.write(state_data.state.item(), font=("Arial", 8, "bold"))
        guessed_states.append(answer)

screen.exitonclick()
