import requests
import json


class WeatherAPI:
    def __init__(self, city, api_key):
        self.city = city
        self.api_key = api_key
        self.json_data = self.get_weather(city)

    def get_weather(self, city):
        url = "http://api.weatherbit.io/v2.0/current?city=" + city + "&key=" + self.api_key + "&include=minutely"
        response = requests.get(url).json()
        return response

    def remove_gust(self):
        for data in self.json_data["data"]:
            del data["gust"]

    def get_updated_json(self):
        return self.json_data









