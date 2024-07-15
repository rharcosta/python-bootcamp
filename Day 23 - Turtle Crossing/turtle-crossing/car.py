from turtle import Turtle
import random

COLORS = ["red", "green", "black", "blue", "pink", "orange", "brown", "purple"]


class Car:
    def __init__(self):
        self.all_cars = []
        self.speed_move = 5

    def create(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle()
            new_car.shape("square")
            # one time the original width (20px) and two times (40px)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-200, 200)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.speed_move)
