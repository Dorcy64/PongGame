from turtle import Turtle
Moves = 0

class Ball(Turtle):
    def __init__(self):
        global SPEED
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.speed(10)
        self.penup()
        self.x_move = 1.15
        self.y_move = 1.15

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        global Moves

        if Moves < 4:
            self.x_move *= -1.3
            self.y_move *= 1.3
            Moves += 1
            print(Moves)

        else:
            self.x_move *= -1




    def reset_back(self):
        self.goto(0, 0)
        self.y_move = 1
        self.x_move = 1
        Moves = 0
        self.x_move *= -1
