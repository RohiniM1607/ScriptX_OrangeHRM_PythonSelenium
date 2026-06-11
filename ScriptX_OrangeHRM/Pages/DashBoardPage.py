from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashBoardPage:

    txt_dashboard = (By.XPATH, "//h6[text()='Dashboard']")
    lnk_my_info   = (By.XPATH, "//span[text()='My Info']")

    def __init__(self, driver):
        self.driver = driver

    def verify_dashboard_loaded(self):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(self.txt_dashboard))

    def get_dashboard_heading_text(self):
        return self.driver.find_element(*self.txt_dashboard).text

    def navigate_to_my_info(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.lnk_my_info)).click()