from selenium.webdriver.common.by import By

class LoginPage:

    ip_username = "//input[@name='username']"
    ip_password = "//input[@name='password']"
    btn_login = "//button[text()=' Login ']"
    txt_invalid_cred = "//p[text()='Invalid credentials']"
    txt_required = "//span[text()='Required']"

    def __init__(self, driver):
        self.driver = driver

    def enter_Username(self,username):
        self.driver.find_element(By.XPATH, self.ip_username).send_keys(username)

    def enter_Password(self,password):
        self.driver.find_element(By.XPATH, self.ip_password).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.btn_login).click()

    def error_Msg_Invalid_Credentials(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_invalid_cred).text
        except:
            pass

    def error_Msg_Required(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_required).text
        except:
            pass
