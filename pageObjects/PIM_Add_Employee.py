from selenium.webdriver.common.by import By

class PIM_Add_Employee:

    ip_first_name = "//input[@name='firstName']"
    ip_middle_name = "//input[@name='middleName']"
    ip_last_name = "//input[@name='lastName']"
    ip_employee_id = "//label[text()='Employee Id']//following::input[contains(@class,'oxd-input')]"
    tog_create_login_details = "//span[contains(@class,'oxd-switch-input')]"
    ip_user_name = "//label[text()='Username']//following::input"
    rdo_enabled = "(//input[@type='radio'])[1]"
    rdo_disabled = "(//input[@type='radio'])[2]"
    ip_password = "//label[text()='Password']//following::input[1]"
    ip_confirm_password = "//label[text()='Confirm Password']//following::input[1]"
    btn_save = "//button[text()=' Save ']"
    txt_validation = "(//div[contains(@class,'orangehrm-horizontal-padding')]//h6)[1]"

    def __init__(self, driver):
        self.driver = driver

    def set_First_Name(self, first_name):
        self.driver.find_element(By.XPATH, self.ip_first_name).send_keys(first_name)

    def set_Middle_Name(self, middle_name):
        self.driver.find_element(By.XPATH, self.ip_middle_name).send_keys(middle_name)

    def set_Last_Name(self, last_name):
        self.driver.find_element(By.XPATH, self.ip_last_name).send_keys(last_name)

    def set_Employee_Id(self, emp_id):
        emp = self.driver.find_element(By.XPATH, self.ip_employee_id)
        emp.clear()
        emp.semd_keys(emp_id)

    def click_create_login_details(self):
        self.driver.find_element(By.XPATH, self.tog_create_login_details).click()

    def set_User_Name(self, user_name):
        self.driver.find_element(By.XPATH, self.ip_user_name).send_keys(user_name)

    def click_Enabled(self):
        self.driver.find_element(By.XPATH, self.rdo_enabled).click()

    def click_Disabled(self):
        self.driver.find_element(By.XPATH, self.rdo_disabled).click()

    def set_Password(self, password):
        self.driver.find_element(By.XPATH, self.ip_password).send_keys(password)

    def set_Confirm_Password(self, confirm_password):
        self.driver.find_element(By.XPATH, self.ip_confirm_password).send_keys(confirm_password)

    def click_Save(self):
        self.driver.find_element(By.XPATH, self.btn_save).click()

    def verifyTextInPIMPage(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_validation).text
        except:
            pass






