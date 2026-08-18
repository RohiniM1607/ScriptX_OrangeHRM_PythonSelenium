from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Pages.jab_categoryPage import JabCategoryPage
from Actions.base_actions import BaseActions
from Pages.homePage import HomePage
import Utilities.log_creator

class JobCategoryAction:
    
    def __init__(self, driver):
        self.driver = driver
        self.jobpage = JabCategoryPage()
        self.homePage = HomePage()
        self.wait = WebDriverWait(driver, 20)
        self.action = ActionChains(self.driver)
        self.baseaction = BaseActions(self.driver)
        self.log = Utilities.log_creator.log_generator()

    def clickMenus(self):
        self.baseaction.click_element(self.homePage.admin_menu)
        self.baseaction.click_element(self.jobpage.job_Menu)
        self.baseaction.click_element(self.jobepage.job_categories)

    def enter_role(self,role):
        self.baseaction.clear_and_enter_text(self.jobpage.input_field,role)

    def clickSave(self):
        self.baseaction.click_element(self.jobpage.save_btn)

    def verifyMessage(self):
        self.baseaction.is_element_displayed(self.jobpage.success_meg)