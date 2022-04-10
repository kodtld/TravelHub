from tkinter import *
import tkinter
from tkinter import font
import datetime
from matplotlib.pyplot import get

import requests
from requests.api import request
from urllib.request import urlopen

root = Tk()
root.title("TravelHUB")
S_Height = 1050
S_Width =  1400
canvas = Canvas(root, height = S_Height, width = S_Width,bg="lightblue")
canvas.pack()

class mainframe():
    def __init__(self):
        self.main_frame = Frame(root,bg="lightblue")
        self.weather_box = Label(self.main_frame,bg="blue")
    
    def format_weather(self,got_weather):
        self.weather_box.place(relx = 0.3, rely = 0, relwidth = 0.7, relheight = 0.2)

        # Current weather box
        current_box = Label(self.weather_box,bg="blue")
        current_box.place(relx = 0, rely = 0, relwidth = 0.2, relheight = 1)
        
        current_weather_day = got_weather['daily'][0]['temp']['day']
        current_weather_min = got_weather['daily'][0]['temp']['min']
        current_date = datetime.datetime.utcfromtimestamp(got_weather['daily'][0]['dt']).strftime('%d-%m')

        current_weather_day_text = Label(current_box,text=f"Daily average: {current_weather_day}°C",font=("helvetica",13),bg="lightblue")
        current_weather_min_text = Label(current_box,text=f"Daily min.: {current_weather_min}°C",font=("helvetica",13),bg="lightblue")
        current_date_text = Label(current_box,text=f"Date: {current_date}",font=("helvetica",13),bg="lightblue")
        
        current_weather_day_text.place(rely=0.55,relheight=0.15,relwidth=1)
        current_weather_min_text.place(rely=0.7,relheight=0.15,relwidth=1)
        current_date_text.place(rely=0.85,relheight=0.15,relwidth=1)
    
        
        # Tomorrow weather box
        one_box = Label(self.weather_box,bg="blue")
        one_box.place(relx = 0.2, rely = 0, relwidth = 0.2, relheight = 1)

        one_weather_day = got_weather['daily'][1]['temp']['day']
        one_weather_min = got_weather['daily'][1]['temp']['min']        
        one_date = datetime.datetime.utcfromtimestamp(got_weather['daily'][1]['dt']).strftime('%d-%m')
        
        one_weather_day_text = Label(one_box,text=f"Daily average: {one_weather_day}°C",font=("helvetica",13),bg="lightblue")
        one_weather_min_text = Label(one_box,text=f"Daily min.: {one_weather_min}°C",font=("helvetica",13),bg="lightblue")
        one_date_text = Label(one_box,text=f"Date: {one_date}",font=("helvetica",13),bg="lightblue")
        
        one_weather_day_text.place(rely=0.55,relheight=0.15,relwidth=1)
        one_weather_min_text.place(rely=0.7,relheight=0.15,relwidth=1)
        one_date_text.place(rely=0.85,relheight=0.15,relwidth=1)

        # Two day weather box
        two_box = Label(self.weather_box,bg="blue")
        two_box.place(relx = 0.4, rely = 0, relwidth = 0.2, relheight = 1)

        two_weather_day = got_weather['daily'][2]['temp']['day']
        two_weather_min = got_weather['daily'][2]['temp']['min']     
        two_date = datetime.datetime.utcfromtimestamp(got_weather['daily'][2]['dt']).strftime('%d-%m')
        
        two_weather_day_text = Label(two_box,text=f"Daily average: {two_weather_day}°C",font=("helvetica",13),bg="lightblue")
        two_weather_min_text = Label(two_box,text=f"Daily min.: {two_weather_min}°C",font=("helvetica",13),bg="lightblue")
        two_date_text = Label(two_box,text=f"Date: {two_date}",font=("helvetica",13),bg="lightblue")
        
        two_weather_day_text.place(rely=0.55,relheight=0.15,relwidth=1)
        two_weather_min_text.place(rely=0.7,relheight=0.15,relwidth=1)
        two_date_text.place(rely=0.85,relheight=0.15,relwidth=1)

        # Three day weather box
        three_box = Label(self.weather_box,bg="blue")
        three_box.place(relx = 0.6, rely = 0, relwidth = 0.2, relheight = 1)

        three_weather_day = got_weather['daily'][3]['temp']['day']
        three_weather_min = got_weather['daily'][3]['temp']['min']   
        three_date = datetime.datetime.utcfromtimestamp(got_weather['daily'][3]['dt']).strftime('%d-%m')

        three_weather_day_text = Label(three_box,text=f"Daily average: {three_weather_day}°C",font=("helvetica",13),bg="lightblue")
        three_weather_min_text = Label(three_box,text=f"Daily min.: {three_weather_min}°C",font=("helvetica",13),bg="lightblue")
        three_date_text = Label(three_box,text=f"Date: {three_date}",font=("helvetica",13),bg="lightblue")
        
        three_weather_day_text.place(rely=0.55,relheight=0.15,relwidth=1)
        three_weather_min_text.place(rely=0.7,relheight=0.15,relwidth=1)
        three_date_text.place(rely=0.85,relheight=0.15,relwidth=1)

        # Four day weather box
        four_box = Label(self.weather_box,bg="blue")
        four_box.place(relx = 0.8, rely = 0, relwidth = 0.2, relheight = 1)

        four_weather_day = got_weather['daily'][4]['temp']['day']
        four_weather_min = got_weather['daily'][4]['temp']['min']   
        four_date = datetime.datetime.utcfromtimestamp(got_weather['daily'][4]['dt']).strftime('%d-%m')
        
        four_weather_day_text = Label(four_box,text=f"Daily average: {four_weather_day}°C",font=("helvetica",13),bg="lightblue")
        four_weather_min_text = Label(four_box,text=f"Daily min.: {four_weather_min}°C",font=("helvetica",13),bg="lightblue")
        four_date_text = Label(four_box,text=f"Date: {four_date}",font=("helvetica",13),bg="lightblue")
        
        four_weather_day_text.place(rely=0.55,relheight=0.15,relwidth=1)
        four_weather_min_text.place(rely=0.7,relheight=0.15,relwidth=1)
        four_date_text.place(rely=0.85,relheight=0.15,relwidth=1)
          
    def get_weather(self,lat,lon):
        weather_key = "10ab2060f30ce15d80acaef3490a3c36"
        weather_call = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current,minutely,hourly,alerts&appid={weather_key}&units=metric"
        request_weather = requests.get(weather_call)
        got_weather = request_weather.json()
        self.format_weather(got_weather)
    
    def load(self,lat,lon,city,country):
        self.main_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
        
        destinationbox = Label(self.main_frame,bg="blue")
        destinationbox.place(relx = 0, rely = 0, relwidth = 0.3, relheight = 0.15)

        destinationtext = Label(destinationbox,text=f"{city}, {country}",font=("helvetica",24),bg="lightblue")
        destinationtext.place(relx=0,rely=0,relwidth=1,relheight=1)

        self.get_weather(lat,lon)

def get_GeoCode(hp):
    
    GeoCode_Key = "61852ccd0bd110bcfe7799d4c7906048"
    Geocode_Call = f"http://api.openweathermap.org/geo/1.0/direct?q={hp}&appid={GeoCode_Key}"
    request_geo = requests.get(Geocode_Call)
    got_geocode = request_geo.json()
    
    try:
        city_name = got_geocode[0]['name']
        country = got_geocode[0]['country']
        lat = got_geocode[0]['lat']
        lon = got_geocode[0]['lon']
        m = mainframe()
        m.load(lat,lon,city_name,country)

        
        
    except:
        valid = Label(root,text="Please enter a valid destination...",font="helvetica",bg="lightblue")
        valid.place(relx = 0.3, rely = 0.75, relwidth = 0.4, relheight = 0.1)

# Set Home Screen Background Image
#bgimage = PhotoImage(file = "BGimagesmarrel.png")
#bg_label = Label(root,image = bgimage)
#bg_label.place(x=0,y=0,relwidth=1, relheight=1)

# Home Screen Entry Box
hp = Entry(root,bg="white",font="helvetica",justify=CENTER)
hp.insert(END,"Type in your destination...")
hp.place(relx = 0.3, rely = 0.5, relwidth = 0.4, relheight = 0.1)

# Home Screen Button
take_button = Button(root, bg="#00BAFF", activebackground="#7EDCFF", text= "Take me there!", font="helvetica", fg="white", activeforeground="white",command= lambda: get_GeoCode(hp.get()))
take_button.place(relx = 0.3, rely = 0.63, relwidth = 0.4, relheight = 0.1)

root.mainloop()
