import datetime as dt
import requests
import json


class OpenweatherAPI:
    def __init__(self, city):
        self.city = city
        self.url = "https://api.openweathermap.org/data/2.5/weather?"
        self.api_key = "a8c9e55ce8db93b4e45420a433b2dd66"

    def get_weather(self):
        url = self.url + "appid=" + self.api_key +"&q=" + self.city
        response = requests.get(url).json()
        return response
    
