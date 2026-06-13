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
        leave = self.wait.until(EC.element_to_be_clickable(self.page.leave_menu))
        leave.click()

        entitlement = self.wait.until(EC.element_to_be_clickable(self.page.entitlement_menu))
        entitlement.click()

        add_ent = self.wait.until(EC.element_to_be_clickable(self.page.add_entitlement))
        add_ent.click()

    # Employee
    from selenium.webdriver.support import expected_conditions as EC

    def enter_employee(self, name):
        field = self.wait.until(
        EC.element_to_be_clickable(self.page.employee_name))
        field.clear()
        field.send_keys(name)


    # If you have a loading/searching spinner
        self.wait.until(
        EC.invisibility_of_element_located(self.page.searching))


    def select_employee_from_list(self, name):

        field = self.wait.until(EC.element_to_be_clickable(self.page.employee_name))

        field.send_keys(name)

        self.wait.until(EC.visibility_of_all_elements_located(self.page.employee_options))

        self.baseaction.press_down_and_enter(1)
        #field.send_keys(Keys.ARROW_DOWN)
        #field.send_keys(Keys.ENTER)

    # Leave Type
    def select_leave_type(self, leave_type):

        self.wait.until(EC.element_to_be_clickable(self.page.leave_type)).click()

        options = self.wait.until(EC.visibility_of_all_elements_located(self.page.leave_type_options))

        for opt in options:
            if opt.text.strip().lower() == leave_type.lower():
                opt.click()
                break

    # Entitlement
    def enter_entitlement(self, value):
        field = self.wait.until(EC.element_to_be_clickable(self.page.entitlement))
        field.clear()
        field.send_keys(value)

    # Save
    def save(self):
        self.wait.until(EC.element_to_be_clickable(self.page.save_btn)).click()

    def confirm_msg(self):
        self.wait.until(EC.element_to_be_clickable(self.page.confirm_btn) ).click()

    # Validations
    def is_required_msg_displayed(self):
        return self.wait.until(EC.visibility_of_element_located(self.page.required_msg)).is_displayed()

    def is_exceed_error_displayed(self):
        return self.wait.until(EC.visibility_of_element_located(self.page.exceed_error)).is_displayed()
