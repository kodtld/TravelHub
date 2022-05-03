from logic.home_logic import HomeLogic
from ui.hub_ui import HubUI
import tkinter as tk

class HomeUI:
    """ Class is responsible for initializing and loading the UI of homepage.

    Atrributes:
        root: Points to target where UI is to be loaded.
        home_entry: Entry box for user to type the name of destination.
        take_button: A button to call further functionality with the user input.
        self_valid: Label, is loaded if user input is not valid.
    """
    def __init__(self,root):
        """ Class constructor is responsible for initializing the UI of homepage.

        Args:
            root: Points to target where UI is to be loaded.
            home_entry: Entry box for user to type the name of destination.
            take_button: A button to call further functionality with the user input.
            self_valid: Label, is loaded if user input is not valid.
        """
        self.root = root
        self.home_frame = tk.Label(self.root, bg="lightblue")
        self.home_logic = HomeLogic()
        self.hub_ui = HubUI(self.root)
        self.logo = tk.Label(self.home_frame, bg="lightblue", font=(
            "helvetica", 64), text="TravelHUB")
        self.home_entry = tk.Entry(self.home_frame, bg="white", font="helvetica", justify=tk.CENTER)

        self.take_button = tk.Button(self.home_frame, bg="#00BAFF",
         activebackground="#7EDCFF", text="Take me there!",
         font="helvetica", fg="white", activeforeground="white",
         command=self.show_hub_ui)

        self.valid = tk.Label(self.home_frame, text="Please enter a valid destination...",
            font="helvetica", bg="lightblue")

    def show_hub_ui(self):
        """ Checks if user input is valid, by making an API call.
         If valid, loads next page, if invalid, calls place_valid() which shows the user a prompt .

        Args:
            return_dict: Dictionary containing the latitude, longitude, and city name gotten from get_geo_code API call.
            load_hub_ui: Passes on the latitude, longitude, cityname, and loads the next window (named HUB).
            place_valid: calls place_valid() which shows the user a prompt asking for valid input.
        """
        return_dict = self.home_logic.get_geo_code(self.home_entry.get())
        if return_dict != "Invalid":
            self.hub_ui.load_hub_ui(return_dict['lat'],return_dict['lon'],return_dict['city_name'],return_dict['country'])
        
        else:
            self.place_valid()

    def place_home_ui(self):
        """ Places the UI elements initialized in the constructor.

        """
        self.home_frame.place(relheight=1,relwidth=1,relx=0,rely=0)
        self.logo.place(relx=0.25, rely=0.15, relheight=0.5, relwidth=0.5)
        self.home_entry.insert(tk.END,"Type in your destination city...")
        self.home_entry.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.1)
        self.take_button.place(relx=0.3, rely=0.63, relwidth=0.4, relheight=0.1)

    def place_valid(self):
        """ Places the prompt asking user for valid input.
        """
        self.valid.place(relx=0.3, rely=0.75, relwidth=0.4, relheight=0.1)
        
        


        