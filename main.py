from turtle import Screen, Turtle

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snek Game")

starting_positions = [(0 , 0) , (-20 , 0) , (-40, 0)]

for position in starting_positions:
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape("square")
    new_turtle.color("white")
    new_turtle.goto(position)





























screen.exitonclick()