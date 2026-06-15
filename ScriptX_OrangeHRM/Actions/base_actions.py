from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BaseActions:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 25)

    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locator))).click()

    def click_tuple_locator(self, locator_tuple):
        element = self.wait.until(EC.element_to_be_clickable(locator_tuple))
        element.click()

    def enter_text(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.clear()
        element.send_keys(text)

    def enter_text_and_tab(self, locator_tuple, text):
        element = self.wait.until(EC.element_to_be_clickable(locator_tuple))
        element.click()     
        element.clear()
        element.send_keys(text)
        #element.send_keys(Keys.TAB)

    def clear_and_enter_text(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        element.click()
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.DELETE)
        element.send_keys(text)

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

    def wait_for_invisibility(self, locator_tuple):
        self.wait.until(EC.invisibility_of_element_located(locator_tuple))

    def wait_for_all_elements_visible(self, locator_tuple):
        return self.wait.until(EC.visibility_of_all_elements_located(locator_tuple))

    def wait_for_element_tuple(self, locator_tuple):
        return self.wait.until(EC.visibility_of_element_located(locator_tuple))
    
    def wait_for_element_all(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located((By.XPATH, locator)))

    def wait_for_element_invisible(self, locator):
        self.wait.until(EC.invisibility_of_element_located((By.XPATH, locator)))

    def js_click(self, locator):
        element = self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def upload_file(self, locator, file_path):
        element = self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        element.send_keys(file_path)

    def press_down_and_enter(self, count):
        active_element = self.driver.switch_to.active_element
        for _ in range(count):
            active_element.send_keys(Keys.ARROW_DOWN)
            active_element.send_keys(Keys.ENTER)
        
    def wait_for_element_presence(self, locator_tuple, timeout=5):
        short_wait = WebDriverWait(self.driver, timeout)
        return short_wait.until(EC.presence_of_element_located(locator_tuple))    