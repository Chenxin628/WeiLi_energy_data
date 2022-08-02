#coding=utf-8
from base.actionMethod import ActionMethod
from handle.login_test import LoginTest
from log.log import CaseLog
import unittest
import os

file_path = os.path.join(os.getcwd()+"\\config\\Energy_typeElement.ini")
action=ActionMethod(file_path)
class Energy_type_handle(unittest.TestCase):
    def __init__(self):
        LoginTest()
        self.log = CaseLog()
        self.logger = self.log.get_log()
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
        # action.click_cancel("ant-message-notice-content","关 闭")
        if action.get_xpath_text(name_t):
            self.logger.info("找到文本:"+name_t+",能源类型添加成功")
            return True
        else:
            self.logger.info("未找到文本:"+name_t+",能源类型添加失败")
            return False

        

        # action.click_next()

        # action.close_browser()
    

    





if __name__ == '__main__':
    unittest.main()
    # action.generate_report(Energy_type_handle,"用能类型管理")
    # action.close_browser()


