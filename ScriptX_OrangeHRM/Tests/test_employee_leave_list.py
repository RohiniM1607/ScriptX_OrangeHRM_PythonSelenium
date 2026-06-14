import pytest
from Actions.employee_leave_list_action import EmployeeLeaveListActions
from Actions.login_action import LoginAction
from Utilities.Read_Config import get_config
from Utilities.log_creator import log_generator



log = log_generator()
@pytest.mark.usefixtures("setup_and_teardown")
class TestEmployeeLeaveList:

    def test_employee_leave_list_status(self):
        log.info("Starting test: test_employee_leave_list_status")

        username   = get_config("employee_leave", "username")
        password   = get_config("employee_leave", "password")
        leave_type = get_config("employee_leave", "leave_type")

        
        LoginAction(self.driver).login(username, password)
        log.info("Login successful")

        actions = EmployeeLeaveListActions(self.driver)
        log.info(f"Searching leave status for leave type: {leave_type}")
        status  = actions.search_leave_and_get_status(leave_type)

        log.info(f"Leave Status : {status}")

        assert status == "Scheduled (1.00)", f"Status is Pending Approval, Leave is not yet approved. Actual status: '{status}'"
        log.info("Test passed: Leave status verified successfully")

    def test_search_without_leave_type(self):
        log.info("Starting test: test_search_without_leave_type")

        username = get_config("employee_leave", "username")
        password = get_config("employee_leave", "password")

        log.info(f"Logging in as: {username}")
        LoginAction(self.driver).login(username, password)
<<<<<<< Updated upstream
        log.info("Login successful")

        actions     = EmployeeLeaveListActions(self.driver)
        log.info("Searching without selecting leave type")
        record_text = actions.search_without_leave_type()

        log.info(f"Record Count Text : {record_text}")

        assert "No Records Found" in record_text, f"Expected 0 records but got: '{record_text}'"
        log.info("Test passed: No Records Found displayed when searched without leave type")

=======
 
        actions      = EmployeeLeaveListActions(self.driver)
        record_text  = actions.without_applying_leave()
 
        print(f"Record Count Text : {record_text}")
 
        assert " No  Records found" in record_text, f"Expected 0 records but got: '{record_text}'"
        print("Validation passed: 0 Records found when searched without leave type")
        
>>>>>>> Stashed changes
    def test_remaining_leave_balance(self):
        log.info("Starting test: test_remaining_leave_balance")

        username   = get_config("employee_leave", "username")
        password   = get_config("employee_leave", "password")
        leave_type = get_config("employee_leave", "leave_type")

        log.info(f"Logging in as: {username}")
        LoginAction(self.driver).login(username, password)
        log.info("Login successful")

        actions      = EmployeeLeaveListActions(self.driver)
        log.info(f"Fetching leave balance for leave type: {leave_type}")
        balance_text = actions.get_leave_balance_for_leave_type(leave_type)

        log.info(f"Remaining Leave Balance : {balance_text}")

        try:
            balance = float(balance_text)
            assert balance > 0, f"No remaining leave balance. Remaining Leave Balance : {balance_text}"
            log.info(f"Test passed: Leave balance is available. Remaining Leave Balance : {balance_text}")
        except ValueError:
            log.error(f"Unexpected leave balance value found : '{balance_text}'")
            pytest.fail(f"Unexpected leave balance value found : '{balance_text}'")