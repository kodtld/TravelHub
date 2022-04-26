from logic.home_logic import HomeLogic
import tkinter as tk

class HomeUI:
    def __init__(self,root):
        self.root = root
        self.home_frame = tk.Label(self.root, bg="lightblue")
        home_logic = HomeLogic(self.root)
        self.logo = tk.Label(self.home_frame, bg="lightblue", font=(
            "helvetica", 64), text="TravelHUB")
        self.home_entry = tk.Entry(self.home_frame, bg="white", font="helvetica", justify=tk.CENTER)
        self.take_button = tk.Button(self.home_frame, bg="#00BAFF",
         activebackground="#7EDCFF", text="Take me there!",
         font="helvetica", fg="white", activeforeground="white",
         command=lambda: home_logic.get_geo_code(self.root,self.home_entry.get()))
        self.valid = tk.Label(self.home_frame, text="Please enter a valid destination...",
            font="helvetica", bg="lightblue")

    def place_home_ui(self):
        self.home_frame.place(relheight=1,relwidth=1,relx=0,rely=0)
        self.logo.place(relx=0.25, rely=0.15, relheight=0.5, relwidth=0.5)
        self.home_entry.insert(tk.END, "Type in your destination city...")
        self.home_entry.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.1)
        self.take_button.place(relx=0.3, rely=0.63, relwidth=0.4, relheight=0.1)

    def place_valid(self):
        self.place_home_ui()
        self.valid.place(relx=0.3, rely=0.75, relwidth=0.4, relheight=0.1)
        
        


        