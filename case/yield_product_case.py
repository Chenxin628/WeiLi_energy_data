from handle.yield_product_handle import Yield_handle
from base.actionMethod import ActionMethod
from log.log import CaseLog
import unittest
import ddt
import os

file_path = os.path.join(os.getcwd()+"\\config\\YieldElement.ini")
action=ActionMethod(file_path)

@ddt.ddt
class Test_Yield(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.log = CaseLog()
        self.logger = self.log.get_log()
        self.yield_h=Yield_handle()
        self.logger.info("------执行添加生产产品case------")


      
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
        ['脚本测试新建产品','9999','吨','111','222','333']

    )
    @ddt.unpack
    def test_1_add_level(self,name_t,num_t,company_t,industry_t,domestic_t,international_t):
        add=self.yield_h.add_yield(name_t,num_t,company_t,industry_t,domestic_t,international_t)
        self.assertTrue(add,"测试成功")


if __name__ == '__main__':
    # unittest.main()
    action.generate_report(Test_Yield,"生产产品信息")
    action.close_browser()



