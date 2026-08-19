import pytest

from Actions.employee_apply_leave_action import EmployeeApplyLeaveActions
from Actions.login_action import LoginAction
from Utilities.Read_Config import get_config
from Utilities.log_creator import log_generator


@pytest.mark.usefixtures("setup_and_teardown")
class TestEmployeeApplyLeave:

    log = log_generator()

    # ============================================================
    # Valid Leave Application
    # ============================================================

    def test_employee_apply_leave(self):

        self.log.info(
            "Starting test: test_employee_apply_leave"
        )

        username = get_config(
            "employee_leave",
            "username"
        )

        password = get_config(
            "employee_leave",
            "password"
        )

        leave_type = get_config(
            "employee_leave",
            "leave_type"
        )

        from_date = get_config(
            "employee_leave",
            "from_date"
        )

        to_date = get_config(
            "employee_leave",
            "to_date"
        )

        comment = get_config(
            "employee_leave",
            "comment"
        )

        self.log.info(
            f"Logging in as: {username}"
        )

        LoginAction(self.driver).login(
            username,
            password
        )

        self.log.info(
            "Login successful"
        )

        actions = EmployeeApplyLeaveActions(
            self.driver
        )

        self.log.info(
            f"Applying leave | "
            f"Type: {leave_type} | "
            f"From: {from_date} | "
            f"To: {to_date}"
        )

        result = actions.apply_leave(
            leave_type=leave_type,
            from_date=from_date,
            to_date=to_date,
            comment=comment
        )

        assert result, (
            "Leave application success "
            "message was not displayed"
        )

        self.log.info(
            "Test passed: Employee leave "
            "applied successfully"
        )

    # ============================================================
    # Leave Type Required Validation
    # ============================================================

    def test_apply_leave_without_leave_type(self):

        self.log.info(
            "Starting test: "
            "test_apply_leave_without_leave_type"
        )

        username = get_config(
            "employee_leave",
            "username"
        )

        password = get_config(
            "employee_leave",
            "password"
        )

        from_date = get_config(
            "employee_leave",
            "from_date"
        )

        to_date = get_config(
            "employee_leave",
            "to_date"
        )

        self.log.info(
            f"Logging in as: {username}"
        )

        LoginAction(self.driver).login(
            username,
            password
        )

        self.log.info(
            "Login successful"
        )

        actions = EmployeeApplyLeaveActions(
            self.driver
        )

        self.log.info(
            "Applying leave without "
            "selecting Leave Type"
        )

        result = actions.apply_leave_without_leave_type(
            from_date=from_date,
            to_date=to_date
        )

        assert result, (
            "Expected 'Required' validation "
            "error under Leave Type was not displayed"
        )

        self.log.info(
            "Test passed: Leave Type "
            "required validation displayed"
        )