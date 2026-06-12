import pytest
from Pages.employee_apply_leave_page import EmployeeApplyLeavePage
from Actions.employee_apply_leave_action import EmployeeApplyLeaveActions
from Actions.create_user_credentials_action import CreateUserCredentialActions
from Actions.login_action import LoginAction

@pytest.mark.usefixtures("setup_and_teardown")

class TestEmployeeApplyLeave():
    
    def test_employee_apply_leave(self):
     LoginAction(self.driver).login("Rajaa","Raja@123!!")
     actions=EmployeeApplyLeaveActions(self.driver)
     result= actions.apply_leave("CAN - Personal","2026-07-07","2026-07-07" ) 
     assert result, "Leave application success message was not displayed"
     print("Employee Leave applied successfully")