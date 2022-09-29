import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

api_key = os.getenv('APIKEY')
twilio_sid = os.getenv('TWILIO_SID')
twilio_auth = os.getenv('TWILIO_AUTH')

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall?"

weather_params = {
    "lat": 34.069210,
    "lon": -118.009361,
    "appid": api_key,
    "exclude": "current, minutely, daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
weather_data = response.json()

weather_slice = weather_data['hourly'][:12]

will_rain = False

for hour_data in weather_slice:
    weather_condition = hour_data['weather'][0]['id']
    if int(weather_condition) < 700:
        will_rain = True
  
if will_rain:
    client = Client(twilio_sid, twilio_auth)
    message = client.messages \
                .create(
                     body="Bring an umbrella!",
                     from_='+17407154094',
                     to='+16266794568'
                 )
else:
    client = Client(twilio_sid, twilio_auth)
    message = client.messages \
                .create(
                     body="It's dry right now!",
                     from_='+17407154094',
                     to='+16266794568'
                 )

print(message.status)