import tkinter as tk
import datetime
from urllib.request import urlopen
from PIL import ImageTk
import requests



class HomeFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        s_height = 1050
        s_width = 1920
        self.canvas = tk.Canvas(root, height=s_height,
                             width=s_width, bg="lightblue")
        self.canvas.pack()

        # Home Screen "Logo"
        logo = tk.Label(root, bg="lightblue", font=(
            "helvetica", 64), text="TravelHUB")
        logo.place(relx=0.25, rely=0.15, relheight=0.5, relwidth=0.5)

        # Home Screen Entry
        home_entry = tk.Entry(root, bg="white", font="helvetica", justify=tk.CENTER)
        home_entry.insert(tk.END, "Type in your destination city...")
        home_entry.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.1)

        # Home Screen Button
        take_button = tk.Button(root, bg="#00BAFF", activebackground="#7EDCFF", text="Take me there!",
                             font="helvetica", fg="white", activeforeground="white",
                             command=lambda: self.get_geo_code(home_entry.get()))
        take_button.place(relx=0.3, rely=0.63, relwidth=0.4, relheight=0.1)

    def get_geo_code(self, home_entry):

        geo_code_key = "61852ccd0bd110bcfe7799d4c7906048"
        geocode_call = f"http://api.openweathermap.org/geo/1.0/direct?q={home_entry}&appid={geo_code_key}"
        request_geo = requests.get(geocode_call)
        got_geocode = request_geo.json()

        try:
            city_name = got_geocode[0]['name']
            country = got_geocode[0]['country']
            lat = got_geocode[0]['lat']
            lon = got_geocode[0]['lon']
            main_instance = MainFrame()
            main_instance.load(lat, lon, city_name, country)

        except:
            valid = tk.Label(root, text="Please enter a valid destination...",
                          font="helvetica", bg="lightblue")
            valid.place(relx=0.3, rely=0.75, relwidth=0.4, relheight=0.1)


class MainFrame():
    def __init__(self):
        self.main_frame = tk.Frame(root, bg="lightblue")
        self.weather_box = tk.Label(self.main_frame, bg="darkblue")
        self.destinationbox = tk.Label(self.main_frame, bg="darkblue")

    def format_weather(self, got_weather):
        self.weather_box.place(relx=0.3, rely=0, relwidth=0.7, relheight=0.2)

        # Current weather box -------------------------------------------------
        current_box = tk.Label(self.weather_box, bg="darkblue")
        current_box.place(relx=0, rely=0, relwidth=0.2, relheight=1)

        current_weather_day = got_weather['daily'][0]['temp']['day']
        current_weather_min = got_weather['daily'][0]['temp']['min']
        current_date = datetime.datetime.utcfromtimestamp(
            got_weather['daily'][0]['dt']).strftime('%d-%m')

        current_weather_day_text = tk.Label(
            current_box, text=f"Daily average: {current_weather_day}°C", font=("helvetica", 13), bg="lightblue")
        current_weather_min_text = tk.Label(
            current_box, text=f"Daily min.: {current_weather_min}°C", font=("helvetica", 13), bg="lightblue")
        current_date_text = tk.Label(current_box, text=f"Date: {current_date}", font=(
            "helvetica", 13), bg="lightblue")

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
            current_box, image=current_photo, background="lightblue")
        current_icon_label.image = current_photo
        current_icon_label.place(relwidth=1, relheight=0.53)

        # Tomorrow weather box -------------------------------------------------
        one_box = tk.Label(self.weather_box, bg="darkblue")
        one_box.place(relx=0.2, rely=0, relwidth=0.2, relheight=1)

        one_weather_day = got_weather['daily'][1]['temp']['day']
        one_weather_min = got_weather['daily'][1]['temp']['min']
        one_date = datetime.datetime.utcfromtimestamp(
            got_weather['daily'][1]['dt']).strftime('%d-%m')

        one_weather_day_text = tk.Label(one_box, text=f"Daily average: {one_weather_day}°C", font=(
            "helvetica", 13), bg="lightblue")
        one_weather_min_text = tk.Label(one_box, text=f"Daily min.: {one_weather_min}°C", font=(
            "helvetica", 13), bg="lightblue")
        one_date_text = tk.Label(one_box, text=f"Date: {one_date}", font=(
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
        one_icon_label = tk.Label(one_box, image=one_photo,
                               background="lightblue")
        one_icon_label.image = one_photo
        one_icon_label.place(relwidth=1, relheight=0.53)

        # Two day weather box -------------------------------------------------
        two_box = tk.Label(self.weather_box, bg="darkblue")
        two_box.place(relx=0.4, rely=0, relwidth=0.2, relheight=1)

        two_weather_day = got_weather['daily'][2]['temp']['day']
        two_weather_min = got_weather['daily'][2]['temp']['min']
        two_date = datetime.datetime.utcfromtimestamp(
            got_weather['daily'][2]['dt']).strftime('%d-%m')

        two_weather_day_text = tk.Label(two_box, text=f"Daily average: {two_weather_day}°C", font=(
            "helvetica", 13), bg="lightblue")
        two_weather_min_text = tk.Label(two_box, text=f"Daily min.: {two_weather_min}°C", font=(
            "helvetica", 13), bg="lightblue")
        two_date_text = tk.Label(two_box, text=f"Date: {two_date}", font=(
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
        two_icon_label = tk.Label(two_box, image=two_photo,
                               background="lightblue")
        two_icon_label.image = two_photo
        two_icon_label.place(relwidth=1, relheight=0.53)

        # Three day weather box -------------------------------------------------
        three_box = tk.Label(self.weather_box, bg="darkblue")
        three_box.place(relx=0.6, rely=0, relwidth=0.2, relheight=1)

        three_weather_day = got_weather['daily'][3]['temp']['day']
        three_weather_min = got_weather['daily'][3]['temp']['min']
        three_date = datetime.datetime.utcfromtimestamp(
            got_weather['daily'][3]['dt']).strftime('%d-%m')

        three_weather_day_text = tk.Label(
            three_box, text=f"Daily average: {three_weather_day}°C", font=("helvetica", 13), bg="lightblue")
        three_weather_min_text = tk.Label(
            three_box, text=f"Daily min.: {three_weather_min}°C", font=("helvetica", 13), bg="lightblue")
        three_date_text = tk.Label(three_box, text=f"Date: {three_date}", font=(
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
            three_box, image=three_photo, background="lightblue")
        three_icon_label.image = three_photo
        three_icon_label.place(relwidth=1, relheight=0.53)

        # Four day weather box -------------------------------------------------
        four_box = tk.Label(self.weather_box, bg="darkblue")
        four_box.place(relx=0.8, rely=0, relwidth=0.2, relheight=1)

        four_weather_day = got_weather['daily'][4]['temp']['day']
        four_weather_min = got_weather['daily'][4]['temp']['min']
        four_date = datetime.datetime.utcfromtimestamp(
            got_weather['daily'][4]['dt']).strftime('%d-%m')

        four_weather_day_text = tk.Label(four_box, 
            text=f"Daily average: {four_weather_day}°C", 
            font=("helvetica", 13), bg="lightblue")
        four_weather_min_text = tk.Label(four_box, text=f"Daily min.: {four_weather_min}°C", font=(
            "helvetica", 13), bg="lightblue")
        four_date_text = tk.Label(four_box, text=f"Date: {four_date}", font=(
            "helvetica", 13), bg="lightblue")

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
            four_box, image=four_photo, background="lightblue")
        four_icon_label.image = four_photo
        four_icon_label.place(relwidth=1, relheight=0.53)

    def get_weather(self, lat, lon):
        weather_key = "10ab2060f30ce15d80acaef3490a3c36"
        weather_call = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current,minutely,hourly,alerts&appid={weather_key}&units=metric"
        request_weather = requests.get(weather_call)
        got_weather = request_weather.json()
        self.format_weather(got_weather)

    def loadback(self):
        self.main_frame.place_forget()
        HomeFrame(root).pack(side="top", fill="both", expand=True)

    def load(self, lat, lon, city, country):
        self.main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.destinationbox.place(relx=0, rely=0, relwidth=0.3, relheight=0.2)
        destinationtext = tk.Label(self.destinationbox, text=f"{city}, {country}", font=(
            "helvetica", 24), bg="lightblue")
        destinationtext.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.return_button = tk.Button(self.destinationbox, text="Return", font="helvetica",
                             bg="#7EDCFF", activebackground="lightblue",
                             command=lambda: self.loadback())
        self.return_button.place(relx=0, rely=0, relwidth=0.3)

        self.get_weather(lat, lon)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("TravelHUB")
    HomeFrame(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
