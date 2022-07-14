import random
from turtle import Turtle


class Food(Turtle):  # inherit from Turtle class
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # (0.5 * original_dimension = (10,10))
        self.color('blue')
        self.speed('fastest')
        self.goto(random.randint(-260, 260), random.randint(-260, 260))

    # 4. detect collision with food
    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))


