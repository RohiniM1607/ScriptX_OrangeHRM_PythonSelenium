from Pages.employee_leave_list_page import EmployeeLeaveListPage
from Actions.employee_apply_leave_action import EmployeeApplyLeaveActions
from Actions.base_actions import BaseActions
from selenium.webdriver.common.by import By



class EmployeeLeaveListActions(BaseActions):

    def __init__(self, driver):
        super().__init__(driver)
        self.page = EmployeeLeaveListPage()
        self._apply_actions = EmployeeApplyLeaveActions(driver)

    def navigate_to_my_leave_page(self):
        self.click_tuple_locator(self.page.leave_menu)
        self.click_tuple_locator(self.page.my_leave_sub_menu)
        self.wait_for_invisibility(self.page.loader)

    def select_leave_type(self, leave_type_name):
        self._apply_actions.select_leave_type(leave_type_name)

    def click_search(self):
        self.click_tuple_locator(self.page.search_button)
        self.wait_for_invisibility(self.page.loader)
      

    def get_total_rows(self):
        rows = self.driver.find_elements(*self.page.table_rows)
        return len(rows)

    def get_status_for_leave_type(self, leave_type_name):
        total_rows = self.get_total_rows()
        for row_index in range(1, total_rows + 1):
            leave_type_el = self.driver.find_element(By.XPATH, self.page.leave_type_cell_by_row.format(row=row_index))
            if leave_type_el.text.strip().lower() == leave_type_name.lower():
                status_el = self.driver.find_element(By.XPATH, self.page.status_cell_by_row.format(row=row_index))
                return status_el.text.strip()

    def search_leave_and_get_status(self, leave_type_name):
        self.navigate_to_my_leave_page()
        self.select_leave_type(leave_type_name)
        self.click_search()
        return self.get_status_for_leave_type(leave_type_name)

    def search_without_leave_type(self):
        self.navigate_to_my_leave_page()
        self.click_search()
        element = self.wait_for_element_tuple(self.page.record_count_text)
        return element.text.strip()

    def get_leave_balance_for_leave_type(self, leave_type_name):
        self.navigate_to_my_leave_page()
        self.select_leave_type(leave_type_name)
        self.click_search()
        total_rows = self.get_total_rows()
        for row_index in range(1, total_rows + 1):
            leave_type_el = self.driver.find_element(By.XPATH, self.page.leave_type_cell_by_row.format(row=row_index))
            if leave_type_el.text.strip().lower() == leave_type_name.lower():
                balance_el = self.driver.find_element(By.XPATH, self.page.leave_balance_cell_by_row.format(row=row_index))
                return balance_el.text.strip()