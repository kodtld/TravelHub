import requests
from pathlib import Path
from datetime import datetime
script_location = Path(__file__).absolute().parent
cur_code_location = script_location / 'cur_code_by_a2.txt'
latest_cur_location = script_location / 'latest_cur.txt'

from ui.home_ui import HomeUI
from api_format.hub_format_weather import FormatWeather
from api_format.hub_format_news import FormatNews
from api_format.hub_format_currency import FormatCurrency

class HubLogic:
    def __init__(self,root):
        self.root = root
        self.cur_data = {}
        self.rate_data = {}
        self.full_country_name = ""
        self.alpha_2 = ""
        self.currency_name = ""
        self.currency_code = ""

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

    def get_currency(self,root,amount,country,currency_name,currency_code):
        with open (latest_cur_location,"r") as rate_file:
            for line in rate_file:
                split_line = line.split(',')
                c_code = split_line[0]
                c_rate = split_line[1]
                self.rate_data[c_code] = c_rate
            
            rate = self.rate_data[currency_code]
            rate = float(rate.strip('\n'))
            ratesum = amount*rate
            format_currency = FormatCurrency(root)
            format_currency.format_all(root,country,currency_name,amount,ratesum,currency_code)
            

    def check_currency(self,root,country,currency_name,currency_code):
        current_date = datetime.today().strftime('%d-%m-%Y')
        with open (latest_cur_location,'r') as checkdate:
            latest=checkdate.readline().split(',')
        
        # Check if latest request is from same date -------
            if current_date == latest[1].strip('\n'):
                print("Previous currency data")
                self.get_currency(root,10,country,currency_name,currency_code)
        
        # If latest request is old, get new one --------
            else:
                print("New currency request")
                currency_key = "dec91b528e3e153051ddb55d9c26f488"
                currency_call = f"http://data.fixer.io/api/latest?access_key={currency_key}&base=EUR"
                request_currency = requests.get(currency_call)
                got_currency = request_currency.json()
                with open (latest_cur_location,'w') as w_file:
                    w_file.write(f"Latest_request,{current_date}")
                    w_file.write('\n')
                    for line in got_currency['rates']:
                        code = line
                        rate = got_currency['rates'][line]
                        w_file.write(f"{line},{rate}")
                        w_file.write('\n')
                self.get_currency(root,country,currency_name,currency_code)

    def setup_currency_code(self,root,country):
        with open(cur_code_location,'r') as r_file:
            for line in r_file:
                split_line = line.split(',')
                self.full_country_name = split_line[0]
                self.alpha_2 = split_line[1]
                self.currency_name = split_line[2]
                self.currency_code = split_line[3].strip("\n")
                self.cur_data[self.alpha_2] = [self.full_country_name,self.currency_name,self.currency_code]
        
        valid_country_name = self.cur_data[country][0]
        valid_currency_name = self.cur_data[country][1]
        valid_currency_code = self.cur_data[country][2]
        self.check_currency(root,valid_country_name,valid_currency_name,valid_currency_code)


    def load_back(self,root):
        home_ui = HomeUI(root)
        home_ui.place_home_ui()
