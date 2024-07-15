import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

# ==================== Set up the Flight Search ====================================

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# origin airport
origin_city_iata = "EIN"

# ==================== Update the Airport Codes in Google Sheet ====================

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        time.sleep(2)  # slowing down requests to avoid rate limit
print(f"Sheet Data:\n{sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_destination_code()

# ==================== Retrieve your Customer Emails ===============================

customer_data = data_manager.get_customer_emails()
customer_email_list = [row["whatIsYourEmail?"] for row in customer_data]

# ==================== Search for Direct Flights ===================================

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
    print(f"{destination['city']}: {cheapest_flight.price} euros.")
    time.sleep(2)

# ==================== Search for Indirect Flights =================================

    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
        stopover_flights = flight_search.check_flights(
            origin_city=origin_city_iata,
            destination_city=destination["iataCode"],
            departure_date=tomorrow,
            return_date=six_months_from_today,
            is_direct=False,
        )
        cheapest_flight = find_cheapest_flight(stopover_flights)
        print(f"Cheapest indirect flight price is: {cheapest_flight.price} euros.")

# ==================== Send Notifications and Emails ===============================

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        if cheapest_flight.stops == 0:
            message = f"Low price alert! "\
                      f"Only {cheapest_flight.price} euros to fly "\
                      f"from {cheapest_flight.origin_airport} "\
                      f"to {cheapest_flight.destination_airport}, "\
                      f"on {cheapest_flight.departure_date} "\
                      f"until {cheapest_flight.return_date}."
        else:
            message = f"Low price alert! "\
                      f"Only {cheapest_flight.price} euros to fly "\
                      f"from {cheapest_flight.origin_airport} "\
                      f"to {cheapest_flight.destination_airport}, "\
                      f"with {cheapest_flight.stops} stop(s). "\
                      f"Departing on {cheapest_flight.departure_date} and "\
                      f"returning on {cheapest_flight.return_date}."

        print(f"Check your email. Lower price flight found to {destination['city']}!")

        notification_manager.send_sms(message_body=message)
        notification_manager.send_email(email_list=customer_email_list, email_body=message)
