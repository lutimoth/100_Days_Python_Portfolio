import requests
from datetime import datetime

MY_LAT = 34.069210 # Your latitude
MY_LONG = -118.009360 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#If the ISS is close to my current position
def iss_close():
    if abs(iss_longitude - MY_LONG) <= 5 and abs(iss_latitude - MY_LAT) <= 5:
        return True
    else:
        return False

# and it is currently dark
def check_night():
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True
    else:
        return False

# Then send me an email to tell me to look up.

if iss_close() and check_night():
    print("It's dark and ISS is close")
elif iss_close():
    print("ISS close but not dark")
elif check_night():
    print("It's night but ISS is not close")
else:
    print("ISS is not close and it's not dark")
# BONUS: run the code every 60 seconds.



