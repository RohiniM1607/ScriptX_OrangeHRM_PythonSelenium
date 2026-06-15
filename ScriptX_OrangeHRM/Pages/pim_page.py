class PimPage:

    pim_menu = "//span[text()='PIM']"
    add_employee_menu = "//a[text()='Add Employee']"
    first_name = "//input[@name='firstName']"
    last_name = "//input[@name='lastName']"
    emp_id = "//label[text()='Employee Id']/parent::div/following-sibling::div//input"
    submit_button = "//button[@type='submit']"
    pim_page_header = "//h6[text()='PIM']"
    personal_details_header = "//h6[text()='Personal Details']"
    success_message = "//div[contains(@class,'oxd-toast-content')]"

    employee_name_search = "(//input[@placeholder='Type for hints...'])[1]"
    search_button = "//button[@type='submit']"
    employee_record = "//div[@role='rowgroup']"
    no_records_found = "//span[text()='No Records Found']"