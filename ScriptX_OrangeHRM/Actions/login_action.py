from Pages.login_page import LoginPage


class LoginAction:

    def __init__(self, driver):
        self.login_page = LoginPage(driver)

    def login(self, username, password):

        if username:
            self.login_page.enter_username(username)

        if password:
            self.login_page.enter_password(password)

        self.login_page.click_login()

    def login_with_valid_credentials(self, username, password):
        self.login(username, password)

    def login_with_invalid_credentials(self, username, password):
        self.login(username, password)

    def login_with_empty_username(self, password):
        self.login("", password)

    def login_with_empty_password(self, username):
        self.login(username, "")

    def login_with_empty_credentials(self):
        self.login("", "")