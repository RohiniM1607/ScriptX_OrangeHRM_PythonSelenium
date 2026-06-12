from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.employee_apply_leave_page import EmployeeApplyLeavePage


class EmployeeApplyLeaveActions:
    def __init__(self, driver):
        self.driver = driver
        self.page = EmployeeApplyLeavePage()
        self.wait = WebDriverWait(driver, 20)

    def navigate_to_apply_leave_page(self):
     self.wait.until(EC.element_to_be_clickable(self.page.leave_menu)).click()
     self.wait.until(EC.element_to_be_clickable(self.page.apply_sub_menu)).click()
     self.wait_for_loader_to_disappear()
    
    def select_leave_type(self, leave_type_name):
     self.wait_for_loader_to_disappear()
     dropdown = self.wait.until(EC.element_to_be_clickable(self.page.leave_type_dropdown))
     dropdown.click()
     options = self.wait.until( EC.visibility_of_all_elements_located( self.page.leave_type_options ) )

     for opt in options:
        if opt.text.strip().lower() == leave_type_name.lower():
            opt.click()
            break

    def enter_from_date(self, from_date):
     field = self.wait.until(
        EC.element_to_be_clickable(self.page.from_date_input)  )
     field.clear()
     field.send_keys(from_date)



    def enter_to_date(self, to_date):
        
        field = self.wait.until(
        EC.element_to_be_clickable(self.page.to_date_input)   )
        field.clear()
        field.send_keys(to_date)
        
    def enter_dates(self, from_date, to_date):
      fields = self.driver.find_elements(*self.page.Date_fields)

      fields[0].clear()
      fields[0].send_keys(from_date)

      fields[1].clear()
      fields[1].send_keys(to_date)    

    def enter_comments(self, comment):
        field = self.driver.find_element(*self.page.comments_textarea)
        field.clear()
        field.send_keys(comment)

    def apply(self):
        self.driver.find_element(*self.page.apply_button).click()

    def save(self):
        self.driver.find_element(*self.page.save_btn).click()

    def close_notification(self):
        self.driver.find_element(*self.page.close_info_notification).click()

    def wait_for_loader_to_disappear(self):
        self.wait.until(
            EC.invisibility_of_element_located(
                self.page.loader
            )
        )

    

    def get_success_message_display(self):
     toast_msg = self.wait.until(
        EC.visibility_of_element_located(
           self.page.success_msg 
        )
    ).is_displayed()
   

    def apply_leave(self, leave_type, from_date, to_date):
        self.navigate_to_apply_leave_page()
        self.select_leave_type(leave_type)
        # self.enter_from_date(from_date)
        # self.enter_to_date(to_date)
        self.enter_dates(from_date, to_date)
        self.apply()
        self.wait_for_loader_to_disappear()
        return self.get_success_message_display()  
       