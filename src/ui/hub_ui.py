import tkinter as tk
from api_format.hub_format_weather import FormatWeather
from api_format.hub_format_news import FormatNews
from api_format.hub_format_attractions import FormatAttractions
from api_format.hub_format_currency import FormatCurrency
from logic.hub_logic import HubLogic
class HubUI:
    """ Class is responsible for initializing and loading the UI of HUB page.

    Atrributes:
        hub_frame: frame where the UI is loaded to
        visual: all visual content and a label for "each content box"
        imports: imports all API format classes for later use
    """        
    def __init__(self,root):
        """ Class is responsible for initializing and loading the UI of HUB page.

        Atrributes:
            hub_frame: frame where the UI is loaded to
            visual: all visual content and a label for "each content box"
            imports: imports all API format classes for later use
        """        
        self.root = root
        self.hub_frame = tk.Label(self.root, bg="lightblue")
        self.destinationbox = tk.Label(self.hub_frame, bg="darkblue")
        self.weather_box = tk.Label(self.hub_frame, bg="darkblue")
        self.news_box = tk.Label(self.hub_frame, bg="darkblue")
        self.currency_box = tk.Label(self.hub_frame, bg="darkblue")
        self.currency_bg = tk.Label(self.currency_box,bg="lightblue")
        self.currency_scale = tk.Scale(self.currency_bg, bg="#7EDCFF",
         from_=0,to=500,tickinterval=50,length=500,orient="horizontal",command=self.get_val)
        self.scale_text = tk.Label(self.currency_scale,bg="#7EDCFF",
         text="Try a different amount!",font=("helvetica",15))
        self.attractions_box = tk.Label(self.hub_frame,bg="darkblue")
        
        self.hub_logic = HubLogic()
        self.format_weather = FormatWeather()
        self.format_news = FormatNews()
        self.format_attractions = FormatAttractions()
        self.format_currency = FormatCurrency(self.currency_box)    
    
    def get_val(self,val):
        """ Function that gets slider value from currency_scale slider, used for self.get_currency

        Returns: value
        """
        self.amount2 = int(val)

    def load_back(self,root):
        """ Function that loads the home UI back, launched by pressing the "return" button.

        """
        from ui.home_ui import HomeUI
        home_ui = HomeUI(root)
        home_ui.place_home_ui()

    def setup_currency(self,country):
        """ Calls hub_logic and gets the currency code of target country,
        after getting currency code, calls check_currency() to see if new API call is needed for exchange rates.
        After checking if API call is needed, calls self.get_currency()

        Args:
            country

        Returns:
            country (str): country name
            currency_name (str): name of currency
            currency_code (str): currency code
        """
        setup_currency_return = self.hub_logic.setup_currency_code(country)
        self.country = setup_currency_return[0]
        self.currency_name = setup_currency_return[1]
        self.currency_code = setup_currency_return[2]
        self.hub_logic.check_currency()
        self.get_currency(10,self.country,self.currency_name,self.currency_code)
    
    def get_currency(self,amount,country,currency_name,currency_code):
        """ Calls hub logic get.currency() and with the return calls api_format.format_currency()

        Args:
            amount (int): amount of money to be exchanged
            country (str): country name
            currency_name (str): name of currency
            currency_code (str): currency code
        """
        get_currency_return = self.hub_logic.get_currency(amount,country,currency_name,currency_code)
        amount = get_currency_return[2]
        ratesum = get_currency_return[3]
        self.format_currency.format_all(country,currency_name,amount,ratesum)

    def load_hub_ui(self,lat,lon,city,country):
        """ Loads the hub ui and makes hub logic calls to get information for the hub page

        Args:
            lat (float): latitude of city
            lon (float): longitude of city
            city (str): city name
            country (str): country name
        """
        self.hub_frame.place(relheight=1,relwidth=1,relx=0,rely=0)
        self.currency_bg.place(relx=0,rely=0,relheight=1,relwidth=1)
        self.currency_scale.place(relx=0,rely=0.5,relheight=0.5,relwidth=1)
        self.scale_text.place(relx=0.0125,rely=0.6,relheight=0.3,relwidth=0.3)

        """ Content box for the name of the city on UI
        """
        self.destinationbox.place(relx=0, rely=0, relwidth=0.3, relheight=0.2)
        self.destinationtext = tk.Label(self.destinationbox, text=f"{city}, {country}", font=(
            "helvetica", 24), bg="lightblue")
        self.destinationtext.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        """ Return button, which takes you back to homeUI
        """
        return_button = tk.Button(self.destinationbox, text="Return", font="helvetica",
                bg="#7EDCFF", activebackground="lightblue",command=lambda: self.load_back(self.root))
        return_button.place(relx=0, rely=0, relwidth=0.3)
        
        """ Content box for weather, and makes initial weather call to hub_logic, and api_format call for the result
        """
        self.weather_box.place(relx=0.3, rely=0, relwidth=0.7, relheight=0.2)
        weather_return = self.hub_logic.get_weather(lat,lon)
        
        for i in weather_return:
            self.format_weather.form_weather(self.weather_box,weather_return[i][0]['weather'],weather_return[i][0]['weather_min'],weather_return[i][0]['date'],weather_return[i][0]['icon'],i)
        
        """ Content box for news, and makes initial news call to hub_logic, and api_format call for the result
        """
        self.news_box.place(relx=0,rely=0.2,relwidth=0.44,relheight=0.8)
        self.news_header_text = tk.Label(self.news_box,text=f"Latest news from: {city}",font=("helvetica",20),bg="darkblue",fg="white")
        self.news_header_text.place(relx=0,rely=0,relwidth=1,relheight=0.2)
        news_return = self.hub_logic.get_news(city)
        for i in news_return:
            self.format_news.form_news(self.news_box,news_return[i][0]['title'],news_return[i][0]['source'],news_return[i][0]['link'],i)
        
        """ Content box for currency, and makes initial self.setup_currency call 
        """
        self.currency_box.place(relx=0.44,rely=0.2,relheight=0.32,relwidth=0.56)
        self.setup_currency(country)
        currency_button = tk.Button(self.currency_scale,bg="darkblue",
         text="Exchange",font=("helvetica",15),fg="white",
         command=lambda:self.get_currency(self.amount2,
         self.country,self.currency_name,self.currency_code))
        currency_button.place(relx=0.65,rely=0.6,relheight=0.3,relwidth=0.3)
        
        """ Content box for attractions, and makes initial attractions call to hub_logic, and api_format call for the result
        """
        self.attractions_box.place(relx=0.44,rely=0.52,relwidth=0.56,relheight=0.48)
        attractions_title = tk.Label(self.attractions_box,text=f"Popular attractions in the radius of 10km from {city} centre:",font=("helvetica",20),bg="darkblue",fg="white")
        attractions_title.place(relwidth=1,relheight=0.3,relx=0,rely=0)
        attract_return = self.hub_logic.get_attractions(lat,lon,city)
        for i in attract_return:
            self.format_attractions.form_att(self.attractions_box,attract_return[i][0]['name'],attract_return[i][0]['dist'],attract_return[i][0]['tags'],attract_return[i][0]['link'],i)

        
        