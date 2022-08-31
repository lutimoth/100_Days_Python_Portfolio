from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.create_scoreboard()

    def create_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 12, "normal"))

    def score_add(self):
        self.score += 1
        self.clear()
        self.create_scoreboard()