import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Utilities import read_config
from Utilities import logCreator


class MyInfoPage:
    logger = logCreator.log_generator()

    personal_details_tab    = "//a[text()='Personal Details']"
    first_name_field        = "//input[@name='firstName']"
    middle_name_field       = "//input[@name='middleName']"
    last_name_field         = "//input[@name='lastName']"
    other_id_field          = "(//input[@class='oxd-input oxd-input--active'])[6]"
    drivers_license_field   = "(//input[@class='oxd-input oxd-input--active'])[7]"
    license_expiry_field    = "(//input[@placeholder='yyyy-dd-mm'])[1]"
    nationality_dropdown    = "(//select)[1]"
    marital_status_dropdown = "(//select)[2]"
    dob_field               = "(//input[@placeholder='yyyy-dd-mm'])[2]"
    gender_male_radio       = "//label[contains(.,'Male')]//input[@type='radio']"
    gender_female_radio     = "//label[contains(.,'Female')]//input[@type='radio']"
    save_button             = "(//button[@type='submit'])[1]"
    success_message         = "//div[@class='oxd-toast-content oxd-toast-content--success']"

    def __init__(self, driver):
        self.driver = driver
        self.logger.info("MyInfoPage: Driver initialized")

    def _wait_visible(self, xpath, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def _wait_clickable(self, xpath, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath)))

    def _clear_and_type(self, xpath, value):
        el = self._wait_visible(xpath)
        el.click()
        el.send_keys(Keys.CONTROL + "a")
        el.send_keys(Keys.DELETE)
        el.send_keys(value)

    def _select_by_visible_text(self, xpath, value):
        el = self._wait_visible(xpath)
        Select(el).select_by_visible_text(value)
        self.logger.info(f"MyInfoPage: Selected '{value}' from dropdown")

    def verify_my_info_loaded(self):
        self._wait_visible(self.personal_details_tab)
        self.logger.info("MyInfoPage: My Info page loaded")

    def click_personal_details_tab(self):
        time.sleep(1)
        self._wait_clickable(self.personal_details_tab).click()
        time.sleep(1)
        self.logger.info("MyInfoPage: Personal Details tab clicked")

    def enter_first_name(self):
        val = read_config.get_config("personal details", "first_name")
        self._clear_and_type(self.first_name_field, val)
        self.logger.info(f"MyInfoPage: First name entered as '{val}'")

    def enter_middle_name(self):
        val = read_config.get_config("personal details", "middle_name")
        self._clear_and_type(self.middle_name_field, val)
        self.logger.info(f"MyInfoPage: Middle name entered as '{val}'")

    def enter_last_name(self):
        val = read_config.get_config("personal details", "last_name")
        self._clear_and_type(self.last_name_field, val)
        self.logger.info(f"MyInfoPage: Last name entered as '{val}'")

    def enter_other_id(self):
        val = read_config.get_config("personal details", "other_id")
        self._clear_and_type(self.other_id_field, val)
        self.logger.info(f"MyInfoPage: Other ID entered as '{val}'")

    def enter_drivers_license(self):
        val = read_config.get_config("personal details", "drivers_license")
        self._clear_and_type(self.drivers_license_field, val)
        self.logger.info(f"MyInfoPage: Driver's License entered as '{val}'")

    def enter_license_expiry(self):
        val = read_config.get_config("personal details", "license_expiry")
        self._clear_and_type(self.license_expiry_field, val)
        self.logger.info(f"MyInfoPage: License expiry entered as '{val}'")

    def select_nationality(self):
        val = read_config.get_config("personal details", "nationality")
        self._select_by_visible_text(self.nationality_dropdown, val)
        self.logger.info(f"MyInfoPage: Nationality set to '{val}'")

    def select_marital_status(self):
        val = read_config.get_config("personal details", "marital_status")
        self._select_by_visible_text(self.marital_status_dropdown, val)
        self.logger.info(f"MyInfoPage: Marital status set to '{val}'")

    def enter_date_of_birth(self):
        val = read_config.get_config("personal details", "date_of_birth")
        self._clear_and_type(self.dob_field, val)
        self.logger.info(f"MyInfoPage: Date of birth entered as '{val}'")

    def select_gender(self):
        val = read_config.get_config("personal details", "gender")
        if val.lower() == "male":
            self._wait_clickable(self.gender_male_radio).click()
        else:
            self._wait_clickable(self.gender_female_radio).click()
        self.logger.info(f"MyInfoPage: Gender selected as '{val}'")

    def click_save(self):
        time.sleep(1)
        self._wait_clickable(self.save_button).click()
        self.logger.info("MyInfoPage: Save button clicked")

    def verify_save_success(self):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, self.success_message))
        )
        self.logger.info("MyInfoPage: Save success message verified")
        assert True, "Personal details saved successfully"