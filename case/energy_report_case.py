from handle.energy_report_handle import Energy_report_handle
from base.actionMethod import ActionMethod
from log.log import CaseLog
import unittest
import ddt
import os

file_path = os.path.join(os.getcwd()+"\\config\\Energy_report_Element.ini")
action=ActionMethod(file_path)

@ddt.ddt
class Test_Energy_report(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.log = CaseLog()
        self.logger = self.log.get_log()
        self.energy_h=Energy_report_handle()
        self.logger.info("------执行添加能效报告case------")


      
    def tearDown(self) :
        
        for method_name,error in self._outcome.errors:
            if error:
                case_name=self._testMethodName
                file_path=os.path.join(os.getcwd()+"\\img\\"+case_name+".png")
                action.save_img(file_path)
        print("这是case的后置调键")
    
    @classmethod
    def tearDownClass(self):
        self.log.close_handle()
        action.refresh()


    
    @ddt.data(
        ['脚本测试新建报告']

    )
    @ddt.unpack
    def test_1_add_report(self,name_t):
        add_error=self.energy_h.add_report(name_t)
        # self.assertTrue(add_error,"测试成功")

    @ddt.data(
        ['脚本测试新建报告']

    )
    @ddt.unpack
    def test_2_add_module(self,name_t):
        add_error=self.energy_h.add_module(name_t)
        # self.assertTrue(add_error,"测试成功")
  



if __name__ == '__main__':
    # unittest.main()
    action.generate_report(Test_Energy_report,"能效报告")
    action.close_browser()



