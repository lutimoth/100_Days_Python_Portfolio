from turtle import Turtle

STARTING = (0, -280)

class Player(Turtle):
    
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.goto(STARTING)
        
    def forward(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)
        
    def backward(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)