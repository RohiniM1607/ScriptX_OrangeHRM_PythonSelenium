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

        assert status.lower() == "approved", f"Status is Pending Approval, Leave is not yet approved. Actual status: '{status}'"