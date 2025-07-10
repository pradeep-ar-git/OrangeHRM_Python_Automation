import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.HomePage import HomePage
import os
from utilities.readProperties import ReadConfig
from utilities.take_Screenshot import Screenshot


class TestTC01Login:

    app_URL = ReadConfig.get_Application_Url()
    password = ReadConfig.get_Password()
    username = ReadConfig.get_Username()

    @pytest.mark.sanity
    def test_login_with_valid_credentials(self, setup):
        self.driver = setup
        self.driver.get(self.app_URL)
        self.driver.maximize_window()
        time.sleep(3)
        self.lp = LoginPage(self.driver)
        self.lp.enter_Username(self.username)
        self.lp.enter_Password(self.password)
        self.lp.click_login()
        time.sleep(3)
        self.hp = HomePage(self.driver)
        actual_text = self.hp.verifyTextInHomePage()
        self.driver.close()
        if actual_text == 'Dashboard':
            assert True
        else:
            self.sc = Screenshot()
            self.sc.take_screenshot(self.driver, "test_TC01_Login_failure.png")
            # self.driver.save_screenshot(os.path.abspath(os.curdir)+".\\screenshots\\test_login_page.png")
            self.driver.close()
            assert False


    def test_login_with_invalid_credentials(self, setup):
        self.driver = setup
        self.driver.get(self.app_URL)
        self.driver.maximize_window()
        time.sleep(3)
        self.lp = LoginPage(self.driver)
        self.lp.enter_Username(self.username)
        self.lp.enter_Password('test123')
        self.lp.click_login()
        time.sleep(3)
        actual = self.lp.error_Msg_Invalid_Credentials()
        self.driver.close()
        if actual == 'Invalid credentials':
            assert True
        else:
            self.sc = Screenshot()
            self.sc.take_screenshot(self.driver, "test_TC01_Login_failure.png")
            self.driver.close()
            assert False

    def test_login_with_empty_credentials(self, setup):
        self.driver = setup
        self.driver.get(self.app_URL)
        self.driver.maximize_window()
        time.sleep(3)
        self.lp = LoginPage(self.driver)
        self.lp.enter_Username('')
        self.lp.enter_Password('')
        self.lp.click_login()
        time.sleep(3)
        actual = self.lp.error_Msg_Required()
        self.driver.close()
        if actual == 'Required':
            assert True
        else:
            self.sc = Screenshot()
            self.sc.take_screenshot(self.driver, "test_TC01_Login_failure.png")
            self.driver.close()
            assert False





        

