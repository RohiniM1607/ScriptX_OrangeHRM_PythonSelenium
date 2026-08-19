from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    StaleElementReferenceException,
    ElementClickInterceptedException,
    TimeoutException,
)

from Pages.employee_apply_leave_page import EmployeeApplyLeavePage
from Actions.base_actions import BaseActions


class EmployeeApplyLeaveActions(BaseActions):

    def __init__(self, driver):
        super().__init__(driver)
        self.page = EmployeeApplyLeavePage()

    # ============================================================
    # NAVIGATION
    # ============================================================

    def navigate_to_apply_leave_page(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.page.leave_menu
            )
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(
                self.page.apply_sub_menu
            )
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                self.page.leave_type_dropdown
            )
        )

    # ============================================================
    # LEAVE TYPE
    # ============================================================

    def select_leave_type(self, leave_type_name):

        self.wait.until(
            EC.element_to_be_clickable(
                self.page.leave_type_dropdown
            )
        ).click()

        def find_and_click_option(driver):

            try:
                options = driver.find_elements(
                    *self.page.leave_type_options
                )

                for option in options:

                    if not option.is_displayed():
                        continue

                    option_text = option.text.strip()

                    if (
                        option_text.lower()
                        == leave_type_name.strip().lower()
                    ):

                        driver.execute_script(
                            "arguments[0].scrollIntoView({block:'center'});",
                            option
                        )

                        try:
                            option.click()
                        except (
                            StaleElementReferenceException,
                            ElementClickInterceptedException,
                        ):
                            return False

                        return True

                return False

            except StaleElementReferenceException:
                return False

        self.wait.until(
            find_and_click_option
        )

    # ============================================================
    # DATE FIELD
    # ============================================================

    def _replace_date(
        self,
        locator_tuple,
        date_value
    ):

        def enter_date(driver):

            try:

                element = driver.find_element(
                    *locator_tuple
                )

                if not element.is_displayed():
                    return False

                if not element.is_enabled():
                    return False

                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    element
                )

                element.click()

                # Select existing date
                element.send_keys(
                    Keys.CONTROL,
                    "a"
                )

                # Remove existing value
                element.send_keys(
                    Keys.BACKSPACE
                )

                # Enter new date
                element.send_keys(
                    str(date_value)
                )

                # Trigger blur/change event
                element.send_keys(
                    Keys.TAB
                )

                return True

            except StaleElementReferenceException:
                return False

            except ElementClickInterceptedException:
                return False

        self.wait.until(
            enter_date
        )

        def verify_date(driver):

            try:

                element = driver.find_element(
                    *locator_tuple
                )

                current_value = element.get_attribute(
                    "value"
                )

                return (
                    current_value
                    == str(date_value)
                )

            except StaleElementReferenceException:
                return False

        self.wait.until(
            verify_date
        )

    # ============================================================
    # FROM DATE
    # ============================================================

    def enter_from_date(self, from_date):

        self._replace_date(
            self.page.from_date_input,
            from_date
        )

    # ============================================================
    # TO DATE
    # ============================================================

    def enter_to_date(self, to_date):

        self._replace_date(
            self.page.to_date_input,
            to_date
        )

    # ============================================================
    # COMMENTS
    # ============================================================

    def enter_comments(self, comment):

        if not comment:
            return

        element = self.wait.until(
            EC.element_to_be_clickable(
                self.page.comments_textarea
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        element.click()

        element.send_keys(
            Keys.CONTROL,
            "a"
        )

        element.send_keys(
            Keys.BACKSPACE
        )

        element.send_keys(
            str(comment)
        )

    # ============================================================
    # APPLY BUTTON
    # ============================================================

    def apply(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.page.apply_button
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            button
        )

        button.click()

    # ============================================================
    # SUCCESS MESSAGE
    # ============================================================

    def get_success_message_display(self):

        try:

            element = self.wait.until(
                EC.visibility_of_element_located(
                    self.page.success_msg
                )
            )

            return element.is_displayed()

        except TimeoutException:
            return False

    # ============================================================
    # TO DATE VALIDATION ERROR
    # ============================================================

    def get_to_date_error(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.page.to_date_error_msg
            )
        )

    # ============================================================
    # LEAVE TYPE REQUIRED ERROR
    # ============================================================

    def get_leave_type_required_error(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.page.leave_type_required_error
            )
        )

    # ============================================================
    # APPLY LEAVE
    # ============================================================

    def apply_leave(
        self,
        leave_type,
        from_date,
        to_date,
        comment=None
    ):

        self.navigate_to_apply_leave_page()

        # Select Leave Type
        self.select_leave_type(
            leave_type
        )

        # Enter From Date
        self.enter_from_date(
            from_date
        )

        # Enter To Date
        self.enter_to_date(
            to_date
        )

        # Enter Comments
        self.enter_comments(
            comment
        )

        # Click Apply
        self.apply()

        # Check success message
        return self.get_success_message_display()

    # ============================================================
    # APPLY LEAVE WITHOUT LEAVE TYPE
    # ============================================================

    def apply_leave_without_leave_type(
        self,
        from_date,
        to_date=None
    ):

        self.navigate_to_apply_leave_page()

        # Do not select Leave Type

        # Enter From Date
        self.enter_from_date(
            from_date
        )

        # Enter To Date
        if to_date:
            self.enter_to_date(
                to_date
            )

        # Click Apply
        self.apply()

        # Verify Leave Type required error
        try:

            error = self.wait.until(
                EC.visibility_of_element_located(
                    self.page.leave_type_required_error
                )
            )

            return error.is_displayed()

        except TimeoutException:
            return False