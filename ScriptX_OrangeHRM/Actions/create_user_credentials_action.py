from Pages.create_user_credentials_page import CreateUserCredentialsPage

class CreateUserCredentialActions:
    def __init__(self, driver):
        self.page = CreateUserCredentialsPage(driver)

    def navigate_to_admin_user_management_page(self):
        self.page.click_admin_menu()

    def click_add_button(self):
        self.page.click_add_button()

    def verify_add_user_page(self):
        self.page.is_add_user_page_displayed()

    def enter_user_credetials(self, role, emp_name, status, username, password, confirm_password):
        self.page.select_user_role_dropdown(role)
        self.page.enter_employee_name(emp_name)
        self.page.select_status_dropdown(status)
        self.page.enter_username(username)
        self.page.enter_password(password)
        self.page.enter_confirm_password(confirm_password)

    def click_save_button(self):
        self.page.click_save_button()

    def verify_success_message_displayed(self):
        self.page.is_success_message_displayed()