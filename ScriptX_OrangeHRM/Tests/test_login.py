import pytest
from Actions.login_action import LoginAction
from Utilities.Read_Config import get_config


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    def test_valid_login(self):
        action = LoginAction(self.driver)

        action.login_valid(
            get_config("Login Details", "username"),
            get_config("Login Details", "password")
        )

        assert action.get_dashboard_text() == "Dashboard"


    def test_invalid_login(self):
        action = LoginAction(self.driver)

        action.login_invalid(
            get_config("Login Details", "username"),
            get_config("Login Details", "invalid_password")
        )

        assert action.get_invalid_message() == "Invalid credentials"


    def test_empty_credentials(self):
        action = LoginAction(self.driver)

        action.login_empty_credentials(
            get_config("Login Details", "empty_username"),
            get_config("Login Details", "empty_password")
        )

        assert action.get_required_message() == "Required"