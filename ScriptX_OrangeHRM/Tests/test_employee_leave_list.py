import pytest
from Actions.employee_leave_list_action import EmployeeLeaveListActions
from Actions.login_action import LoginAction
from Utilities.Read_Config import get_config
from Utilities.log_creator import log_generator


@pytest.mark.usefixtures("setup_and_teardown")
class TestEmployeeLeaveList:
    
    log = log_generator()
     
    def test_employee_leave_list_status(self):
        self.log.info("Starting test: test_employee_leave_list_status")

        username   = get_config("employee_leave", "username")
        password   = get_config("employee_leave", "password")
        leave_type = get_config("employee_leave", "leave_type")

        
        LoginAction(self.driver).login(username, password)
        self.log.info("Login successful")

        actions = EmployeeLeaveListActions(self.driver)
        self.log.info(f"Searching leave status for leave type: {leave_type}")
        status = actions.search_leave_and_get_status(leave_type)

        self.log.info(f"Leave Status : {status}")

        assert status == "Scheduled (1.00)", \
            f"Expected status 'Scheduled (1.00)' but got '{status}'"

        self.log.info("Test passed: Leave status verified successfully")


    def test_remaining_leave_balance(self):
        self.log.info("Starting test: test_remaining_leave_balance")

        username   = get_config("employee_leave", "username")
        password   = get_config("employee_leave", "password")
        leave_type = get_config("employee_leave", "leave_type")

        self.log.info(f"Logging in as: {username}")
        LoginAction(self.driver).login(username, password)
        self.log.info("Login successful")

        actions = EmployeeLeaveListActions(self.driver)
        self.log.info(f"Fetching leave balance for leave type: {leave_type}")
        balance_text = actions.get_leave_balance_for_leave_type(leave_type)

        self.log.info(f"Remaining Leave Balance : {balance_text}")

        try:
            balance = float(balance_text)
            assert balance > 0, f"No remaining leave balance. Remaining Leave Balance : {balance_text}"
            self.log.info(
                f"Test passed: Leave balance is available. Remaining Leave Balance : {balance_text}"
            )
        except ValueError:
            self.log.error(f"Unexpected leave balance value found : '{balance_text}'")
            pytest.fail(f"Unexpected leave balance value found : '{balance_text}'")