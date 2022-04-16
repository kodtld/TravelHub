import tkinter as tk
class HubUI:
    def __init__(self,root):
        self.root = root
        self.hub_frame = tk.Label(self.root, bg="lightblue")
        self.destinationbox = tk.Label(self.hub_frame, bg="darkblue")
        self.weather_box = tk.Label(self.hub_frame, bg="darkblue")
        self.news_box = tk.Label(self.hub_frame, bg="darkblue")
        
    def load_hub_ui(self,lat,lon,city,country):
        self.hub_frame.place(relheight=1,relwidth=1,relx=0,rely=0)
        self.destinationbox.place(relx=0, rely=0, relwidth=0.3, relheight=0.2)
        self.destinationtext = tk.Label(self.destinationbox, text=f"{city}, {country}", font=(
            "helvetica", 24), bg="lightblue")
        self.destinationtext.place(relx=0, rely=0, relwidth=1, relheight=1)

        from logic.hub_logic import HubLogic
        hub_logic = HubLogic(self.hub_frame)
        return_button = tk.Button(self.destinationbox, text="Return", font="helvetica",
                bg="#7EDCFF", activebackground="lightblue",command=lambda: hub_logic.load_back(self.root))
        return_button.place(relx=0, rely=0, relwidth=0.3)

        self.weather_box.place(relx=0.3, rely=0, relwidth=0.7, relheight=0.2)
        hub_logic.get_weather(self.weather_box,lat,lon)

        self.news_box.place(relx=0,rely=0.2,relwidth=0.44,relheight=0.8)
        self.news_header_text = tk.Label(self.news_box,text=f"Latest news from: {city}",font=("helvetica",20),bg="darkblue",fg="white")
        self.news_header_text.place(relx=0,rely=0,relwidth=1,relheight=0.2)
        hub_logic.get_news(self.news_box,city)



        
        