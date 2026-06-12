from Pages.login_page import LoginPage
from Actions.base_actions import BaseActions


class LoginAction:

    def __init__(self, driver):
        self.base = BaseActions(driver)
        self.page = LoginPage()

    def login(self, username, password):
        self.base.enter_text(self.page.txt_username, username)
        self.base.enter_text(self.page.txt_password, password)
        self.base.click_element(self.page.btn_login)

    def login_valid(self, username, password):
        self.login(username, password)

    def login_invalid(self, username, password):
        self.login(username, password)

    def login_empty_credentials(self, username, password):
        self.login(username, password)

    def get_dashboard_text(self):
        return self.base.get_text(self.page.txt_dashboard)

    def get_invalid_message(self):
        return self.base.get_text(self.page.txt_invalid_credentials)

    def get_required_message(self):
        return self.base.get_text(self.page.txt_required)