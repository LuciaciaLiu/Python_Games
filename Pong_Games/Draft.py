# 1. create the screen
# 2. create and  move paddle
# 3. create and  move another paddle
# 4. create moving ball

# 5. detect collision with wall and bounce
# 6. detect collision with paddle
# 7. detect when paddle misses

# 8. scoreboard


# 1. create the screen
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Ping Pang Game")
screen.tracer(0)

# 2.1 create paddles
paddle = Turtle()
paddle.shape('square')
paddle.color('white')
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(370, 0)


# 2.2 move paddles
def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()  # start listening
screen.onkey(fun=go_up, key='Up')
screen.onkey(fun=go_down, key='Down')

game_is_on = True
while game_is_on:
    screen.update()












screen.exitonclick()
