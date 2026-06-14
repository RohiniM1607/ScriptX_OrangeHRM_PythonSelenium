import pytest

from Actions.login_action import LoginAction
from Actions.pim_action import PimAction
from Utilities.Read_Config import get_config
from Utilities.Excel_Reader import get_data

test_data = get_data("Configurations/TestData.xlsx", "CreateUser")


@pytest.mark.usefixtures("setup_and_teardown")
class TestPim:

    @pytest.mark.parametrize("firstname, lastname, empid", test_data)
    def test_add_employee(self, firstname, lastname, empid):
        login = LoginAction(self.driver)

        login.login_valid(
            get_config("Login Details", "username"),
            get_config("Login Details", "password")
        )

        assert login.get_dashboard_text() == "Dashboard"

        pim = PimAction(self.driver)

        pim.open_pim_module()
        assert pim.is_pim_page_displayed() is True

        pim.add_employee(firstname, lastname, empid)

        assert pim.is_success_message_displayed() is True