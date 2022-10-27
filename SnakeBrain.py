import random
from turtle import Screen, Turtle
import time
from typing import List, Any


class SnakeBrain:
    segments = []

    def __init__(self):
        self.length = 3
        self.speed = 10
        self.game_is_on = True
        self.heading = 0
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.make_snake(positions=self.starting_positions)
        self.screen = Screen()
        self.head = self.segments[0]


    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].seth(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].seth(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].seth(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].seth(0)

    def play_snake(self):
        pos_list = []
        for num in range(1, self.length):
            if num > len(self.segments) - 1:
                new_turtle = Turtle("square")
                new_turtle.penup()
                new_turtle.color("white")
                self.segments.append(new_turtle)
        for segment in self.segments:
            old_pos = segment.pos()
            pos_list.append(old_pos)
        self.segments[0].forward(self.speed)
        self.screen.onkey(self.up, "w")
        self.screen.onkey(self.down, "s")
        self.screen.onkey(self.left, "a")
        self.screen.onkey(self.right, "d")
        for num in range(1, self.length):
            new_pos = pos_list[num - 1]
            self.segments[num].goto(new_pos)


    def make_snake(self, positions):
        for position in positions:
            new_turtle = Turtle("square")
            new_turtle.penup()
            new_turtle.color("white")
            new_turtle.goto(position)
            self.segments.append(new_turtle)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.length = 3
        self.segments.clear()
        self.make_snake(positions=self.starting_positions)
        self.head = self.segments[0]