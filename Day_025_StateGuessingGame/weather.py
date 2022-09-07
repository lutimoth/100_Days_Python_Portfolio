# import csv

# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperature = []
#     for row in data:
#         temperature.append(row[1])
#     print(temperature)

import pandas as pd

weather = pd.read_csv('./weather_data.csv')
print(weather)
print(weather['temp'])