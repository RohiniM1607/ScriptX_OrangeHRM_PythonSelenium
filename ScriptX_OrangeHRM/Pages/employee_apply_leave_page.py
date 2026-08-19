from selenium.webdriver.common.by import By


class EmployeeApplyLeavePage:

    # =========================================================
    # Loader
    # =========================================================

    loader = (
        By.CSS_SELECTOR,
        "div.oxd-form-loader"
    )

    # =========================================================
    # Navigation
    # =========================================================

    leave_menu = (
        By.XPATH,
        "//a[contains(@href,'viewLeaveModule')]"
    )

    apply_sub_menu = (
        By.XPATH,
        "//a[normalize-space()='Apply']"
    )

    # =========================================================
    # Leave Type
    # =========================================================

    leave_type_dropdown = (
        By.XPATH,
        "//label[normalize-space()='Leave Type']"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//div[contains(@class,'oxd-select-text')]"
    )

    leave_type_options = (
        By.XPATH,
        "//div[@role='listbox']"
        "//div[contains(@class,'oxd-select-option')]"
    )

    # =========================================================
    # From Date
    # =========================================================

    from_date_input = (
        By.XPATH,
        "//label[normalize-space()='From Date']"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//input"
    )

    # =========================================================
    # To Date
    # =========================================================

    to_date_input = (
        By.XPATH,
        "//label[normalize-space()='To Date']"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//input"
    )

    # =========================================================
    # Comments
    # =========================================================

    comments_textarea = (
        By.XPATH,
        "//label[normalize-space()='Comments']"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//textarea"
    )

    # =========================================================
    # Apply Button
    # =========================================================

    apply_button = (
        By.XPATH,
        "//button[normalize-space()='Apply']"
    )

    # =========================================================
    # Success Message
    # =========================================================

    success_msg = (
        By.XPATH,
        "//div[contains(@class,'oxd-toast--success')]"
    )

    # =========================================================
    # Leave Type Required
    # =========================================================

    leave_type_required_error = (
        By.XPATH,
        "//label[normalize-space()='Leave Type']"
        "/ancestor::div[contains(@class,'oxd-input-group')]"
        "//span[normalize-space()='Required']"
    )

    # =========================================================
    # To Date Validation
    # =========================================================

    to_date_error_msg = (
        By.XPATH,
        "//span[normalize-space()='"
        "To date should be after from date"
        "']"
    )

    # =========================================================
    # Leave Balance
    # =========================================================

    leave_balance_text = (
        By.XPATH,
        "//*[contains(normalize-space(),'Day(s)')]"
    )

    # =========================================================
    # Notification
    # =========================================================

    close_info_notification = (
        By.XPATH,
        "//div[contains(@class,'oxd-toast')]"
        "//button[contains(@class,'oxd-toast-close')]"
    )