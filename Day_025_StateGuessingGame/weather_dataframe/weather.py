# import csv

# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperature = []
#     for row in data:
#         temperature.append(row[1])
#     print(temperature)

import weakref
import pandas as pd

weather = pd.read_csv('./weather_data.csv')
#print(weather)
#print(weather['temp'])

# Get mean and max temp
print(round(weather['temp'].mean(),2))
print(weather['temp'].max())

# Get data in row
print(weather[weather['day'] == 'Monday'])
print(weather[weather['temp'] == weather['temp'].max()])

# Create dataframe from dict
data_dict = {
    "students":["Amy", "James", "Angela"],
    "scores": [76,56,65]
}

data = pd.DataFrame(data_dict)
print(data)