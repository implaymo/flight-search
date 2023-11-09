import requests
from flight_data import FlightData
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.row = 1
        self.rows_data = []
        self.flight_data = FlightData()

    def put_spreadsheet(self):
        """Edits row from spreadsheet"""
        for city_info in self.flight_data.city_data_list:
            self.row += 1
            data_for_spreadsheet = {
                "price":
                    {
                        "city": city_info["city"],
                        "iata": city_info["iata"],
                        "lowest": city_info["price"]
                    }

            }
            response = requests.put(url=f"https://api.sheety.co/3864f9e32cb6490ca4e1118527c50e15/flightDeals/prices/"
                                        f"{self.row}", json=data_for_spreadsheet)
            response.raise_for_status()

    def get_row_spreadsheet(self):
        """Compares prices from data with spreadsheet"""

        # Gets data from rows
        get_sheety_api = "https://api.sheety.co/3864f9e32cb6490ca4e1118527c50e15/flightDeals/prices"
        response = requests.get(url=get_sheety_api)
        response.raise_for_status()

        data = response.json()
        for key in range(len(data["prices"])):
            city = data["prices"][key]["city"]
            price = data["prices"][key]["lowest"]
            rows_flights_info = {
                "city": city,
                "price": price,
            }
            self.rows_data.append(rows_flights_info)

    def compare_data(self):

