import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+'\\configurations\\config.ini')

class ReadConfig:

    @staticmethod
    def get_Application_Url():
        app_URL = (config.get('commonInfo', 'app_URL'))
        return app_URL

    @staticmethod
    def get_Username():
        username = (config.get('commonInfo', 'username'))
        return username

    @staticmethod
    def get_Password():
        pwd = (config.get('commonInfo', 'password'))
        return pwd


