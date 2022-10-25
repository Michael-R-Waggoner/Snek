from turtle import Turtle, Screen

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
    def make_snake(self,starting_positions):
        for i in range(1,length):
            new_turtle = Turtle("square")
            new_turtle.penup()
            new_turtle.color("white")
            for position in starting_positions:
                new_turtle.goto(position)
                segments.append(new_turtle)
    def play_snake(self):
        while game_is_on:
            screen.update()
            time.sleep(0.1)
            segments[0].forward(speed)
            for int in range(1, length-1):
                segments[int].setpos( segments[int - 1].pos)


