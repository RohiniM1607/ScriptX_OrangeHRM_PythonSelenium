from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CreateUserCredentialsPage:
    admin_menu = "//span[text()='Admin']"
    add_btn = "//button[normalize-space()='Add']"
    add_user_title = "//h6[text()='Add User']"
    user_role = "(//div[@class='oxd-select-text-input'])[1]"
    emp_name = "//label[text()='Employee Name']/parent::div/following-sibling::div//input"
    employee_suggestion = "//div[@role='listbox']//span"
    status = "(//div[@class='oxd-select-text-input'])[2]"
    user_name = "//label[text()='Username']/parent::div/following-sibling::div//input"
    password = "//label[text()='Password']/parent::div/following-sibling::div//input"
    confirm_password = "//label[text()='Confirm Password']/parent::div/following-sibling::div//input"
    save_btn = "//button[@type='submit']"
    success_msg = "//p[contains(@class,'oxd-text--toast-message')]"
    required_validation_msg = "//span[text()='Required']"
    duplicate_username_validation_msg = "//span[text()='Already exists']"
    password_mismatch_validation_msg = "//span[text()='Passwords do not match']"

    