from handle.collect_data_handle import Collect_data_handle
from base.actionMethod import ActionMethod
from log.log import CaseLog
import unittest
import ddt
import os
file_path = os.path.join(os.getcwd()+"\\config\\Collect_data_Element.ini")
action=ActionMethod(file_path)

@ddt.ddt
class Test_Collect_data(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.log = CaseLog()
        self.logger = self.log.get_log()
        self.collect_h=Collect_data_handle()
        self.logger.info("------执行添加采集数据项case------")



    def tearDown(self) :
        
        for method_name,error in self._outcome.errors:
            if error:
                case_name=self._testMethodName
                file_path=os.path.join(os.getcwd()+"\\img\\"+case_name+".png")
                action.save_img(file_path)

    
    @classmethod
    def tearDownClass(self):
        self.log.close_handle()


    @ddt.data(
        ['脚本测试新建采集数据项','生产工序单元','脚本测试新建工序','脚本测试新建工序单元','二次能源','焦炭','购进已消费','实时，日，月','111','现场仪表','是','否']
    )
    @ddt.unpack
    def test_1_add_collect(self,name_t,range_t,product_t,product_unit_t,data_type_t,data_class_t,usage_code_t,frequency_t,max_t,data_source_t,formula_t,repor_t,equipment_t=None):
        add_error=self.collect_h.add_collect_data(name_t,range_t,product_t,product_unit_t,data_type_t,data_class_t,usage_code_t,frequency_t,max_t,data_source_t,formula_t,repor_t,equipment_t)
        self.assertTrue(add_error,"测试成功")




if __name__ == '__main__':
    # unittest.main()
    action.generate_report(Test_Collect_data,"采集数据项信息")
    action.close_browser()



