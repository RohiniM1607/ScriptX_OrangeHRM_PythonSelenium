from Pages.attendance_page import AttendancePage
from Actions.base_actions import BaseActions


class AttendanceAction:

    def __init__(self, driver):
        self.base = BaseActions(driver)
        self.page = AttendancePage

    def open_punch_page(self):
        self.base.click_element(self.page.time_menu)
        self.base.click_element(self.page.attendance_menu)
        self.base.click_element(self.page.punch_in_out_menu)

    def punch_in(self, note):
        self.open_punch_page()

        self.base.wait_for_element(self.page.note_textarea)
        self.base.enter_text(self.page.note_textarea, note)

        self.base.js_click(self.page.in_out_button)

        self.base.wait_for_element(self.page.punch_out_header)

    def punch_out(self, note):
        self.base.wait_for_element(self.page.note_textarea)

        self.base.enter_text(self.page.note_textarea, note)

        self.base.js_click(self.page.in_out_button)

        self.base.wait_for_element(self.page.punch_in_header)

    def is_punch_in_page_displayed(self):
        return self.base.is_element_displayed(self.page.punch_in_header)

    def is_punch_out_page_displayed(self):
        return self.base.is_element_displayed(self.page.punch_out_header)

    def is_success_message_displayed(self):
        return self.base.is_element_displayed(self.page.success_message)