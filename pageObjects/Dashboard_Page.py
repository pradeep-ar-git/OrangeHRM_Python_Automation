from selenium.webdriver.common.by import By

class Dashboard_Page:

    user_options = "//p[@class='oxd-userdropdown-name']"
    logout = "//a[text()='Logout']"

    def __init__(self, driver):
        self.driver =  driver

    def click_User_Options(self):
        self.driver.find_element(By.XPATH, self.user_options).click()

    def click_Logout(self):
        self.driver.find_element(By.XPATH, self.logout).click()

