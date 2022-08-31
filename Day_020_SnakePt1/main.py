from turtle import Screen, Turtle, tracer
import time
from snake import Snake

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake-y Snake Time")

# Turn off automatic animations
screen.tracer(0)

snake = Snake()

gaming = True

while gaming:
    # Keep update outside for loop so we only update when all 3 segments moved
    screen.update()
    time.sleep(0.1)
    
    # for seg in segments: This is not good
    #     seg.forward(20)  Prevents turning

    snake.move()
    
    # Move the last segment (head) forward

screen.exitonclick()