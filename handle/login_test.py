#coding=utf-8
from base.actionMethod import ActionMethod
import os
class LoginTest():
    def __init__(self) :
        #登入操作
        file_path = os.path.join(os.getcwd()+"\\config\\LoginElement.ini")
        action_method=ActionMethod(file_path)
        action_method.get_url("http://172.16.2.210:8081/user/login?redirect=%2Fdashboard%2Fanalysis")
        
        action_method.show_wait("ant-layout-footer")
        
        #判断是否有登陆状态，有登陆态则跳过登陆步骤，没有则重新登陆
        if action_method.get_element("LoginElement","validation"):
            print("已有登陆状态，跳过登陆步骤")
        else:
            action_method.sleep_time()
            if action_method.get_element("LoginElement","again_login"):
                # print("找到重新登陆按钮")
                action_method.click_element("LoginElement","again_login")
            print("没有登陆状态，重新登陆")
            filename="D:\sihe\weili02\img\code.png"
            text=action_method.get_code(filename)
            action_method.element_send_keys("LoginElement","username","admin")
            action_method.element_send_keys("LoginElement","password","123456")
            action_method.element_send_keys("LoginElement","code_text",text)
            action_method.is_success(filename)

        if action_method.get_element("LoginElement","fold"):
            action_method.click_element("LoginElement","fold")
        
        # action_method.close_browser()
  

if __name__ == '__main__':
    LoginTest()
