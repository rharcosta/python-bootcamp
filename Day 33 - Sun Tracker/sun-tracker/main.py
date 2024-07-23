import smtplib
import requests
import time
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
my_lat = 42.055821
my_long = 14.273472
my_email = os.environ["EMAIL"]
password = os.environ["PASSWORD"]
smtp_address = os.environ["SMTP_ADDRESS"]

# ---------------------- CURRENT_LOCATION ---------------------- #
# http://open-notify.org/Open-Notify-API/ISS-Location-Now/


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()
    # print(data)

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(f"ISS Latitude: {iss_latitude}\nISS Longitude: {iss_longitude}\n")

    # checking if my position is in the same position as the iss
    if (my_lat - 5 <= iss_latitude <= my_lat + 5) and (my_long - 5 <= iss_longitude <= my_long + 5):
        return True

# ---------------------- MY_DATA_LOCATION ---------------------- #
# https://sunrise-sunset.org/api
# https://www.latlong.net/Show-Latitude-Longitude.html


def is_night():
    parameters = {
        "lat": my_lat,
        "lng": my_long,
        "formatted": 0  # 12 hour formate
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # print(data)

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])  # to take only the hour
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    print(f"Your Latitude: {my_lat}\nYour Longitude: {my_long}\n")
    print(f"Sunrise: {sunrise}h\nSunset: {sunset}h")

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


# ---------------------- SEND_AN_EMAIL ---------------------- #
while True:
    time.sleep(60)
    if iss_overhead() and is_night():
        with smtplib.SMTP(smtp_address) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg="Subject: Look up ☝️\n\nThe ISS is above you in the sky!"
                                )
