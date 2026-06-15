import pytest
from Actions.employee_buzz_action import BuzzActions
from Actions.login_action import LoginAction
from Utilities.Read_Config import get_config
from Utilities import Excel_Reader
from Utilities.log_creator import log_generator


@pytest.mark.usefixtures("setup_and_teardown")
class TestBuzz:

    log = log_generator()

    @pytest.mark.parametrize(
        "post_text",
        [row[0] for row in Excel_Reader.get_buzz_data("Configurations/TestData.xlsx", "BuzzDetails")]
    )
    def test_create_post(self, post_text):
        self.log.info("Starting test: test_create_post")

        username      = get_config("employee_leave", "username")
        password      = get_config("employee_leave", "password")
        expected_name = get_config("employee_leave", "full_name")

        self.log.info(f"Logging in as: {username}")
        LoginAction(self.driver).login(username, password)
        self.log.info("Login successful")

        actions = BuzzActions(self.driver)
        self.log.info("Navigating to Buzz page")
        actions.navigate_to_buzz_page()

        self.log.info(f"Creating post with text: {post_text}")
        actions.create_post(post_text)

        post_user = actions.get_latest_post_username()
        self.log.info(f"Latest post username: {post_user}")

        assert post_user == expected_name, f"Expected username '{expected_name}' but got '{post_user}'"
        self.log.info("Test passed: Post created and username matched successfully")

    @pytest.mark.parametrize(
        "edit_text",
        [row[1] for row in Excel_Reader.get_buzz_data("Configurations/TestData.xlsx", "BuzzDetails")]
    )
    def test_edit_post(self, edit_text):
        self.log.info("Starting test: test_edit_post")

        username = get_config("employee_leave", "username")
        password = get_config("employee_leave", "password")

        self.log.info(f"Logging in as: {username}")
        LoginAction(self.driver).login(username, password)
        self.log.info("Login successful")

        actions = BuzzActions(self.driver)
        self.log.info("Navigating to Buzz page")
        actions.navigate_to_buzz_page()

        self.log.info(f"Editing latest post with text: {edit_text}")
        actions.edit_latest_post(edit_text)

        actual_text = actions.get_latest_post_text()
        self.log.info(f"Post text after edit: {actual_text}")

        assert actual_text == edit_text, f"Post text not updated. Expected: '{edit_text}' but got: '{actual_text}'"
        self.log.info("Test passed: Post edited and text matched successfully")