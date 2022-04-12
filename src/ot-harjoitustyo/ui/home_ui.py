import tkinter as tk
from logic.home_logic import HomeLogic


class HomeScreenUI:
    def do_that(self,root):
        get = HomeLogic()
        logo = tk.Label(root, bg="lightblue", font=(
            "helvetica", 64), text="TravelHUB")
        logo.place(relx=0.25, rely=0.15, relheight=0.5, relwidth=0.5)

        # Home Screen Entry
        home_entry = tk.Entry(root, bg="white", font="helvetica", justify=tk.CENTER)
        home_entry.insert(tk.END, "Type in your destination city...")
        home_entry.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.1)

        # Home Screen Button
        take_button = tk.Button(root, bg="#00BAFF", activebackground="#7EDCFF",
                                text="Take me there!",
                                font="helvetica", fg="white", activeforeground="white",
                                command=lambda: get.get_geo_code(home_entry.get()))
        take_button.place(relx=0.3, rely=0.63, relwidth=0.4, relheight=0.1)