from turtle import Screen, Turtle
import time


screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snek Game")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]


class SnakeBrain:
    def __init__(self):
        global length
        length = 3
        global speed
        speed = 20
        global segments
        segments = []
        global game_is_on
        game_is_on = True

    def play_snake(self):
        while game_is_on:
            time.sleep(0.1)
            segments[0].forward(speed)
            for int in range(1, length-1):
                segments[int].goto(segments[int - 1].pos())
                screen.update()


def make_snake(positions):
    for i in range(1, length):
        new_turtle = Turtle("square")
        new_turtle.penup()
        new_turtle.color("white")
        for position in positions:
            new_turtle.setpos(position)
            segments.append(new_turtle)
        screen.update()


snake = SnakeBrain()
make_snake(starting_positions)
snake.play_snake()











screen.exitonclick()
