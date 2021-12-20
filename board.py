from turtle import Turtle
import random


def setup_board(pong_list):
    for position in range(-300, 350, 40):
        pong = Turtle("square")
        pong.penup()
        pong.color("white")
        pong.shapesize(stretch_wid=1, stretch_len=.5)
        pong.goto(0, position)
        pong_list.append(pong)


class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.pong_list = []
        setup_board(self.pong_list)
        self.bar_right = self.pong_list[0].clone()
        self.bar_left = self.pong_list[0].clone()
        self.bar_right.goto(400, 0)
        self.bar_left.goto(-400, 0)

    def go_up_right(self):
        self.bar_right.goto(self.bar_right.xcor(), (self.bar_right.ycor() + random.randint(5, 10)))

    def go_down_right(self):
        self.bar_right.goto(self.bar_right.xcor(), (self.bar_right.ycor() - random.randint(5, 10)))

    def go_up_left(self):
        self.bar_left.goto(self.bar_left.xcor(), (self.bar_left.ycor() + random.randint(5, 10)))

    def go_down_left(self):
        self.bar_left.goto(self.bar_left.xcor(), (self.bar_left.ycor() - random.randint(5, 10)))
