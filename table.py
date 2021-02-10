from turtle import Turtle, Screen

SCREEN = Screen()
SCREEN.setup(width=800, height=600)
SCREEN.bgcolor("black")
SCREEN.title("My Pong Game")


# SCREEN.tracer(0)


class Table(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pensize(5)
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.screen_line()

    def screen_line(self):
        for _ in range(15):
            self.penup()
            self.setheading(270)
            self.forward(20)
            self.pendown()
            self.setheading(270)
            self.forward(20)
