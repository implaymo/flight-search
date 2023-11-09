import requests
import os
from flight_data import FlightData
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_post_api_endpoint = os.environ["SHEETY_POST_API_ENDPOINT"]

        self.flight_data = FlightData()

    def post_spreadsheet(self):
        # Spreadsheet POST
        for city_info in self.flight_data.city_data_list:
            data_for_spreadsheet = {
                "price":
                    {
                        "city": city_info["city"],
                        "iata": city_info["iata"],
                        "lowest": city_info["price"]

                    }

            }
            response = requests.post(url=self.sheety_post_api_endpoint, json=data_for_spreadsheet)
            response.raise_for_status()
