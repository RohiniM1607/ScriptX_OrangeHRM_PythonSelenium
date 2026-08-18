import pytest
from Actions.login_action import LoginAction
from Actions.jab_categoryAction import JobCategoryAction
from Utilities.Read_Config import get_config
from Utilities.log_creator import log_generator


log = log_generator()
@pytest.mark.myl
@pytest.mark.jobCategory
@pytest.mark.usefixtures("setup_and_teardown")
class JobCategoryTest:

    def test_add_new_jobCategory(self):
        LoginAction(self.driver).login(
            get_config("Login Details", "username"),
            get_config("Login Details", "password"))
        
        action = JobCategoryAction(self.driver)

        action.clickMenus()
        action.enter_role("role")
        action.clickSave()
        action.verifyMessage()


