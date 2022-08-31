from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake-y Snake Time")

# Turn off automatic animations
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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
    snake.move()
    
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh() # spawn new food
        scoreboard.score_add() # add to the scoreboard
        snake.extend() # extend the snake

    # Detect wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 270 or snake.head.ycor() < -280:
        gaming = False
        scoreboard.game_over()

    # Detect tail collison
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            gaming = False
            scoreboard.game_over()

screen.exitonclick()