import pytest
from Actions.Emergency_Contact_Actions import EmergencyContactsAction
from Actions.login_action import LoginAction
from Utilities.Read_Config import get_config
from Utilities.Excel_Reader import get_data


@pytest.mark.usefixtures("setup_and_teardown")
class TestEmergencyContacts:

    @pytest.mark.parametrize(
        "name, relationship, home_telephone, mobile, work_telephone",
        get_data("ScriptX_OrangeHRM/Configurations/TestData.xlsx", "EmergencyContact")
    )
    def test_add_emergency_contact(self, name, relationship, home_telephone,
                                    mobile, work_telephone):
        LoginAction(self.driver).login("Renukkka R","RenukkkaR@123")
        actions = EmergencyContactsAction(self.driver)
        assert actions.verify_dashboard_loaded(), "Dashboard not loaded."

        actions.navigate_to_my_info()
        actions.navigate_to_emergency_contacts()
        actions.fill_emergency_contact(
            name, relationship, home_telephone, mobile, work_telephone
        )
        assert actions.save_and_verify(), "Save failed success message not displayed."