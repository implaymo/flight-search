from flight_search import FlightSearch

class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):

        self.city_codes = ["CDG", "BER", "NRT", "SYD", "SAW", "KUL", "LGA", "SFO", "CPT"]
        self.city_data_list = []

        # Flight data information
        self.flights = FlightSearch()

        for city in self.city_codes:
            self.flight_data = self.flights.get_flight_data(city_from="LON", city_destination=city)
            self.cheapest_flight_info = self.flight_data["data"]

            date_local_departure = self.cheapest_flight_info[2]["local_departure"].split("T")[0]
            date_local_arrival = self.cheapest_flight_info[2]["local_arrival"].split("T")[0]
            time_local_departure = self.cheapest_flight_info[2]["local_departure"].split("T")[1].split(".")
            time_local_departure = time_local_departure[0]
            time_local_arrival = self.cheapest_flight_info[2]["local_arrival"].split("T")[1].split(".")
            time_local_arrival = time_local_arrival[0]

            city_data = {
                "iata": self.cheapest_flight_info[0]["flyFrom"],
                "city": self.cheapest_flight_info[0]["cityTo"],
                "price": self.cheapest_flight_info[0]["price"],
                "date_local_departure": date_local_departure,
                "date_local_arrival": date_local_arrival,
                "time_local_departure": time_local_departure,
                "time_local_arrival": time_local_arrival
            }
            self.city_data_list.append(city_data)

