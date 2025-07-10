import os.path
import pytest
import time
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.Dashboard_Page import Dashboard_Page
from utilities.readProperties import ReadConfig
from utilities import ExcelUtils


class Test_TC03_Login_DDT:

    appURL = ReadConfig.get_Application_Url()
    #  We are going to get the below two data's from the Excel sheet.
    # username = ReadConfig.get_Username()
    # password = ReadConfig.get_Password()
    path = os.path.abspath(os.curdir)+"\\testData\\OrangeHRM_Login_Data.xlsx"

    # def test_Login_DDT(self, setup):
    #     self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
    #     list_status = []
    #
    #     self.driver = setup
    #     self.driver.get(self.appURL)
    #     self.driver.maximize_window()
    #     time.sleep(3)
    #
    #     for r in range(2, self.rows + 1):
    #         self.lp = LoginPage(self.driver)
    #         self.hp = HomePage(self.driver)
    #         self.dp = Dashboard_Page(self.driver)
    #
    #         self.username = ExcelUtils.readData(self.path, 'Sheet1', r, 1)
    #         self.password = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
    #         self.expected = ExcelUtils.readData(self.path, 'Sheet1', r, 3)
    #
    #         self.lp.enter_Username(self.username)
    #         self.lp.enter_Password(self.password)
    #         time.sleep(3)
    #         self.lp.click_login()
    #         time.sleep(3)
    #
    #         self.actual_text = self.hp.verifyTextInHomePage()
    #
    #         if self.expected == 'Valid':
    #             if self.actual_text == True:
    #                 list_status.append('Pass')
    #                 # Logout to reset session
    #                 self.dp.click_User_Options()
    #                 time.sleep(2)
    #                 self.dp.click_Logout()
    #                 time.sleep(2)
    #             else:
    #                 list_status.append('Fail')
    #         elif self.expected == 'Invalid':
    #             if not self.actual_text:
    #                 list_status.append('Pass')
    #             else:
    #                 list_status.append('Fail')
    #                 # Logout if login was unexpectedly successful
    #                 self.dp.click_User_Options()
    #                 time.sleep(2)
    #                 self.dp.click_Logout()
    #                 time.sleep(2)
    #
    #         # Reload login page for next iteration
    #         self.driver.get(self.appURL)
    #         time.sleep(2)
    #
    #     if 'Fail' not in list_status:
    #         assert True
    #     else:
    #         assert False

    def test_Login_DDT(self,setup):
        self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
        list_status = []

        self.driver = setup
        self.driver.get(self.appURL)
        self.driver.maximize_window()
        time.sleep(3)
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.dp = Dashboard_Page(self.driver)

        for r in range(2, self.rows + 1):
            self.username = ExcelUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
            # self.expected = ExcelUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.enter_Username(self.username)
            self.lp.enter_Password(self.password)
            time.sleep(3)
            self.lp.click_login()
            time.sleep(3)

            # self.actual_text = self.hp.verifyTextInHomePage()
            # print(self.actual_text)
            self.dp.click_User_Options()
            self.dp.click_Logout()
            return

            # if self.actual_text == True:
            #     list_status.append('Pass')
            #     self.dp.click_User_Options()
            #     self.dp.click_Logout()
            # else:
            #     list_status.append('Fail')
            #     self.dp.click_User_Options()
            #     self.dp.click_Logout()
            #     time.sleep(2)

            # self.driver.get(self.appURL)
            # time.sleep(2)

        # if 'Fail' not in list_status:
        #     assert True
        # else:
        #     assert False

            # self.driver.close()
            # if self.actual_text == 'Dashboard':
            #     assert True
            # else:
            #     self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\test_login_page.png")
            #     self.driver.close()
            #     assert False

