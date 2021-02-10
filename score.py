from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.display(self.l_score, self.r_score)

    def display(self, left, right):
        self.clear()
        self.goto(0, 200)
        self.write(f"{left}   {right}", font=(f"Courier", 80, "normal"), align="center", move=False)
