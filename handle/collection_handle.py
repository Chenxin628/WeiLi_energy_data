#coding=utf-8
import imp
from base.actionMethod import ActionMethod
from handle.login_test import LoginTest
from log.log import CaseLog
import os
file_path = os.path.join(os.getcwd()+"\\config\\CollectionElement.ini")
action=ActionMethod(file_path)

class Collection_handle():
    def __init__(self):
        LoginTest()
        self.log = CaseLog()
        self.logger = self.log.get_log()
        # 进入采集源配置
        action.select_data("网闸网关","ant-menu-submenu-inline")
        action.select_data("采集源配置","ant-menu-item")

    def select_table(self,table_t):
        action.click_element("SelectTableElement","select_collection_configure")
        action.click_element("SelectTableElement","select_Table")
        action.select_data(table_t,"ant-select-dropdown-menu-item")
        action.click_element("SelectTableElement","select_Table_submit")
        action.sleep_time()

    def add_collection(self,name_t,table_t,id_t,ip_t,port_t,byte_t,frequency_t=None):
        
        # 进入"脚本测试新增采集源"的"配置解析规则",判断是否存在热能表表计，存在则删除
        if action.select_data(name_t,"vxe-body--row"):
            action.delete_data(name_t,"vxe-body--row","配置解析规则","button")
            self.select_table(table_t)
            while action.get_element("DelectMeteElement","page").text!="共 0 条记录":
                action.click_element("DelectMeteElement","delete_Mete")
                action.get_xpath_element("确 定")
                action.sleep_time()
            action.select_data("采集源配置","ant-menu-item")
            
        # 判断是否有名称为"脚本测试新增采集源"的采集源，有则删除
        action.delete_data(name_t,"vxe-body--row","删除","button","确 定")
        action.get_xpath_text(name_t)


        # 添加采集源
        # 点击添加按钮
        action.click_element("AddCollectionElement","button_addCollection")
        # 采集分类备注
        action.element_send_keys("AddCollectionElement","addCollectionName",name_t)
        # ModBus服务ID
        action.element_send_keys("AddCollectionElement","addModBus_id",id_t)
        # IP
        action.element_send_keys("AddCollectionElement","addCollection_ip",ip_t)
        # 端口
        action.element_send_keys("AddCollectionElement","addCollection_port",port_t)
        # 字节大小端
        action.click_element("AddCollectionElement","addCollection_Byte")
        action.select_data(byte_t,"ant-select-dropdown-menu-item")
        # 采集频率（秒）
        if frequency_t!=None:
            action.element_send_keys("AddCollectionElement","addCollection_frequency",frequency_t)
        # 点击提交
        action.get_xpath_element("提 交")
        action.sleep_time()

 


    def add_parameter(self,table_t,name_t,type_t):
        # 进去表参数配置的热能表
        action.click_element("AddTableElement","table_parameters")
        action.click_element("AddTableElement","select_table_click")
        action.select_data(table_t,"ant-select-dropdown-menu-item")
        # 添加参数
        action.get_xpath_element("添加")
        action.get_element("AddTableElement","parameters_name")[-1].send_keys(name_t)
        action.get_element("AddTableElement","parameters_type")[-1].click()
        action.select_data(type_t,"ant-select-dropdown-menu-item")
        action.get_xpath_element("保 存")
        # 若保存失败则显示原因
        # if action.get_element("AddTableElement","warning"):
        #     text=action.get_element("AddTableElement","message").text
        #     self.logger.warning(text)
        #     action.click_element("AddTableElement","close")
        action.click_cancel("ant-message-notice-content","取 消")

    def add_meter(self,collect_t,table_t,num_t,name_t,methon_t,address_t):
        # 进入"脚本测试新增采集源"的"配置解析规则"
        action.delete_data(collect_t,"vxe-body--row","配置解析规则","button")
        # 查找热能表的表计
        self.select_table(table_t)
        # 添加表计
        action.click_element("AddMeterElement","add_meter")
        action.element_send_keys("AddMeterElement","add_meter_num",num_t)
        action.element_send_keys("AddMeterElement","add_meter_name",name_t)
        action.click_element("AddMeterElement","add_meter_method_click")
        action.select_data(methon_t,"ant-select-dropdown-menu-item")
        action.element_send_keys("AddMeterElement","add_meter_address",address_t)
        action.click_element("AddMeterElement","add_meter_submit")


    

if __name__ == '__main__':

    action.generate_report(Collection_handle,"采集源配置")
    action.close_browser()



