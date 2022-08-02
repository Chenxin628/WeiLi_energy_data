#coding=utf-8
from base.actionMethod import ActionMethod
from handle.login_test import LoginTest
from log.log import CaseLog
import unittest
import os

file_path = os.path.join(os.getcwd()+"\\config\\ProductionElement.ini")
action=ActionMethod(file_path)
class Production_handle(unittest.TestCase):
    def __init__(self):
        LoginTest()
        self.log = CaseLog()
        self.logger = self.log.get_log()
        #进入生产层级信息
        action.select_data("企业信息","ant-menu-submenu-inline")
        action.select_data("生产层级信息","ant-menu-item")


    def add_level(self,level_name_t,level_num_t):
        
        # 判断是否存在90工序，存在查看是否存在90工序下的单元，存在则删除
        if action.select_data(level_num_t,"custom-tree-node"):
            action.show_wait("vxe-pager--total")
            action.sleep_time()
            while action.get_element("UnitElement","page").text !="共 0 条记录":
                action.sleep_time()
                action.click_element("UnitElement","delete_unit")
                action.get_xpath_element("确 定")
                # action.delete_data("确定删除该工序单元吗？","ant-popover-inner","确 定","button")
                action.show_wait("anticon-check-circle")

            action.click_element("ProductionElement","delete_production_button")
            action.get_xpath_element("确 定")
        action.get_xpath_text(level_num_t)
        
 
        #添加90工序
        action.click_element("WholeElement","click_whole")
        action.click_element("ProductionElement","add_production")
        action.element_send_keys("ProductionElement","add_production_name",level_name_t)
        action.element_send_keys("ProductionElement","add_production_num",level_num_t)
        action.select_data("确 定","ant-modal-footer","button")[-1].click()
        # try:
        #     action.show_wait("anticon-check-circle")
        # except:
        #     action.select_data("关 闭","ant-modal-footer","button")[-2].click()
        # action.click_cancel("ant-message-notice-content","关 闭")
        if action.get_xpath_text(level_num_t):
            self.logger.info("找到文本:"+level_name_t+",生产层级添加成功")
            return True
        else:
            self.logger.info("未找到文本:"+level_name_t+",生产层级添加失败")
            return False

        


    def add_Unit(self,level_num_t,name_t,unit_num_t,yield_t,date_t):
        #添加90下的工序单元
        action.select_data(level_num_t,"custom-tree-node")
        action.select_data("新增","table-operator","button")[0].click()
        action.element_send_keys("UnitElement","add_unit_name",name_t) 
        action.element_send_keys("UnitElement","add_unit_num",unit_num_t) 
        action.element_send_keys("UnitElement","add_unit_yield",yield_t) 
        action.click_element("UnitElement","click_unit_date")
        action.element_send_keys("UnitElement","add_unit_date",date_t)
        action.select_data("确 定","ant-modal-footer","button")[-1].click()
        # try:
        #     action.show_wait("anticon-check-circle")
        # except:
        #     action.select_data("关 闭","ant-modal-footer","button")[-2].click()
        # action.click_cancel("ant-message-notice-content","关 闭")
        if action.get_xpath_text(name_t):
            self.logger.info("找到文本:"+name_t+",生产工序单元添加成功")
            return True
        else:
            self.logger.info("未找到文本:"+name_t+",生产工序单元添加失败")
            return False

        
        
  







if __name__ == '__main__':
    # unittest.main()
    action.generate_report(Production_handle,"生产层级信息")
    action.close_browser()


