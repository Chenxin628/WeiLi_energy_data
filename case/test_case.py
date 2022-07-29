#coding=utf-8
from base.actionMethod import ActionMethod
from collection_case import Test_Collect
from energy_type_case import Test_Energy_type
from energy_report_case import Test_Energy_report
from measuring_instruments_case import Test_Measuring_instruments
from yield_product_case import Test_Yield
from production_case import Test_Production
from collect_data_case import Test_Collect_data
from delete_case import Test_Delete_data

import os
import HTMLTestRunner
import unittest

    
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(Test_Collect))
suite.addTest(unittest.makeSuite(Test_Energy_type))
suite.addTest(unittest.makeSuite(Test_Production))
suite.addTest(unittest.makeSuite(Test_Energy_report))
suite.addTest(unittest.makeSuite(Test_Measuring_instruments))
suite.addTest(unittest.makeSuite(Test_Yield))
suite.addTest(unittest.makeSuite(Test_Collect_data))
suite.addTest(unittest.makeSuite(Test_Delete_data))


# runner = unittest.TextTestRunner()

file_path = os.path.join(os.getcwd()+"\\report\\"+"总流程报告.html")
f = open(file_path,'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="总流程报告",description=u"测试报告",verbosity=2)
runner.run(suite)

file_name = os.path.join(os.getcwd()+"\\config\\ProductionElement.ini")
action=ActionMethod(file_name)
action.close_browser()


    