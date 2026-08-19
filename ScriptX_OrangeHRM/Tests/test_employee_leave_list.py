import pytest

from Actions.employee_leave_list_action import EmployeeLeaveListActions
from Actions.login_action import LoginAction

from Utilities.Read_Config import get_config
from Utilities.log_creator import log_generator


@pytest.mark.usefixtures("setup_and_teardown")
class TestEmployeeLeaveList:

    log = log_generator()

    # ============================================================
    # TEST 1 - LEAVE LIST STATUS
    # ============================================================

    def test_employee_leave_list_status(self):

        self.log.info(
            "Starting test: test_employee_leave_list_status"
        )

        # --------------------------------------------------------
        # GET CONFIGURATION
        # --------------------------------------------------------

        username = get_config(
            "employee_leave_list",
            "username"
        )

        password = get_config(
            "employee_leave_list",
            "password"
        )

        leave_type = get_config(
            "employee_leave_list",
            "leave_type"
        )

        from_date = get_config(
            "employee_leave_list",
            "from_date"
        )

        to_date = get_config(
            "employee_leave_list",
            "to_date"
        )

        self.log.info(
            f"Username   : {username}"
        )

        self.log.info(
            f"Leave Type : {leave_type}"
        )

        self.log.info(
            f"From Date  : {from_date}"
        )

        self.log.info(
            f"To Date    : {to_date}"
        )

        # --------------------------------------------------------
        # LOGIN
        # --------------------------------------------------------

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

        # --------------------------------------------------------
        # CREATE LEAVE
        # --------------------------------------------------------

        leave_list_actions = EmployeeLeaveListActions(
            self.driver
        )

        self.log.info(
            "Creating leave for Leave List test"
        )

        apply_result = (
            leave_list_actions.apply_leave_for_leave_list(
                leave_type,
                from_date,
                to_date
            )
        )

        assert apply_result, (
            "Leave was not applied successfully"
        )

        self.log.info(
            "Leave applied successfully"
        )

        # --------------------------------------------------------
        # SEARCH LEAVE AND GET STATUS
        # --------------------------------------------------------

        self.log.info(
            "Searching for applied leave"
        )

        status = (
            leave_list_actions.search_leave_and_get_status(
                leave_type
            )
        )

        self.log.info(
            f"Leave status returned: {status}"
        )

        assert status is not None, (
            f"Leave type '{leave_type}' "
            "was not found in Leave List"
        )

        self.log.info(
            "Employee Leave List status test passed"
        )

    # ============================================================
    # TEST 2 - REMAINING LEAVE BALANCE
    # ============================================================

    def test_remaining_leave_balance(self):

        self.log.info(
            "Starting test: test_remaining_leave_balance"
        )

        # --------------------------------------------------------
        # GET CONFIGURATION
        # --------------------------------------------------------

        username = get_config(
            "employee_leave_list",
            "username"
        )

        password = get_config(
            "employee_leave_list",
            "password"
        )

        leave_type = get_config(
            "employee_leave_list",
            "leave_type"
        )

        from_date = get_config(
            "employee_leave_list",
            "from_date"
        )

        to_date = get_config(
            "employee_leave_list",
            "to_date"
        )

        self.log.info(
            f"Username   : {username}"
        )

        self.log.info(
            f"Leave Type : {leave_type}"
        )

        self.log.info(
            f"From Date  : {from_date}"
        )

        self.log.info(
            f"To Date    : {to_date}"
        )

        # --------------------------------------------------------
        # LOGIN
        # --------------------------------------------------------

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

        # --------------------------------------------------------
        # CREATE LEAVE LIST ACTIONS
        # --------------------------------------------------------

        leave_list_actions = EmployeeLeaveListActions(
            self.driver
        )

        # --------------------------------------------------------
        # GET EXISTING LEAVE BALANCE
        # --------------------------------------------------------
        # No leave is applied in this scenario.
        # This test checks the existing leave balance directly.

        self.log.info(
            f"Getting leave balance for: {leave_type}"
        )

        balance = (
            leave_list_actions.get_leave_balance_for_leave_type(
                leave_type
            )
        )

        self.log.info(
            f"Leave balance returned: {balance}"
        )

        assert balance is not None, (
            f"Leave balance for '{leave_type}' "
            "was not found"
        )

        self.log.info(
            "Remaining leave balance test passed"
        )