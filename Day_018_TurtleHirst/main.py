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

# Draw a hirst painting of a set length (x) and width(y)
# Must be int
# Will take lenght and width as nested for loop and set length as x and width as y
def draw_hirst(length, width):
    hirst.setpos(length * -1, width * -1)

    for y in range(width):
        for x in range(length):
            hirst.setpos(x*30, y*30)
            hirst.dot(20, random.choice(color_list))
        
draw_hirst(20, 20)

# for color in color_list:
#     hirst.dot(20, color)

screen = t.Screen()
screen.exitonclick()