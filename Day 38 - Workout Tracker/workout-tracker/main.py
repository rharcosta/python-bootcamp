import requests
import os
from datetime import datetime

# https://developer.nutritionix.com/
# https://dashboard.sheety.co/new
# env -> run -> edit configurations -> environment variables
# to work is necessary to change the URL of the datasheet("My Workout") in the sheety website

API_KEY = os.environ["ENV_SHEETY_KEY"]
APP_ID = os.environ["ENV_SHEETY_ID"]
USERNAME = os.environ["ENV_SHEETY_USERNAME"]
PASSWORD = os.environ["ENV_SHEETY_PASSWORD"]
TOKEN = os.environ["ENV_SHEETY_TOKEN"]
SHEETY_ENDPOINT = os.environ["ENV_SHEETY_ENDPOINT"]
CALORIES_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
GENDER = "f"
WEIGHT = 63
HEIGHT = 163
AGE = 23

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
parameters = {
    "query": input("Tell me the exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=CALORIES_ENDPOINT, json=parameters, headers=header)
result = response.json()
# print(result)

date = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    # no authentication
    # sheet_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs, headers=header)
    # print(sheet_response.text)

    # basic authentication
    # sheet_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs, auth=(USERNAME, PASSWORD))

    # bearer token authentication
    bearer_headers = {"Authorization": f"Bearer {TOKEN}"}
    sheet_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs, headers=bearer_headers)
