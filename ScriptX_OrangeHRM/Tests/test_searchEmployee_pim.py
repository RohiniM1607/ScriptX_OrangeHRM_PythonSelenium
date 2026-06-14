import pytest

from Actions.login_action import LoginAction
from Actions.pim_action import PimAction
from Utilities.Read_Config import get_config
from Utilities.csv_reader import get_data_csv

search_data = get_data_csv("SearchEmployee.csv")


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearchEmployee:

    @pytest.mark.parametrize("employee_name", search_data)
    def test_search_employee(self, employee_name):

        login = LoginAction(self.driver)

        login.login_valid(
            get_config("Login Details", "username"),
            get_config("Login Details", "password")
        )

        assert login.get_dashboard_text() == "Dashboard"

        pim = PimAction(self.driver)

        pim.search_employee(employee_name)

        assert pim.is_employee_found() is True