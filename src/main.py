from tkinter import *
import tkinter

import requests
from requests.api import request
from urllib.request import urlopen

root = Tk()
root.title("TravelHUB")
S_Height = 800
S_Width =  1100
canvas = Canvas(root, height = S_Height, width = S_Width)
canvas.pack()

def get_GeoCode(hp):
    GeoCode_Key = "61852ccd0bd110bcfe7799d4c7906048"
    Geocode_Call = f"http://api.openweathermap.org/geo/1.0/direct?q={hp}&appid={GeoCode_Key}"
    request_geo = requests.get(Geocode_Call)
    got_geocode = request_geo.json()
    
    try:
        city_name = got_geocode[0]['name']
        country = got_geocode[0]['country']
        Lat = got_geocode[0]['lat']
        Lon = got_geocode[0]['lon']

        return f"City: {city_name}, Latitude: {Lat}, Longitude: {Lon}"

    except:
        return "Please enter valid destination..."

# Set Home Screen Background Image
bgimage = PhotoImage(file = "BGimagesmarrel.png")
bg_label = Label(root,image = bgimage)
bg_label.place(x=0,y=0,relwidth=1, relheight=1)

# Home Screen Entry Box
hp = Entry(root,bg="white",font="helvetica",justify=CENTER)
hp.insert(END,"Type in your destination...")
hp.place(relx = 0.3, rely = 0.5, relwidth = 0.4, relheight = 0.1)

# Home Screen Button
take_button = Button(root, bg="#00BAFF", activebackground="#7EDCFF", text= "Take me there!", font="helvetica", fg="white", activeforeground="white",command= lambda: get_GeoCode(hp.get()))
take_button.place(relx = 0.3, rely = 0.63, relwidth = 0.4, relheight = 0.1)

# Main frame
main_frame = Frame(root)
#main_frame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

root.mainloop()
