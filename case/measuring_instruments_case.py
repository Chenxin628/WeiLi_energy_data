from handle.measuring_instruments_handle import Measuring_instruments_handle
from base.actionMethod import ActionMethod
from log.log import CaseLog
import unittest
import ddt
import os

file_path = os.path.join(os.getcwd()+"\\config\\Measuring_instruments_Element.ini")
action=ActionMethod(file_path)

@ddt.ddt
class Test_Measuring_instruments(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.log = CaseLog()
        self.logger = self.log.get_log()
        self.measuring_h=Measuring_instruments_handle()
        self.logger.info("------执行添加计量器具case------")


      
    def tearDown(self) :
        
        for method_name,error in self._outcome.errors:
            if error:
                case_name=self._testMethodName
                file_path=os.path.join(os.getcwd()+"\\img\\"+case_name+".png")
                action.save_img(file_path)

    
    @classmethod
    def tearDownClass(self):
        self.log.close_handle()
        action.refresh()

    
    @ddt.data(
        ['脚本测试新建计量器具','称重传感器','进出用能计量器具','焦炭','R-1001','脚本测试新增表参数','二次能源','1']


    )
    @ddt.unpack
    def test_1_add_instruments(self,name_t,type_t,grade_t,enery_t,meter_t,fetch,enerytpye_t,magnification_t):
        add=self.measuring_h.add_instruments(name_t,type_t,grade_t,enery_t,meter_t,fetch,enerytpye_t,magnification_t)
        self.assertTrue(add,"测试成功")




if __name__ == '__main__':
    # unittest.main()
    action.generate_report(Test_Measuring_instruments,"用能类型管理")
    action.close_browser()



