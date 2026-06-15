from selenium.webdriver.common.by import By


class BuzzPage:

    loader              = (By.CSS_SELECTOR, "div.oxd-form-loader")

    buzz_menu           = (By.XPATH, "//a[contains(@href,'viewBuzz')]/child::span")

    post_input          = (By.XPATH, "//textarea[@placeholder=\"What's on your mind?\"]")

    post_button         = (By.XPATH, "//button[normalize-space()='Post']")

    post_username       = (By.XPATH, "(//div[contains(@class,'orangehrm-buzz-post-header-details')]//p[contains(@class,'oxd-text--p')])[1]")

    three_dot_button    = (By.XPATH, "(//div[contains(@class,'orangehrm-buzz-post-header-config')]//button[contains(@class,'oxd-icon-button')])[1]")
    edit_post_option    = (By.XPATH, "//p[normalize-space()='Edit Post']")

    edit_post_input     = (By.XPATH, "//div[contains(@class,'orangehrm-dialog-modal')]//textarea")

    edit_post_button    = (By.XPATH, "//div[contains(@class,'orangehrm-buzz-post-modal-actions')]//button[@type='submit']")

    latest_post_text    = (By.XPATH, "(//div[contains(@class,'orangehrm-buzz-post-body')]//p)[1]")