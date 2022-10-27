from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")


    def make_scoreboard(self, score):
        self.penup()
        self.setpos(0,280)
        self.pendown()
        self.write(f"Current Score: {score}",False,"center",font=('arial',14,'normal'))

    def game_over(self):
        self.penup()
        self.setpos(0,0)
        self.pendown()
        self.write("Game Over", False, "center", font = ('arial',30,'normal'))
