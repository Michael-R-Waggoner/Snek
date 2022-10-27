import random
from turtle import Screen, Turtle
import time
from SnakeBrain import SnakeBrain
from Food import Food
from ScoreBoard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snek Game")
screen.tracer(0)





scoreboard = ScoreBoard()
snake = SnakeBrain()
food = Food()
while snake.game_is_on:
    screen.listen()
    screen.update()
    time.sleep(0.05)
    snake.play_snake()
    score = snake.length - 3
    scoreboard.make_scoreboard(score=score)
    if snake.segments[0].distance(food.food_location) < 20:
        food.clearstamps()
        snake.length += 1
        food.make_food()
        scoreboard.clear()
    if snake.segments[0].xcor() > 300 or snake.segments[0].xcor() < -300:
        snake.game_is_on = False
        scoreboard.game_over()
    if snake.segments[0].ycor() > 300 or snake.segments[0].ycor() < -300:
        snake.game_is_on = False
        scoreboard.game_over()
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 5:
            snake.game_is_on = False
            scoreboard.game_over()






screen.exitonclick()
