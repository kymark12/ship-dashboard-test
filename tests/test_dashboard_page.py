import pytest

from utilities.base_case import BaseTestCase

'''
Test Plan
-------------------------------------------------------------
1. Verify valid and invalid search results
2. Verify the functional integrity of the input UI
3. Validate search result data integrity
4. Verify API response
5. Validate API response vs. front-end search result data
'''


class TestDashboardInputs(BaseTestCase):
    @pytest.mark.order("first")
    def test_select_ship_types(self):
        ship = 'Tug'
        self.select_a_ship(ship_name=ship)
        assert self.assert_text(ship, self.ship_type) is True, "Ship type selected is incorrect/missing"

    @pytest.mark.order('second')
    def test_weight_field(self):
        weight_value = "266712"
        self.type(self.weight, weight_value)
        assert self.assert_text(weight_value, self.weight) is True, "Weight input is missing/incorrect"

    @pytest.mark.order('third')
    def test_home_port_field(self):
        port_value = "Port of Los Angeles"
        self.type(self.home_port, port_value)
        assert self.assert_text(port_value, self.home_port) is True, "Port input is missing/incorrect"

    @pytest.mark.order('fourth')
    def test_default_search_result(self):
        self.click(self.search)
        table_result = self.assert_element_visible(self.results_table)
        assert table_result is True, "Search results are not visible!"
        self.save_screenshot_to_logs(name="Search result all")

    @pytest.mark.order('fifth')
    def test_invalid_search_result(self):
        self.type(self.weight, "random word")
        self.click(self.search)
        invalid_message = self.get_text(self.invalid_search)
        self.deferred_assert_element_present(self.invalid_search)
        self.deferred_assert_text(invalid_message, self.invalid_search)
        self.process_deferred_asserts()
        self.save_screenshot_to_logs(name="Invalid search alert")

    @pytest.mark.order('sixth')
    def test_custom_search_result(self):
        test_data = ['Cargo', '451778', "Port Canaveral"]
        self.select_a_ship(ship_name=test_data[0])
        self.type(self.weight, test_data[1])
        self.type(self.home_port, test_data[2])
        self.click(self.search)
        search_results = self.get_search_result()
        for count in range(0, 3):
            assert search_results[count] == test_data[count], f"Result doesn't match the test data: {test_data[count]}"

    @pytest.mark.order('seventh')
    def test_api_response(self):
        search_result_response = self.get_api_response()
        result_list = search_result_response['result']
        assert result_list is not None, f"API response is empty:\n{result_list}"

    def test_search_result_in_api_response(self):
        self.custom_search(ship="Tug", weight="202302", port="Port of Los Angeles")
        search_results = self.get_search_result()
        api_response = self.get_api_response()
        api_response_result = api_response['result']
        assert any(
            search_results[3] == result['ship_name'] for result in api_response_result
        ), "Ship name is NOT found!"
