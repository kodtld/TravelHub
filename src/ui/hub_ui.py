import tkinter as tk
from api_format.hub_format_weather import FormatWeather
from api_format.hub_format_news import FormatNews
from api_format.hub_format_attractions import FormatAttractions
from api_format.hub_format_currency import FormatCurrency
from logic.hub_logic import HubLogic
class HubUI:
    def __init__(self,root):
        self.root = root
        self.format_weather = FormatWeather()
        self.format_news = FormatNews()
        self.format_attractions = FormatAttractions()
        self.hub_frame = tk.Label(self.root, bg="lightblue")
        self.hub_logic = HubLogic()
        self.destinationbox = tk.Label(self.hub_frame, bg="darkblue")
        self.weather_box = tk.Label(self.hub_frame, bg="darkblue")
        self.news_box = tk.Label(self.hub_frame, bg="darkblue")
        self.currency_box = tk.Label(self.hub_frame, bg="darkblue")
        self.format_currency = FormatCurrency(self.currency_box)
        self.attractions_box = tk.Label(self.hub_frame,bg="darkblue")
        
    def load_back(self,root):
        from ui.home_ui import HomeUI
        home_ui = HomeUI(root)
        home_ui.place_home_ui()

    def load_hub_ui(self,lat,lon,city,country):
        self.hub_frame.place(relheight=1,relwidth=1,relx=0,rely=0)
        # Destination box ---------------
        self.destinationbox.place(relx=0, rely=0, relwidth=0.3, relheight=0.2)
        self.destinationtext = tk.Label(self.destinationbox, text=f"{city}, {country}", font=(
            "helvetica", 24), bg="lightblue")
        self.destinationtext.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        # Return button ---------------
        return_button = tk.Button(self.destinationbox, text="Return", font="helvetica",
                bg="#7EDCFF", activebackground="lightblue",command=lambda: self.load_back(self.root))
        return_button.place(relx=0, rely=0, relwidth=0.3)
        
        # Weather box ---------------
        self.weather_box.place(relx=0.3, rely=0, relwidth=0.7, relheight=0.2)
        weather_return = self.hub_logic.get_weather(lat,lon)
        for i in weather_return:
            self.format_weather.form_weather(self.weather_box,weather_return[i][0]['weather'],weather_return[i][0]['weather_min'],weather_return[i][0]['date'],weather_return[i][0]['icon'],i)
        
        # News box ---------------
        self.news_box.place(relx=0,rely=0.2,relwidth=0.44,relheight=0.8)
        self.news_header_text = tk.Label(self.news_box,text=f"Latest news from: {city}",font=("helvetica",20),bg="darkblue",fg="white")
        self.news_header_text.place(relx=0,rely=0,relwidth=1,relheight=0.2)
        news_return = self.hub_logic.get_news(city)
        for i in news_return:
            #print(news_return[i][0]['title'],news_return[i][0]['source'],news_return[i][0]['link'],i)
            self.format_news.form_news(self.news_box,news_return[i][0]['title'],news_return[i][0]['source'],news_return[i][0]['link'],i)
        
        # Currency box ---------------
        self.currency_box.place(relx=0.44,rely=0.2,relheight=0.32,relwidth=0.56)
        setup_currency_return = self.hub_logic.setup_currency_code(country)
        #print(setup_currency_return)
        country = setup_currency_return[0]
        currency_name = setup_currency_return[1]
        currency_code = setup_currency_return[2]
        self.hub_logic.check_currency()
        get_currency_return = self.hub_logic.get_currency(10,country,currency_name,currency_code)
        #print(get_currency_return)
        amount = get_currency_return[2]
        ratesum = get_currency_return[3]
        self.format_currency.format_all(country,currency_name,amount,ratesum,currency_code)
        
        # Attractions box ---------------
        self.attractions_box.place(relx=0.44,rely=0.52,relwidth=0.56,relheight=0.48)
        attractions_title = tk.Label(self.attractions_box,text=f"Popular attractions in the radius of 10km from {city} centre:",font=("helvetica",20),bg="darkblue",fg="white")
        attractions_title.place(relwidth=1,relheight=0.3,relx=0,rely=0)
        attract_return = self.hub_logic.get_attractions(lat,lon,city)
        for i in attract_return:
            self.format_attractions.form_att(self.attractions_box,attract_return[i][0]['name'],attract_return[i][0]['dist'],attract_return[i][0]['tags'],attract_return[i][0]['link'],i)

        
        