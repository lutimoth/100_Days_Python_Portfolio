from turtle import Turtle, Screen

racing = False
screen = Screen()
screen.setup(width = 800, height = 600)
user_bet = screen.textinput(title = "Make your bet", prompt="Which color turtle will win the race?: ")

y_pos = [-150, -100, -50, 0, 50, 100,  150]
color = ["red", "orange", "gold", "green", "blue", "purple", "violet"]
turtle_list = []


for i, c in enumerate(color):
    turt = Turtle(shape= "turtle")
    turt.penup()
    turt.color(c)
    turt.goto(x = -380, y = y_pos[i])

if user_bet: 
    racing = True

while racing:
    rand_dist = random.randint(0,10)



print(screen.turtles())

# tim = Turtle(shape = "turtle")
# tim.pu()
# tim.goto(x = -380, y= 0)


screen.exitonclick()