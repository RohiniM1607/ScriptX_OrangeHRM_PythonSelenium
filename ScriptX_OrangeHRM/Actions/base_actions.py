from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    StaleElementReferenceException,
    ElementClickInterceptedException,
    TimeoutException,
)


class BaseActions:

    def __init__(self, driver):
        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            25,
            poll_frequency=0.3,
            ignored_exceptions=(
                StaleElementReferenceException,
            ),
        )

    # =========================================================
    # Locator helper
    # =========================================================

    @staticmethod
    def _normalize_locator(locator):

        if isinstance(locator, tuple):
            return locator

        return By.XPATH, locator

    # =========================================================
    # Click
    # =========================================================

    def click_element(self, locator):

        locator = self._normalize_locator(locator)

        def click(driver):

            try:

                element = driver.find_element(*locator)

                if not element.is_displayed():
                    return False

                if not element.is_enabled():
                    return False

                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    element
                )

                element.click()

                return True

            except (
                StaleElementReferenceException,
                ElementClickInterceptedException,
            ):
                return False

        self.wait.until(click)

    def click_tuple_locator(self, locator_tuple):

        self.click_element(locator_tuple)

    # =========================================================
    # Enter text
    # =========================================================

    def enter_text(self, locator, text):

        locator = self._normalize_locator(locator)

        def enter(driver):

            try:

                element = driver.find_element(*locator)

                if not element.is_displayed():
                    return False

                if not element.is_enabled():
                    return False

                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    element
                )

                element.click()
                element.clear()
                element.send_keys(str(text))

                return True

            except StaleElementReferenceException:
                return False

        self.wait.until(enter)

    # =========================================================
    # Enter text + TAB
    # =========================================================

    def enter_text_and_tab(self, locator_tuple, text):

        locator = self._normalize_locator(locator_tuple)

        def enter(driver):

            try:

                element = driver.find_element(*locator)

                if not element.is_displayed():
                    return False

                if not element.is_enabled():
                    return False

                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    element
                )

                element.click()
                element.clear()
                element.send_keys(str(text))
                element.send_keys(Keys.TAB)

                return True

            except StaleElementReferenceException:
                return False

        self.wait.until(enter)

    # =========================================================
    # Clear and enter
    # =========================================================

    def clear_and_enter_text(self, locator, text):

        locator = self._normalize_locator(locator)

        def enter(driver):

            try:

                element = driver.find_element(*locator)

                if not element.is_displayed():
                    return False

                if not element.is_enabled():
                    return False

                element.click()

                element.send_keys(
                    Keys.CONTROL + "a"
                )

                element.send_keys(
                    Keys.DELETE
                )

                element.send_keys(
                    str(text)
                )

                return True

            except StaleElementReferenceException:
                return False

        self.wait.until(enter)

    # =========================================================
    # Presence
    # =========================================================

    def is_element_present(self, locator):

        locator = self._normalize_locator(locator)

        try:

            self.driver.find_element(*locator)

            return True

        except Exception:
            return False

    # =========================================================
    # Displayed
    # =========================================================

    def is_element_displayed(self, locator):

        locator = self._normalize_locator(locator)

        try:

            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            return element.is_displayed()

        except TimeoutException:
            return False

    # =========================================================
    # Get text
    # =========================================================

    def get_text(self, locator):

        locator = self._normalize_locator(locator)

        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text

    # =========================================================
    # Wait for element
    # =========================================================

    def wait_for_element(self, locator):

        locator = self._normalize_locator(locator)

        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_tuple(self, locator_tuple):

        locator_tuple = self._normalize_locator(
            locator_tuple
        )

        return self.wait.until(
            EC.visibility_of_element_located(
                locator_tuple
            )
        )

    # =========================================================
    # Presence
    # =========================================================

    def wait_for_element_presence(
        self,
        locator_tuple,
        timeout=10
    ):

        locator_tuple = self._normalize_locator(
            locator_tuple
        )

        short_wait = WebDriverWait(
            self.driver,
            timeout,
            poll_frequency=0.3,
            ignored_exceptions=(
                StaleElementReferenceException,
            ),
        )

        return short_wait.until(
            EC.presence_of_element_located(
                locator_tuple
            )
        )

    # =========================================================
    # Invisibility
    # =========================================================

    def wait_for_invisibility(self, locator_tuple):

        locator_tuple = self._normalize_locator(
            locator_tuple
        )

        try:

            self.wait.until(
                EC.invisibility_of_element_located(
                    locator_tuple
                )
            )

        except TimeoutException:

            # Loader may not be present on the page.
            pass

    def wait_for_element_invisible(self, locator):

        locator = self._normalize_locator(locator)

        self.wait.until(
            EC.invisibility_of_element_located(
                locator
            )
        )

    # =========================================================
    # All elements
    # =========================================================

    def wait_for_element_all(self, locator):

        locator = self._normalize_locator(locator)

        return self.wait.until(
            EC.presence_of_all_elements_located(
                locator
            )
        )

    def wait_for_all_elements_visible(
        self,
        locator_tuple
    ):

        locator_tuple = self._normalize_locator(
            locator_tuple
        )

        return self.wait.until(
            EC.visibility_of_all_elements_located(
                locator_tuple
            )
        )

    # =========================================================
    # JavaScript click
    # =========================================================

    def js_click(self, locator):

        locator = self._normalize_locator(locator)

        def click(driver):

            try:

                element = driver.find_element(*locator)

                if not element.is_displayed():
                    return False

                driver.execute_script(
                    "arguments[0].scrollIntoView({block:'center'});",
                    element
                )

                driver.execute_script(
                    "arguments[0].click();",
                    element
                )

                return True

            except StaleElementReferenceException:
                return False

        self.wait.until(click)

    # =========================================================
    # File upload
    # =========================================================

    def upload_file(self, locator, file_path):

        locator = self._normalize_locator(locator)

        element = self.wait.until(
            EC.presence_of_element_located(
                locator
            )
        )

        element.send_keys(file_path)

    # =========================================================
    # Keyboard
    # =========================================================

    def press_down_and_enter(self, count):

        active_element = self.driver.switch_to.active_element

        for _ in range(count):

            active_element.send_keys(
                Keys.ARROW_DOWN
            )

            active_element.send_keys(
                Keys.ENTER
            )

    # =========================================================
    # Wait for text
    # =========================================================

    def wait_for_text(
        self,
        locator,
        expected_text
    ):

        locator = self._normalize_locator(locator)

        def text_matches(driver):

            try:

                element = driver.find_element(
                    *locator
                )

                return (
                    expected_text in element.text
                )

            except StaleElementReferenceException:

                return False

        return self.wait.until(
            text_matches
        )