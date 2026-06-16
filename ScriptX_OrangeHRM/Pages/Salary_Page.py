class SalaryDetailsPage:

    lnk_salary_details   = "//a[normalize-space()='Salary']"
    btn_add              = "//button[normalize-space()='Add']"
    drp_pay_grade        = "//label[text()='Pay Grade']/following::div[contains(@class,'oxd-select-text')][1]"
    drp_pay_frequency    = "//label[text()='Pay Frequency']/following::div[contains(@class,'oxd-select-text')][1]"
    drp_currency         = "//label[text()='Currency']/following::div[contains(@class,'oxd-select-text')][1]"
    txt_salary_component = "//label[text()='Salary Component']/following::input[1]"
    txt_amount           = "//label[text()='Amount']/following::input[1]"
    txt_comment          = "//label[text()='Comments']/following::textarea[1]"
    option_text          = "//div[@role='option']//span"
    btn_save             = "//button[normalize-space()='Save']"
    msg_success          = "//div[contains(@class,'oxd-toast-content')]//p[1]"
    load_spinner         = "//div[contains(@class,'oxd-loading-spinner-container')]"