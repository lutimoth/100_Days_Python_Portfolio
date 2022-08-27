# Replicate Hirst Painting as a Project
import colorgram
import turtle as t
import random

t.colormode(255)

# Use this code to extract colors from an image
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

color_list = rgb_colors[3:]

# print(color_list)

hirst = t.Turtle()
hirst.speed(10)
hirst.penup()
hirst.hideturtle()

#hirst.setpos(length * -1, width * -1)

# Draw a square Hirst painting of length x
# Will move turtle to create a centered painting 
# Fixed spacing between dots

def draw_hirst(num_dots, length):
    num_rows = num_dots/length # Calculate how many rows of dots for overal height
    width = length//2 * 50 * -1 # Calculate width in dots, divided by 2 for balanced left and right
    height = num_rows//2 * 50 * -1 # Divide number of rows in 2 for balanced height

    hirst.setpos(width, height)

    for dot_count in range(1, num_dots + 1):
        hirst.dot(20, random.choice(color_list))
        hirst.forward(50)

        if dot_count % length == 0:
            hirst.setheading(90)
            hirst.forward(50)
            hirst.setheading(180)
            hirst.forward(length*50)
            hirst.setheading(0)

draw_hirst(100, 20)
        
    # for y in range(width):
    #     for x in range(length):
    #         hirst.setpos(x*30, y*30)
    #         hirst.dot(20, random.choice(color_list))
        
#draw_hirst(20, 20)

# for color in color_list:
#     hirst.dot(20, color)

screen = t.Screen()
screen.exitonclick()