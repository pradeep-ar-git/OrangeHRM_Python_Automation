from datetime import datetime
import pytest
from selenium import webdriver
import os

@pytest.fixture()
def setup(browser):
    if browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()
    return driver

# Below two methods are mandatory if we need to get the parameters from command prompt for cross browser testing.
# This will get the value from CLI
def pytest_addoption(parser):
    parser.addoption('--browser')

# This will return the browser value to the setup method.
@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')

####################### HTML REPORT #####################

#It is a hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Orange HRM'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester Name'] = 'Pradeep A R'
    config._metadata['Browser'] = 'Chrome'

# It is a hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata (metadata) :
    metadata.pop ("JAVA_HOME", None)
    metadata.pop ("Plugins", None)

# Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config) :
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime('%d-%m-%Y %H-%M-%S')+".html"



