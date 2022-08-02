#coding=utf-8
from base.actionMethod import ActionMethod
from handle.login_test import LoginTest
from log.log import CaseLog
import os
file_path = os.path.join(os.getcwd()+"\\config\\Delete_Element.ini")
action=ActionMethod(file_path)
class Delete_handle():
    def __init__(self):
        LoginTest()
        self.log = CaseLog()
        self.logger = self.log.get_log()
        
    def delete_collect_data(self,collectdata_name_t):
        #进入采集数据项信息
        action.select_data("企业信息","ant-menu-submenu-inline")
        action.select_data("采集数据项信息","ant-menu-item")
        # 列表更改为表结构
        action.click_element("StateElement","state")
        action.click_element("StateElement","page")
        action.get_xpath_element("100条/页")
        action.show_wait("vxe-pager--next-btn.is--disabled")
        # 判断是否存在"脚本测试新建产品"，存在则删除
        element=action.select_form_data(collectdata_name_t,"body--wrapper","fixed-right--wrapper","vxe-body--row",-1,"button")
        if element:
            element.click()
            action.get_xpath_element("确 定")
        action.show_wait("ant-message-notice-content")
        
        if action.get_xpath_text(collectdata_name_t):
            self.logger.info("找到文本:"+collectdata_name_t+",采集项添加成功")
            return True
        else:
            self.logger.info("未找到文本:"+collectdata_name_t+",采集项添加失败")
            return False
       

        

    def delete_instruments(self,meter_t):
        #进入计量器具信息
        action.select_data("企业信息","ant-menu-submenu-inline")
        action.select_data("计量器具信息","ant-menu-item")
        action.click_element("StateElement","page")
        action.get_xpath_element("100条/页")
        action.show_wait("vxe-pager--next-btn.is--disabled")
        # 判断是否存在"R-1001"，存在则删除
        element=action.select_form_data(meter_t,"body--wrapper","fixed-right--wrapper","vxe-body--row",-1,"button")
        if element:
            element.click()
            action.get_xpath_element("确 定",-1)
        action.get_xpath_text(meter_t)



    def delete_Yield(self,Yield_name_t):
        #进入生产层级信息
        action.select_data("企业信息","ant-menu-submenu-inline")
        action.select_data("生产产品信息","ant-menu-item")
        # 判断是否存在"脚本测试新建产品"，存在则删除
        action.delete_data(Yield_name_t,"vxe-body--row","确 定","button")
        action.get_xpath_text(Yield_name_t)




    def delete_Production(self,level_num_t):
        #进入生产层级信息
        action.select_data("企业信息","ant-menu-submenu-inline")
        action.select_data("生产层级信息","ant-menu-item")
        # 判断是否存在90工序，存在查看是否存在90工序下的单元，存在则删除
        if action.select_data(level_num_t,"custom-tree-node"):
            action.show_wait("vxe-pager--total")
            action.sleep_time()
            while action.get_element("UnitElement","page").text !="共 0 条记录":
                action.click_element("UnitElement","delete_unit")
                # action.delete_data("确定删除该工序单元吗？","ant-popover-inner","确 定","button")
                action.get_xpath_element("确 定")
                action.show_wait("anticon-check-circle")

            action.click_element("UnitElement","delete_production_button")
            action.get_xpath_element("确 定")
        action.get_xpath_text(level_num_t)


        

    def delete_Energy_type(self,Energytype_name_t):
        #进入用能类型管理
        action.select_data("企业信息","ant-menu-submenu-inline")
        action.select_data("用能类型管理","ant-menu-item")
        # 判断是否存在"仪表风"，存在则删除
        action.delete_data(Energytype_name_t,"vxe-body--row","确 定","button")
        action.get_xpath_text(Energytype_name_t)




    def delete_Energy_report(self,Energyreport_name_t):
        action.get_xpath_element("能效报告")
        #进去报告模板定义
        action.get_xpath_element("报告模板定义")
        # 判断是否存在，存在则删除
        action.delete_data(Energyreport_name_t,"custom-tree-node","确 定","a")
        action.get_xpath_text(Energyreport_name_t)



    
    def delete_Collection(self,Collection_name_t,table_t):
        # 进入采集源配置
        action.select_data("网闸网关","ant-menu-submenu-inline")
        action.select_data("采集源配置","ant-menu-item")
        # 进入"脚本测试新增采集源"的"配置解析规则",判断是否存在热能表表计，存在则删除
        if action.select_data(Collection_name_t,"vxe-body--row"):
            action.delete_data(Collection_name_t,"vxe-body--row","配置解析规则","button")
            action.click_element("SelectTableElement","select_collection_configure")
            action.click_element("SelectTableElement","select_Table")
            action.select_data(table_t,"ant-select-dropdown-menu-item")
            action.click_element("SelectTableElement","select_Table_submit")
            action.sleep_time()
            while action.get_element("DelectMeteElement","page").text!="共 0 条记录":
                action.click_element("DelectMeteElement","delete_Mete")
                action.get_xpath_element("确 定")
                action.sleep_time()
            action.select_data("采集源配置","ant-menu-item")

        # 判断是否有名称为"脚本测试新增采集源"的采集源，有则删除
        action.delete_data(Collection_name_t,"vxe-body--row","删除","button","确 定")
        action.get_xpath_text(Collection_name_t)
        



    def main(self,collectdata_name_t,meter_t,Yield_name_t,level_num_t,Energytype_name_t,Energyreport_name_t,Collection_name_t,table_t):
        self.delete_collect_data(collectdata_name_t)
        self.delete_instruments(meter_t)
        self.delete_Yield(Yield_name_t)
        self.delete_Production(level_num_t)
        self.delete_Energy_type(Energytype_name_t)
        self.delete_Energy_report(Energyreport_name_t)
        self.delete_Collection(Collection_name_t,table_t)





# if __name__ == '__main__':
    # unittest.main()
    # action.generate_report(Collect_data_handle,"生产产品信息")
    # action.close_browser()



