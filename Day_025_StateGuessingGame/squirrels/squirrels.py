import pandas as pd

squirrels = pd.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrels_color = squirrels['Primary Fur Color'].value_counts()

print(squirrels_color)