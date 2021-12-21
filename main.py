from turtle import Screen
import time

from ball import Ball
from score import Score
from board import Board

screen = Screen()
screen.setup(1050, 700)
screen.bgcolor("black")
screen.title("Pong")
score = Score()
screen.tracer(0)

right_board = Board(500, 0)
left_board = Board(-500, 0)
ball = Ball()
screen.listen()
screen.onkey(right_board.go_up, "Up")
screen.onkey(right_board.go_down, "Down")
screen.onkey(left_board.go_up, "a")
screen.onkey(left_board.go_down, "z")

for position in range(-300, 300, 50):
    center_board = Board(0, position)


is_game_on = True
while is_game_on:
    ball.move()
    screen.update()
    time.sleep(0.1)
    if ball.ycor() > 250 or ball.ycor() < -250:
        ball.bounce()
screen.exitonclick()
