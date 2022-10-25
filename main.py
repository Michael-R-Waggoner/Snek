from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snek Game")
screen.tracer(0)

starting_positions = [(0 , 0) , (-20 , 0) , (-40, 0)]

segments = []

for position in starting_positions:
    new_turtle = Turtle("square")
    new_turtle.penup()
    new_turtle.color("white")
    new_turtle.goto(position)
    segments.append(new_turtle)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    head_pos = segments[0].pos()
    mid_pos = segments[1].pos()
    segments[0].forward(20)
    segments[1].setpos(head_pos)
    segments[2].setpos(mid_pos)





























screen.exitonclick()