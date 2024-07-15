import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

# ==================== Set up the Flight Search ====================================

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()
print(sheet_data)

# origin airport
origin_city_iata = "LON"

# ==================== Update the Airport Codes in Google Sheet ====================

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        time.sleep(2)  # slowing down requests to avoid rate limit

data_manager.destination_data = sheet_data
data_manager.update_destination_code()

# ==================== Search for Flights and Send Notifications ===================

today = datetime.now()
# timedelta = calculating future dates
tomorrow = today + timedelta(days=1)  # +1 day
six_months_from_today = today + timedelta(days=(6*30))  # +6 months

for destination in sheet_data:
    print(f"Getting flights for {destination}...")
    flights = flight_search.check_flights(origin_city=origin_city_iata,
                                          destination_city=destination["iataCode"],
                                          departure_date=tomorrow,
                                          return_date=six_months_from_today)
    cheapest_flight = find_cheapest_flight(flights)
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}.")
        notification_manager.send_whatsapp(message_body=f"Low price alert! "
                                                        f"Only {cheapest_flight.price} euros to fly "
                                                        f"from {cheapest_flight.origin_airport} "
                                                        f"to {cheapest_flight.destination_airport}, "
                                                        f"on {cheapest_flight.departure_date} "
                                                        f"until {cheapest_flight.return_date}.")
