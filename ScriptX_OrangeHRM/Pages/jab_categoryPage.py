class JabCategoryPage:
    job_Menu = "(//span//i[@class='oxd-icon bi-chevron-down'])[2]"
    job_categories = "//a[contains(text(),'Job Categories')]"
    add_job_btn = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"
    input_field = "(//input[@class='oxd-input oxd-input--active'])[2]"
    save_btn = "button[type='submit']"
    required_message = "span[class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']"
    already_exists_msg = "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']"
    success_meg = "div[aria-live='assertive']"