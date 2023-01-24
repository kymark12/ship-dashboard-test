import requests
from typing import Any

from seleniumbase import BaseCase
from .page_object import Dashboard


class BaseTestCase(BaseCase, Dashboard):
    def setUp(self, **kwargs):
        super().setUp()
        self.open('http://localhost:3000/')
        # <<< Run custom setUp() code for tests AFTER the super().setUp() >>>

    def tearDown(self):
        self.save_teardown_screenshot()  # If test fails, or if "--screenshot"
        if self.has_exception():
            # <<< Run custom code if the test failed. >>>
            pass
        else:
            pass
            # <<< Run custom code if the test passed. >>>
        # (Wrap unreliable tearDown() code in a try/except block.)
        # <<< Run custom tearDown() code BEFORE the super().tearDown() >>>
        super().tearDown()

    @staticmethod
    def remove_first_element(given_list):
        # using del keyword to delete the first index
        del given_list[0]
        # return the result list
        return given_list

    def get_ship_list(self):
        list_of_ships: list[Any] = []
        self.click(self.ship_type)
        ships = self.find_elements('li', by='tag name')
        for ship in ships:
            list_of_ships.append(ship.text)
        list_of_ships = self.remove_first_element(given_list=list_of_ships)
        return list_of_ships

    def select_a_ship(self, ship_name):
        ship_types = self.get_ship_list()
        for ship in ship_types:
            if ship == ship_name:
                self.click(f'li[data-value="{ship}"]')
                break
            else:
                pass

    def custom_search(self, ship, weight, port):
        self.select_a_ship(ship_name=ship)
        self.type(self.weight, weight)
        self.type(self.home_port, port)
        self.click(self.search)

    def get_search_result(self):
        results = []
        first_row = self.find_elements('td', by='tag name')
        for data in first_row:
            results.append(data.text)
        return results

    @staticmethod
    def get_api_response():
        get_dashboard_data = requests.get("http://localhost:4000/ships").json()
        return get_dashboard_data
