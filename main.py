
import time
from turtle import Screen

from Food import Food
from ScoreBoard import ScoreBoard
from SnakeBrain import SnakeBrain

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
    scoreboard.make_scoreboard()
    if snake.segments[0].distance(food.food_location) < 20:
        food.clearstamps()
        snake.length += 1
        scoreboard.score += 1
        food.make_food()
        scoreboard.clear()
    if snake.segments[0].xcor() > 300 or snake.segments[0].xcor() < -300:
        scoreboard.reset()
        snake.reset()
    if snake.segments[0].ycor() > 300 or snake.segments[0].ycor() < -300:
        scoreboard.reset()
        snake.reset()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            scoreboard.reset()
            snake.reset()







screen.exitonclick()
