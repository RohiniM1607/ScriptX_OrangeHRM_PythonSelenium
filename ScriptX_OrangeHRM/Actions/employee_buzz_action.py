from Pages.employee_buzz_page import BuzzPage
from Actions.base_actions import BaseActions
import time


class BuzzActions(BaseActions):

    log = None

    def __init__(self, driver):
        super().__init__(driver)
        self.page = BuzzPage()

    def navigate_to_buzz_page(self):
        self.click_tuple_locator(self.page.buzz_menu)

    def create_post(self, post_text):
        self.enter_text_and_tab(self.page.post_input, post_text)
        self.click_tuple_locator(self.page.post_button)
        time.sleep(2)

    def get_latest_post_username(self):
        element = self.wait_for_element_tuple(self.page.post_username)
        return element.text.strip()

    def edit_latest_post(self, edit_text):
        self.click_tuple_locator(self.page.three_dot_button)
        self.click_tuple_locator(self.page.edit_post_option)
        edit_input = self.wait_for_element_tuple(self.page.edit_post_input)
        edit_input.clear()
        edit_input.send_keys(edit_text)
        self.click_tuple_locator(self.page.edit_post_button)
        time.sleep(2)

    def get_latest_post_text(self):
        element = self.wait_for_element_tuple(self.page.latest_post_text)
        return element.text.strip()