import pytest
from Utilities.Read_Config import get_config
from Actions.login_action import LoginAction
from Actions.Leave_entitlement_action import AddLeaveEntitlementActions
from Utilities import Excel_Reader


@pytest.mark.usefixtures("setup_and_teardown")
class TestLeaveEntitlement:
    
    @pytest.mark.parametrize("EmployeeName, LeaveType, Entitlement",
            [("Emily Jones","CAN - Personal", "50"),
            ("Employee 1","CAN - Personal", "60")])
    def test_valid_leave_entitlement(self,EmployeeName,LeaveType,Entitlement):

        LoginAction(self.driver).login(
            get_config("Login Details", "username"),
            get_config("Login Details", "password"))

        action = AddLeaveEntitlementActions(self.driver)

        action.open_leave_page()

        action.enter_employee(EmployeeName)
        action.select_employee_from_list(EmployeeName)

        action.select_leave_type(LeaveType)
        action.enter_entitlement(Entitlement)

        action.save()
        action.confirm_msg()


    @pytest.mark.parametrize("LeaveType, Entitlement", Excel_Reader.invalid_AddLeave_data("Configurations/TestData.xlsx", "All Leave"))
    def test_required_validation(self,LeaveType,Entitlement):

        LoginAction(self.driver).login(
            get_config("Login Details", "username"),
            get_config("Login Details", "password"))

        action = AddLeaveEntitlementActions(self.driver)

        action.open_leave_page()

        action.select_leave_type(LeaveType)
        action.enter_entitlement(Entitlement)
        action.save()

        assert action.is_required_msg_displayed()
  
    @pytest.mark.parametrize("EmployeeName, LeaveType, Entitlement", Excel_Reader.exceed_LeaveLimit("Configurations/TestData.xlsx", "All Leave"))
    def test_exceed_validation(self,EmployeeName,LeaveType,Entitlement):

        LoginAction(self.driver).login(
            get_config("Login Details", "username"),
            get_config("Login Details", "password"))

        action = AddLeaveEntitlementActions(self.driver)

        action.open_leave_page()

        action.enter_employee(EmployeeName)
        action.select_employee_from_list(EmployeeName)
        action.select_leave_type(LeaveType)
        action.enter_entitlement(Entitlement)

        assert action.is_exceed_error_displayed()