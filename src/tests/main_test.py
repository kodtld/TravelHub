import unittest
from main import get_GeoCode

class Testget_GeoCode(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_hello_world(self):
        self.assertEqual("Hello world", "Hello world")