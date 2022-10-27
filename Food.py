from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.food_xcor = 0
        self.food_ycor = 0
        self.food_location = ()
        self.make_food()

    def make_food(self):
        self.hideturtle()
        self.penup()
        self.shape("circle")
        self.food_xcor = round(random.randint(-280, 280), -1)
        self.food_ycor = round(random.randint(-280, 280), -1)
        self.food_location = (self.food_xcor, self.food_ycor)
        self.goto(self.food_location)
        self.color("blue")
        self.stamp()







