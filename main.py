# Imports
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Screen Configuration
screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(width=800, height=600)
screen.tracer(0)

# Class initialization
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Snake Control
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 400 or snake.head.xcor() < -400 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        # is_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()


    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # is_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()

screen.exitonclick()