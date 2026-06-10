from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CreateUserCredentialsPage:
    admin_menu = "//span[text()='Admin']"
    add_btn = "//button[normalize-space()='Add']"
    add_user_title = "//h6[text()='Add User']"
    user_role_dropdown = "(//div[@class='oxd-select-text-input'])[1]"
    emp_name = "//label[text()='Employee Name']/parent::div/following-sibling::div//input"
    status_dropdown = "(//div[@class='oxd-select-text-input'])[2]"
    user_name = "//label[text()='Username']/parent::div/following-sibling::div//input"
    password = "//label[text()='Password']/parent::div/following-sibling::div//input"
    confirm_password = "//label[text()='Confirm Password']/parent::div/following-sibling::div//input"
    save_btn = "//button[@type='submit']"
    success_msg = "//p[contains(@class,'oxd-text--toast-message')]"
    required_validation_msg = "//span[text()='Required']"
    duplicate_username_validation_msg = "//span[text()='Already exists']"
    password_mismatch_validation_msg = "//span[text()='Passwords do not match']"

    def __init__(self, driver):
        self.driver = driver

    def click_admin_menu(self):
        self.driver.find_element(By.XPATH, self.admin_menu).click()

    def click_add_button(self):
        self.driver.find_element(By.XPATH, self.add_btn).click()

    def is_add_user_page_displayed(self):
        return self.driver.find_element(By.XPATH,self.add_user_title).is_displayed()

    def select_user_role_dropdown(self):
        self.driver.find_element(By.XPATH,self.user_role_dropdown).click()

    def enter_employee_name(self, employee_name):
        self.driver.find_element(By.XPATH, self.emp_name).send_keys(employee_name)

    def select_status_dropdown(self):
        self.driver.find_element(By.XPATH, self.status_dropdown).click()

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.user_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH,self.password).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(By.XPATH, self.confirm_password).send_keys(confirm_password)

    def click_save_button(self):
        self.driver.find_element(By.XPATH,self.save_btn).click()

    def is_success_message_displayed(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.success_msg)))
        return self.driver.find_element(By.XPATH,self.success_msg).is_displayed()

