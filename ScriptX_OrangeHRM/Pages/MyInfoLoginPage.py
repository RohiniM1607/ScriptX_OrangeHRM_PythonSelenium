import time
from selenium.webdriver.common.by import By
from Utilities import read_config
from Utilities import logCreator


class LoginPage:
    logger = logCreator.log_generator()
    
    username_field = "//input[@name='username']"
    password_field = "//input[@name='password']"
    login_button   = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver
        self.logger.info("LoginPage: Driver initialized")

    def enter_username(self):
        time.sleep(2)
        val = read_config.get_config("login credentials", "username")
        self.driver.find_element(By.XPATH, self.username_field).clear()
        self.driver.find_element(By.XPATH, self.username_field).send_keys(val)
        self.logger.info("LoginPage: Username entered")

    def enter_password(self):
        time.sleep(1)
        val = read_config.get_config("login credentials", "password")
        self.driver.find_element(By.XPATH, self.password_field).clear()
        self.driver.find_element(By.XPATH, self.password_field).send_keys(val)
        self.logger.info("LoginPage: Password entered")

    def click_login(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.login_button).click()
        self.logger.info("LoginPage: Login button clicked")
