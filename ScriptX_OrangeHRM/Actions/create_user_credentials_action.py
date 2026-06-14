from Pages.create_user_credentials_page import CreateUserCredentialsPage
from Actions.base_actions import BaseActions
import time
import random
from Utilities import log_creator

class CreateUserCredentialActions:
    def __init__(self, driver):
        self.base = BaseActions(driver)
        self.page = CreateUserCredentialsPage()
        self.driver = driver

    def click_admin_menu(self):
        self.base.click_element(self.page.admin_menu)

    def click_add_button(self):
        self.base.click_element(self.page.add_btn)

    def verify_add_user_page(self):
        return self.base.is_element_displayed(self.page.add_user_title)

    def select_user_role(self, role):
        self.base.click_element(self.page.user_role)
        if role.lower() == "admin":
            self.base.press_down_and_enter(1)

        elif role.lower() == "ess":
            self.base.press_down_and_enter(2)

    def enter_employee_name(self, employee_name):
        self.base.click_element(self.page.emp_name)
        self.base.enter_text(self.page.emp_name, employee_name)
        self.base.wait_for_element(self.page.employee_suggestion)
        self.base.press_down_and_enter(1)

    def select_status(self, status):
        self.base.click_element(self.page.status)
        if status.lower() == "enabled":
            self.base.press_down_and_enter(1)

        elif status.lower() == "disabled":
            self.base.press_down_and_enter(2)

    def enter_username(self, username, handle_duplicate):
        self.base.clear_text(self.page.user_name)
        self.base.enter_text(self.page.user_name, username)

        if handle_duplicate:
            try:
                self.base.wait_for_element(self.page.duplicate_username_validation_msg)

                username = f"{username}{random.randint(1000, 9999)}"

                self.base.clear_text(self.page.user_name)
                self.base.enter_text(self.page.user_name, username)

            except Exception:
                pass

        time.sleep(2)
                
    def enter_password(self, password):
        self.base.enter_text(self.page.password,password)

    def enter_confirm_password(self, confirm_password):
        self.base.enter_text(self.page.confirm_password,confirm_password)

    def enter_user_credentials(self, role, emp_name, status,username, password, confirm_password,handle_duplicate=True):
        if role is not None:
            self.select_user_role(role)

        if emp_name is not None:
            self.enter_employee_name(emp_name)

        if status is not None:
            self.select_status(status)

        if username is not None:
            self.enter_username(username, handle_duplicate)

        if password is not None:
            self.enter_password(password)

        if confirm_password is not None:
            self.enter_confirm_password(confirm_password)

    def verify_duplicate_username_message(self):
        return self.base.is_element_present(self.page.duplicate_username_validation_msg)
    
    def verify_required_field_messages(self):
        return self.base.is_element_present(self.page.required_field_validation_msg)

    def verify_password_mismatch_message(self):
        return self.base.is_element_present(self.page.password_mismatch_validation_msg)
    
    def click_save_button(self):
        time.sleep(2)
        self.base.click_element(self.page.save_btn)

    def verify_success_message_displayed(self):
        return self.base.is_element_displayed(self.page.success_msg)
    
    def verify_password_mismatch_message(self):
        return self.base.is_element_present(self.page.password_mismatch_validation_msg)