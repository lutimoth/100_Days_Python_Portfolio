from turtle import Turtle
import random

COLORS = ['red','orange','blue','green','black','purple']
INIT_SPEED = 5
ACCELERATION = 10

class Cars(Turtle):
    
    def __init__(self):
        self.all_cars = []
        
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid = 1.0, stretch_len = 2.0)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
    
    def move_cars(self):
        for car in self.all_cars:
            car.backward(INIT_SPEED)