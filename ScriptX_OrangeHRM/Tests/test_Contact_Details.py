import pytest
from Actions.Contact_Details_Actions import ContactDetailsAction
from Actions.login_action import LoginAction
from Utilities.Read_Config import get_config
from Utilities.Excel_Reader  import get_contact_details_data

@pytest.mark.usefixtures("setup_and_teardown")
class TestContactDetails:
    @pytest.mark.parametrize("street1, street2, city, state, zip_code, country, home_telephone, mobile, work_telephone, work_email",
                             get_contact_details_data("ScriptX_OrangeHRM/Configurations/TestData.xlsx", "ContactDetails"))
    def test_fill_contact_details(self, street1, street2, city, state, zip_code, country, home_telephone, mobile, work_telephone, work_email):
        LoginAction(self.driver).login("Renukkka R","RenukkkaR@123")
        actions = ContactDetailsAction(self.driver)
        assert actions.verify_dashboard_loaded(), "Dashboard not loaded."
        actions.navigate_to_my_info()
        actions.navigate_to_contact_details()
        actions.fill_contact_details(street1, street2, city, state, zip_code,country, home_telephone, mobile, work_telephone, work_email)
        assert actions.save_and_verify(), "Save failed — success message not displayed."

    
    def test_add_attachment(self):
        LoginAction(self.driver).login("Renukkka R","RenukkkaR@123")
        actions = ContactDetailsAction(self.driver)
        assert actions.verify_dashboard_loaded(), "Dashboard not loaded."
        actions.navigate_to_my_info()
        actions.navigate_to_contact_details()
        actions.add_attachment()
        assert actions.verify_attachment(), "Attachment upload failed success message not displayed."
