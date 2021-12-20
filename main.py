from turtle import Screen
from score import Score
from board import Board

screen = Screen()
screen.setup(900, 700)
screen.bgcolor("black")
screen.title("Pong")
score = Score()
screen.tracer()

board = Board()
screen.listen()
screen.onkey(board.go_up, "Up")
screen.onkey(board.go_down, "Down")
is_game_on = True

while is_game_on:

    screen.update()


screen.exitonclick()
