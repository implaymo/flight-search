from flight_search import FlightSearch

flights = FlightSearch()

flight_data = flights.get_flight_data(city_from="LON", city_destination="PAR")
print(flight_data)