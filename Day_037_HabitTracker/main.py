# habit tracker
import os
from dotenv import load_dotenv
import requests

load_dotenv()

pixela_token = os.getenv("PIXELA_TOKEN")
pixela_user = os.getenv("PIXELA_USER")

pixela_endpoint = "https://pixe.la/v1/users"

user_params ={
    "token":pixela_token,
    "username": pixela_user,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

r = requests.post(url = pixela_endpoint, json= user_params)
print(r.text)
