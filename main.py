from turtle import Turtle, Screen
from table import Table
from players import Players
from ball import Ball
from score import Score

screen = Screen()
screen.tracer(0)
table = Table()

player1 = Players(0)
player2 = Players(1)

score = Score()
ball = Ball()
l_score = 0
r_score = 0

stoppage = 0
while 1 > stoppage:
    screen.update()
    ball.move()
    score.display(l_score, r_score)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 330 and ball.distance(player2) < 50:
        ball.bounce_x()

    if ball.xcor() < -330 and ball.distance(player1) < 50:
        ball.bounce_x()

    if ball.xcor() > 340:
        l_score += 1
        ball.reset_back()
    if ball.xcor() < -340:
        r_score += 1
        ball.reset_back()

    screen.listen()
    screen.onkeypress(key="w", fun=player1.up)
    screen.onkey(key="s", fun=player1.down)

    screen.onkey(key="Up", fun=player2.up)
    screen.onkey(key="Down", fun=player2.down)


screen.exitonclick()
