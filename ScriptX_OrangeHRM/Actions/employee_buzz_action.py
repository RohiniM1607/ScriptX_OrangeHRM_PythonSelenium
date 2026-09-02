from selenium.webdriver.common.keys import Keys

from Pages.employee_buzz_page import BuzzPage
from Actions.base_actions import BaseActions


class BuzzActions(BaseActions):

    def __init__(self, driver):
        super().__init__(driver)
        self.page = BuzzPage()

    def navigate_to_buzz_page(self):
        print("\n[BUZZ DEBUG] Navigating to Buzz page")

        self.click_tuple_locator(
            self.page.buzz_menu
        )

        print("[BUZZ DEBUG] Buzz menu clicked")

        self.wait_for_element_tuple(
            self.page.post_input
        )

        print("[BUZZ DEBUG] Buzz post input is visible")

    def create_post(self, post_text):
        print(
            f"\n[BUZZ DEBUG] Creating post: {post_text}"
        )

        self.enter_text_and_tab(
            self.page.post_input,
            post_text
        )

        print("[BUZZ DEBUG] Post text entered")

        post_input = self.wait_for_element_tuple(
            self.page.post_input
        )

        actual_input = post_input.get_attribute("value")

        print(
            f"[BUZZ DEBUG] Input value before Post: "
            f"{actual_input!r}"
        )

        self.click_tuple_locator(
            self.page.post_button
        )

        print("[BUZZ DEBUG] Post button clicked")

    def get_latest_post_username(self):
        print(
            "\n[BUZZ DEBUG] Getting latest post username"
        )

        element = self.wait_for_element_tuple(
            self.page.post_username
        )

        username = element.text.strip()

        print(
            f"[BUZZ DEBUG] Latest post username: "
            f"{username!r}"
        )

        return username

    def edit_latest_post(self, edit_text):
        print(
            "\n========== BUZZ EDIT DEBUG START =========="
        )

        # Step 1
        print(
            "[BUZZ DEBUG] Step 1: "
            "Clicking three-dot button"
        )

        self.click_tuple_locator(
            self.page.three_dot_button
        )

        print(
            "[BUZZ DEBUG] Step 1 SUCCESS"
        )

        # Step 2
        print(
            "[BUZZ DEBUG] Step 2: "
            "Clicking Edit Post"
        )

        self.click_tuple_locator(
            self.page.edit_post_option
        )

        print(
            "[BUZZ DEBUG] Step 2 SUCCESS"
        )

        # Step 3
        print(
            "[BUZZ DEBUG] Step 3: "
            "Waiting for edit textarea"
        )

        edit_input = self.wait_for_element_tuple(
            self.page.edit_post_input
        )

        print(
            "[BUZZ DEBUG] Step 3 SUCCESS: "
            "Edit textarea found"
        )

        # Read original text
        old_value = edit_input.get_attribute(
            "value"
        )

        print(
            f"[BUZZ DEBUG] Existing textarea value: "
            f"{old_value!r}"
        )

        # Step 4
        print(
            "[BUZZ DEBUG] Step 4: "
            "Clicking textarea"
        )

        edit_input.click()

        print(
            "[BUZZ DEBUG] Step 4 SUCCESS"
        )

        # Step 5
        print(
            "[BUZZ DEBUG] Step 5: "
            "Selecting existing text"
        )

        edit_input.send_keys(
            Keys.CONTROL,
            "a"
        )

        print(
            "[BUZZ DEBUG] Step 5 SUCCESS"
        )

        # Step 6
        print(
            "[BUZZ DEBUG] Step 6: "
            "Clearing existing text"
        )

        edit_input.send_keys(
            Keys.BACKSPACE
        )

        cleared_value = edit_input.get_attribute(
            "value"
        )

        print(
            f"[BUZZ DEBUG] Textarea after clear: "
            f"{cleared_value!r}"
        )

        # Step 7
        print(
            f"[BUZZ DEBUG] Step 7: "
            f"Entering new text: {edit_text!r}"
        )

        edit_input.send_keys(
            edit_text
        )

        entered_value = edit_input.get_attribute(
            "value"
        )

        print(
            f"[BUZZ DEBUG] Textarea after new text: "
            f"{entered_value!r}"
        )

        if entered_value != edit_text:
            print(
                "[BUZZ DEBUG] WARNING: "
                "Textarea value does NOT match expected text!"
            )
        else:
            print(
                "[BUZZ DEBUG] SUCCESS: "
                "Textarea value matches expected text"
            )

        # Step 8
        print(
            "[BUZZ DEBUG] Step 8: "
            "Waiting for Save button"
        )

        self.wait_for_element_tuple(
            self.page.edit_post_button
        )

        print(
            "[BUZZ DEBUG] Step 8 SUCCESS"
        )

        # Step 9
        print(
            "[BUZZ DEBUG] Step 9: "
            "Clicking Save button"
        )

        self.click_tuple_locator(
            self.page.edit_post_button
        )

        print(
            "[BUZZ DEBUG] Step 9 SUCCESS: "
            "Save button clicked"
        )

        # Step 10
        print(
            "[BUZZ DEBUG] Step 10: "
            "Waiting for edit dialog to close"
        )

        # IMPORTANT:
        # edit_post_input is a tuple locator.
        # wait_for_invisibility() accepts tuple locators.
        self.wait_for_invisibility(
            self.page.edit_post_input
        )

        print(
            "[BUZZ DEBUG] Step 10 SUCCESS: "
            "Edit dialog closed"
        )

        print(
            "=========== BUZZ EDIT DEBUG END ===========\n"
        )

    def get_latest_post_text(self):
        print(
            "\n[BUZZ DEBUG] Reading latest post text"
        )

        element = self.wait_for_element_tuple(
            self.page.latest_post_text
        )

        text = element.text.strip()

        print(
            f"[BUZZ DEBUG] Latest post text returned: "
            f"{text!r}"
        )

        return text