import pytest
from Actions.create_user_credentials_action import CreateUserCredentialActions
from Utilities import Excel_Reader
from Actions.login_action import LoginAction
from Utilities.Read_Config import get_config
from Utilities import log_creator
@pytest.mark.usefixtures("setup_and_teardown")
class TestCreateUserCredentials:
    logger = log_creator.log_generator()
    @pytest.mark.parametrize("role, emp_name, status, user_name, password, confirmpassword", Excel_Reader.get_filtered_data("Configurations/TestData.xlsx", "CreateUserCredentials", "AdminCredential"))
    def test_create_admin_user_credentials(self, role, emp_name, status, user_name, password, confirmpassword):
        self.logger.info("Login to the application")
        login_action = LoginAction(self.driver)
        login_action.login_valid(
            get_config("Login Details", "username"),
            get_config("Login Details", "password")
        )
        actions = CreateUserCredentialActions(self.driver)
        actions.click_admin_menu()
        actions.click_add_button()
        assert actions.verify_add_user_page(), "Add User page is not displayed."
        actions.enter_user_credentials(role,emp_name,status,user_name,password,confirmpassword,  handle_duplicate=True)
        actions.click_save_button()
        assert actions.verify_success_message_displayed(), "Success message not displayed."

    @pytest.mark.parametrize("role, emp_name, status, user_name, password, confirmpassword", Excel_Reader.get_filtered_data("Configurations/TestData.xlsx","CreateUserCredentials","EmployeeCredential"))
    def test_create_employee_user_credentials(self, role, emp_name, status, user_name, password, confirmpassword):

        login_action = LoginAction(self.driver)
        login_action.login_valid(
            get_config("Login Details", "username"),
            get_config("Login Details", "password")
        )

        actions = CreateUserCredentialActions(self.driver)
        actions.click_admin_menu()
        actions.click_add_button()

        assert actions.verify_add_user_page()

        actions.enter_user_credentials(role, emp_name, status, user_name, password, confirmpassword, handle_duplicate=True)
        actions.click_save_button()
        assert actions.verify_success_message_displayed()
            

    @pytest.mark.parametrize("role, emp_name, status, user_name, password, confirmpassword", Excel_Reader.get_filtered_data("Configurations/TestData.xlsx", "CreateUserCredentials", "DuplicateUser"))
    def test_duplicate_username_validation(self, role, emp_name, status,user_name, password, confirmpassword):

        login_action = LoginAction(self.driver)
        login_action.login_valid(
            get_config("Login Details", "username"),
            get_config("Login Details", "password")
        )

        actions = CreateUserCredentialActions(self.driver)
        actions.click_admin_menu()
        actions.click_add_button()
        actions.enter_user_credentials(role,emp_name,status,user_name,password,confirmpassword, handle_duplicate=False)
        actions.click_save_button()
        assert actions.verify_duplicate_username_message(), "Duplicate username validation message not displayed."

    @pytest.mark.parametrize("role, emp_name, status, user_name, password, confirmpassword", Excel_Reader.get_filtered_data("Configurations/TestData.xlsx", "CreateUserCredentials", "WithoutMandatoryField"))
    def test_submit_without_mandatory_fields(self, role, emp_name, status, user_name, password, confirmpassword):

        login_action = LoginAction(self.driver)
        login_action.login_valid(
            get_config("Login Details", "username"),
            get_config("Login Details", "password")
        )

        actions = CreateUserCredentialActions(self.driver)
        actions.click_admin_menu()
        actions.click_add_button()

        actions.enter_user_credentials(role, emp_name, status, user_name, password, confirmpassword)

        actions.click_save_button()

        assert actions.verify_required_field_messages(), "Required field validations are not displayed."


    @pytest.mark.parametrize("role, emp_name, status, user_name, password, confirmpassword",Excel_Reader.get_filtered_data("Configurations/TestData.xlsx","CreateUserCredentials","PasswordMismatch"))
    def test_create_user_with_password_mismatch(self,role,emp_name,status,user_name,password,confirmpassword):

        login_action = LoginAction(self.driver)
        login_action.login_valid(
            get_config("Login Details", "username"),
            get_config("Login Details", "password")
        )

        actions = CreateUserCredentialActions(self.driver)

        actions.click_admin_menu()
        actions.click_add_button()

        assert actions.verify_add_user_page(), "Add User page is not displayed."

        actions.enter_user_credentials(role,emp_name,status,user_name,password,confirmpassword,handle_duplicate=True)

        actions.click_save_button()

        assert actions.verify_password_mismatch_message(), "Password mismatch validation message is not displayed."