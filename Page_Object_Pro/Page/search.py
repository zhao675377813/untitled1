from selenium.webdriver.common.by import By

from Page_Object_Pro.Base.base import Base

class Search_Page:
    def __init__(self,driver):

        self.s_b = (By.ID, "android:id/search_src_text")

        self.s_m = (By.ID, "android:id/search_src_text")

        self.s_p = (By.CLASS_NAME, "android.widget.ImageView")

        self.search_obj=Base(driver)
    def click_search(self):
        #dianji
        self.search_obj.click_element(self.s_b)
        #shuru
    def search_input(self,input_text):
        self.search_obj.input_element(self.s_m,input_text)
        #fanhui
    def click_return(self):
        self.search_obj.click_element(self.s_p)


