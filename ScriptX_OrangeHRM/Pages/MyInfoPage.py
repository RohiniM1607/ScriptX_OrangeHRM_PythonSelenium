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
    btn_save             = "//button[contains(@class,'oxd-button--secondary') and contains(@class,'orangehrm-left-space')]"
    msg_success          = "//div[@class='oxd-toast-content oxd-toast-content--success']"
    load_spinnner        = "//div[contains(@class,'oxd-loading-spinner-container')]"
    blood_type           = "//label[text()='Blood Type']/following::div[contains(@class,'oxd-select-text')][1]"
    Test_field           = "//label[text()='Test_Field']/following::input[1]"
    btn1_save            = "(//button[normalize-space()='Save'])[1]"
    msg1_success         = "//div[contains(@class,'oxd-toast ')]//p[contains(@class,'oxd-text')]"

    def __init__(self, driver):
        self.driver = driver

    def wait_for_page_load(self):
        WebDriverWait(self.driver, 15).until(EC.invisibility_of_element_located((By.XPATH, self.load_spinnner)))

    def click_personal_details_tab(self):
        el = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.lnk_personal_details)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", el)
        self.driver.execute_script("arguments[0].click();", el)

    def enter_license_expiry(self, license_expiry):
        self.wait_for_page_load()
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
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.msg_success)))
        return self.driver.find_element(By.XPATH, self.msg_success).is_displayed()

    def click_blood_type(self, blood):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.blood_type))).click()
        options = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, self.option_text)))
        for option in options:
            if option.text.strip() == blood:
                option.click()
                break

    def type_blood_field(self, testfield):
        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.Test_field)))
        el.click()
        el.send_keys(Keys.CONTROL + 'a')
        el.send_keys(Keys.DELETE)
        el.send_keys(testfield)

    def click_save1(self):
        self.driver.find_element(By.XPATH, self.btn1_save).click()

    def success_message(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.msg1_success)))
        return self.driver.find_element(By.XPATH, self.msg1_success).is_displayed()