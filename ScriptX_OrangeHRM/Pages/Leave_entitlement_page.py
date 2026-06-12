from selenium.webdriver.common.by import By


class AddLeaveEntitlementPage:

    leave_menu = (By.XPATH, "//span[normalize-space()='Leave']")
    entitlement_menu = (By.XPATH, "//span[normalize-space()='Entitlements']")
    add_entitlement = (By.XPATH, "//ul[@role='menu']/child::li[1]")

    employee_name = (By.XPATH, "//input[@placeholder='Type for hints...']")
    employee_options = (By.XPATH, "//div[@role='option']")
    searching = (By.XPATH, "//div[text()='Searching...']")
    

    leave_type = (By.XPATH, "//div[contains(@class,'oxd-select-text-input')]")
    leave_type_options = (By.XPATH, "//div[@role='listbox']//span")

    entitlement = (By.XPATH, "//div[@class='oxd-input-group__label-wrapper']/child::label[text()='Entitlement']/following::input")
    save_btn = (By.XPATH, "//button[@type='submit']")
    confirm_btn = (By.XPATH, "//button[normalize-space()='Confirm']")

    required_msg = (By.XPATH, "//span[text()='Required']")
    exceed_error = (By.XPATH, "//span[text()='Should be less than 10000']")