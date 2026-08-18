from Pages.employee_entitlements_page import EmployeeEntitlementPage
from Actions.base_actions import BaseActions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class EmployeeEntitlementActions:
    def __init__(self, driver):
        self.driver = driver
        self.base = BaseActions(driver)
        self.page = EmployeeEntitlementPage()

    def navigate_to_employee_entitlements(self):
        self.base.click_element(self.page.leave_menu)
        self.base.js_click(self.page.entitlements_menu)
        self.base.js_click(self.page.employee_entitlements_option)
        self.base.wait_for_element(self.page.employee_entitlements_title)

    def enter_employee_name(self, employee_name):
        self.base.clear_text(self.page.employee_name)
        self.base.enter_text(self.page.employee_name, employee_name)

        try:
            self.base.wait_for_element_all(self.page.employee_suggestion)

            ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

        except Exception:
            pass

    def select_leave_type(self, leave_type):
        mapping = {
            "CAN - Bereavement": 1,
            "CAN - FMLA": 2,
            "CAN - Maternity": 3,
            "CAN - Personal": 4,
            "CAN - Vacation": 5
        }

        self.base.click_element(self.page.leave_type)
        self.base.press_down_and_enter(mapping[leave_type])

    def select_leave_period(self, leave_period):
        mapping = {
            "01-01-2020 - 31-12-2020": 1,
            "01-01-2021 - 31-12-2021": 2,
            "01-01-2022 - 31-12-2022": 3,
            "01-01-2023 - 31-12-2023": 4,
            "01-01-2024 - 31-12-2024": 5,
            "01-01-2025 - 31-12-2025": 6,
            "01-01-2026 - 31-12-2026": 7,
            "01-01-2027 - 31-12-2027": 8
        }

        self.base.click_element(self.page.leave_period)

        self.base.press_down_and_enter( mapping[leave_period])

    def click_search(self):
        self.base.js_click(self.page.search_button)

    def search_by_employee_name(self, employee_name):
        self.enter_employee_name(employee_name)
        self.click_search()

    def search_by_leave_type(self, leave_type):
        self.select_leave_type(leave_type)
        self.click_search()

    def search_by_leave_period(self, leave_period):
        self.select_leave_period(leave_period)
        self.click_search()

    def search_invalid_employee(self,employee_name,leave_type,leave_period):
        self.base.clear_text(self.page.employee_name)
        self.base.enter_text(self.page.employee_name,employee_name)
        ActionChains(self.driver).send_keys(Keys.TAB).perform()
        self.base.wait_for_element(self.page.invalid_validation_msg)
        self.select_leave_type(leave_type)
        self.select_leave_period(leave_period)
        self.click_search()

    def search_without_employee_name(self,leave_type,leave_period):
        self.select_leave_type(leave_type)
        self.select_leave_period(leave_period)
        self.click_search()

    def verify_search_result(self):
        return self.base.is_element_displayed(self.page.search_result)

    def verify_invalid_validation(self):
        return self.base.is_element_displayed(self.page.invalid_validation_msg)

    def verify_required_validation(self):
        return self.base.is_element_displayed(self.page.required_validation_msg)