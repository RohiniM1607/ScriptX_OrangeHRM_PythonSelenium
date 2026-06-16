from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Pages.Leave_entitlement_page import AddLeaveEntitlementPage
from selenium.webdriver.common.keys import Keys
from Actions.base_actions import BaseActions


class AddLeaveEntitlementActions:

    def __init__(self, driver):
        self.driver = driver
        self.page = AddLeaveEntitlementPage()
        self.wait = WebDriverWait(driver, 20)
        self.action = ActionChains(self.driver)
        self.baseaction = BaseActions(self.driver)


    # Navigation
    def open_leave_page(self):
        self.baseaction.click_tuple_locator(self.page.leave_menu)
        self.baseaction.click_tuple_locator(self.page.entitlement_menu)
        self.baseaction.click_tuple_locator(self.page.add_entitlement)

    def enter_employee(self, name):
        self.baseaction.enter_text_and_tab(self.page.employee_name,name)
        self.baseaction.wait_for_invisibility(self.page.searching)

    def select_employee_from_list(self, name):
        field = self.wait.until(EC.element_to_be_clickable(self.page.employee_name))
        field.send_keys(name)
        self.baseaction.wait_for_all_elements_visible(self.page.employee_options)
        self.baseaction.press_down_and_enter(1)
        #field.send_keys(Keys.ARROW_DOWN)
        #field.send_keys(Keys.ENTER)

    # Leave Type
    def select_leave_type(self, leave_type):
        self.baseaction.click_tuple_locator(self.page.leave_type)
        options = self.baseaction.wait_for_all_elements_visible(self.page.leave_type_options)
        for opt in options:
            if opt.text.strip().lower() == leave_type.lower():
                opt.click()
                break

    def enter_entitlement(self, value):
        self.baseaction.enter_text_and_tab(self.page.entitlement,value)
        
    def save(self):
        self.baseaction.click_tuple_locator(self.page.save_btn)

    def confirm_msg(self):
        self.baseaction.click_tuple_locator(self.page.confirm_btn)

    # Validations
    def is_required_msg_displayed(self):
        return self.baseaction.is_element_displayed(self.page.required_msg)

    def is_exceed_error_displayed(self):
        return self.baseaction.is_element_displayed(self.page.exceed_error)
    
    def invalid_empName(self):
        field = self.wait.until(EC.element_to_be_clickable(self.page.employee_name))
        opt = self.baseaction.wait_for_all_elements_visible(self.page.employee_options)
        return opt[0].text