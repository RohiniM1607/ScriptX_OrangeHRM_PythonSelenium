import pytest
from Pages.DashBoardPage import DashBoardPage
from Actions.PersonalDetailsActions import PersonalDetailsAction


@pytest.mark.usefixtures("setup_and_teardown")
class TestPersonalDetails:

    def test_fill_personal_details(self):
        dashboard = DashBoardPage(self.driver)
        dashboard.verify_dashboard_loaded()       

        dashboard.navigate_to_my_info()
        personal_details = PersonalDetailsAction(self.driver)
        personal_details.navigate_to_personal_details()

        personal_details.fill_personal_details()

        assert personal_details.save_and_verify(), "Save failed — success toast not displayed"