from WeatherAPI import WeatherAPI


class WeatherAdapterBIT(WeatherAPI):
    def __init__(self, city, api_key):
        super().__init__(api_key)
        self.city = city
        self.json_data = self.get_weather(city)

    def get_uv_index(self):
        uv_index = self.json_data["data"][0]["uv"]
        return uv_index

    def get_sunrise_sunset(self):
        sunrise = self.json_data["data"][0]["sunrise"]
        sunset = self.json_data["data"][0]["sunset"]
        return sunrise, sunset

    def get_visibility(self):
        visibility = self.json_data["data"][0]["vis"]
        return visibility


