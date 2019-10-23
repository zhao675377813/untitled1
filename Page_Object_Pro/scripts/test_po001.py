from selenium.webdriver.common.by import By
import  pytest
from Page_Object_Pro.Base.base  import Base
from appium import  webdriver

class Test_search:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0.0'
        desired_caps['deviceName'] = 'A5RNW18208010252'
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.HWSettings'

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        self.base_obj=Base(self.driver)
    def test_po001(self):
        s_b=(By.ID,"android:id/search_src_text")
        self.base_obj.click_element(s_b)
        s_m=(By.ID,"android:id/search_src_text")
        self.base_obj.input_element(s_m,'123')
        s_p=(By.CLASS_NAME,"android.widget.ImageView")
        self.base_obj.click_element(s_p)

    def teardown(self):
        self.driver.quit()





