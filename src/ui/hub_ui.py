import tkinter as tk
class HubUI:
    def __init__(self,root):
        self.root = root
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
        hub_logic.get_weather(self.weather_box,lat,lon)
        # News box ---------------
        self.news_box.place(relx=0,rely=0.2,relwidth=0.44,relheight=0.8)
        self.news_header_text = tk.Label(self.news_box,text=f"Latest news from: {city}",font=("helvetica",20),bg="darkblue",fg="white")
        self.news_header_text.place(relx=0,rely=0,relwidth=1,relheight=0.2)
        hub_logic.get_news(self.news_box,city)
        # Currency box ---------------
        self.currency_box.place(relx=0.44,rely=0.2,relheight=0.32,relwidth=0.56)
        hub_logic.setup_currency_code(self.currency_box,country)
        # Attractions box ---------------
        self.attractions_box.place(relx=0.44,rely=0.52,relwidth=0.56,relheight=0.48)
        attractions_title = tk.Label(self.attractions_box,text=f"Popular attractions in the radius of 10km from {city} centre:",font=("helvetica",20),bg="darkblue",fg="white")
        attractions_title.place(relwidth=1,relheight=0.3,relx=0,rely=0)
        hub_logic.get_attractions(self.attractions_box,lat,lon,city)

        
        