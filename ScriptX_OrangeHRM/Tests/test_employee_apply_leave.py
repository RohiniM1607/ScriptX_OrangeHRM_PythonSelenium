import pytest
from Actions.employee_apply_leave_action import EmployeeApplyLeaveActions
from Actions.login_action import LoginAction
from Utilities.Read_Config import get_config


@pytest.mark.usefixtures("setup_and_teardown")
class TestEmployeeApplyLeave:

    def test_employee_apply_leave(self):
        username   = get_config("employee_leave", "username")
        password   = get_config("employee_leave", "password")
        leave_type = get_config("employee_leave", "leave_type")
        from_date  = get_config("employee_leave", "from_date")
        to_date    = get_config("employee_leave", "to_date")
        comment    = get_config("employee_leave", "comment")

        LoginAction(self.driver).login(username, password)

        actions = EmployeeApplyLeaveActions(self.driver)
        result  = actions.apply_leave(leave_type, from_date)

        assert result, "Leave application success message was not displayed"
        print("Employee leave applied successfully")
       

     
    