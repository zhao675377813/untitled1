from selenium.webdriver.common.by import By
import  pytest
from  Page_Object_Pro.Base.base import Base

class Send_Sms:
    def __init__(self,driver):
        self.base_obj=Base(driver)
        #添加按钮
        self.add_sms=((By.CLASS_NAME,"android.widget.TextView"))
        #输入收件人
        self.accept_user=(By.ID,"com.android.mms:id/recipients_editor")
        #输入信息
        self.input_sms=(By.ID,"com.android.mms:id/embedded_text_editor")
        #发送按钮
        self.button=(By.ID,"com.android.mms:id/button_singlesim_model")


    def add_sms_btn(self):
        self.base_obj.find_elements(self.add_sms)[2].click()


    def accept_user_input(self,phone):
        self.base_obj.input_element(self.accept_user,phone)

    def send_sms_input(self,text):
        self.base_obj.input_element(self.input_sms,text)

        self.base_obj.click_element(self.button)

