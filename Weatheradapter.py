from OpenweatherAPI import OpenweatherAPI

class OPWInterface:
    def __init__(self, city):
        self.weather_api = OpenweatherAPI(city)

    def get_temperature(self):
        response = self.weather_api.get_weather()
        if 'main' in response:
            temperature = response['main']['temp']
            return temperature
        else:
            return None

    def get_description(self):
        response = self.weather_api.get_weather()
        if 'weather' in response:
            description = response['weather'][0]['description']
            return description
        else:
            return None

    def get_humidity(self):
        response = self.weather_api.get_weather()
        if 'main' in response:
            humidity = response['main']['humidity']
            return humidity
        else:
            return None

    def get_pressure(self):
        response = self.weather_api.get_weather()
        if 'main' in response:
            pressure = response['main']['pressure']
            return pressure
        else:
            return None

    def get_wind_speed(self):
        response = self.weather_api.get_weather()
        if 'wind' in response:
            wind_speed = response['wind']['speed']
            return wind_speed
        else:
            return None

    def get_wind_direction(self):
        response = self.weather_api.get_weather()
        if 'wind' in response:
            wind_direction = response['wind']['deg']
            return wind_direction
        else:
            return None

    def get_cloudiness(self):
        response = self.weather_api.get_weather()
        if 'clouds' in response:
            cloudiness = response['clouds']['all']
            return cloudiness
        else:
            return None

    def get_temperature_in_celsius(self):
        temperature_k = self.get_temperature()
        if temperature_k is not None:
            temperature_c = temperature_k - 273.15
            return temperature_c
        else:
            return None