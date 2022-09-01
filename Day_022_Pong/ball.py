from turtle import Turtle
import time
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.initiate_move()
    
    def initiate_move(self):
        self.goto(0,0)
        self.x_move = random.choice([10, -10])
        self.y_move = random.choice([10, -10])
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.xcor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_move *= -1
    
    def paddle_bounce(self):
        self.x_move *= -1

    def reset(self):
        self.initiate_move()
        
