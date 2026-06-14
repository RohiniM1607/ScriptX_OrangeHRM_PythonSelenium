from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class BaseActions:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        element.click()

    def enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        element.click()
        element.send_keys(text)

    def clear_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        element.clear()
    
    def is_element_displayed(self, locator):
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        return element.is_displayed()
    
    def is_element_present(self, locator):
        try:
            self.driver.find_element(By.XPATH, locator)
            return True
        except:
            return False

    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        return element.text
    
    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
    
    def press_down_and_enter(self, count):
        active_element = self.driver.switch_to.active_element

        for _ in range(count):
            active_element.send_keys(Keys.ARROW_DOWN)
        active_element.send_keys(Keys.ENTER)