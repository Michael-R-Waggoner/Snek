from turtle import Turtle
with open("High_score") as file:
    number = file.read()
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.high_score = number


    def make_scoreboard(self):
        self.penup()
        self.setpos(0,280)
        self.pendown()
        self.write(f"Current Score: {self.score}  High Score: {self.high_score}",False,"center",font=('arial',14,'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
    #def game_over(self):
     #   self.penup()
      #  self.setpos(0,0)
       # self.pendown()
        #self.write("Game Over", False, "center", font = ('arial',30,'normal'))
