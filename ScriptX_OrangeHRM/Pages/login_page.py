from selenium.webdriver.common.by import By


class LoginPage:

    txt_username = (By.NAME, "username")
    txt_password = (By.NAME, "password")
    btn_login = (By.XPATH, "//button[@type='submit']")

    txt_dashboard = (By.XPATH, "//h6[text()='Dashboard']")
    txt_invalid_credentials = (By.XPATH, "//p[text()='Invalid credentials']")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*self.txt_username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.txt_password).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.btn_login).click()

    def get_dashboard_text(self):
        return self.driver.find_element(*self.txt_dashboard).text

    def get_invalid_message(self):
        return self.driver.find_element(*self.txt_invalid_credentials).text