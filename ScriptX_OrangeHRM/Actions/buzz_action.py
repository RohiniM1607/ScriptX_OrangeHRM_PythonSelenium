from Pages.buzz_page import BuzzPage
from Actions.base_actions import BaseActions


class BuzzAction:

    def __init__(self, driver):
        self.base = BaseActions(driver)
        self.page = BuzzPage
        self.driver = driver

    def open_buzz_module(self):
        self.base.click_element(self.page.buzz_menu)

    def create_post(self, post_text):
        self.open_buzz_module()
        self.base.wait_for_element(self.page.post_text_area)
        self.base.enter_text(self.page.post_text_area, post_text)
        self.base.js_click(self.page.post_button)

    def create_invalid_post(self, invalid_text):
        self.open_buzz_module()
        self.base.wait_for_element(self.page.post_text_area)
        self.base.enter_text(self.page.post_text_area, invalid_text)
        self.base.js_click(self.page.post_button)

    def is_success_message_displayed(self):
        self.base.wait_for_element(self.page.success_message)
        return self.base.is_element_displayed(self.page.success_message)

    def get_latest_post_text(self):
        # Wait for the feed to load up the post element
        self.base.wait_for_element(self.page.latest_post_text)
        element = self.driver.find_element("xpath", self.page.latest_post_text)
        # Clean out any leading/trailing whitespace
        return element.text.strip()