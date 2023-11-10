import requests
from flight_data import FlightData
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.rows_data = []

        self.sheet_prices = []
        self.data_prices = []
        self.flight_data = FlightData()

    def get_row_spreadsheet(self):
        """Compares prices from data with spreadsheet"""

        # Gets data from rows
        get_sheety_api = "https://api.sheety.co/3864f9e32cb6490ca4e1118527c50e15/flightDeals/prices"
        response = requests.get(url=get_sheety_api)
        response.raise_for_status()

        data = response.json()
        for key in range(len(data["prices"])):
            city = data["prices"][key]["city"]
            iata = data["prices"][key]["iata"]
            price = data["prices"][key]["lowest"]
            rows_flights_info = {
                "city": city,
                "iata": iata,
                "price": price,
            }
            self.rows_data.append(rows_flights_info)

    def data_flight_api(self):
        # Gets new flight data from API and stores as data_prices tuple list
        for row in range(len(self.flight_data.city_data_list)):
            new_lowest_price = (self.flight_data.city_data_list[row]["price"],
                                self.flight_data.city_data_list[row]["iata"],
                                self.flight_data.city_data_list[row]["city"])
            self.data_prices.append(new_lowest_price)

    def spreadsheet_data(self):
        # Gets flight from spreadsheet
        self.get_row_spreadsheet()
        for row in range(len(self.rows_data)):
            sheet_flight_price = (self.rows_data[row]["price"],
                                  self.rows_data[row]["iata"],
                                  self.rows_data[row]["city"])
            self.sheet_prices.append(sheet_flight_price)

    def price_compare(self):
        """Gets price data from sheet and from flight api and compares it, in order to check which is lower"""
        self.data_flight_api()
        self.spreadsheet_data()
        for new_price, new_iata, new_city in self.data_prices:
            for price, iata, city in self.sheet_prices:
                if new_city == city and new_price < price:
                    self.put_spreadsheet(city, new_iata, new_price)

    def put_spreadsheet(self, city, iata, price):
        """Edits row from spreadsheet"""
        for row, row_data in enumerate(self.rows_data):
            if row_data["city"] == city:
                data_for_spreadsheet = {
                    "price":
                        {
                            "city": city,
                            "iata": iata,
                            "lowest": price
                        }

                }
                response = requests.put(url=f"https://api.sheety.co/3864f9e32cb6490ca4e1118527c50e15/flightDeals/prices/"
                                            f"{row + 2}", json=data_for_spreadsheet)
                response.raise_for_status()


