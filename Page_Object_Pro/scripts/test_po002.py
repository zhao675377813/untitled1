import sys,os
sys.path.append(os.getcwd())
from  Page_Object_Pro.Page.search import Search_Page
import  pytest
from  appium import  webdriver
class Test_search_text:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0.0'
        desired_caps['deviceName'] = 'A5RNW18208010252'
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.HWSettings'

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)


        self.search_obj=Search_Page(self.driver)

    def teardown(self):
        ...
    @pytest.mark.parametrize("text",[1,2,3])
    def test_search(self,text):
        self.search_obj.search_text(text)


