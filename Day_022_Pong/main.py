from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Ol Pongerson")
screen.tracer(0)
    
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Score()
# ball.set_direction()

screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")

screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

gaming = True

while gaming:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # Detect collison with wall
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.wall_bounce()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 55 and ball.xcor() > 320 \
    or ball.distance(l_paddle) < 55 and ball.xcor() < -320:
        ball.paddle_bounce()
    
    if ball.xcor() > 380:
        ball.reset()
        score.score_add("left")

    if ball.xcor() < -380:
        ball.reset()
        score.score_add("right")


screen.exitonclick()