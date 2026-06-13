from Pages.employee_apply_leave_page import EmployeeApplyLeavePage
from Actions.base_actions import BaseActions
import time

class EmployeeApplyLeaveActions(BaseActions):

    def __init__(self, driver):
        super().__init__(driver)
        self.page = EmployeeApplyLeavePage()

    def navigate_to_apply_leave_page(self):
        self.click_tuple_locator(self.page.leave_menu)
        self.click_tuple_locator(self.page.apply_sub_menu)
        self.wait_for_invisibility(self.page.loader)

    def select_leave_type(self, leave_type_name):
        self.wait_for_invisibility(self.page.loader)
        self.click_tuple_locator(self.page.leave_type_dropdown)

        options = self.wait_for_all_elements_visible(self.page.leave_type_options)

        for opt in options:
            if opt.text.strip().lower() == leave_type_name.lower():
                opt.click()
                break

    def enter_from_date(self, from_date):
        time.sleep(10)
        self.enter_text_and_tab(self.page.from_date_input, from_date)

    def enter_to_date(self, to_date):
        self.enter_text_and_tab(self.page.to_date_input, to_date)

    def enter_comments(self, comment):
        self.enter_text(self.page.comments_input, comment)

    def close_notification(self):
        self.click_tuple_locator(self.page.close_info_notification)

    def apply(self):
        self.click_tuple_locator(self.page.apply_button)

   
 
    def get_success_message_display(self):
     element = self.wait_for_element_presence(self.page.success_msg)
     return element.is_displayed()

    def get_to_date_error(self):
        return self.wait_for_element(self.page.to_date_error)

    def apply_leave(self, leave_type, from_date):
        self.navigate_to_apply_leave_page()
        self.select_leave_type(leave_type)
        self.enter_from_date(from_date)
        # self.enter_from_date(to_date)
        self.apply()
        element = self.wait_for_element_presence(self.page.success_msg)
        return element.is_displayed()
        # return self.get_success_message_display()
    
    def apply_leave_without_leave_type(self, from_date):
     self.navigate_to_apply_leave_page() 
     self.enter_from_date(from_date) 
    #  self.enter_from_date(to_date)    
     self.apply()
     error = self.wait_for_element_tuple(self.page.leave_type_required_error)
     return error.is_displayed()