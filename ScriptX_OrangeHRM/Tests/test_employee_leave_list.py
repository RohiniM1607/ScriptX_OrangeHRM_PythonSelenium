import pytest
from Actions.employee_leave_list_action import EmployeeLeaveListActions
from Actions.login_action import LoginAction
from Utilities.Read_Config import get_config


@pytest.mark.usefixtures("setup_and_teardown")
class TestEmployeeLeaveList:

    def test_employee_leave_list_status(self):
        username   = get_config("employee_leave", "username")
        password   = get_config("employee_leave", "password")
        leave_type = get_config("employee_leave", "leave_type")

        LoginAction(self.driver).login(username, password)

        actions = EmployeeLeaveListActions(self.driver)
        status  = actions.search_leave_and_get_status(leave_type)

        print(f"Leave Status : {status}")

        assert status == "Scheduled (1.00)", f"Status is Pending Approval, Leave is not yet approved. Actual status: '{status}'"
        
    def test_search_without_leave_type(self):
        username = get_config("employee_leave", "username")
        password = get_config("employee_leave", "password")
 
        LoginAction(self.driver).login(username, password)
 
        actions      = EmployeeLeaveListActions(self.driver)
        record_text  = actions.search_without_leave_type()
 
        print(f"Record Count Text : {record_text}")
 
        assert "(0)" in record_text, f"Expected 0 records but got: '{record_text}'"
        print("Validation passed: 0 Records found when searched without leave type")
        
    def test_remaining_leave_balance(self):
        username   = get_config("employee_leave", "username")
        password   = get_config("employee_leave", "password")
        leave_type = get_config("employee_leave", "leave_type")
 
        LoginAction(self.driver).login(username, password)
 
        actions       = EmployeeLeaveListActions(self.driver)
        balance_text  = actions.get_leave_balance_for_leave_type(leave_type)
 
        print(f"Remaining Leave Balance : {balance_text}")
 
        try:
            balance = float(balance_text)
            assert balance > 0, f"No remaining leave balance. Remaining Leave Balance : {balance_text}"
            print(f"Leave balance is available. Remaining Leave Balance : {balance_text}")
        except ValueError:
            pytest.fail(f"Unexpected leave balance value found : '{balance_text}'")    