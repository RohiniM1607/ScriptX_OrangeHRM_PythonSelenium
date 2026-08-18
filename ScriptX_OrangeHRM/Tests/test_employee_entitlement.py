import pytest
from Actions.employee_entitlements_action import EmployeeEntitlementActions
from Utilities.CSV_Reader import CSVReader
from Actions.login_action import LoginAction
from Utilities.Read_Config import get_config

data = CSVReader.get_data(
    "Configurations/TestDataCSV.csv"
)


employee_name_data = [
    row for row in data
    if row["testcase"] == "employee_name"
]

leave_type_data = [
    row for row in data
    if row["testcase"] == "leave_type"
]

leave_period_data = [
    row for row in data
    if row["testcase"] == "leave_period"
]

invalid_employee_data = [
    row for row in data
    if row["testcase"] == "invalid_employee"
]

without_employee_data = [
    row for row in data
    if row["testcase"] == "without_employee"
]

@pytest.mark.usefixtures("setup_and_teardown")
class TestEmployeeEntitlement:

    @pytest.mark.parametrize("test_data", employee_name_data)
    def test_search_by_employee_name(self, test_data):
        login_action = LoginAction(self.driver)
        login_action.login_valid(
            get_config("Login Details", "username"),
            get_config("Login Details", "password")
        )

        actions = EmployeeEntitlementActions(self.driver)
        actions.navigate_to_employee_entitlements()
        actions.search_by_employee_name(test_data["employee_name"])
        assert actions.verify_search_result(), "Search result is not displayed"
        
    @pytest.mark.parametrize("test_data", leave_type_data)
    def test_search_by_leave_type(self, test_data):
        login_action = LoginAction(self.driver)
        login_action.login_valid(
            get_config("Login Details", "username"),
            get_config("Login Details", "password")
        )

        actions = EmployeeEntitlementActions(self.driver)
        actions.navigate_to_employee_entitlements()
        actions.search_by_leave_type(test_data["leave_type"])
        assert actions.verify_search_result(), "Search result is not displayed"
    

    @pytest.mark.parametrize("test_data", leave_period_data)
    def test_search_by_leave_period(self, test_data):
        login_action = LoginAction(self.driver)
        login_action.login_valid(
            get_config("Login Details", "username"),
            get_config("Login Details", "password")
        )

        actions = EmployeeEntitlementActions(self.driver)
        actions.navigate_to_employee_entitlements()
        actions.search_by_leave_period(test_data["leave_period"])
        assert actions.verify_search_result(), "Search result is not displayed"

    @pytest.mark.parametrize("test_data", invalid_employee_data)
    def test_invalid_employee_name(self, test_data):

        login_action = LoginAction(self.driver)
        login_action.login_valid(
            get_config("Login Details", "username"),
            get_config("Login Details", "password")
        )

        actions = EmployeeEntitlementActions(self.driver)
        actions.navigate_to_employee_entitlements()
        actions.search_invalid_employee(test_data["employee_name"],test_data["leave_type"],test_data["leave_period"])
        assert actions.verify_invalid_validation(), "Invalid employee validation is not displayed"
    
        @pytest.mark.parametrize("test_data", without_employee_data)
        def test_without_employee_name(self, test_data):
            login_action = LoginAction(self.driver)
            login_action.login_valid(
                get_config("Login Details", "username"),
                get_config("Login Details", "password")
            )

            actions = EmployeeEntitlementActions(self.driver)
            actions.navigate_to_employee_entitlements()
            actions.search_without_employee_name(test_data["leave_type"],test_data["leave_period"])
            assert actions.verify_required_validation(), "Required validation is not displayed"