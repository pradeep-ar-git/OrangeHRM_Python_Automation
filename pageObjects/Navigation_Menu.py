from selenium.webdriver.common.by import By

class Navigation_Menu:

    nav_admin = "//span[text()='Admin']"
    nav_pim = "//span[text()='PIM']"
    nav_leave = "//span[text()='Leave']"
    nav_time = "//span[text()='Time']"
    nav_recruitment = "//span[text()='Recruitment']"
    nav_my_info = "//span[text()='My Info']"
    nav_performance = "//span[text()='Performance']"
    nav_dashboard = "//span[text()='Dashboard']"
    nav_directory = "//span[text()='Directory']"
    nav_maintenance = "//span[text()='Maintenance']"
    nav_claim = "//span[text()='Claim']"
    nav_buzz = "//span[text()='Buzz']"

    def __init__(self, driver):
        self.driver = driver

    def click_Navigate_Admin(self):
        self.driver.find_element(By.XPATH, self.nav_admin).click()

    def click_Navigate_PIM(self):
        self.driver.find_element(By.XPATH, self.nav_pim).click()

    def click_Navigate_Leave(self):
        self.driver.find_element(By.XPATH, self.nav_leave).click()

    def click_Navigate_Time(self):
        self.driver.find_element(By.XPATH, self.nav_time).click()

    def click_Navigate_Recruitment(self):
        self.driver.find_element(By.XPATH, self.nav_recruitment).click()

    def click_Navigate_MyInfo(self):
        self.driver.find_element(By.XPATH, self.nav_my_info).click()

    def click_Navigate_Performance(self):
        self.driver.find_element(By.XPATH, self.nav_performance).click()

    def click_Navigate_Dashboard(self):
        self.driver.find_element(By.XPATH, self.nav_dashboard).click()

    def click_Navigate_Directory(self):
        self.driver.find_element(By.XPATH, self.nav_directory).click()

    def click_Navigate_Maintenance(self):
        self.driver.find_element(By.XPATH, self.nav_maintenance).click()

    def click_Navigate_Claim(self):
        self.driver.find_element(By.XPATH, self.nav_claim).click()

    def click_Navigate_Buzz(self):
        self.driver.find_element(By.XPATH, self.nav_buzz).click()

