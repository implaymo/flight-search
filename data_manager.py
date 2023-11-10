import requests
from flight_data import FlightData
from notification_manager import NotificationManager
from dotenv import load_dotenv

load_dotenv()


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.rows_data = []

        self.sheet_prices = []
        self.data_prices = []
        self.flight_data = FlightData()
        self.notification_manager = NotificationManager()

    def get_row_spreadsheet(self):
        """Gets data from spreadsheet and stores in self.rows_data list"""

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

    def spreadsheet_data(self):
        # Gets flight from spreadsheet
        self.get_row_spreadsheet()
        for row in range(len(self.rows_data)):
            sheet_flight_data = {
                "price": self.rows_data[row]["price"],
                "iata": self.rows_data[row]["iata"],
                "city": self.rows_data[row]["city"],
                                 }
            self.sheet_prices.append(sheet_flight_data)

    def price_compare(self):
        """Gets price data from sheet and from flight api and compares it, in order to check which is lower"""
        self.spreadsheet_data()
        for new_data in self.flight_data.city_data_list:
            for sheet_data in self.sheet_prices:
                if new_data["city"] == sheet_data["city"] and new_data["price"] < sheet_data["price"]:
                    city_to = new_data["city"]
                    iata = new_data["iata"]
                    price = new_data["price"]
                    date = new_data["date_local_departure"]
                    time_departure = new_data["time_local_departure"]
                    time_arrival = new_data["time_local_arrival"]

                    message = (f"Cheaper tickets! To {city_to} for {price}€ "
                               f"in {date} at {time_departure} with arrival at {time_arrival}")
                    self.notification_manager.send_message(message)
                    self.put_spreadsheet(city_to, iata, price)

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


