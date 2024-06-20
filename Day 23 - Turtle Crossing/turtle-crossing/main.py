from turtle import Screen
from player import Player
from car import Car
from score import Score
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.bgcolor("black")

player = Player()
score = Score()
car = Car()

screen.listen()
screen.onkeypress(fun=player.up, key="Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car.create()
    car.move()

    # collision with a car
    for car_manager in car.all_cars:
        if car_manager.distance(player) < 20:
            game_on = False
            score.finish_game()

    # collision with the wall
    if player.ycor() > 270:
        score.update_score()
        player.reset_position()
        car.speed_move += 10

screen.exitonclick()
