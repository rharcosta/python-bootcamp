# this class is responsible for structuring the flight data.

class FlightData:
    def __init__(self, price, origin_airport, destination_airport, departure_date, return_date, stops):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.departure_date = departure_date
        self.return_date = return_date
        self.stops = stops


def find_cheapest_flight(data):
    # empty data/no flights/amadeus rate limit exceeded
    if data is None or not data["data"]:
        print("No flight data.")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")

    # data from the first flight
    first_flight = data["data"][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    nr_stops = len(first_flight["itineraries"][0]["segments"]) - 1
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][nr_stops]["arrival"]["iataCode"]
    departure_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

    # initialize FlightData with the first flight for comparison
    cheapest_flight = FlightData(lowest_price, origin, destination, departure_date, return_date, nr_stops)

    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = price
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flight["itineraries"][0]["segments"][nr_stops]["arrival"]["iataCode"]
            departure_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

            cheapest_flight = FlightData(lowest_price, origin, destination, departure_date, return_date, nr_stops)
            print(f"Lowest price to {destination} is {lowest_price} euros.")

    return cheapest_flight
