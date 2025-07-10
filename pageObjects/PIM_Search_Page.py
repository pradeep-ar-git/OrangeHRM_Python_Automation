from selenium.webdriver.common.by import By

class PIM_Search_Page:

    btn_add = "//button[text()=' Add ']"

    def __init__(self, driver):
        self.driver = driver

    def click_Add_Button(self):
        self.driver.find_element(By.XPATH, self.btn_add).click()

