import os
from dotenv import load_dotenv
from datetime import datetime
import requests

load_dotenv()

NUTRI_ID = os.getenv("NUTRI_ID")
NUTRI_KEY = os.getenv("NUTRI_KEY")
NUTRI_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_KEY = os.getenv("SHEETY_KEY")
SHEETY_URL = f"https://api.sheety.co/{SHEETY_KEY}/copyOfMyWorkouts/workouts"

header = {
    "x-app-id":NUTRI_ID,
    "x-app-key":NUTRI_KEY
}

nutri_params = {
    "query":input("What was your exercise? "),
    "gender":"male",
    "weight_kg":110,
    "height_cm":180,
    "age":28
}

exercise = requests.post(url=NUTRI_URL, json=nutri_params, headers=header)

print(exercise.text)

now = datetime.now()

# sheety_params = {
#     "workouts":{
#          "date": now.strftime("%Y-%m-%d"),
#          "time": now.strftime("%H:%M")
#          "exercise":
#          "duration":
#          "calories":
#     }
   
# }

# sheet_add = requests.post(url=SHEETY_URL, jso=sheety_params)