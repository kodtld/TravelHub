import tkinter as tk
from urllib.request import urlopen
from PIL import ImageTk

class FormatWeather:
    def form_weather(self,root,weather,weather_min,date,icon,i):
        self.current_box = tk.Label(root, bg="darkblue")
        if i == 0:
            x = 0
        if i == 1:
            x = 0.2
        if i == 2:
            x = 0.4
        if i == 3:
            x = 0.6
        if i == 4:
            x = 0.8
        # Current weather box -------------------------------------------------
        self.current_box.place(relx=x, rely=0, relwidth=0.2, relheight=1)
        current_weather_day_text = tk.Label(
            self.current_box, text=f"Daily average: {weather}°C",
             font=("helvetica", 13), bg="lightblue")
        current_weather_min_text = tk.Label(
            self.current_box, text=f"Daily min.: {weather_min}°C",
             font=("helvetica", 13), bg="lightblue")
        current_date_text = tk.Label(self.current_box, text=f"Date: {date}",
         font=("helvetica", 13), bg="lightblue")
        current_weather_day_text.place(rely=0.55, relheight=0.15, relwidth=1)
        current_weather_min_text.place(rely=0.7, relheight=0.15, relwidth=1)
        current_date_text.place(rely=0.85, relheight=0.15, relwidth=1)

        # Current weather icon
        with urlopen(icon) as current_u:
            current_raw_data = current_u.read()
            current_u.close()
        current_photo = ImageTk.PhotoImage(data=current_raw_data)  # <-----
        current_icon_label = tk.Label(
            self.current_box, image=current_photo, background="lightblue")
        current_icon_label.image = current_photo
        current_icon_label.place(relwidth=1, relheight=0.53)
