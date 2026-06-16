import pytest
from Actions.Profile_Picture_Actions import ProfilePictureAction
from Actions.login_action import LoginAction
from Utilities.Read_Config import get_config


@pytest.mark.usefixtures("setup_and_teardown")
class TestProfilePicture:

    def test_upload_profile_picture(self):
        LoginAction(self.driver).login("Renukkka R", "RenukkkaR@123")
        actions = ProfilePictureAction(self.driver)
        assert actions.verify_dashboard_loaded(), "Dashboard not loaded."
        actions.navigate_to_my_info()
        assert actions.upload_and_verify(), "Profile picture upload failed — success message not displayed."