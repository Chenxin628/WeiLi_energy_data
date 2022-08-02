import os
import sys
curPath = os.path.abspath(os.path.join(os.getcwd()))
sys.path.append(curPath)
from handle.collection_handle import Collection_handle
from base.actionMethod import ActionMethod
# from log.log import CaseLog
import unittest
import ddt
file_path = os.path.join(os.getcwd()+"\\config\\CollectionElement.ini")
action=ActionMethod(file_path)

@ddt.ddt
class Test_Collect(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # self.log = CaseLog()
        # self.logger = self.log.get_log()
        self.collect_h=Collection_handle()
        # self.logger.info("------执行添加采集源case------")

    
    # def setUp(self):
    #     # action.refresh()
    #     self.logger.info("this is chrome")

    def tearDown(self) :
        
        for method_name,error in self._outcome.errors:
            if error:
                case_name=self._testMethodName
                file_path=os.path.join(os.getcwd()+"\\img\\"+case_name+".png")
                action.save_img(file_path)

    
    @classmethod
    def tearDownClass(self):
        # self.log.close_handle()
        # action.close_browser()
        action.refresh()
        

    @ddt.data(
        ['脚本测试新建采集源','热能表','1','1.1.1.1','1111','Big-Endian']

    )
    @ddt.unpack
    def test_1_add_collect(self,name_t,table_t,id_t,ip_t,port_t,byte_t,frequency_t=None):
        add=self.collect_h.add_collection(name_t,table_t,id_t,ip_t,port_t,byte_t,frequency_t)
        self.assertTrue(add,"测试成功")

    @ddt.data(
        ['热能表','脚本测试新增表参数','累计值']

    )
    @ddt.unpack
    def test_2_add_parameter(self,table_t,name_t,type_t):
        add_error=self.collect_h.add_parameter(table_t,name_t,type_t)
        # self.assertTrue(add_error,"测试成功")
    
    @ddt.data(
        ['脚本测试新建采集源','热能表','R-1001','脚本测试新建表计','Float','14']

    )
    @ddt.unpack
    def test_3_add_meter(self,collect_t,table_t,num_t,name_t,methon_t,address_t):
        add=self.collect_h.add_meter(collect_t,table_t,num_t,name_t,methon_t,address_t)
        self.assertTrue(add,"测试成功")




if __name__ == '__main__':
    # unittest.main()
    action.generate_report(Test_Collect,"采集源配置")
    action.close_browser()



