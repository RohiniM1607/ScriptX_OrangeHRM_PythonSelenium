import os
import time
from selenium.webdriver.common.keys import Keys

from Pages.MyInfo_Page import MyInfoPage
from Pages.DashBoard_Page import DashBoardPage
from Actions.base_actions import BaseActions
from Utilities.Read_Config import get_config
from Utilities.log_creator import log_generator


class PersonalDetailsAction:

    logger = log_generator()

    def __init__(self, driver):
        self.base      = BaseActions(driver)
        self.page      = MyInfoPage()
        self.dashboard = DashBoardPage()
        self.driver    = driver
        self.logger.info("PersonalDetailsAction initialized")

    def verify_dashboard_loaded(self):
        self.logger.info("Verifying dashboard is loaded")
        return self.base.is_element_displayed(self.dashboard.txt_dashboard)

    def navigate_to_my_info(self):
        self.base.click_element(self.dashboard.lnk_my_info)
        self.logger.info("Navigated to My Info")

    def navigate_to_personal_details(self):
        self.base.wait_for_element_invisible(self.page.load_spinner)
        self.base.js_click(self.page.lnk_personal_details)
        self.logger.info("Navigated to Personal Details tab")

    def enter_license_expiry(self, license_expiry):
        self.base.wait_for_element_invisible(self.page.load_spinner)
        self.base.clear_and_enter_text(self.page.txt_license_expiry, license_expiry)
        try:
            self.base.send_keys(self.page.txt_license_expiry, Keys.ESCAPE)
        except:
            element = self.driver.find_element(*self.page.txt_license_expiry)
            element.send_keys(Keys.ESCAPE)
        self.logger.info(f"License expiry entered: {license_expiry}")

    def select_nationality(self, nationality):
        self.base.click_element(self.page.drp_nationality)
        options = self.base.wait_for_element_all(self.page.option_text)
        for option in options:
            if option.text.strip() == nationality:
                option.click()
                break
        self.logger.info(f"Nationality selected: {nationality}")

    def select_marital_status(self, marital_status):
        self.base.click_element(self.page.drp_marital_status)
        options = self.base.wait_for_element_all(self.page.option_text)
        for option in options:
            if option.text.strip() == marital_status:
                option.click()
                break
        self.logger.info(f"Marital status selected: {marital_status}")

    def select_gender(self, gender):
        locator = self.page.rdo_male if gender.lower() == "male" else self.page.rdo_female
        self.base.click_element(locator)
        self.logger.info(f"Gender selected: {gender}")

    def select_blood_type(self, blood):
        self.base.click_element(self.page.blood_type)
        options = self.base.wait_for_element_all(self.page.option_text)
        for option in options:
            if option.text.strip() == blood:
                option.click()
                break
        self.logger.info(f"Blood type selected: {blood}")

    def enter_test_field(self, testfield):
        self.base.clear_and_enter_text(self.page.test_field, testfield)
        self.logger.info(f"Test field entered: {testfield}")

    def fill_personal_details(self):
        self.logger.info("Filling personal details form")
        self.enter_license_expiry(get_config("personal details", "license_expiry"))
        self.select_nationality(get_config("personal details", "nationality"))
        self.select_marital_status(get_config("personal details", "marital_status"))
        self.select_gender(get_config("personal details", "gender"))
        self.select_blood_type(get_config("personal details", "blood"))
        self.enter_test_field(get_config("personal details", "testfield"))
        self.logger.info("Personal details form filled successfully")

    def save_and_verify(self):
        self.base.click_element(self.page.btn_save)
        self.logger.info("Save button clicked")
        result = self.base.is_element_displayed(self.page.msg_success)
        self.logger.info(f"Success message displayed: {result}")
        return result

    def save_and_verify1(self):
        self.base.click_element(self.page.btn1_save)
        self.logger.info("Save button 1 clicked")
        result = self.base.is_element_displayed(self.page.msg1_success)
        self.logger.info(f"Success message 1 displayed: {result}")
        return result

    def click_add_attachment(self):
        self.base.wait_for_element_invisible(self.page.load_spinner)
        self.base.js_click(self.page.btn_add_attachment)
        self.logger.info("Add attachment button clicked")

    def upload_attachment_file(self, file_path):
        self.base.upload_file(self.page.inp_file_upload, file_path)
        self.logger.info(f"File uploaded: {file_path}")

    def enter_attachment_description(self, description):
        self.base.clear_and_enter_text(self.page.txt_attachment_desc, description)
        self.logger.info(f"Attachment description entered: {description}")

    def save_attachment(self):
        self.base.js_click(self.page.btn_save_attachment)
        self.logger.info("Attachment save button clicked")

    def add_attachment(self):
        self.logger.info("Starting valid attachment upload")
        self.click_add_attachment()
        self.upload_attachment_file(os.path.abspath(get_config("personal details", "attachment_path")))
        self.enter_attachment_description(get_config("personal details", "attachment_desc"))
        self.save_attachment()
        self.logger.info("Valid attachment upload completed")

    def verify_attachment(self):
        result = self.base.is_element_displayed(self.page.msg_attachment_success)
        self.logger.info(f"Attachment success message displayed: {result}")
        return result

    def add_invalid_attachment(self):
        self.logger.info("Starting invalid attachment upload")
        self.click_add_attachment()
        self.upload_attachment_file(os.path.abspath(get_config("personal details", "attachment_path1")))
        self.save_attachment()
        self.logger.info("Invalid attachment upload completed")

    def verify_file_attachment(self):
        result = self.base.is_element_displayed(self.page.file_size_exceed)
        self.logger.info(f"File size exceed message displayed: {result}")
        return result