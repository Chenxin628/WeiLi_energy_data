import imp
import unittest
import os
import HTMLTestReportCN

from log.log import CaseLog
log=CaseLog()
logger = log.get_log()
class TestDemo(unittest.TestCase):

    def test_one(self):
        logger.info("case name:test_one")
        assert 1 == 1

    def test_two(self):
        logger.info("case name:test_two")
        assert 'H' in "Helloword!"
        
    def test_three(self):
        logger.info("case name:test_three")
        assert 5 == 10
if __name__ == '__main__':
    file_path = os.path.join(os.getcwd()+"\\report\\111.html")
    f = open(file_path,'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDemo)
    runner = HTMLTestReportCN.HTMLTestRunner(stream=f,title="测试报告",description=u"测试报告",verbosity=2)
    runner.run(suite)
