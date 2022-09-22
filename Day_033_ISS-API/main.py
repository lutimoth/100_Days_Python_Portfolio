import requests
from datetime import datetime
import smtplib
import os
from dotenv import load_dotenv
import sched
import time

load_dotenv()

my_email = "tlupython@gmail.com"
password = os.getenv('PASSWORD')

MY_LAT = 34.069210 # Your latitude
MY_LONG = -118.009360 # Your longitude

#Your position is within +5 or -5 degrees of the ISS position.
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

#If the ISS is close to my current position
def iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if abs(iss_longitude - MY_LONG) <= 5 and abs(iss_latitude - MY_LAT) <= 5:
        return True
    else:
        return False

# and it is currently dark
def is_night():
    time = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    time.raise_for_status()
    data = time.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True
    else:
        return False

# Then send me an email to tell me to look up.
def iss_emailer():
    iss_close()
    is_night()

    if iss_close() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs='lutimoth@gmail.com', 
                msg=f"Subject: Look up\n\n ISS is right above tonight, check it out!")
    elif iss_close():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs='lutimoth@gmail.com', 
                msg=f"Subject: Too bad\n\n ISS is close but it's bright")
    elif is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs='lutimoth@gmail.com', 
                msg=f"Subject: Nothing up there\n\n It's night but ISS is not up there")
    else:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs='lutimoth@gmail.com', 
                msg=f"Subject: Don't wait up\n\n ISS is not close and it's bright")
    
while is_night:
    time.sleep(60)
    iss_emailer()
    # sc.enter(60, 1, iss_emailer, (sc,))
    # part of the scheduler, need to put sc as arg in function for it to work

# BONUS: run the code every 60 seconds.
# s = sched.scheduler(time.time, time.sleep)
# s.enter(60, 1, iss_emailer, (s,))
# s.run()




