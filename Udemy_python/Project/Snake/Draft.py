# 1. Create a snake body
# 2. Move the snake
# 3. control the snake
# 4. detect collision with food
# 5. create a scoreboard
# 6. detect collision with wall
# 7. detect collision with tail

from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

# 1. Create a snake body

# 1.1 method one
# segment_1 = Turtle(shape='square')
# segment_1.color('white')

# segment_2 = Turtle(shape='square')
# segment_2.color('white')
# segment_2.goto(-20,0)

# segment_3 = Turtle(shape='square')
# segment_3.color('white')
# segment_3.goto(-40,0)

# method 2:
segments = []
for i in range(3):
    new_segment = Turtle(shape='square')
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(i * (-20), 0)
    segments.append(new_segment)

# 2. Move the snake
screen.update()
game_is_on = True

# move forward
while game_is_on:
    screen.update()
    time.sleep(0.2)
    # for seg in segments:
    #     seg.forward(20)
    for i in range(len(segments)-1, 0, -1):
        new_x = segments[i - 1].xcor()
        new_y = segments[i - 1].ycor()
        segments[i].goto(new_x, new_y)
    segments[0].forward(20)

# 3. control the snake



screen.exitonclick()
