from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BaseActions:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 25)

    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        element.click()

    def click_tuple_locator(self, locator_tuple):
        element = self.wait.until(EC.element_to_be_clickable(locator_tuple))
        element.click()

    def enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        element.click()
        element.clear()
        element.send_keys(text)

    def enter_text_and_tab(self, locator_tuple, text):
        element = self.wait.until(EC.element_to_be_clickable(locator_tuple))
        element.click()
        element.clear()
        element.send_keys(text)
        element.send_keys(Keys.TAB)

    def is_element_displayed(self, locator):
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        return element.is_displayed()

    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        return element.text

    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))

    def wait_for_invisibility(self, locator_tuple):
        self.wait.until(EC.invisibility_of_element_located(locator_tuple))

    def wait_for_all_elements_visible(self, locator_tuple):
        return self.wait.until(EC.visibility_of_all_elements_located(locator_tuple))

    def wait_for_element_tuple(self, locator_tuple):
        return self.wait.until(EC.visibility_of_element_located(locator_tuple))

    def press_down_and_enter(self, count):
        active_element = self.driver.switch_to.active_element
        for _ in range(count):
            active_element.send_keys(Keys.ARROW_DOWN)
        active_element.send_keys(Keys.ENTER)