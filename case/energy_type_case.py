from handle.energy_type_handle import Energy_type_handle
from base.actionMethod import ActionMethod
from log.log import CaseLog
import unittest
import ddt
import os

file_path = os.path.join(os.getcwd()+"\\config\\Energy_typeElement.ini")
action=ActionMethod(file_path)

@ddt.ddt
class Test_Energy_type(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.log = CaseLog()
        self.logger = self.log.get_log()
        self.energy_h=Energy_type_handle()
        self.logger.info("------执行添加用能类型case------")


      
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
        ['其他风']

    )
    @ddt.unpack
    def test_1_add_report(self,name_t):
        add_error=self.energy_h.add_energy(name_t)
        # self.assertTrue(add_error,"测试成功")




if __name__ == '__main__':
    # unittest.main()
    action.generate_report(Test_Energy_type,"用能类型管理")
    action.close_browser()



