from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.initiate_move()
        self.move_speed = 0.1
        self.hit_wall = 0
    
    def initiate_move(self):
        self.goto(0,0)
        self.x_move = random.choice([10, -10])
        self.y_move = random.choice([10, -10])
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.initiate_move()
        self.move_speed = 0.1
        
