import os
import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.Navigation_Menu import Navigation_Menu
from pageObjects.PIM_Add_Employee import PIM_Add_Employee
from pageObjects.PIM_Search_Page import PIM_Search_Page
from utilities.readProperties import ReadConfig

class Test_TC02_Add_Employee:

    app_URL = ReadConfig.get_Application_Url()
    username = ReadConfig.get_Username()
    password = ReadConfig.get_Password()

    @pytest.mark.regression
    def test_Add_Employee_With_Login_Credentials(self, setup):

        self.driver = setup
        self.driver.get(self.app_URL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        time.sleep(3)
        self.lp.enter_Username(self.username)
        self.lp.enter_Password(self.password)
        self.lp.click_login()
        time.sleep(3)
        self.nav = Navigation_Menu(self.driver)
        self.nav.click_Navigate_PIM()
        time.sleep(2)
        self.pim_search = PIM_Search_Page(self.driver)
        self.pim_search.click_Add_Button()
        time.sleep(2)
        self.pim_add = PIM_Add_Employee(self.driver)
        self.pim_add.set_First_Name('Tom')
        self.pim_add.set_Middle_Name('And')
        self.pim_add.set_Last_Name('Jerry')
        time.sleep(2)
        self.pim_add.click_create_login_details()
        time.sleep(2)
        self.pim_add.set_User_Name('hnbfhm')
        self.pim_add.set_Password('qwerty1234')
        self.pim_add.set_Confirm_Password('qwerty1234')
        time.sleep(3)
        self.pim_add.click_Save()
        time.sleep(6)
        actual_txt = self.pim_add.verifyTextInPIMPage()
        self.driver.close()
        if actual_txt == 'Personal Details':
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_PIM_Add_Employee.png")
            self.driver.close()
            assert False





