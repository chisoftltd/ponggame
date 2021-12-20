from turtle import Turtle


def setup_board(pong_list):
    for position in range(-300, 350, 40):
        pong = Turtle("square")
        pong.penup()
        pong.color("white")
        pong.shapesize(stretch_wid=, stretch_len=.5)
        pong.goto(0, position)
        pong_list.append(pong)


def right_bar(pong_list):
    print(pong_list[0].ycor())
    if pong_list[0].ycor() >= 200:
        start = 300
        end = -300
        step = -20
    elif pong_list[0].ycor() <= -200:
        start = -300
        end = 300
        step = 20
    for right_bar_position in range(start, end, step):
        print(f"right_bar_position {right_bar_position}")
        pong_list[0].penup()
        pong_list[0].goto(400, right_bar_position)
        pong_list[0].clear()
        pong_list[0].shapesize(1, 0.25)


def left_bar(pong_list):
    print(pong_list[1].ycor())
    if pong_list[1].ycor() >= 200:
        start = -300
        end = 300
        step = 20
    elif pong_list[1].ycor() <= -200:
        start = 300
        end = -300
        step = -20
    for left_bar_position in range(start, end, step):
        print(f"left_bar_position {left_bar_position}")
        pong_list[1].penup()
        pong_list[1].goto(-400, left_bar_position)
        pong_list[1].clear()
        pong_list[1].shapesize(1, 0.25)


class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.pong_list = []
        setup_board(self.pong_list)
        right_bar(self.pong_list)
        left_bar(self.pong_list)

    def go_up(self):
        self.pong_list[0].goto(self.pong_list[0].xcor(), self.pong_list[0].xcor() + 20)

    def go_down(self):
        self.pong_list[0].goto(self.pong_list[0].xcor(), self.pong_list[0].xcor() - 20)