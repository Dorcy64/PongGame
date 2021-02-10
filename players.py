from turtle import Turtle, Screen
screen = Screen()


class Players(Turtle):
    def __init__(self, place):
        super().__init__()
        self.showturtle()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        positions = [(-350, 0), (350, 0)]

        self.players(positions[place])

    def players(self, position):
        self.goto(position)

    def up(self):
        self.setheading(90)
        self.forward(30)

    def down(self):
        self.setheading(270)
        self.forward(30)
