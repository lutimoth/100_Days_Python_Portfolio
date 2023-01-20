import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt
import pandas as pd

img = img.imread('milfordtest.jpg')
# print(img)
# print(img.shape)
color, count = np.unique(img.reshape(-1, img.shape[-1]), axis=0, return_counts=True)

color_df = pd.DataFrame(color, columns=['R','G','B'])
color_df['count'] = count

def rgb_to_hex(r,g,b):
    return ('{:02X}' *3).format(r,g,b)

def top_ten_colors(counted_colors):
    top_ten = counted_colors.sort_values(by='count', ascending=False).head(10)
    
    colors={}
    
    for i in top_ten.index.values:
        R = top_ten.loc[i]['R']
        G = top_ten.loc[i]['G']
        B = top_ten.loc[i]['B']
        color_string = f'{R}, {G}, {B}' 
        colors[color_string] = rgb_to_hex(R, G, B)
    return colors

print(top_ten_colors(color_df))