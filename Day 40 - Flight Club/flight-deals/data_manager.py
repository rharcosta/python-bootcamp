# this class is responsible for talking to the Google Sheet

import requests
import os
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

# load environment variables from .env file
load_dotenv()
prices_endpoint = "https://api.sheety.co/dd96cfff50d4f9bdd4ec6ee945041756/flightDeals/prices"
users_endpoint = "https://api.sheety.co/dd96cfff50d4f9bdd4ec6ee945041756/flightDeals/users"

class DataManager:

    def __init__(self):
        self.user = os.environ["USERNAME"]
        self.password = os.environ["PASSWORD"]
        self.auth = HTTPBasicAuth(self.user, self.password)
        self.destination_data = {}
        self.customer_data = {}

        self.headers = {
            "Authorization": "Basic cnViaWFyY2hhbmpvOmhqaGFqZGpvZG9rYWRva3dv"
        }

    def get_destination_data(self):
        try:
            response = requests.get(url=prices_endpoint, auth=self.auth, headers=self.headers)
            # response.raise_for_status()
            data = response.json()
            if "errors" in data:
                print("Error in API:", data["errors"][0]["detail"])
                return None
            self.destination_data = data["prices"]
            return self.destination_data
        except requests.exceptions.RequestException as e:
            print("Request failed:", e)
            return None

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {"price": {"iataCode": city["iataCode"]}}
            response = requests.put(url=f"{prices_endpoint}/{city['id']}",
                                    auth=self.auth,
                                    json=new_data)
            print(response.text)

    def get_customer_emails(self):
        try:
            response = requests.get(url=users_endpoint, auth=self.auth, headers=self.headers)
            data = response.json()
            self.customer_data = data["users"]
            return self.customer_data
        except requests.exceptions.RequestException as e:
            print("Request failed:", e)
            return None
