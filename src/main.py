from tkinter import *
import tkinter
from tkinter import font
import datetime
from matplotlib.pyplot import get

import requests
from requests.api import request
from urllib.request import urlopen

class homeframe(Frame):
    def __init__(self):
        S_Height = 1050
        S_Width =  1400
        self.canvas = Canvas(root, height = S_Height, width = S_Width,bg="lightblue")
        self.canvas.pack()

        # Home Screen Entry
        self.hp = Entry(root,bg="white",font="helvetica",justify=CENTER)
        self.hp.insert(END,"Type in your destination...")
        self.hp.place(relx = 0.3, rely = 0.5, relwidth = 0.4, relheight = 0.1)

        # Home Screen Button
        self.take_button = Button(root, bg="#00BAFF", activebackground="#7EDCFF", text= "Take me there!", font="helvetica", fg="white", activeforeground="white",command= lambda: self.get_GeoCode(self.hp.get()))
        self.take_button.place(relx = 0.3, rely = 0.63, relwidth = 0.4, relheight = 0.1)


    def get_GeoCode(hp):
        
        GeoCode_Key = "61852ccd0bd110bcfe7799d4c7906048"
        Geocode_Call = f"http://api.openweathermap.org/geo/1.0/direct?q={hp}&appid={GeoCode_Key}"
        request_geo = requests.get(Geocode_Call)
        got_geocode = request_geo.json()
        
        #try:
        city_name = got_geocode[0]['name']
        country = got_geocode[0]['country']
        lat = got_geocode[0]['lat']
        lon = got_geocode[0]['lon']
        m = mainframe()
        m.load(lat,lon,city_name,country)
        return f""
            
            
        #except:
        #    valid = Label(root,text="Please enter a valid destination...",font="helvetica",bg="lightblue")
        #    valid.place(relx = 0.3, rely = 0.75, relwidth = 0.4, relheight = 0.1)


class mainframe():
    def __init__(self):
        self.main_frame = Frame(root,bg="lightblue")
    
    def format_weather(self,got_weather):
        print(got_weather['current'])

    def get_weather(self,lat,lon):
        weather_key = "10ab2060f30ce15d80acaef3490a3c36"
        weather_call = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,alerts&appid={weather_key}&units=metric"
        request_weather = requests.get(weather_call)
        got_weather = request_weather.json()
        self.format_weather(got_weather)
    
    def load(self,lat,lon,city,country):
        self.main_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        destinationbox = Label(self.main_frame,bg="lightgray",text=f"{city}, {country}",font=("helvetica",24))
        destinationbox.place(relx = 0, rely = 0, relwidth = 0.3, relheight = 0.15)

        self.get_weather(lat,lon)


if __name__ == "__main__":
    root = Tk()
    root.title("TravelHUB")
    homeframe(root)
    root.mainloop()
