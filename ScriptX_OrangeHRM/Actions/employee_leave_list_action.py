from Pages.employee_leave_list_page import EmployeeLeaveListPage
from Actions.employee_apply_leave_action import EmployeeApplyLeaveActions
from Actions.base_actions import BaseActions

from Utilities.log_creator import log_generator

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class EmployeeLeaveListActions(BaseActions):

    def __init__(self, driver):

        super().__init__(driver)

        self.page = EmployeeLeaveListPage()

        self._apply_actions = EmployeeApplyLeaveActions(
            driver
        )

        self.log = log_generator()

    # ============================================================
    # NAVIGATION
    # ============================================================

    def navigate_to_my_leave_page(self):

        self.log.info(
            "[Leave List] Navigating to My Leave page"
        )

        self.click_tuple_locator(
            self.page.leave_menu
        )

        self.log.info(
            "[Leave List] Leave menu clicked"
        )

        self.click_tuple_locator(
            self.page.my_leave_sub_menu
        )

        self.log.info(
            "[Leave List] My Leave submenu clicked"
        )

        self.wait_for_invisibility(
            self.page.loader
        )

        self.log.info(
            "[Leave List] My Leave page loaded"
        )

    # ============================================================
    # CLOSE DATE PICKER
    # ============================================================

    def close_date_picker(self):

        self.log.info(
            "[Leave List] Attempting to close date picker"
        )

        try:

            active_element = self.driver.switch_to.active_element

            self.log.debug(
                "[Leave List] Sending ESC to active element"
            )

            active_element.send_keys(Keys.ESCAPE)

            self.log.info(
                "[Leave List] ESC sent successfully"
            )

        except Exception as e:

            self.log.warning(
                f"[Leave List] Could not close date picker using ESC: {e}"
            )

        # Click somewhere safe outside the date picker
        try:

            self.driver.execute_script(
                "document.activeElement.blur();"
            )

            self.log.debug(
                "[Leave List] Active element blurred"
            )

        except Exception as e:

            self.log.warning(
                f"[Leave List] Could not blur active element: {e}"
            )

    # ============================================================
    # ENTER TO DATE
    # ============================================================

    def enter_to_date_for_leave_list(self, to_date):

        self.log.info(
            f"[Leave List] Preparing to enter To Date: {to_date}"
        )

        # --------------------------------------------------------
        # CLOSE FROM-DATE CALENDAR
        # --------------------------------------------------------

        self.close_date_picker()

        # --------------------------------------------------------
        # GET TO DATE ELEMENT
        # --------------------------------------------------------

        try:

            self.log.info(
                "[Leave List] Waiting for To Date input"
            )

            to_date_element = self.wait.until(
                EC.presence_of_element_located(
                    self.page.to_date_input
                )
            )

            self.log.info(
                "[Leave List] To Date element found"
            )

        except TimeoutException:

            self.log.error(
                "[Leave List] To Date element was NOT found",
                exc_info=True
            )

            raise

        # --------------------------------------------------------
        # SCROLL TO TO DATE
        # --------------------------------------------------------

        try:

            self.driver.execute_script(
                """
                arguments[0].scrollIntoView({
                    block: 'center',
                    inline: 'center'
                });
                """,
                to_date_element
            )

            self.log.debug(
                "[Leave List] Scrolled To Date into view"
            )

        except Exception as e:

            self.log.warning(
                f"[Leave List] Could not scroll To Date: {e}"
            )

        # --------------------------------------------------------
        # CLICK TO DATE
        # --------------------------------------------------------

        try:

            self.log.info(
                "[Leave List] Clicking To Date input"
            )

            self.driver.execute_script(
                "arguments[0].click();",
                to_date_element
            )

            self.log.info(
                "[Leave List] To Date input clicked"
            )

        except Exception as e:

            self.log.error(
                "[Leave List] Failed to click To Date input",
                exc_info=True
            )

            raise

        # --------------------------------------------------------
        # ENTER DATE
        # --------------------------------------------------------

        try:

            self.log.info(
                f"[Leave List] Clearing To Date input"
            )

            to_date_element.send_keys(
                Keys.CONTROL,
                "a"
            )

            to_date_element.send_keys(
                Keys.BACKSPACE
            )

            self.log.info(
                f"[Leave List] Entering To Date: {to_date}"
            )

            to_date_element.send_keys(
                to_date
            )

            self.log.info(
                "[Leave List] To Date value entered"
            )

            # ----------------------------------------------------
            # TAB OUT
            # ----------------------------------------------------

            to_date_element.send_keys(
                Keys.TAB
            )

            self.log.info(
                "[Leave List] TAB pressed after To Date"
            )

        except Exception as e:

            self.log.error(
                "[Leave List] Failed while entering To Date",
                exc_info=True
            )

            raise

    # ============================================================
    # APPLY LEAVE FOR LEAVE LIST FEATURE
    # ============================================================

    def apply_leave_for_leave_list(
        self,
        leave_type,
        from_date,
        to_date
    ):

        self.log.info(
            "[Leave List] ========================================"
        )

        self.log.info(
            "[Leave List] Starting leave creation"
        )

        self.log.info(
            f"[Leave List] Leave Type : {leave_type}"
        )

        self.log.info(
            f"[Leave List] From Date  : {from_date}"
        )

        self.log.info(
            f"[Leave List] To Date    : {to_date}"
        )

        try:

            # ====================================================
            # NAVIGATE TO APPLY LEAVE
            # ====================================================

            self.log.info(
                "[Leave List] Navigating to Apply Leave page"
            )

            self._apply_actions.navigate_to_apply_leave_page()

            self.log.info(
                "[Leave List] Apply Leave page opened"
            )

            # ====================================================
            # SELECT LEAVE TYPE
            # ====================================================

            self.log.info(
                f"[Leave List] Selecting leave type: {leave_type}"
            )

            self._apply_actions.select_leave_type(
                leave_type
            )

            self.log.info(
                "[Leave List] Leave type selected successfully"
            )

            # ====================================================
            # FROM DATE
            # ====================================================

            self.log.info(
                f"[Leave List] Entering From Date: {from_date}"
            )

            self._apply_actions.enter_from_date(
                from_date
            )

            self.log.info(
                "[Leave List] From Date entered successfully"
            )

            # ====================================================
            # TO DATE
            # ====================================================

            self.log.info(
                f"[Leave List] Entering To Date: {to_date}"
            )

            self.enter_to_date_for_leave_list(
                to_date
            )

            self.log.info(
                "[Leave List] To Date entered successfully"
            )

            # ====================================================
            # APPLY BUTTON
            # ====================================================

            self.log.info(
                "[Leave List] Preparing to click Apply button"
            )

            # Close any remaining date picker
            self.close_date_picker()

            self.log.info(
                "[Leave List] Date picker closed"
            )

            self.log.info(
                "[Leave List] Waiting for Apply button"
            )

            apply_button = self.wait.until(
                EC.element_to_be_clickable(
                    self.page.apply_button
                )
            )

            self.log.info(
                "[Leave List] Apply button is clickable"
            )

            # Scroll Apply button into view
            self.driver.execute_script(
                """
                arguments[0].scrollIntoView({
                    block: 'center',
                    inline: 'center'
                });
                """,
                apply_button
            )

            self.log.info(
                "[Leave List] Apply button scrolled into view"
            )

            # Normal Selenium click first
            try:

                apply_button.click()

                self.log.info(
                    "[Leave List] Apply button clicked successfully"
                )

            except Exception as click_error:

                self.log.warning(
                    "[Leave List] Normal Apply click failed"
                )

                self.log.warning(
                    f"[Leave List] Click error: {click_error}"
                )

                self.log.info(
                    "[Leave List] Trying JavaScript click"
                )

                self.driver.execute_script(
                    "arguments[0].click();",
                    apply_button
                )

                self.log.info(
                    "[Leave List] Apply button clicked using JavaScript"
                )

            # ====================================================
            # SUCCESS MESSAGE
            # ====================================================

            self.log.info(
                "[Leave List] Waiting for success message"
            )

            result = (
                self._apply_actions
                .get_success_message_display()
            )

            self.log.info(
                f"[Leave List] Success message displayed: {result}"
            )

            if result:

                self.log.info(
                    "[Leave List] Leave creation completed successfully"
                )

            else:

                self.log.warning(
                    "[Leave List] Leave creation completed but "
                    "success message was not displayed"
                )

            return result

        except Exception as e:

            self.log.error(
                "[Leave List] Leave creation FAILED",
                exc_info=True
            )

            raise

    # ============================================================
    # LEAVE TYPE
    # ============================================================

    def select_leave_type(
        self,
        leave_type_name
    ):

        self.log.info(
            f"[Leave List] Selecting leave type: {leave_type_name}"
        )

        self._apply_actions.select_leave_type(
            leave_type_name
        )

        self.log.info(
            "[Leave List] Leave type selected"
        )

    # ============================================================
    # SEARCH
    # ============================================================

    def click_search(self):

        self.log.info(
            "[Leave List] Clicking Search button"
        )

        self.click_tuple_locator(
            self.page.search_button
        )

        self.log.info(
            "[Leave List] Search button clicked"
        )

        self.wait_for_invisibility(
            self.page.loader
        )

        self.log.info(
            "[Leave List] Search completed"
        )

    # ============================================================
    # TABLE
    # ============================================================

    def get_total_rows(self):

        rows = self.driver.find_elements(
            *self.page.table_rows
        )

        total_rows = len(rows)

        self.log.info(
            f"[Leave List] Total table rows: {total_rows}"
        )

        return total_rows

    # ============================================================
    # GET STATUS
    # ============================================================

    def get_status_for_leave_type(
        self,
        leave_type_name
    ):

        total_rows = self.get_total_rows()

        self.log.info(
            f"[Leave List] Searching status for: {leave_type_name}"
        )

        for row_index in range(
            1,
            total_rows + 1
        ):

            leave_type_locator = (
                By.XPATH,
                self.page.leave_type_cell_by_row.format(
                    row=row_index
                )
            )

            leave_type_el = self.driver.find_element(
                *leave_type_locator
            )

            current_leave_type = (
                leave_type_el.text.strip()
            )

            self.log.debug(
                f"[Leave List] Row {row_index} "
                f"Leave Type: {current_leave_type}"
            )

            if (
                current_leave_type.lower()
                == leave_type_name.strip().lower()
            ):

                status_locator = (
                    By.XPATH,
                    self.page.status_cell_by_row.format(
                        row=row_index
                    )
                )

                status_el = self.driver.find_element(
                    *status_locator
                )

                status = status_el.text.strip()

                self.log.info(
                    f"[Leave List] Found '{leave_type_name}' "
                    f"with status '{status}'"
                )

                return status

        self.log.warning(
            f"[Leave List] Leave type '{leave_type_name}' "
            f"was not found"
        )

        return None

    # ============================================================
    # SEARCH LEAVE AND GET STATUS
    # ============================================================

    def search_leave_and_get_status(
        self,
        leave_type_name
    ):

        self.log.info(
            f"[Leave List] Searching leave type: "
            f"{leave_type_name}"
        )

        self.navigate_to_my_leave_page()

        self.select_leave_type(
            leave_type_name
        )

        self.click_search()

        return self.get_status_for_leave_type(
            leave_type_name
        )

    # ============================================================
    # WITHOUT APPLYING LEAVE
    # ============================================================

    def without_applying_leave(self):

        self.log.info(
            "[Leave List] Checking leave list "
            "without applying leave"
        )

        self.navigate_to_my_leave_page()

        self.click_search()

        element = self.wait_for_element_tuple(
            self.page.record_count_text
        )

        result = element.text.strip()

        self.log.info(
            f"[Leave List] Record count: {result}"
        )

        return result

    # ============================================================
    # GET LEAVE BALANCE
    # ============================================================

    def get_leave_balance_for_leave_type(
        self,
        leave_type_name
    ):

        self.log.info(
            f"[Leave List] Getting balance for: "
            f"{leave_type_name}"
        )

        self.navigate_to_my_leave_page()

        self.select_leave_type(
            leave_type_name
        )

        self.click_search()

        total_rows = self.get_total_rows()

        self.log.info(
            f"[Leave List] Searching balance in "
            f"{total_rows} rows"
        )

        for row_index in range(
            1,
            total_rows + 1
        ):

            leave_type_locator = (
                By.XPATH,
                self.page.leave_type_cell_by_row.format(
                    row=row_index
                )
            )

            leave_type_el = self.driver.find_element(
                *leave_type_locator
            )

            current_leave_type = (
                leave_type_el.text.strip()
            )

            if (
                current_leave_type.lower()
                == leave_type_name.strip().lower()
            ):

                balance_locator = (
                    By.XPATH,
                    self.page.leave_balance_cell_by_row.format(
                        row=row_index
                    )
                )

                balance_el = self.driver.find_element(
                    *balance_locator
                )

                balance = balance_el.text.strip()

                self.log.info(
                    f"[Leave List] Leave balance for "
                    f"'{leave_type_name}': {balance}"
                )

                return balance

        self.log.warning(
            f"[Leave List] Balance not found for "
            f"'{leave_type_name}'"
        )

        return None