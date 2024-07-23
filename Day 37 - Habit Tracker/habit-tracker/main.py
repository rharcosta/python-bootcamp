import requests
import os
from dotenv import load_dotenv
from datetime import datetime
# in browser = https://pixe.la/v1/users/rubia/graphs/graph1.html

load_dotenv()
username = os.environ["USERNAME"]
token = os.environ["TOKEN"]
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/graph1"
update_endpoint = f"{pixela_endpoint}/{username}/graphs/graph1/20240709"
delete_endpoint = f"{pixela_endpoint}/{username}/graphs/graph1/20240709"

parameters = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

header = {
    "X-USER-TOKEN": token
}

graph_parameters = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "kilogram",
    "type": "float",
    "color": "shibafu"
}
# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=header)
# print(response.text)

# setting a data:
# day = datetime(year=2024, month=7, day=8)
day = datetime.now()
today = day.strftime("%Y%m%d")

pixel_parameters = {
    "date": today,
    "quantity": input("How many Km did you cycle today? "),
}
# response = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=header)
# print(response.text)

# UPDATE A PIXEL
# response = requests.put(url=update_endpoint, json=pixel_parameters, headers=header)
# print(response.text)

# DELETE A PIXEL
response = requests.delete(url=delete_endpoint, headers=header)
print(response.text)
