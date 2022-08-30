from turtle import Turtle, Screen
import random

# Set screen size and game condition
racing = False
screen = Screen()
screen.setup(width = 800, height = 600)
user_bet = screen.textinput(title = "Make your bet", prompt="Which color turtle will win the race?: ")

# Set foundation for turtles (color and position)
y_pos = [-150, -100, -50, 0, 50, 100,  150]
color = ["red", "orange", "gold", "green", "blue", "purple", "violet"]
turtle_list = []

# Create our turtles and the list of turtles
for i, c in enumerate(color):
    turt = Turtle(shape= "turtle")
    turt.penup()
    turt.color(c)
    turt.goto(x = -380, y = y_pos[i])
    turtle_list.append(turt)

if user_bet: 
    racing = True

while racing:
    # Check if a turtle has crossed the "finish line"
    for turtle in turtle_list:   
        if turtle.xcor() > 380:
            racing = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner! ")
            else:
                print(f"You've lost! The {winner} turtle is the winner! ")
    
        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)
        
# print(screen.turtles())
# tim = Turtle(shape = "turtle")
# tim.pu()
# tim.goto(x = -380, y= 0)

screen.exitonclick()