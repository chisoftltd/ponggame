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
        self.goto(-100, 200)
        self.write(f"{score}", move=False, align="center", font=("Courier", 80, "normal"))

    def left_score(self, score):
        self.goto(100, 200)
        self.write(f"{score}", move=False, align="center", font=("Courier", 80, "normal"))

    def increment_score(self):
        self.score += 1
        return self.score
