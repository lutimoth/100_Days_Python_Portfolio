from msilib.schema import Directory
import turtle as t
import random

t.colormode(255)

timmy = t.Turtle()
timmy.shape('turtle')
timmy.color('red')

# Draw a Square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)


# Draw a Dashed Line
# for _ in range(25):
#     timmy.pd()
#     timmy.forward(10)
#     timmy.pu()
#     timmy.forward(10)


# Draw diff shapes 
# set of colors
colors = ['red', 'green', 'blue', 'black', 'indigo', 'violet', 'Cornflower Blue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue']

# Draw shape based on number of sides
# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)

# Draw 10 shapes
# for i in range(3,11):
#     timmy.color(random.choice(colors))
#     draw_shape(i)
    

# Random Walk
# Set possible directions
directions = [0, 90, 180, 270]

# Set RGB Color
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

# # Set speed and drawing size
# timmy.speed(10)
# timmy.pensize(13)

# # Set amount of lines to draw
# for _ in range(500):
#     timmy.forward(50)
#     timmy.setheading(random.choice(directions))
#     timmy.color(random_color())


# Draw a Spirograph



screen = t.Screen()
screen.exitonclick()