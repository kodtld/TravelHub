import tkinter as tk
import datetime
from urllib.request import urlopen
from PIL import ImageTk
import requests
#from main import MainFrame

class HomeLogic:
    def get_geo_code(self, home_entry):

        geo_code_key = "61852ccd0bd110bcfe7799d4c7906048"
        geocode_call = f"http://api.openweathermap.org/geo/1.0/direct?q={home_entry}&appid={geo_code_key}"
        request_geo = requests.get(geocode_call)
        got_geocode = request_geo.json()
        print(got_geocode)

        try:
            city_name = got_geocode[0]['name']
            country = got_geocode[0]['country']
            lat = got_geocode[0]['lat']
            lon = got_geocode[0]['lon']
            main_instance = MainFrame()
            main_instance.load(lat, lon, city_name, country)

        except:
            valid = tk.Label(self.root, text="Please enter a valid destination...",
                            font="helvetica", bg="lightblue")
            valid.place(relx=0.3, rely=0.75, relwidth=0.4, relheight=0.1)