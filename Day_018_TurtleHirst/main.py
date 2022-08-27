# Replicate Hirst Painting as a Project


import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

color_list = rgb_colors[3:]

print(rgb_colors)
print(color_list)