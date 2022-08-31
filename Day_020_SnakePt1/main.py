from turtle import Screen
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake-y Snake Time")

# Turn off automatic animations
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

gaming = True
while gaming:
    # Keep update outside for loop so we only update when all 3 segments moved
    screen.update()
    time.sleep(0.1)
    # for seg in segments: This is not good
    #     seg.forward(20)  Prevents turning
    snake.move()
    
    # detect collision with food
    if snake.head.distance(food) < 15:
        print("nom nom nom")

screen.exitonclick()