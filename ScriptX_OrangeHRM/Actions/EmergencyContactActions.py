from Pages.EmergencyContactPage import EmergencyContactsPage
from Pages.DashBoardPage import DashBoardPage
from Actions.base_actions import BaseActions
from Utilities.Read_Config import get_config
from Utilities.Excel_Reader import get_data


class EmergencyContactsAction:

    def __init__(self, driver):
        self.base      = BaseActions(driver)
        self.page      = EmergencyContactsPage()
        self.dashboard = DashBoardPage()
        self.driver    = driver


    def verify_dashboard_loaded(self):
        return self.base.is_element_displayed(self.dashboard.txt_dashboard)

    def navigate_to_my_info(self):
        self.base.click_element(self.dashboard.lnk_my_info)

    def navigate_to_emergency_contacts(self):
        self.base.wait_for_element_invisible(self.page.load_spinner)
        self.base.js_click(self.page.lnk_emergency_contacts)

    def click_add(self):
        self.base.wait_for_element_invisible(self.page.load_spinner)
        self.base.js_click(self.page.btn_add)

    def enter_name(self, name):
        self.base.clear_and_enter_text(self.page.txt_name, name)

    def enter_relationship(self, relationship):
        self.base.clear_and_enter_text(self.page.txt_relationship, relationship)

    def enter_home_telephone(self, home_telephone):
        self.base.clear_and_enter_text(self.page.txt_home_telephone, home_telephone)

    def enter_mobile(self, mobile):
        self.base.clear_and_enter_text(self.page.txt_mobile, mobile)

    def enter_work_telephone(self, work_telephone):
        self.base.clear_and_enter_text(self.page.txt_work_telephone, work_telephone)

    def fill_emergency_contact(self, name, relationship, home_telephone,
                                mobile, work_telephone):
        self.click_add()
        self.enter_name(name)
        self.enter_relationship(relationship)
        self.enter_home_telephone(home_telephone)
        self.enter_mobile(mobile)
        self.enter_work_telephone(work_telephone)

    def save_and_verify(self):
        self.base.js_click(self.page.btn_save)
        return self.base.is_element_displayed(self.page.msg_success)