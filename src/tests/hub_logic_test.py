import unittest
from logic.hub_logic import HubLogic

class Testget_Weather(unittest.TestCase):

    def test_valid_insert(self):
        assert len(HubLogic.get_weather(self,60.192059,24.945831)) == 5

    def test_invalid_insert(self):
        self.assertEqual(HubLogic.get_weather(self,321,1233132),
                         "None")

class Testget_News(unittest.TestCase):

    def test_valid_insert(self):
        test_case = HubLogic.get_news(self,"Helsinki")
        assert test_case[0][0]['title'] != "Couldn't find more news..."

    def test_invalid_insert(self):
        self.assertEqual(HubLogic.get_news(self,"Xichuan"),
                         {0: [{'title': "Couldn't find more news...", 'source': '', 'link': ''}], 1: [{'title': "Couldn't find more news...", 'source': '', 'link': ''}], 2: [{'title': "Couldn't find more news...", 'source': '', 'link': ''}], 3: 
                         [{'title': "Couldn't find more news...", 'source': '', 'link': ''}]})

class Testall_Currency(unittest.TestCase):
    def setUp(self):
        self.rate_data = {}
        self.cur_data = {}
        
    def test_get_currency(self):
        self.assertEqual(HubLogic.get_currency(self,10,"Finland","Euro","EUR"),
                         ("Finland","Euro",10,10,"EUR"))

    def test_setup_currency(self):
        self.assertEqual(HubLogic.setup_currency_code(self,"FI"),
                    ('Finland', 'Euro', 'EUR'))

class Testget_Attractions(unittest.TestCase):
    def test_valid_insert(self):
        test_case = HubLogic.get_attractions(self,60.192059,24.945831,"Helsinki")
        assert test_case[0][0]['name'] != "Couldn't find an attraction"
        
    def test_invalid_insert(self):
        self.assertEqual(HubLogic.get_attractions(self,31.456781,102.843018,"Xichuan"),
                         {0: [{'name': "Couldn't find an attraction", 'dist': '', 'tags': '', 'link': 'None'}], 1: [{'name': "Couldn't find an attraction", 'dist': '', 'tags': '', 'link': 'None'}], 2: [{'name': "Couldn't find an attraction", 'dist': '', 'tags': '', 'link': 'None'}]})


