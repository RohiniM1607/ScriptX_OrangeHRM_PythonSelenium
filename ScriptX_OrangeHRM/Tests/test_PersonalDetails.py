import pytest
from Actions.PersonalDetailsActions import PersonalDetailsAction
from Actions.login_action import LoginAction
from Utilities.Read_Config import get_config


@pytest.mark.usefixtures("setup_and_teardown")
class TestPersonalDetails:

    def test_fill_personal_details(self):
        LoginAction(self.driver).login("Renukkka R","RenukkkaR@123")
        actions = PersonalDetailsAction(self.driver)
        assert actions.verify_dashboard_loaded(), "Dashboard not loaded."

        actions.navigate_to_my_info()
        actions.navigate_to_personal_details()
        actions.fill_personal_details()
        assert actions.save_and_verify(), "Save failed — success message not displayed."

    def test_add_attachment(self):
        LoginAction(self.driver).login("Renukkka R","RenukkkaR@123")
        actions = PersonalDetailsAction(self.driver)
        assert actions.verify_dashboard_loaded(), "Dashboard not loaded."

        actions.navigate_to_my_info()
        actions.navigate_to_personal_details()
        actions.add_attachment()
        assert actions.verify_attachment(), "Attachment upload failed — success message not displayed."

    def test_add_invalid_attachment(self):
        LoginAction(self.driver).login("Renukkka R","RenukkkaR@123")
        actions = PersonalDetailsAction(self.driver)
        assert actions.verify_dashboard_loaded(), "Dashboard not loaded."

        actions.navigate_to_my_info()
        actions.navigate_to_personal_details()
        actions.add_invalid_attachment()
        assert actions.verify_file_attachment(), "File size error message not displayed."
        