# API (Application Programming Interface): set of commands, functions protocols and objects
# that programmers can use to create software or interact with an external system

import requests

# end point url / API request
# http://open-notify.org/Open-Notify-API/ISS-Location-Now/
response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.status_code)
response.raise_for_status()  # give the response of the status code

data = response.json()
print(data)
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

iss_position = (latitude, longitude)
print(iss_position)

# Response (status codes):
# https://www.webfx.com/web-development/glossary/http-status-codes/
# 1XX: Hold on
# 2XX: Here you go
# 3XX: Go away
# 4XX: You screwed up
# 5XX: I screwed up
