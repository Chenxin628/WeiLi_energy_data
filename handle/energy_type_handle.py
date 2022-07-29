#coding=utf-8
from base.actionMethod import ActionMethod
from handle.login_test import LoginTest
import unittest
import os

file_path = os.path.join(os.getcwd()+"\\config\\Energy_typeElement.ini")
action=ActionMethod(file_path)
class Energy_type_handle(unittest.TestCase):
    def __init__(self):
        LoginTest()
        #进入用能类型管理
        action.select_data("企业信息","ant-menu-submenu-inline")
        action.select_data("用能类型管理","ant-menu-item")

    def add_energy(self,name_t):
        # 判断是否存在"仪表风"，存在则删除
        action.delete_data(name_t,"vxe-body--row","确 定","button")
        action.get_xpath_text(name_t)


        #添加能源
        action.get_xpath_element("新增")
        action.click_element("AddEnergyElement","energy_click")
        action.select_data(name_t,"ant-select-dropdown-menu-item")
        action.get_xpath_element("确 定",-1)
        action.click_cancel("ant-message-notice-content","关 闭")
        

        # action.click_next()

        # action.close_browser()
    

    





if __name__ == '__main__':
    unittest.main()
    # action.generate_report(Energy_type_handle,"用能类型管理")
    # action.close_browser()


