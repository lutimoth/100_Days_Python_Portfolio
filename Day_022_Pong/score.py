from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 30, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.create_scoreboard()

    def create_scoreboard(self):
        self.clear()
        self.goto(-100, 250)
        self.write(f"{self.lscore}", align=ALIGNMENT, font=FONT)
        self.goto(100, 250)
        self.write(f"{self.rscore}", align=ALIGNMENT, font=FONT)

    def score_add(self, side):
        if side == "left":
            self.lscore += 1
            self.create_scoreboard()
        if side == "right":
            self.rscore += 1
            self.create_scoreboard()