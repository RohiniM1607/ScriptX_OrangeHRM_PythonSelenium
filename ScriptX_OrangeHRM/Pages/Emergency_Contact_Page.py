class EmergencyContactsPage:

    lnk_emergency_contacts = "//a[normalize-space()='Emergency Contacts']"
    btn_add                = "//h6[text()='Assigned Emergency Contacts']/following::button[contains(@class,'oxd-button')][1]"
    txt_name               = "//label[text()='Name']/following::input[1]"
    txt_relationship       = "//label[text()='Relationship']/following::input[1]"
    txt_home_telephone     = "//label[text()='Home Telephone']/following::input[1]"
    txt_mobile             = "//label[text()='Mobile']/following::input[1]"
    txt_work_telephone     = "//label[text()='Work Telephone']/following::input[1]"
    btn_save               = "(//div[contains(@class,'orangehrm-card-container')])[1]//button[normalize-space()='Save']"
    msg_success            = "//div[contains(@class,'oxd-toast-content')]//p[1]"
    load_spinner           = "//div[contains(@class,'oxd-loading-spinner-container')]"