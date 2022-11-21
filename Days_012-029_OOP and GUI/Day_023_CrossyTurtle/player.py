from turtle import Turtle

STARTING = (0, -280)
MOVE_DISTANCE = 10

class Player(Turtle):
    
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.goto(STARTING)
        
    def forward(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
        
    def backward(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
        
    def level_up(self):
        self.goto(STARTING)
        
    def squished(self):
        self.goto(STARTING)