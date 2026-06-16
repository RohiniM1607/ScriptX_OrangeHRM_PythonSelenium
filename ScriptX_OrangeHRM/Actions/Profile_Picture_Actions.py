import os
from Pages.Profile_Picture_Page import ProfilePicturePage
from Pages.DashBoard_Page import DashBoardPage
from Actions.base_actions import BaseActions
from Utilities.Read_Config import get_config


class ProfilePictureAction:

    def __init__(self, driver):
        self.base      = BaseActions(driver)
        self.page      = ProfilePicturePage()
        self.dashboard = DashBoardPage()
        self.driver    = driver

    def verify_dashboard_loaded(self):
        return self.base.is_element_displayed(self.dashboard.txt_dashboard)

    def navigate_to_my_info(self):
        self.base.click_element(self.dashboard.lnk_my_info)

    def click_profile_picture(self):
        self.base.wait_for_element_invisible(self.page.load_spinner)
        self.base.js_click(self.page.clk_profile)

    def click_add_icon(self):
        self.base.wait_for_element_invisible(self.page.load_spinner)
        self.base.js_click(self.page.btn_add_icon)

    def upload_profile_picture(self):
        file_path = os.path.abspath(get_config("profile picture", "image_path"))
        self.base.upload_file(self.page.inp_file_upload, file_path)

    def save_profile_picture(self):
        self.base.js_click(self.page.btn_save)

    def verify_upload_success(self):
        return self.base.is_element_displayed(self.page.msg_success)

    def upload_and_verify(self):
        self.click_profile_picture()   
        self.click_add_icon()           
        self.upload_profile_picture() 
        self.save_profile_picture()    
        return self.verify_upload_success()  