# 1. create the screen
from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Ping Pang Game")
screen.tracer(0)

r_paddle = Paddle((374,0))
l_paddle = Paddle((-384,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()  # start listening
screen.onkey(fun=r_paddle.go_up, key='Up')
screen.onkey(fun=r_paddle.go_down, key='Down')

screen.onkey(fun=l_paddle.go_up, key='w')
screen.onkey(fun=l_paddle.go_down, key='s')

# 4. create moving ball
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.ball_move()
    # 5. detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:  # bounce
        ball.bounce_y()
    # 6. detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor()>340 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()

    # 7. detect when paddle misses
    if ball.xcor() > 370:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    # 8. scoreboard








