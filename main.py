from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
import pytz
import requests
import time
from Weatheradapter import OPWInterface

root = Tk()
root.title("AUA RAIY APP")
root.geometry("900x500+300+200")
root.resizable(False, False)

root.wm_title("My Weather App")

frame = tk.Frame(root)
frame.pack()

image = tk.PhotoImage(file="search.png")
mylabel = tk.Label(frame, image=image)
mylabel.grid(row=0, column=0)

textfield = tk.Entry(mylabel)
textfield.insert(0, "")
textfield.grid(row=0, column=1)

search_icon_image = tk.PhotoImage(file="search_icon.png")

class OpenweatherAPI:
    def __init__(self, city):
        self.city = city
        self.url = "https://api.openweathermap.org/data/2.5/weather?"
        self.api_key = "a8c9e55ce8db93b4e45420a433b2dd66"

    def get_weather(self):
        url = f"{self.url}appid={self.api_key}&q={self.city}"
        response = requests.get(url).json()
        return response

class OPWInterface:
    def __init__(self, city):
        self.weather_api = OpenweatherAPI(city)

    def get_temperature(self):
        response = self.weather_api.get_weather()
        if 'main' in response:
            temperature_k = response['main']['temp']
            temperature_c = temperature_k - 273.15
            return temperature_c
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

def perform_search():
    city = textfield.get()
    opw_interface = OPWInterface(city)

    temperature = opw_interface.get_temperature()
    description = opw_interface.get_description()
    cloudiness = opw_interface.get_cloudiness()
    wind_speed = opw_interface.get_wind_speed()
    humidity = opw_interface.get_humidity()
    pressure = opw_interface.get_pressure()

    t.config(text=f" {temperature:.2f}°C")  
    d.config(text=f" {description}")
    y.config(text=f" {cloudiness}%")
    w.config(text=f" {wind_speed} m/s")
    h.config(text=f" {humidity}%")
    c.config(text=f"{pressure} hPa")

def update_time_label():
    current_time = time.strftime("%H:%M:%S")  
    time_label.config(text=f"Current Time: {current_time}")



logo_image = tk.PhotoImage(file="logo.png")
logo = tk.Label(image=logo_image)
logo.place(x=150, y = 90)

Frame_image = tk.PhotoImage(file = "box.png")
frame = tk.Label(image=Frame_image)
frame.pack(padx=5,pady=5,side=BOTTOM)


label1 = Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="black", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = Label(root, text="Humidity", font=("Helvetica", 15, 'bold'), fg="black", bg="#1ab5ef")
label2.place(x=240, y=400)

label3 = Label(root, text="Description", font=("Helvetica", 15, 'bold'), fg="black", bg="#1ab5ef")
label3.place(x=360, y=400)

label4 = Label(root, text="Pressure", font=("Helvetica", 15, 'bold'), fg="black", bg="#1ab5ef")
label4.place(x=480, y=400)

label5 = Label(root, text="Cloudiness", font=("Helvetica", 15, 'bold'), fg="black", bg="#1ab5ef")
label5.place(x=650, y=400)

t = tk.Label(font=("arial",70 ,"bold" ), fg = "#ee666d")
t.place(x=400, y=150)

c = tk.Label(font=("arial",15, "bold"))
c.place(x=400,y=250)

w =tk.Label(text="...", font=("arial", 10, 'bold'), bg= "#1ab5ef")
w.place(x=120,y=430)

h =tk.Label(text="...", font=("arial", 10, 'bold'), bg= "#1ab5ef")
h.place(x=240,y=430)
d =tk.Label(text="...", font=("arial", 10, 'bold'), bg= "#1ab5ef")
d.place(x=360,y=430)
c =tk.Label(text="...", font=("arial", 10, 'bold'), bg= "#1ab5ef")
c.place(x=480,y=430)
y=tk.Label(text="...", font=("arial", 10, 'bold'), bg= "#1ab5ef")
y.place(x=650,y=430)

current_weather_label = tk.Label(text="Current Weather", font=("arial", 16, "bold"), fg="#ee666d")
current_weather_label.place(x=20, y=20)  

time_label = tk.Label(font=("arial", 14, "bold"), fg="#ee666d")
time_label.place(x=20, y=60)


search_button = tk.Button(mylabel, image=search_icon_image, command=perform_search)
search_button.grid(row=0, column=2)

root.after(1000, update_time_label)

root.mainloop()

