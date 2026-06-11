import pytest
from Pages.MyInfoLoginPage import MyInfoLoginPage
from Pages.DashBoardPage import DashboardPage
from Pages.MyInfoPage import MyInfoPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestPersonalDetails:

    def test_fill_personal_details(self):
        login_page = MyInfoLoginPage(self.driver)
        login_page.enter_username()
        login_page.enter_password()
        login_page.click_login()

        dashboard = DashboardPage(self.driver)
        dashboard.verify_dashboard_loaded()
        dashboard.navigate_to_my_info()

        my_info = MyInfoPage(self.driver)
        my_info.verify_my_info_loaded()
        my_info.click_personal_details_tab()
        my_info.enter_first_name()
        my_info.enter_middle_name()
        my_info.enter_last_name()
        my_info.enter_other_id()
        my_info.enter_drivers_license()
        my_info.enter_license_expiry()
        my_info.select_nationality()
        my_info.select_marital_status()
        my_info.enter_date_of_birth()
        my_info.select_gender()
        my_info.click_save()
        my_info.verify_save_success()