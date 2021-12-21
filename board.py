from turtle import Turtle



class Board(Turtle):

    def __init__(self, x_position, y_position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=2, stretch_len=0.5)
        self.goto(x_position, y_position)

    def go_up(self):
        self.goto(self.xcor(), (self.ycor() + 50))

    def go_down(self):
        self.goto(self.xcor(), (self.ycor() - 50))

