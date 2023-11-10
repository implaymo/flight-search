import os
import requests
from datetime import date
from dateutil.relativedelta import relativedelta

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.search_api_key = os.environ["SEARCH_API_KEY"]
        self.search_api_endpoint = os.environ["SEARCH_API_ENDPOINT"]
        self.today = date.today().strftime("%d/%m/%Y")
        self.six_month_date = (date.today() + relativedelta(months=+6)).strftime("%d/%m/%Y")

        self.search_header = {
            "apikey": self.search_api_key,
            "Content-Type": "application/json",
            }

    def get_flight_data(self, city_from, city_destination):
        search_params = {
            "fly_from": city_from,
            "date_from": self.today,
            "date_to": self.six_month_date,
            "fly_to": city_destination,
        }

        response = requests.get(url=self.search_api_endpoint, headers=self.search_header, params=search_params)
        response.raise_for_status()
        data = response.json()
        return data

