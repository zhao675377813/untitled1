import sys,os
sys.path.append(os.getcwd())
from  appium import webdriver
import  pytest
from Page_Object_Pro.Page.sms import Send_Sms
from  Page_Object_Pro.Base.base import Base
class Test_Search:
    def setup_class(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0.0'
        desired_caps['deviceName'] = 'A5RNW18208010252'
        desired_caps['appPackage'] = 'com.android.mms'
        desired_caps['appActivity'] = '.ui.ConversationList'

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.Teb_obj=Base(self.driver)
        self.search_obj=Send_Sms(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize("phone",['123456789'])
    def test_add_input_phone(self,phone):
        self.search_obj.add_sms_btn()

        self.search_obj.accept_user_input(phone)

    @pytest.mark.parametrize("text", ['123456789'])
    def test_input_sms(self,text):
        self.search_obj.send_sms_input(text)


if __name__ == '__main__':
    pytest.main()