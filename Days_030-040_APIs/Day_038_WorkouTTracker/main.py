import os
from dotenv import load_dotenv
from datetime import datetime
import requests

load_dotenv()

GENDER = "male"
WEIGHT_KG = 115
HEIGHT_CM = 180
AGE = 28


NUTRI_ID = os.getenv("NUTRI_ID")
NUTRI_KEY = os.getenv("NUTRI_KEY")
NUTRI_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_KEY = os.getenv("SHEETY_KEY")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")
SHEETY_URL = f"https://api.sheety.co/{SHEETY_KEY}/copyOfMyWorkouts/workouts"


nutri_header = {
    "x-app-id":NUTRI_ID,
    "x-app-key":NUTRI_KEY
}

nutri_params = {
    "query":input("What was your exercise? "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

nutri_response = requests.post(url=NUTRI_URL, json=nutri_params, headers=nutri_header)
exercises = nutri_response.json()

print(exercises)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheety_header = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

for exercise in exercises["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEETY_URL, json=sheet_inputs, headers=sheety_header)

    print(sheet_response.text)