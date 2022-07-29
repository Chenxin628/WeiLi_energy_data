#coding=utf-8
import imp
from base.actionMethod import ActionMethod
from login_test import LoginTest
import unittest
import os

file_path = os.path.join(os.getcwd()+"\\config\\Meter_energy_Element.ini")
action=ActionMethod(file_path)
class Test001_handle(unittest.TestCase):
    def test_1_case01(self):
        LoginTest()
        action.select_data("能源报表","ant-menu-submenu-inline")
        action.select_data("表计能耗报表","ant-menu-item")
        action.get_xpath_element("按日分析")
        action.click_element("case","page")
        action.select_form_data("T10-0001","fixed-left--wrapper","body--wrapper","vxe-body--row",5,"td")

       


       
        action.close_browser()
        

if __name__ == '__main__':
    unittest.main()


