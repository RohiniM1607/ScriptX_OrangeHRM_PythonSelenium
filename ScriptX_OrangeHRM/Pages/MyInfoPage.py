from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.keys import Keys


class MyInfoPage:

    lnk_personal_details = "//a[text()='Personal Details']"
    txt_license_expiry   = "//label[text()='License Expiry Date']/following::input[1]"
    option_text          = "//div[@role='option']//span"
    drp_nationality      = "//label[text()='Nationality']/following::div[contains(@class,'oxd-select-text')][1]"
    drp_marital_status   = "//label[text()='Marital Status']/following::div[contains(@class,'oxd-select-text')][1]"
    rdo_male             = "//label[normalize-space()='Male']"
    rdo_female           = "//label[normalize-space()='Female']"
    btn_save             = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"
    msg_success          = "//div[@class='oxd-toast-content oxd-toast-content--success']"

    def __init__(self, driver):
        self.driver = driver

    def verify_my_info_loaded(self):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, self.lnk_personal_details)))

    def click_personal_details_tab(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.lnk_personal_details))).click()

    def enter_license_expiry(self, license_expiry):
        el = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.txt_license_expiry)))
        el.click()
        el.send_keys(Keys.CONTROL + 'a')
        el.send_keys(Keys.DELETE)
        el.send_keys(license_expiry)

    def select_nationality(self, nationality): 
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.drp_nationality))).click()
        options = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, self.option_text)))
        for option in options:
            if option.text.strip() == nationality:
                option.click()
                break
    def select_marital_status(self, marital_status):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.drp_marital_status))).click()
        options = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, self.option_text)))
        for option in options:
            if option.text.strip() == marital_status:
                option.click()
                break

    def select_gender(self, gender):
        locator = self.rdo_male if gender.lower() == "male" else self.rdo_female
        self.driver.find_element(By.XPATH, locator).click()

    def click_save(self):
        self.driver.find_element(By.XPATH, self.btn_save).click()

    def verify_save_success(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.msg_success)))
        return self.driver.find_element(By.XPATH, self.msg_success).is_displayed()