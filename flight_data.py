from flight_search import FlightSearch


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):

        # Flight data
        self.flights = FlightSearch()

        self.flight_data = self.flights.get_flight_data(city_from=input("City from? "),
                                                        city_destination=input("City to? "))
        self.cheapest_flight_info = self.flight_data["data"]
        self.iata_info = self.cheapest_flight_info[0]["flyFrom"]
        self.city_from = self.cheapest_flight_info[0]["cityFrom"]
        self.city_to = self.cheapest_flight_info[0]["cityTo"]
        self.price_flight = self.cheapest_flight_info[0]["price"]

