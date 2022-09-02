from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 10, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(-270, 270)
        self.hideturtle()
        self.create_scoreboard()

    def create_scoreboard(self):
        self.write(f"Level: {self.score}", align=ALIGNMENT, font=FONT)

    def score_add(self):
        self.score += 1
        self.clear()
        self.create_scoreboard()