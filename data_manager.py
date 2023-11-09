import requests
import os
from flight_data import FlightData
class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.sheety_post_api_endpoint = os.environ["SHEETY_POST_API_ENDPOINT"]

        self.data = FlightData()

    def post_spreadsheet(self):
        # Spreadsheet POST
        data_for_spreadsheet = {
            "price":
                {
                    "city": self.data.city_to,
                    "iata": self.data.iata_info,
                    "lowest": self.data.price_flight

                }

        }

        response = requests.post(url=self.sheety_post_api_endpoint, json=data_for_spreadsheet)
        response.raise_for_status()
