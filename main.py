from turtle import Screen
from score import Score
from board import Board

screen = Screen()
screen.setup(900, 700)
screen.bgcolor("black")
screen.title("Pong")
score = Score()
screen.tracer(0)

board = Board()
screen.listen()
# screen.onkey(board.go_up_right, "Up")
# screen.onkey(board.go_down_right, "Down")
is_game_on = True

while is_game_on:
    for _ in range(1):
        board.go_up_right()
        board.go_down_left()
    for _ in range(1):
        board.go_up_left()
        board.go_down_right()
    screen.update()


screen.exitonclick()
