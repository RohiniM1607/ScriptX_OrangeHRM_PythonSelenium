import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities import logCreator


class DashboardPage:
    logger = logCreator.log_generator()

    dashboard_header  = "//h6[text()='Dashboard']"
    my_info_menu      = "//span[text()='My Info']"

    def __init__(self, driver):
        self.driver = driver
        self.logger.info("DashboardPage: Driver initialized")

    def verify_dashboard_loaded(self):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, self.dashboard_header)))
        header_text = self.driver.find_element(By.XPATH, self.dashboard_header).text
        assert header_text == "Dashboard", f"Expected 'Dashboard', get '{header_text}'"
        self.logger.info("DashboardPage: Dashboard loaded and verified")

    def navigate_to_my_info(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.my_info_menu)))
        self.driver.find_element(By.XPATH, self.my_info_menu).click()
        self.logger.info("DashboardPage: Navigated to My Info page")
