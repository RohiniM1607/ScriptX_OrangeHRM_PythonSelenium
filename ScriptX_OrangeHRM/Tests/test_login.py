import pytest
from Actions.login_action import LoginAction
from Pages.login_page import LoginPage
from Utilities.Read_Config import get_config


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    def test_valid_login(self):

        action = LoginAction(self.driver)
        page = LoginPage(self.driver)

        action.login(
            get_config("Login Details", "username"),
            get_config("Login Details", "password")
        )

        actual_result = page.get_dashboard_text()
        expected_result = "Dashboard"

        assert actual_result == expected_result

    def test_invalid_login(self):

        action = LoginAction(self.driver)
        page = LoginPage(self.driver)

        action.login(
            get_config("Login Details", "username"),
            get_config("Login Details", "invalid_password")
        )

        actual_result = page.get_invalid_message()
        expected_result = "Invalid credentials"

        assert actual_result == expected_result