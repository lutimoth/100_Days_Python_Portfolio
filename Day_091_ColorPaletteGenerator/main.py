import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt
import pandas as pd

img = img.imread('milfordtest.jpg')
# print(img)
# print(img.shape)
color, count = np.unique(img.reshape(-1, img.shape[-1]), axis=0, return_counts=True)

color_df = pd.DataFrame({'color':color.reshape(-1),'count':count})
print(color_df)
