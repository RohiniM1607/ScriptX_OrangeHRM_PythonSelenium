from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EmployeeApplyLeavePage:

    loader                           = "div.oxd-form-loader"
    close_info_notification          = "//div[contains(@class,'oxd-toast')]//button[contains(@class,'oxd-toast-close')]"
    leave_menu                       = "//span[contains(@class,'oxd-main-menu-item--name') and text()='Leave']"
    apply_sub_menu                   = "//a[contains(@class,'oxd-topbar-body-nav-tab-item') and normalize-space()='Apply']"
    leave_type_dropdown              = "//label[text()='Leave Type']/parent::div/following-sibling::div//div[contains(@class,'oxd-select-text-input')]"
    leave_type_options               = "//div[@role='listbox']//span"
    leave_balance_text               = "//*[contains(text(),'Day(s)')]"
    from_date_input                  = "(//input[@placeholder='yyyy-dd-mm'])[1]"
    to_date_input                    = "(//input[@placeholder='yyyy-dd-mm'])[2]"
    comments_textarea                = "//textarea[@placeholder='Type here']"
    apply_button                     = "//button[normalize-space()='Apply']"
    save_btn                         = "//button[@type='submit']"
    success_msg                      = "//div[contains(@class,'oxd-toast--success')]//p[2]"
    confirm_toast                    = "//div[contains(@class,'oxd-toast') and .//p[text()='Successfully Saved']]"
    emp_option                       = "//div[@role='listbox']"

    def __init__(self, driver):
        self.driver = driver

    def click_leave_menu(self):
        self.driver.find_element(By.XPATH, self.leave_menu).click()

    def click_apply_sub_menu(self):
        self.driver.find_element(By.XPATH, self.apply_sub_menu).click()

    def select_leave_type_dropdown(self):
        self.driver.find_element(By.XPATH, self.leave_type_dropdown).click()

    def select_leave_type_option(self, leave_type_name):
        options = self.driver.find_elements(By.XPATH, self.leave_type_options)
        for option in options:
            if option.text.strip() == leave_type_name:
                option.click()
                break

    def get_leave_balance_text(self):
        return self.driver.find_element(By.XPATH, self.leave_balance_text).text

    def enter_from_date(self, from_date):
        el = self.driver.find_element(By.XPATH, self.from_date_input)
        el.clear()
        el.send_keys(from_date)

    def enter_to_date(self, to_date):
        el = self.driver.find_element(By.XPATH, self.to_date_input)
        el.clear()
        el.send_keys(to_date)

    def enter_comments(self, comment):
        el = self.driver.find_element(By.XPATH, self.comments_textarea)
        el.clear()
        el.send_keys(comment)

    def click_apply_button(self):
        self.driver.find_element(By.XPATH, self.apply_button).click()

    def click_save_button(self):
        self.driver.find_element(By.XPATH, self.save_btn).click()

    def close_notification(self):
        self.driver.find_element(By.XPATH, self.close_info_notification).click()

    def wait_for_loader_to_disappear(self):
        WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, self.loader))
        )

    def is_success_message_displayed(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.success_msg))
        )
        return self.driver.find_element(By.XPATH, self.success_msg).is_displayed()

    def get_success_message_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.success_msg))
        )
        return self.driver.find_element(By.XPATH, self.success_msg).text