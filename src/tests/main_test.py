import unittest
from main import get_GeoCode

class Testget_GeoCode(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_invalid_insert(self):
        self.assertEqual(get_GeoCode("asdiof"),"Please enter valid destination...")
    
    def test_valid_insert(self):
        self.assertEqual(get_GeoCode("London"),"City: London, Latitude: 51.5073219, Longitude: -0.1276474")