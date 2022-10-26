import random
from turtle import Screen, Turtle
import time
from SnakeBrain import SnakeBrain
from Food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snek Game")
screen.tracer(0)






snake = SnakeBrain()
food = Food()
while snake.game_is_on:
    screen.listen()
    screen.update()
    time.sleep(0.05)
    snake.play_snake()
    if snake.segments[0].distance(food.food_location) < 20:
        food.clearstamps()
        snake.length += 1
        food.make_food()


screen.exitonclick()
