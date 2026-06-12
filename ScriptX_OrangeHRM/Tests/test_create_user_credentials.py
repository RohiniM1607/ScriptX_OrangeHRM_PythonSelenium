import pytest
from Actions.create_user_credentials_action import CreateUserCredentialActions
from Utilities import Excel_Reader
from Actions.login_action import LoginAction
from Utilities.Read_Config import get_config
from Utilities import log_creator
@pytest.mark.usefixtures("setup_and_teardown")
class TestCreateUserCredentials:
    logger = log_creator.log_generator()
    @pytest.mark.parametrize("role, emp_name, status, user_name, password, confirmpassword", Excel_Reader.get_filtered_data("Configurations/TestData.xlsx", "CreateUserCredentials", "Admin"))
    def test_create_admin_user_credentials(self, role, emp_name, status, user_name, password, confirmpassword):
        self.logger.info("Login to the application")
        login_action = LoginAction(self.driver)
        login_action.login_with_valid_credentials(
            get_config("Login Details", "username"),
            get_config("Login Details", "password")
        )
        actions = CreateUserCredentialActions(self.driver)
        actions.click_admin_menu()
        actions.click_add_button()
        assert actions.verify_add_user_page(), "Add User page is not displayed."
        actions.enter_user_credentials(role,emp_name,status,user_name,password,confirmpassword)
        actions.click_save_button()
        assert actions.verify_success_message_displayed(), "Success message not displayed."

    @pytest.mark.parametrize("role, emp_name, status, user_name, password, confirmpassword", Excel_Reader.get_filtered_data("Configurations/TestData.xlsx","CreateUserCredentials","Employee"))
    def test_create_employee_user_credentials(self, role, emp_name, status, user_name, password, confirmpassword):

        login_action = LoginAction(self.driver)
        login_action.login_with_valid_credentials(
            get_config("Login Details", "username"),
            get_config("Login Details", "password")
        )

        actions = CreateUserCredentialActions(self.driver)
        actions.click_admin_menu()
        actions.click_add_button()

        assert actions.verify_add_user_page()

        actions.enter_user_credentials(role, emp_name, status, user_name, password, confirmpassword)
        actions.click_save_button()
        assert actions.verify_success_message_displayed()
            
