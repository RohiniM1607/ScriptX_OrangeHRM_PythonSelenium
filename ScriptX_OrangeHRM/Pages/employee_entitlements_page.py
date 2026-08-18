from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EmployeeEntitlementPage:
    leave_menu = "//span[text()='Leave']"
    entitlements_menu = "//span[text()='Entitlements ']"
    employee_entitlements_option = "//a[text()='Employee Entitlements']"
    employee_entitlements_title = "//h5[normalize-space()='Leave Entitlements']"
    employee_name = "//label[text()='Employee Name']/parent::div/following-sibling::div//input"
    employee_suggestion = "//div[@role='listbox']//span"
    leave_type = "(//div[@class='oxd-select-text-input'])[1]"
    leave_period = "(//div[@class='oxd-select-text-input'])[2]"
    search_button = "//button[@type='submit']"
    search_result = "//div[@class='orangehrm-container']"
    invalid_validation_msg = "//span[text()='Invalid']"
    required_validation_msg = "//span[text()='Required']"
    employee_name_required_msg = "//label[text()='Employee Name']/ancestor::div[contains(@class,'oxd-input-group')]//span[contains(@class,'oxd-input-field-error-message')]"