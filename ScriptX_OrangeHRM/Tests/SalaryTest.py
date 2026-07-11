import pytest
from Actions.Salary_Actions import SalaryDetailsAction
from Actions.login_action import LoginAction
from Utilities.Read_Config import get_config
from Utilities.Excel_Reader import get_data


@pytest.mark.usefixtures("setup_and_teardown")
class TestSalaryDetails:

    @pytest.mark.parametrize(
        "salary_component, pay_grade, pay_frequency, currency, amount, comment",
        get_data("ScriptX_OrangeHRM/Configurations/TestData.xlsx", "SalaryDetails")
    )
    def test_add_salary_details(self, salary_component, pay_grade,
                                 pay_frequency, currency, amount, comment):
        LoginAction(self.driver).login(
            get_config("login credentials", "username"),
            get_config("login credentials", "password")
        )
        actions = SalaryDetailsAction(self.driver)
        assert actions.verify_dashboard_loaded(), "Dashboard not loaded."

        actions.navigate_to_my_info()
        actions.navigate_to_salary()
        actions.fill_salary_details(
            salary_component, pay_grade,
            pay_frequency, currency, amount, comment
        )
        assert actions.save_and_verify(), "Save failed — success message not displayed."