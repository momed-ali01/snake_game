# Imports
import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(a=-330, b=330)
        random_y = random.randint(a=-280, b=280)
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = random.randint(a=-280, b=280)
        random_y = random.randint(a=-280, b=280)
        self.goto(random_x, random_y)
