from  appium import  webdriver
from selenium.webdriver.common.by import By
from Page_Object_Pro.Base.base import Base
import pytest
from  Page_Object_Pro.Page.sms import Send_Sms
class  Test_abc:
    def setup_class(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0.0'
        desired_caps['deviceName'] = 'A5RNW18208010252'
        desired_caps['appPackage'] = 'com.android.mms'
        desired_caps['appActivity'] = '.ui.ConversationList'

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.Tea_obj=Base(driver)
        self.Tes_obj=Send_Sms(driver)
    def test_abc(self):

        self.Tes_obj.add_sms_btn()


if __name__ == '__main__':
    pytest.main()