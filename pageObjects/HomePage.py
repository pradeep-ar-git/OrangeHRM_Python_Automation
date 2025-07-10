from selenium.webdriver.common.by import By


class HomePage:

    txt_dashboard = "//h6[text()='Dashboard']"

    def __init__(self,driver):
        self.driver = driver

    def verifyTextInHomePage(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_dashboard).text
        except:
            pass

