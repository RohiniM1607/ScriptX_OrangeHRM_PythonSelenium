from Pages.pim_page import PimPage
from Actions.base_actions import BaseActions


class PimAction:

    def __init__(self, driver):
        self.base = BaseActions(driver)
        self.page = PimPage

    def open_pim_module(self):
        self.base.wait_for_element(self.page.pim_menu)
        self.base.click_element(self.page.pim_menu)

    def open_add_employee(self):
        self.base.click_element(self.page.add_employee_menu)

    def is_pim_page_displayed(self):
        return self.base.is_element_displayed(self.page.pim_page_header)

    def is_success_message_displayed(self):
        return self.base.is_element_displayed(self.page.success_message)

    def add_employee(self, firstname, lastname, empid):
        self.open_pim_module()
        self.open_add_employee()
        self.base.enter_text(self.page.first_name, firstname)
        self.base.enter_text(self.page.last_name, lastname)
        self.base.enter_text(self.page.emp_id, empid)
        self.base.click_element(self.page.submit_button)