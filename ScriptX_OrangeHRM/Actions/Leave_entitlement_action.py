from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Pages.Leave_entitlement_page import AddLeaveEntitlementPage
from Actions.base_actions import BaseActions
import Utilities.log_creator


class AddLeaveEntitlementActions:

    def __init__(self, driver):
        self.driver = driver
        self.page = AddLeaveEntitlementPage()
        self.wait = WebDriverWait(driver, 20)
        self.action = ActionChains(self.driver)
        self.baseaction = BaseActions(self.driver)
        self.log = Utilities.log_creator.log_generator()


    # Navigation
    def open_leave_page(self):
        self.baseaction.click_tuple_locator(self.page.leave_menu)
        self.log.info("Clicked Leave menu")
        self.baseaction.click_tuple_locator(self.page.entitlement_menu)
        self.log.info("clicked Add entitlement Menu")
        self.baseaction.click_tuple_locator(self.page.add_entitlement)
        self.log.info("Clicked  Add entitlement sub menu")

    def enter_employee(self, name):
        self.baseaction.enter_text_and_tab(self.page.employee_name,name)
        self.log.info(f"Entering employee name: {name}")
        self.baseaction.wait_for_invisibility(self.page.searching)
        self.log.info("Wait for invisibility of searching text")

    def select_employee_from_list(self, name):
        field = self.wait.until(EC.element_to_be_clickable(self.page.employee_name))
        field.send_keys(name)

        emp_options = self.baseaction.wait_for_all_elements_visible(self.page.employee_options)

        self.log.info(f"Employee suggestion found: {emp_options[0].text}")

        self.baseaction.press_down_and_enter(1)

        self.log.info(f"Selected Employee name: {name}")
        #field.send_keys(Keys.ARROW_DOWN)
        #field.send_keys(Keys.ENTER)

    # Leave Type
    def select_leave_type(self, leave_type):
        self.baseaction.click_tuple_locator(self.page.leave_type)
        self.log.info("Selecting leave type")
        options = self.baseaction.wait_for_all_elements_visible(self.page.leave_type_options)
        for opt in options:
            if opt.text.strip().lower() == leave_type.lower():
                self.log.info(f"Selected leave type is: {opt.text}")
                opt.click()
                break

    def enter_entitlement(self, value):
        self.baseaction.enter_text_and_tab(self.page.entitlement,value)
        self.log.info(f"Entering leave entitlement days {value}")
        
    def save(self):
        self.baseaction.click_tuple_locator(self.page.save_btn)
        self.log.info("Click on save button")

    def confirm_msg(self):
        self.baseaction.click_tuple_locator(self.page.confirm_btn)
        self.log.info("Getting Confirmation message for added leave entitlement")

    # Validations
    def is_required_msg_displayed(self):
        self.log.info("Required message for empty employee name field")
        return self.baseaction.wait_for_element_tuple(self.page.required_msg).is_displayed()
        

    def is_exceed_error_displayed(self):
        self.log.info("Exceed error message for entering exceed leave entitlement days")
        return self.baseaction.wait_for_element_tuple(self.page.exceed_error).is_displayed()
    
    def invalid_empName(self):
        field = self.wait.until(EC.element_to_be_clickable(self.page.employee_name))
        opt = self.baseaction.wait_for_all_elements_visible(self.page.employee_options)
        self.log.info(f"Getting {opt[0].text} for invalid employee name")
        return opt[0].text