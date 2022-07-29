#coding=utf-8
from base.actionMethod import ActionMethod
from handle.login_test import LoginTest
import unittest
import os

file_path = os.path.join(os.getcwd()+"\\config\\Measuring_instruments_Element.ini")
action=ActionMethod(file_path)
class Measuring_instruments_handle(unittest.TestCase):
    def __init__(self):
        LoginTest()
        #进入计量器具信息
        action.select_data("企业信息","ant-menu-submenu-inline")
        action.select_data("计量器具信息","ant-menu-item")
        action.click_element("StateElement","page")
        action.get_xpath_element("100条/页")
        action.show_wait("vxe-pager--next-btn.is--disabled")

    def add_instruments(self,name_t,type_t,grade_t,enery_t,meter_t,fetch,enerytpye_t,magnification_t):
        
        # 判断是否存在"R-1001"，存在则删除
        element=action.select_form_data(meter_t,"body--wrapper","fixed-right--wrapper","vxe-body--row",-1,"button")
        if element:
            element.click()
            action.get_xpath_element("确 定")
        action.get_xpath_text(name_t)
        
        action.get_xpath_element("新增")
        # 计量器具名称
        action.get_placeholder_element("请输入计量器具名称",name_t)
        # 计量器具类型
        action.get_xpath_element("请选择计量器具类型")
        action.sleep_time()
        action.select_data(type_t,"ant-select-tree-treenode-switcher-open")
        # 计量器具等级
        action.get_xpath_element("请选择计量器具等级")
        action.select_data(grade_t,"ant-select-dropdown-menu-item")
        # 计量相关参数
        action.get_xpath_element("请选择计量相关参数")
        action.select_data(enery_t,"ant-select-dropdown-menu-item")
        # 计量器具编号（表计编号）
        action.get_placeholder_element("请输入计量器具编号（表计编号）",meter_t)
        # 表计取数字段
        action.get_xpath_element("请选择表计取数字段")
        action.get_xpath_element(fetch)
        # 用能方式
        action.get_xpath_element("请选择用能方式")
        action.select_data("在线使用","ant-select-dropdown-menu-item")
        # 计量参数类型
        action.get_xpath_element("请选择计量参数类型")
        action.select_data(enerytpye_t,"ant-select-dropdown-menu-item")
        # 是否与监测工作相关
        action.get_xpath_element("请选择是否与监测工作相关")
        action.select_data("是","ant-select-dropdown-menu-item")
        # 计量器具的生产厂家
        action.get_placeholder_element("请输入计量器具的生产厂家","产家111")
        # 型号规格
        action.get_placeholder_element("请输入型号规格","型号111")
        # 准确度等级
        action.get_placeholder_element("请输入准确度等级","等级111")
        # 测量范围
        action.get_placeholder_element("请输入测量范围","范围111")
        # 用能单位内部的计量器具管理编号
        action.get_placeholder_element("请输入用能单位内部的计量器具管理编号","编号111")
        # 检定/校准状态
        action.get_xpath_element("请选择检定/校准状态")
        action.select_data("合格","ant-select-dropdown-menu-item")
        # 检定/校准周期
        action.get_placeholder_element("请输入检定/校准周期，按 x 月或 x 年填写","1年")
        # 检验机构
        action.get_placeholder_element("请输入检验机构","检验机构")
        # 安装地点
        action.get_placeholder_element("请输入安装地点","安装地点")
        # 安装方
        action.get_xpath_element("请选择安装方")
        action.select_data("用能单位","ant-select-dropdown-menu-item")
        # 最近检定/校准时间
        action.click_element("AddElement","last_time")
        action.click_element("AddElement","send_time")
        # 下次检定/校准时间
        action.click_element("AddElement","send_time")
        # 安装时间
        action.click_element("AddElement","install_time")
        action.click_element("AddElement","send_time")
        # 状态发生时间
        action.click_element("AddElement","state_time")
        action.click_element("AddElement","send_time")
        # 倍率
        action.get_placeholder_element("请输入倍率",magnification_t)
        # PT
        action.get_placeholder_element("请输入PT","1")
        # CT
        action.get_placeholder_element("请输入CT","1")

        # 接入系统
        action.get_xpath_element("请选择接入系统")
        action.select_data("用能单位自身管理系统","ant-select-dropdown-menu-item")
        # 目前状态
        action.get_xpath_element("请选择目前状态")
        action.select_data("正常","ant-select-dropdown-menu-item")

        action.select_data("确 定","ant-modal-footer","button")[-1].click()

        # try:
        #     action.show_wait("anticon-check-circle")
        # except:
        #     action.select_data("关 闭","ant-modal-footer","button")[-2].click()
        action.click_cancel("ant-message-notice-content","关 闭")
        

    # def test_2_add(self):
    #     action.click_next()

    #     # action.sleep_time()
    #     action.close_browser()
    







if __name__ == '__main__':
    unittest.main()
    # action.generate_report(Measuring_instruments_handle,"计量器具信息")
    # action.close_browser()



