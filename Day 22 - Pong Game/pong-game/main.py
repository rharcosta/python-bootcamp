from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

screen.listen()
screen.onkeypress(fun=right_paddle.up, key="o")
screen.onkeypress(fun=right_paddle.down, key="l")
screen.onkeypress(fun=left_paddle.up, key="q")
screen.onkeypress(fun=left_paddle.down, key="a")

ball = Ball()
score = Score()
game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # collision with the wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    # collision with the paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.left_point()

    # detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.right_point()

screen.exitonclick()
