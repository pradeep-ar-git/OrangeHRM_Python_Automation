import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.HomePage import HomePage
import os
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class TestTC01Login:

    app_URL = ReadConfig.get_Application_Url()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_login_with_valid_credentials(self, setup):
        self.logger.info('**** STARTED ****')
        self.driver = setup
        self.driver.get(self.app_URL)
        self.driver.maximize_window()
        time.sleep(3)
        self.lp = LoginPage(self.driver)
        self.lp.enter_Username(ReadConfig.get_Username())
        self.lp.enter_Password(ReadConfig.get_Password())
        self.lp.click_login()
        time.sleep(3)
        self.hp = HomePage(self.driver)
        actual_text = self.hp.verifyTextInHomePage()
        self.driver.close()
        if actual_text == 'Dashboard':
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_login_page.png")
            self.driver.close()
            assert False




        

