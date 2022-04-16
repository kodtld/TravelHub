import tkinter as tk
import datetime
from urllib.request import urlopen
from PIL import ImageTk

class FormatWeather:
    def __init__(self,root) -> None:
        self.root = root
        self.current_box = tk.Label(self.root, bg="darkblue")
        self.one_box = tk.Label(self.root, bg="darkblue")
        self.two_box = tk.Label(self.root, bg="darkblue")
        self.three_box = tk.Label(self.root, bg="darkblue")
        self.four_box = tk.Label(self.root, bg="darkblue")

    def current_weather(self,got_weather):
        # Current weather box -------------------------------------------------
        self.current_box.place(relx=0, rely=0, relwidth=0.2, relheight=1)
        current_weather_day = got_weather['daily'][0]['temp']['day']
        current_weather_min = got_weather['daily'][0]['temp']['min']
        current_date = datetime.datetime.utcfromtimestamp(
            got_weather['daily'][0]['dt']).strftime('%d-%m')
        current_weather_day_text = tk.Label(
            self.current_box, text=f"Daily average: {current_weather_day}°C",
             font=("helvetica", 13), bg="lightblue")
        current_weather_min_text = tk.Label(
            self.current_box, text=f"Daily min.: {current_weather_min}°C",
             font=("helvetica", 13), bg="lightblue")
        current_date_text = tk.Label(self.current_box, text=f"Date: {current_date}",
         font=("helvetica", 13), bg="lightblue")
        current_weather_day_text.place(rely=0.55, relheight=0.15, relwidth=1)
        current_weather_min_text.place(rely=0.7, relheight=0.15, relwidth=1)
        current_date_text.place(rely=0.85, relheight=0.15, relwidth=1)

        # Current weather icon
        current_icon_for_call = (got_weather['daily'][0]['weather'][0]['icon'])
        current_iconcall = f"http://openweathermap.org/img/wn/{current_icon_for_call}@2x.png"
        with urlopen(current_iconcall) as current_u:
            current_raw_data = current_u.read()
            current_u.close()
        current_photo = ImageTk.PhotoImage(data=current_raw_data)  # <-----
        current_icon_label = tk.Label(
            self.current_box, image=current_photo, background="lightblue")
        current_icon_label.image = current_photo
        current_icon_label.place(relwidth=1, relheight=0.53)

    def one_weather(self,got_weather):
        # One weather box -------------------------------------------------
        self.one_box.place(relx=0.2, rely=0, relwidth=0.2, relheight=1)
        one_weather_day = got_weather['daily'][1]['temp']['day']
        one_weather_min = got_weather['daily'][1]['temp']['min']
        one_date = datetime.datetime.utcfromtimestamp(
            got_weather['daily'][1]['dt']).strftime('%d-%m')
        one_weather_day_text = tk.Label(self.one_box, text=f"Daily average: {one_weather_day}°C", font=(
            "helvetica", 13), bg="lightblue")
        one_weather_min_text = tk.Label(self.one_box, text=f"Daily min.: {one_weather_min}°C", font=(
            "helvetica", 13), bg="lightblue")
        one_date_text = tk.Label(self.one_box, text=f"Date: {one_date}", font=(
            "helvetica", 13), bg="lightblue")
        one_weather_day_text.place(rely=0.55, relheight=0.15, relwidth=1)
        one_weather_min_text.place(rely=0.7, relheight=0.15, relwidth=1)
        one_date_text.place(rely=0.85, relheight=0.15, relwidth=1)

        # Tomorrow weather icon
        one_icon_for_call = (got_weather['daily'][1]['weather'][0]['icon'])
        one_iconcall = f"http://openweathermap.org/img/wn/{one_icon_for_call}@2x.png"
        with urlopen(one_iconcall) as one_u:
            one_raw_data = one_u.read()
            one_u.close()
        one_photo = ImageTk.PhotoImage(data=one_raw_data)  # <-----
        one_icon_label = tk.Label(self.one_box, image=one_photo,
                               background="lightblue")
        one_icon_label.image = one_photo
        one_icon_label.place(relwidth=1, relheight=0.53)

    def two_weather(self,got_weather):
        # Two weather box -------------------------------------------------
        self.two_box.place(relx=0.4, rely=0, relwidth=0.2, relheight=1)
        two_weather_day = got_weather['daily'][2]['temp']['day']
        two_weather_min = got_weather['daily'][2]['temp']['min']
        two_date = datetime.datetime.utcfromtimestamp(
            got_weather['daily'][2]['dt']).strftime('%d-%m')
        two_weather_day_text = tk.Label(self.two_box, text=f"Daily average: {two_weather_day}°C", font=(
            "helvetica", 13), bg="lightblue")
        two_weather_min_text = tk.Label(self.two_box, text=f"Daily min.: {two_weather_min}°C", font=(
            "helvetica", 13), bg="lightblue")
        two_date_text = tk.Label(self.two_box, text=f"Date: {two_date}", font=(
            "helvetica", 13), bg="lightblue")
        two_weather_day_text.place(rely=0.55, relheight=0.15, relwidth=1)
        two_weather_min_text.place(rely=0.7, relheight=0.15, relwidth=1)
        two_date_text.place(rely=0.85, relheight=0.15, relwidth=1)

        # Two weather icon
        two_icon_for_call = (got_weather['daily'][2]['weather'][0]['icon'])
        two_iconcall = f"http://openweathermap.org/img/wn/{two_icon_for_call}@2x.png"
        with urlopen(two_iconcall) as two_u:
            two_raw_data = two_u.read()
            two_u.close()
        two_photo = ImageTk.PhotoImage(data=two_raw_data)  # <-----
        two_icon_label = tk.Label(self.two_box, image=two_photo,
                               background="lightblue")
        two_icon_label.image = two_photo
        two_icon_label.place(relwidth=1, relheight=0.53)

    def three_weather(self,got_weather):
        # Three weather box -------------------------------------------------
        self.three_box.place(relx=0.6, rely=0, relwidth=0.2, relheight=1)
        three_weather_day = got_weather['daily'][3]['temp']['day']
        three_weather_min = got_weather['daily'][3]['temp']['min']
        three_date = datetime.datetime.utcfromtimestamp(
            got_weather['daily'][3]['dt']).strftime('%d-%m')
        three_weather_day_text = tk.Label(
            self.three_box, text=f"Daily average: {three_weather_day}°C",
             font=("helvetica", 13), bg="lightblue")
        three_weather_min_text = tk.Label(
            self.three_box, text=f"Daily min.: {three_weather_min}°C",
             font=("helvetica", 13), bg="lightblue")
        three_date_text = tk.Label(self.three_box, text=f"Date: {three_date}", font=(
            "helvetica", 13), bg="lightblue")
        three_weather_day_text.place(rely=0.55, relheight=0.15, relwidth=1)
        three_weather_min_text.place(rely=0.7, relheight=0.15, relwidth=1)
        three_date_text.place(rely=0.85, relheight=0.15, relwidth=1)

        # Three weather icon
        three_icon_for_call = (got_weather['daily'][3]['weather'][0]['icon'])
        three_iconcall = f"http://openweathermap.org/img/wn/{three_icon_for_call}@2x.png"
        with urlopen(three_iconcall) as three_u:
            three_raw_data = three_u.read()
            three_u.close()
        three_photo = ImageTk.PhotoImage(data=three_raw_data)  # <-----
        three_icon_label = tk.Label(
            self.three_box, image=three_photo, background="lightblue")
        three_icon_label.image = three_photo
        three_icon_label.place(relwidth=1, relheight=0.53)

    def four_weather(self,got_weather):
        # Four weather box -------------------------------------------------
        self.four_box.place(relx=0.8, rely=0, relwidth=0.2, relheight=1)
        four_weather_day = got_weather['daily'][4]['temp']['day']
        four_weather_min = got_weather['daily'][4]['temp']['min']
        four_date = datetime.datetime.utcfromtimestamp(
            got_weather['daily'][4]['dt']).strftime('%d-%m')
        four_weather_day_text = tk.Label(self.four_box,
            text=f"Daily average: {four_weather_day}°C",
            font=("helvetica", 13), bg="lightblue")
        four_weather_min_text = tk.Label(self.four_box, text=f"Daily min.: {four_weather_min}°C",
         font=("helvetica", 13), bg="lightblue")
        four_date_text = tk.Label(self.four_box, text=f"Date: {four_date}",
         font=("helvetica", 13), bg="lightblue")
        four_weather_day_text.place(rely=0.55, relheight=0.15, relwidth=1)
        four_weather_min_text.place(rely=0.7, relheight=0.15, relwidth=1)
        four_date_text.place(rely=0.85, relheight=0.15, relwidth=1)

        # Four weather icon
        four_icon_for_call = (got_weather['daily'][4]['weather'][0]['icon'])
        four_iconcall = f"http://openweathermap.org/img/wn/{four_icon_for_call}@2x.png"
        with urlopen(four_iconcall) as four_u:
            four_raw_data = four_u.read()
            four_u.close()
        four_photo = ImageTk.PhotoImage(data=four_raw_data)  # <-----
        four_icon_label = tk.Label(
            self.four_box, image=four_photo, background="lightblue")
        four_icon_label.image = four_photo
        four_icon_label.place(relwidth=1, relheight=0.53)

    def format_all(self,got_weather):
        self.current_weather(got_weather)
        self.one_weather(got_weather)
        self.two_weather(got_weather)
        self.three_weather(got_weather)
        self.four_weather(got_weather)