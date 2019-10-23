
from  appium import  webdriver
import  pytest
from Page_Object_Pro.Page.search import Search_Page
from  Page_Object_Pro.Base.base import Base

class Test_Searchx:
    def setup_class(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0.0'
        desired_caps['deviceName'] = 'A5RNW18208010252'
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.HWSettings'

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.search_obj=Search_Page(self.driver)
        self.searchs_obj = Base(self.driver)

    def teardown_class(self):
        self.driver.quit()


    def test_search01(self):
        self.search_obj.click_search()

    @pytest.mark.parametrize("text",[1,2,3])
    def test_search02(self,text):
        self.search_obj.search_input(text)

    def test_search03(self):
        self.search_obj.click_return()

if __name__ == '__main__':
    pytest.main()