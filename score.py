from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        self.right_score(self.score)
        self.left_score(self.score)
        self.hideturtle()

    def right_score(self, score):
        self.goto(-50, 280)
        self.write(f"{score}", move=False, align="left", font=("Arial Black", 45, "normal"))

    def left_score(self, score):
        self.goto(50, 280)
        self.write(f"{score}", move=False, align="right", font=("Arial Black", 45, "normal"))
