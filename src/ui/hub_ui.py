import tkinter as tk
from api_format.hub_format_weather import FormatWeather
from api_format.hub_format_news import FormatNews
class HubUI:
    def __init__(self,root):
        self.root = root
        self.format_weather = FormatWeather()
        self.format_news = FormatNews()
        self.hub_frame = tk.Label(self.root, bg="lightblue")
        self.destinationbox = tk.Label(self.hub_frame, bg="darkblue")
        self.weather_box = tk.Label(self.hub_frame, bg="darkblue")
        self.news_box = tk.Label(self.hub_frame, bg="darkblue")
        self.currency_box = tk.Label(self.hub_frame, bg="darkblue")
        self.attractions_box = tk.Label(self.hub_frame,bg="darkblue")

    def load_hub_ui(self,lat,lon,city,country):
        self.hub_frame.place(relheight=1,relwidth=1,relx=0,rely=0)
        # Destination box ---------------
        self.destinationbox.place(relx=0, rely=0, relwidth=0.3, relheight=0.2)
        self.destinationtext = tk.Label(self.destinationbox, text=f"{city}, {country}", font=(
            "helvetica", 24), bg="lightblue")
        self.destinationtext.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        # Return button ---------------
        from logic.hub_logic import HubLogic
        hub_logic = HubLogic(self.hub_frame)
        return_button = tk.Button(self.destinationbox, text="Return", font="helvetica",
                bg="#7EDCFF", activebackground="lightblue",command=lambda: hub_logic.load_back(self.root))
        return_button.place(relx=0, rely=0, relwidth=0.3)
        
        # Weather box ---------------
        self.weather_box.place(relx=0.3, rely=0, relwidth=0.7, relheight=0.2)
        weather_return = hub_logic.get_weather(lat,lon)
        for i in weather_return:
            self.format_weather.form_weather(self.weather_box,weather_return[i][0]['weather'],weather_return[i][0]['weather_min'],weather_return[i][0]['date'],weather_return[i][0]['icon'],i)
        
        # News box ---------------
        self.news_box.place(relx=0,rely=0.2,relwidth=0.44,relheight=0.8)
        self.news_header_text = tk.Label(self.news_box,text=f"Latest news from: {city}",font=("helvetica",20),bg="darkblue",fg="white")
        self.news_header_text.place(relx=0,rely=0,relwidth=1,relheight=0.2)
        news_return = hub_logic.get_news(city)
        for i in news_return:
            #print(news_return[i][0]['title'],news_return[i][0]['source'],news_return[i][0]['link'],i)
            self.format_news.form_news(self.news_box,news_return[i][0]['title'],news_return[i][0]['source'],news_return[i][0]['link'],i)
        
        # Currency box ---------------
        self.currency_box.place(relx=0.44,rely=0.2,relheight=0.32,relwidth=0.56)
        hub_logic.setup_currency_code(self.currency_box,country)
        
        # Attractions box ---------------
        self.attractions_box.place(relx=0.44,rely=0.52,relwidth=0.56,relheight=0.48)
        attractions_title = tk.Label(self.attractions_box,text=f"Popular attractions in the radius of 10km from {city} centre:",font=("helvetica",20),bg="darkblue",fg="white")
        attractions_title.place(relwidth=1,relheight=0.3,relx=0,rely=0)
        hub_logic.get_attractions(self.attractions_box,lat,lon,city)

        
        