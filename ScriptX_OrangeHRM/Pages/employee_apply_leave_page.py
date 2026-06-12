from selenium.webdriver.common.by import By


class EmployeeApplyLeavePage:

  
    loader                  = (By.CSS_SELECTOR, "div.oxd-form-loader")
    close_info_notification = (By.XPATH, "//div[contains(@class,'oxd-toast')]//button[contains(@class,'oxd-toast-close')]")
    leave_menu              = (By.XPATH, "//a[contains(@href,'viewLeaveModule')]/child::span")
    apply_sub_menu          = (By.XPATH, "//a[normalize-space()='Apply']")
    leave_type_dropdown     = (By.XPATH, "//div[@class='oxd-select-wrapper']//descendant::div[@class='oxd-select-text--after']")
    leave_type_options      = (By.XPATH, "//div[@role='listbox']//span")
    from_date_input         = (By.XPATH, "(//div[@class='oxd-date-input']//child::input[@class='oxd-input oxd-input--active'])[1]")
    to_date_input           = (By.XPATH, "(//div[@class='oxd-date-input']//child::input[@class='oxd-input oxd-input--active'])[2]")
    comments_textarea       = (By.XPATH, "//textarea[@placeholder='Type here']")
    apply_button            = (By.XPATH, "//button[normalize-space()='Apply']")
    success_msg             = (By.XPATH, "//div[contains(@class,'oxd-toast--success')]//p[2]")
    to_date_error_msg       = (By.XPATH, "//span[text()='To date should be after from date']") 
    leave_balance_text      = (By.XPATH, "//*[contains(text(),'Day(s)')]")