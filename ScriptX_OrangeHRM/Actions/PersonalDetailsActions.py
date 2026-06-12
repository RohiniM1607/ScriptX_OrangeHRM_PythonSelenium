from Pages.MyInfoPage import MyInfoPage
from Utilities.Read_Config import get_config

class PersonalDetailsAction:

    def __init__(self, driver):
        self.page = MyInfoPage(driver)

    def navigate_to_personal_details(self):
        self.page.wait_for_page_load()
        self.page.click_personal_details_tab()

    def fill_personal_details(self):
        license_expiry  = get_config("personal details", "license_expiry")
        nationality     = get_config("personal details", "nationality")
        marital_status  = get_config("personal details", "marital_status")
        gender          = get_config("personal details", "gender")
        blood           = get_config("personal details", "blood")
        testfield       = get_config("personal details", "testfield")

        self.page.enter_license_expiry(license_expiry)
        self.page.select_nationality(nationality)
        self.page.select_marital_status(marital_status)
        self.page.select_gender(gender)
        self.page.click_blood_type(blood)
        self.page.type_blood_field(testfield)

    def save_and_verify(self):
        self.page.click_save()
        return self.page.verify_save_success()
    
    def save_and_verify1(self):
        self.page.click_save1()
        return self.page.success_message()