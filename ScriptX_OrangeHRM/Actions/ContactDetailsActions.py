import os
from Pages.ContactDetailsPage import ContactDetailsPage
from Pages.DashBoardPage import DashBoardPage
from Actions.base_actions import BaseActions
from Utilities.Read_Config import get_config
from Utilities import excel_reader


class ContactDetailsAction:

    def __init__(self, driver):
        self.base      = BaseActions(driver)
        self.page      = ContactDetailsPage()
        self.dashboard = DashBoardPage()
        self.driver    = driver


    def verify_dashboard_loaded(self):
        return self.base.is_element_displayed(self.dashboard.txt_dashboard)

    def navigate_to_my_info(self):
        self.base.click_element(self.dashboard.lnk_my_info)

    def navigate_to_contact_details(self):
        self.base.wait_for_element_invisible(self.page.load_spinner)
        self.base.js_click(self.page.lnk_contact_details)

    def enter_street1(self, street1):
        self.base.clear_and_enter_text(self.page.txt_street1, street1)

    def enter_street2(self, street2):
        self.base.clear_and_enter_text(self.page.txt_street2, street2)

    def enter_city(self, city):
        self.base.clear_and_enter_text(self.page.txt_city, city)

    def enter_state(self, state):
        self.base.clear_and_enter_text(self.page.txt_state, state)

    def enter_zip(self, zip_code):
        self.base.clear_and_enter_text(self.page.txt_zip, zip_code)

    def select_country(self, country):
        self.base.click_element(self.page.drp_country)
        options = self.base.wait_for_element_all(self.page.option_text)
        for option in options:
            if option.text.strip() == country:
                option.click()
                break

    def enter_home_telephone(self, home_telephone):
        self.base.clear_and_enter_text(self.page.txt_home_telephone, home_telephone)

    def enter_mobile(self, mobile):
        self.base.clear_and_enter_text(self.page.txt_mobile, mobile)

    def enter_work_telephone(self, work_telephone):
        self.base.clear_and_enter_text(self.page.txt_work_telephone, work_telephone)

    def enter_work_email(self, work_email):
        self.base.clear_and_enter_text(self.page.txt_work_email, work_email)

    def fill_contact_details(self, street1, street2, city, state,
                              zip_code, country, home_telephone,
                              mobile, work_telephone, work_email):
        self.base.wait_for_element_invisible(self.page.load_spinner)
        self.enter_street1(street1)
        self.enter_street2(street2)
        self.enter_city(city)
        self.enter_state(state)
        self.enter_zip(zip_code)
        self.select_country(country)
        self.enter_home_telephone(home_telephone)
        self.enter_mobile(mobile)
        self.enter_work_telephone(work_telephone)
        self.enter_work_email(work_email)

    def save_and_verify(self):
        self.base.click_element(self.page.btn_save)
        return self.base.is_element_displayed(self.page.msg_success)

    