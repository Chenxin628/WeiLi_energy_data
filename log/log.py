#coding=utf-8
import logging
import os
import datetime

class CaseLog(object):

    def __init__(self):
        self.logger = logging.getLogger("test")
        # logging.Logger.manager.loggerDict.pop("test")
        # self.logger.handlers=[]
        # self.logger.removeHandler(self.logger.handlers)
        # if not self.logger.handlers:

        self.logger.setLevel(logging.DEBUG)
        #控制台输出日志
        # self.consle = logging.StreamHandler()
        # self.logger.addHandler(consle)
        # self.consle.setLevel(logging.INFO)


        #文件名字
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir,"logs")
        log_file = datetime.datetime.now().strftime("%Y-%m-%d")+".log"
        log_name = log_dir+"\\"+log_file
        # print(log_name)
        #文件输出日志
        self.file_handle = logging.FileHandler(log_name,'a',encoding='utf-8')
        self.file_handle.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(filename)s--> %(funcName)s %(levelno)s: %(levelname)s ----->%(message)s')
        self.file_handle.setFormatter(formatter)
        if not self.logger.handlers:
            self.logger.addHandler(self.file_handle)
            # self.logger.addHandler(self.consle)



    def get_log(self):
        return self.logger
        
    
    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        # self.logger.removeHandler(self.consle)

        self.file_handle.close()
        


if __name__ == '__main__':
    case = CaseLog()
    log = case.get_log()
    log.info('test')
    case.close_handle()