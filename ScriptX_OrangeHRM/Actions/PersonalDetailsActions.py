import os
from Pages.MyInfoPage import MyInfoPage
from Pages.DashBoardPage import DashBoardPage
from Actions.base_actions import BaseActions
from Utilities.Read_Config import get_config


class PersonalDetailsAction:

    def __init__(self, driver):
        self.base      = BaseActions(driver)
        self.page      = MyInfoPage()
        self.dashboard = DashBoardPage()
        self.driver    = driver

    def verify_dashboard_loaded(self):
        return self.base.is_element_displayed(self.dashboard.txt_dashboard)

    def navigate_to_my_info(self):
        self.base.click_element(self.dashboard.lnk_my_info)

    def navigate_to_personal_details(self):
        self.base.wait_for_element_invisible(self.page.load_spinner)
        self.base.js_click(self.page.lnk_personal_details)

    def enter_license_expiry(self, license_expiry):
        self.base.wait_for_element_invisible(self.page.load_spinner)
        self.base.clear_and_enter_text(self.page.txt_license_expiry, license_expiry)

    def select_nationality(self, nationality):
        self.base.click_element(self.page.drp_nationality)
        options = self.base.wait_for_element_all(self.page.option_text)
        for option in options:
            if option.text.strip() == nationality:
                option.click()
                break

    def select_marital_status(self, marital_status):
        self.base.click_element(self.page.drp_marital_status)
        options = self.base.wait_for_element_all(self.page.option_text)
        for option in options:
            if option.text.strip() == marital_status:
                option.click()
                break

    def select_gender(self, gender):
        locator = self.page.rdo_male if gender.lower() == "male" else self.page.rdo_female
        self.base.click_element(locator)

    def select_blood_type(self, blood):
        self.base.click_element(self.page.blood_type)
        options = self.base.wait_for_element_all(self.page.option_text)
        for option in options:
            if option.text.strip() == blood:
                option.click()
                break

    def enter_test_field(self, testfield):
        self.base.clear_and_enter_text(self.page.test_field, testfield)

    def fill_personal_details(self):
        self.enter_license_expiry(get_config("personal details", "license_expiry"))
        self.select_nationality(get_config("personal details", "nationality"))
        self.select_marital_status(get_config("personal details", "marital_status"))
        self.select_gender(get_config("personal details", "gender"))
        self.select_blood_type(get_config("personal details", "blood"))
        self.enter_test_field(get_config("personal details", "testfield"))

    def save_and_verify(self):
        self.base.click_element(self.page.btn_save)
        return self.base.is_element_displayed(self.page.msg_success)

    def save_and_verify1(self):
        self.base.click_element(self.page.btn1_save)
        return self.base.is_element_displayed(self.page.msg1_success)

    def click_add_attachment(self):
        self.base.wait_for_element_invisible(self.page.load_spinner)
        self.base.js_click(self.page.btn_add_attachment)

    def upload_attachment_file(self, file_path):
        self.base.upload_file(self.page.inp_file_upload, file_path)

    def enter_attachment_description(self, description):
        self.base.clear_and_enter_text(self.page.txt_attachment_desc, description)

    def save_attachment(self):
        self.base.js_click(self.page.btn_save_attachment)

    def add_attachment(self):
        self.click_add_attachment()
        self.upload_attachment_file(os.path.abspath(get_config("personal details", "attachment_path")))
        self.enter_attachment_description(get_config("personal details", "attachment_desc"))
        self.save_attachment()

    def verify_attachment(self):
        return self.base.is_element_displayed(self.page.msg_attachment_success)

    def add_invalid_attachment(self):
        self.click_add_attachment()
        self.upload_attachment_file(os.path.abspath(get_config("personal details", "attachment_path1")))
        self.save_attachment()

    def verify_file_attachment(self):
        return self.base.is_element_displayed(self.page.file_size_exceed)