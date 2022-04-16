from ui.hub_ui import HubUI
import requests
class HomeLogic:
    def __init__(self,root):
        self.root = root
        self.hub_ui = HubUI(self.root)

    def get_geo_code(self,root,home_entry):
        from ui.home_ui import HomeUI
        home_ui = HomeUI(self.root)
        geo_code_key = "61852ccd0bd110bcfe7799d4c7906048"
        geocode_call = f"http://api.openweathermap.org/geo/1.0/direct?q={home_entry}&appid={geo_code_key}"
        try:
            request_geo = requests.get(geocode_call)
            got_geocode = request_geo.json()
            city_name = got_geocode[0]['name']
            country = got_geocode[0]['country']
            lat = got_geocode[0]['lat']
            lon = got_geocode[0]['lon']
            self.hub_ui.load_hub_ui(lat, lon, city_name,country)
            
        except:
            home_ui.place_valid()


    