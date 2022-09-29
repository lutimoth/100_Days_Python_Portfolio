import requests
import os
from dotenv import getenv



OWM_Endpoint = "https://api.openweathermap.org/data/3,0/onecall"

weather_params = {
    "lat": 34.069210
    "long": -118.009361
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=weather_params)