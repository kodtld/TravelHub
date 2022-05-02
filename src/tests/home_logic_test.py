from logging import root
import unittest
from logic.home_logic import HomeLogic


class Testget_GeoCode(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")
        self.root = root

    def test_invalid_insert(self):
        self.assertEqual(HomeLogic.get_geo_code(self,"adshfiuahsdiufhaiu"),
                         "Invalid")

    def test_valid_insert(self):
        self.assertEqual(HomeLogic.get_geo_code(self,"Helsinki"), {'lat': 60.1674881, 'lon': 24.9427473, 'city_name': 'Helsinki', 'country': 'FI'})
