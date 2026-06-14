import pytest

from Actions.login_action import LoginAction
from Actions.buzz_action import BuzzAction
from Utilities.Read_Config import get_config


@pytest.mark.usefixtures("setup_and_teardown")
class TestBuzz:

    def test_create_valid_buzz_post(self):
        login = LoginAction(self.driver)
        login.login_valid(
            get_config("Login Details", "username"),
            get_config("Login Details", "password")
        )
        assert login.get_dashboard_text() == "Dashboard"

        buzz = BuzzAction(self.driver)
        buzz.create_post(get_config("Buzz Details", "valid_post"))
        assert buzz.is_success_message_displayed()

    def test_create_invalid_buzz_post(self):
        login = LoginAction(self.driver)
        login.login_valid(
            get_config("Login Details", "username"),
            get_config("Login Details", "password")
        )
        assert login.get_dashboard_text() == "Dashboard"

        buzz = BuzzAction(self.driver)
        buzz.create_invalid_post(get_config("Buzz Details", "invalid_post"))

        # Capture the text of the topmost post in the timeline
        latest_post = buzz.get_latest_post_text()

        # Verification steps: Assert that the post content is NOT empty
        assert latest_post != "", "Error: The latest post text content is completely empty!"
        assert len(latest_post) > 0, "Error: The length of the latest post string is 0!"