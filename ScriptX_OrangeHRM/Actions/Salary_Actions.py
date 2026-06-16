from Pages.Salary_Page import SalaryDetailsPage
from Pages.DashBoard_Page import DashBoardPage
from Actions.base_actions import BaseActions
from Utilities.Read_Config import get_config
from Utilities.log_creator import log_generator
from Utilities.Excel_Reader import get_data


class SalaryDetailsAction:

    logger = log_generator()

    def __init__(self, driver):
        self.base      = BaseActions(driver)
        self.page      = SalaryDetailsPage()
        self.dashboard = DashBoardPage()
        self.driver    = driver
        self.logger.info("SalaryDetailsAction initialized")

    def verify_dashboard_loaded(self):
        self.logger.info("Verifying dashboard is loaded")
        return self.base.is_element_displayed(self.dashboard.txt_dashboard)

    def navigate_to_my_info(self):
        self.base.click_element(self.dashboard.lnk_my_info)
        self.logger.info("Navigated to My Info")

    def navigate_to_salary(self):
        self.base.wait_for_element_invisible(self.page.load_spinner)
        self.base.js_click(self.page.lnk_salary_details)
        self.logger.info("Navigated to Salary tab")

    def click_add(self):
        self.base.wait_for_element_invisible(self.page.load_spinner)
        self.base.js_click(self.page.btn_add)
        self.logger.info("Add button clicked")

    def enter_salary_component(self, salary_component):
        self.base.scroll_and_enter_text(self.page.txt_salary_component, salary_component)
        self.logger.info(f"Salary component entered: {salary_component}")

    def select_pay_grade(self, pay_grade):
        self.base.click_element(self.page.drp_pay_grade)
        options = self.base.wait_for_element_all(self.page.option_text)
        for option in options:
            if option.text.strip() == pay_grade:
                option.click()
                break
        self.logger.info(f"Pay grade selected: {pay_grade}")

    def select_pay_frequency(self, pay_frequency):
        self.base.click_element(self.page.drp_pay_frequency)
        options = self.base.wait_for_element_all(self.page.option_text)
        for option in options:
            if option.text.strip() == pay_frequency:
                option.click()
                break
        self.logger.info(f"Pay frequency selected: {pay_frequency}")

    def select_currency(self, currency):
        self.base.click_element(self.page.drp_currency)
        options = self.base.wait_for_element_all(self.page.option_text)
        for option in options:
            if option.text.strip() == currency:
                option.click()
                break
        self.logger.info(f"Currency selected: {currency}")

    def enter_amount(self, amount):
        self.base.scroll_and_enter_text(self.page.txt_amount, amount)
        self.logger.info(f"Amount entered: {amount}")

    def enter_comment(self, comment):
        self.base.scroll_and_enter_text(self.page.txt_comment, comment)
        self.logger.info(f"Comment entered: {comment}")

    def fill_salary_details(self, salary_component, pay_grade,
                             pay_frequency, currency, amount, comment):
        self.logger.info("Filling salary details form")
        self.click_add()
        self.enter_salary_component(salary_component)
        self.select_pay_grade(pay_grade)
        self.select_pay_frequency(pay_frequency)
        self.select_currency(currency)
        self.enter_amount(amount)
        self.enter_comment(comment)
        self.logger.info("Salary details form filled successfully")

    def save_and_verify(self):
        self.base.js_click(self.page.btn_save)
        self.logger.info("Save button clicked")
        result = self.base.is_element_displayed(self.page.msg_success)
        self.logger.info(f"Success message displayed: {result}")
        return result