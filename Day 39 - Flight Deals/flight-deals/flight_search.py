# this class is responsible for talking to the Flight Search API
# IATA - INTERNATIONAL AIR TRANSPORT ASSOCIATION
# https://developers.amadeus.com/

import os
import requests
from dotenv import load_dotenv

load_dotenv()


class FlightSearch:

    def __init__(self):
        self.api_key = os.environ["API_KEY"]
        self.api_secret = os.environ["API_SECRET"]
        self.token_endpoint = os.environ["TOKEN_ENDPOINT"]
        self.iata_endpoint = os.environ["IATA_ENDPOINT"]
        self.flight_endpoint = os.environ["FLIGHT_ENDPOINT"]
        self.token = self.get_new_token()

    def get_new_token(self):
        # as Amadeus documentation
        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret,
        }
        response = requests.post(url=self.token_endpoint, headers=header, data=body)
        token = response.json()
        print(f"Your token is {token['access_token']}.")
        print(f"Your token expires in {token['expires_in']} seconds.")

        return token['access_token']

    def get_destination_code(self, city_name):
        header = {"Authorization": f"Bearer {self.token}"}
        parameters = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(url=self.iata_endpoint, headers=header, params=parameters)
        print(f"Status Code: {response.status_code}. Airport IATA: {response.text}")

        try:
            code = response.json()["data"][0]["iataCode"]
        except IndexError:  # doesn't exist in the list
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:  # incorrect name
            print(f"KeyError: No airport code found for {city_name}")
            return "Not Found"
        return code

    def check_flights(self, origin_city, destination_city, departure_date, return_date):
        header = {"Authorization": f"Bearer {self.token}"}
        parameters = {
            "originLocationCode": origin_city,
            "destinationLocationCode": destination_city,
            "departureDate": departure_date,
            "returnDate": return_date,
            "adults": 2,
            "nonStop": "true",
            "currencyCode": "EUR",
            "max": 10,
        }
        response = requests.get(url=self.flight_endpoint, headers=header, params=parameters)

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()
