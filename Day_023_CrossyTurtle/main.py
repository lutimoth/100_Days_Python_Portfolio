import time
from turtle import Screen

screen = Screen()
screen.setup(width = 600, height = 600)
screen.tracer(0)

gaming = True

while gaming:
    time.sleep(0.1)
    screen.update()
    
    

screen.exitonclick()