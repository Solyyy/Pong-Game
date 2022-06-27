from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from game_board import GameBoard

import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)
scoreboard = Scoreboard()
game_board = GameBoard()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

# User input
screen.listen()
screen.onkeypress(r_paddle.move_up, 'Up')
screen.onkeypress(r_paddle.move_down, 'Down')
screen.onkeypress(l_paddle.move_up, 'w')
screen.onkeypress(l_paddle.move_down, 's')

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle:
    if ball.distance(r_paddle.position()) < 20 or ball.distance(l_paddle.position()) < 20:
        if ball.xcor() > 325 or ball.xcor() < -325:
            ball.bounce_x()

    # Detect R Paddle Miss, L scores
    if ball.xcor() > 370:
        ball.reset_position()
        scoreboard.add_score_l()

    # Detect L Paddle Miss, R scores
    if ball.xcor() < -370:
        ball.reset_position()
        scoreboard.add_score_r()

screen.exitonclick()





