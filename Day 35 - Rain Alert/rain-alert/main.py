import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
my_lat = 42.057670
my_long = 14.274070
api_key = os.environ["API_KEY"]
account_sid = os.environ["ACCOUNT_SID"]
auth_token = os.environ["AUTH_TOKEN"]
virtual_number = os.environ["VIRTUAL_NUMBER"]
my_number = os.environ["MY_NUMBER"]

parameters = {
    "lat": my_lat,
    "lon": my_long,
    "appid": api_key,
    "cnt": 4,  # only four registers
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)
# ["list"][0]["weather"][0]["id"] or
will_rain = False
for hour_data in weather_data["list"]:
    condition = hour_data["weather"][0]["id"]
    if int(condition) < 900:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_=virtual_number,
        to=my_number,
    )
    print(message.status)

# WhatsApp
# message = client.messages.create(
#   from_="whatsapp:TWILIO_WHATSAPP_NUMBER",
#   body="It's going to rain today. Remember to bring an umbrella",
#   to="whatsapp:YOUR_TWILIO_VERIFIED_NUMBER"
# )
