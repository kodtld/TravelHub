import requests

class HomeLogic:
    """ Class is in charge of logistic operations of the homepage.
    """
    def get_geo_code(self,query):
        """ Function gets the geo code from homeUI user input.
        Args:
        geo_key: API key
        geocode_call: API call

        Returns:
        If API call is succesfull = Dictionary with latitude, longitude, city name, and country.
        If API call is NOT succesfull = "Invalid".
        """

        geo_key = "61852ccd0bd110bcfe7799d4c7906048"
        geocode_call = f"http://api.openweathermap.org/geo/1.0/direct?q={query}&appid={geo_key}"

        request_geo = requests.get(geocode_call)
        got_geocode = request_geo.json()
        try:
            city_name = got_geocode[0]['name']
            country = got_geocode[0]['country']
            lat = got_geocode[0]['lat']
            lon = got_geocode[0]['lon']
            re_dict = {"lat":lat,"lon":lon,"city_name":city_name,"country":country}

        except IndexError:
            re_dict = "Invalid"
        return re_dict
