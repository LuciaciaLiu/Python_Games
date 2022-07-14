import time
from turtle import Screen
from scoreboard import Scoreboard

import food
from snack import Snack

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

# 1. Create a snake body
snack = Snack()
food = food.Food()
scoreboard = Scoreboard()

# 3. control the snake
screen.listen()  # start listening
screen.onkey(fun=snack.up, key='Up')
screen.onkey(fun=snack.down, key='Down')
screen.onkey(fun=snack.left, key='Left')
screen.onkey(fun=snack.right, key='Right')

game_is_on = True

# 2. Move the snake

while game_is_on:
    screen.update()
    time.sleep(0.15)
    snack.move()

    # 4. detect collision with food

    if snack.head.distance(food) <= 19:
        food.refresh()
        scoreboard.increase_score()
        snack.extend()

    # 6. detect collision with wall
    if snack.head.xcor() > 281 or snack.head.xcor() < -281 or snack.head.ycor() > 281 or snack.head.ycor() < -281:
        game_is_on = False
        scoreboard.game_over()

    # 7. detect collision with tail
    for segment in snack.segments[1:]:
        if snack.head.distance(segment) < 5:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
