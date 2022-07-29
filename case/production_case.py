from handle.production_handle import Production_handle
from base.actionMethod import ActionMethod
from log.log import CaseLog
import unittest
import ddt
import os

file_path = os.path.join(os.getcwd()+"\\config\\ProductionElement.ini")
action=ActionMethod(file_path)

@ddt.ddt
class Test_Production(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.log = CaseLog()
        self.logger = self.log.get_log()
        self.production_h=Production_handle()
        self.logger.info("------执行添加生产层级case------")


      
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
        ['脚本测试新建工序','90']

    )
    @ddt.unpack
    def test_1_add_level(self,level_name_t,level_num_t):
        add_error=self.production_h.add_level(level_name_t,level_num_t)
        # self.assertTrue(add_error,"测试成功")

    @ddt.data(
        ['90','脚本测试新建工序单元','01','100','2022年07月19日']

    )
    @ddt.unpack
    def test_2_add_Unit(self,level_num_t,name_t,unit_num_t,yield_t,date_t):
        add_error=self.production_h.add_Unit(level_num_t,name_t,unit_num_t,yield_t,date_t)
        # self.assertTrue(add_error,"测试成功")



if __name__ == '__main__':
    # unittest.main()
    action.generate_report(Test_Production,"生产层级信息")
    action.close_browser()



