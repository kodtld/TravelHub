import requests
from ui.home_ui import HomeUI
from api_format.hub_format_weather import FormatWeather
from api_format.hub_format_news import FormatNews

class HubLogic:
    def __init__(self,root):
        self.root = root

    def get_weather(self,root, lat, lon):
        weather_key = "10ab2060f30ce15d80acaef3490a3c36"
        weather_call = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current,minutely,hourly,alerts&appid={weather_key}&units=metric"
        request_weather = requests.get(weather_call)
        got_weather = request_weather.json()
        format_weather = FormatWeather(root)
        format_weather.format_all(got_weather)

    def get_news(self,root,city):
        news_key = "pub_65366296de188355aee04321d64daafeca16"
        news_call = f"https://newsdata.io/api/1/news?apikey={news_key}&q={city}&language=en&category=top,world"
        request_news = requests.get(news_call)
        got_news = request_news.json()
        format_news = FormatNews(root)
        format_news.format_all(got_news)

    def load_back(self,root):
        home_ui = HomeUI(root)
        home_ui.place_home_ui()
