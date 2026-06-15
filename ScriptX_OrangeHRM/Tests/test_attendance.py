import pytest

from Actions.login_action import LoginAction
from Actions.attendance_action import AttendanceAction
from Utilities.Read_Config import get_config

@pytest.mark.jagadeep
@pytest.mark.usefixtures("setup_and_teardown")
class TestAttendance:

    def test_punch_in_out(self):

        login = LoginAction(self.driver)

        login.login_valid(
            get_config("Login Details", "username"),
            get_config("Login Details", "password")
        )

        attendance = AttendanceAction(self.driver)

        attendance.punch_in("Starting work")

        assert attendance.is_punch_out_page_displayed()

        attendance.punch_out("Ending work")

        assert attendance.is_punch_in_page_displayed()
