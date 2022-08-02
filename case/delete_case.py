from handle.delect_handle import Delete_handle
from base.actionMethod import ActionMethod
from log.log import CaseLog
import unittest
import ddt
import os

file_path = os.path.join(os.getcwd()+"\\config\\Delete_Element.ini")
action=ActionMethod(file_path)
@ddt.ddt
class Test_Delete_data(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.log = CaseLog()
        self.logger = self.log.get_log()
        self.delete_h=Delete_handle()
        self.logger.info("------删除所有脚本新增数据------")
    
    def setUp(self):
        action.refresh()
        action.show_wait("ant-avatar-circle")
      
    def tearDown(self) :
        
        for method_name,error in self._outcome.errors:
            if error:
                case_name=self._testMethodName
                file_path=os.path.join(os.getcwd()+"\\img\\"+case_name+".png")
                action.save_img(file_path)

    
    @classmethod
    def tearDownClass(self):
        self.log.close_handle()


    # @ddt.data(
    #     ['脚本测试新建采集数据项','R-1001','脚本测试新建产品','90','仪表风','脚本测试新建报告','脚本测试新建采集源','热能表']
    # )
    # @ddt.unpack
    # def test_1_delete(self,collectdata_name_t,meter_t,Yield_name_t,level_num_t,Energytype_name_t,Energyreport_name_t,Collection_name_t,table_t):
    #     add_error=self.delete_h.main(collectdata_name_t,meter_t,Yield_name_t,level_num_t,Energytype_name_t,Energyreport_name_t,Collection_name_t,table_t)
    #     # self.assertTrue(add_error,"测试成功")
    @ddt.data(
        ['脚本测试新建采集数据项']
    )
    @ddt.unpack
    def test_1_delete_collect_data(self,collectdata_name_t):
        delete=self.delete_h.delete_collect_data(collectdata_name_t)
        self.assertFalse(delete,"删除成功")


    @ddt.data(
        ['R-1001']
    )
    @ddt.unpack
    def test_2_delete_instruments(self,meter_t):
        delete=self.delete_h.delete_instruments(meter_t)
        self.assertFalse(delete,"删除成功")



    @ddt.data(
        ['脚本测试新建产品']
    )
    @ddt.unpack
    def test_3_delete_Yield(self,Yield_name_t):
        delete=self.delete_h.delete_Yield(Yield_name_t)
        self.assertFalse(delete,"删除成功")



    @ddt.data(
        ['90']
    )
    @ddt.unpack
    def test_4_delete_Production(self,level_num_t):
        delete=self.delete_h.delete_Production(level_num_t)
        self.assertFalse(delete,"删除成功")



    @ddt.data(
        ['其他风']
    )
    @ddt.unpack
    def test_5_delete_Energy_type(self,Energytype_name_t):
        delete=self.delete_h.delete_Energy_type(Energytype_name_t)
        self.assertFalse(delete,"删除成功")



    @ddt.data(
        ['脚本测试新建报告']
    )
    @ddt.unpack
    def test_6_delete_Energy_report(self,Energyreport_name_t):
        delete=self.delete_h.delete_Energy_report(Energyreport_name_t)
        self.assertFalse(delete,"删除成功")



    @ddt.data(
        ['脚本测试新建采集源','热能表']
    )
    @ddt.unpack
    def test_7_delete_Collection(self,Collection_name_t,table_t):
        delete=self.delete_h.delete_Collection(Collection_name_t,table_t)
        self.assertFalse(delete,"删除成功")




if __name__ == '__main__':
    # unittest.main()
    action.generate_report(Test_Delete_data,"删除")
    action.close_browser()



