from selenium.webdriver.common.by import By
from Pages.employee_apply_leave_page import EmployeeApplyLeavePage


class EmployeeLeaveListPage(EmployeeApplyLeavePage):

    my_leave_sub_menu      = (By.XPATH, "//a[normalize-space()='My Leave']")

    search_button          = (By.XPATH, "//button[normalize-space()='Search']")

    table_rows             = (By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']")

    leave_type_cell_by_row = "//div[@class='oxd-table-body']//div[@role='row'][{row}]//div[@role='cell'][3]/div"

    status_cell_by_row     = "//div[@class='oxd-table-body']//div[@role='row'][{row}]//div[@role='cell'][6]/div"