from turtle import Screen, Turtle
import time


screen = Screen()
screen.setup(width=600, height=600)
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
        global heading
        heading = 0

    def up(self):
        segments[0].seth(90)

    def down(self):
        segments[0].seth(270)

    def left(self):
        segments[0].seth(180)

    def right(self):
        segments[0].seth(0)
    def play_snake(self):
        while game_is_on:
            screen.listen()
            pos_list = []
            screen.update()
            time.sleep(0.1)
            for segment in segments:
                old_pos = segment.pos()
                pos_list.append(old_pos)
                print(pos_list)
            segments[0].forward(speed)
            screen.onkey(self.up, "w")
            screen.onkey(self.down, "s")
            screen.onkey(self.left, "a")
            screen.onkey(self.right, "d")
            for num in range(1, length):
                new_pos = pos_list[num-1]
                segments[num].goto(new_pos)


    def make_snake(self, positions):
        for position in positions:
            new_turtle = Turtle("square")
            new_turtle.penup()
            new_turtle.color("white")
            new_turtle.goto(position)
            segments.append(new_turtle)


snake = SnakeBrain()
snake.make_snake(positions=starting_positions)
snake.play_snake()












screen.exitonclick()
