import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('APIKEY')
print(api_key)

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall?"

weather_params = {
    "lat": 34.069210,
    "long": -118.009361,
    "appid": api_key,
    "exclude": "current, minutely, daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.url)
weather_data = response.json()
print(weather_data)

weather_slice = weather_data['hourly'][:12]

will_rain = False

for hour_data in weather_slice:
    weather_condition = hour_data['weather'][0]['id']
    if int(weather_condition) < 700:
        will_rain = True
  
if will_rain:
    print("bring an umbrella")
else:
    print("it's dry!")