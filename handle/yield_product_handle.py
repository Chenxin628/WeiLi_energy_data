#coding=utf-8
from base.actionMethod import ActionMethod
from handle.login_test import LoginTest
import unittest
import os
from log.log import CaseLog

file_path = os.path.join(os.getcwd()+"\\config\\YieldElement.ini")
action=ActionMethod(file_path)
class Yield_handle(unittest.TestCase):
    def __init__(self):
        LoginTest()
        self.log = CaseLog()
        self.logger = self.log.get_log()

        #进入生产层级信息
        action.select_data("企业信息","ant-menu-submenu-inline")
        action.select_data("生产产品信息","ant-menu-item")


    def add_yield(self,name_t,num_t,company_t,industry_t,domestic_t,international_t):
        
        # 判断是否存在"脚本测试新建产品"，存在则删除
        action.delete_data(name_t,"vxe-body--row","确 定","button")
        action.get_xpath_text(name_t)
        

        #添加产品
        action.click_element("AddElement","add")
        action.element_send_keys("AddElement","add_name",name_t)
        action.element_send_keys("AddElement","add_num",num_t)
        action.element_send_keys("AddElement","add_company",company_t)
        action.element_send_keys("AddElement","add_industry",industry_t)
        action.element_send_keys("AddElement","add_domestic",domestic_t)
        action.element_send_keys("AddElement","add_international",international_t)
        action.select_data("确 定","ant-modal-footer","button")[-1].click()

        
        # try:
        #     action.show_wait("anticon-check-circle")
        # except:
        #     action.select_data("关 闭","ant-modal-footer","button")[-2].click()
        action.click_cancel("ant-message-notice-content","关 闭")
        if action.get_element("AddElement","messiage"):
            return True
        else:
            return False
    








if __name__ == '__main__':
    # unittest.main()
    action.generate_report(Yield_handle,"生产产品信息")
    action.close_browser()


