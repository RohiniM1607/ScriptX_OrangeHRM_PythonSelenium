import pytest

from Actions.login_action import LoginAction
from Actions.Leave_entitlement_action import AddLeaveEntitlementActions


@pytest.mark.usefixtures("setup_and_teardown")
class TestLeaveEntitlement:

    def test_valid_leave_entitlement(self):

        LoginAction(self.driver).login("Admin","admin123")

        action = AddLeaveEntitlementActions(self.driver)

        action.open_leave_page()

        action.enter_employee("Admin  1")
        action.select_employee_from_list("Admin  1")

        action.select_leave_type("CAN - Vacation")
        action.enter_entitlement("5")

        action.save()
        action.confirm_msg()

    def test_required_validation(self):

        LoginAction(self.driver).login("Admin","admin123")

        action = AddLeaveEntitlementActions(self.driver)

        action.open_leave_page()

        action.select_leave_type("CAN - Vacation")
        action.enter_entitlement("5")
        action.save()

        assert action.is_required_msg_displayed()

    def test_exceed_validation(self):

        LoginAction(self.driver).login("Admin","admin123")

        action = AddLeaveEntitlementActions(self.driver)

        action.open_leave_page()

        action.enter_employee("Admin  1")
        action.select_employee_from_list("Admin  1")
        action.select_leave_type("CAN - Vacation")
        action.enter_entitlement("10001")

        assert action.is_exceed_error_displayed()