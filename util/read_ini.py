import configparser
import os

class ReadIni(object):
    def __init__(self,filename=None):
        if filename==None:
            file_path = os.path.join(os.getcwd()+"\\config\\LoginElement.ini")
            self.filename=file_path
        # if node==None:
        #     self.node="LoginElement"
        else:
        #     self.node=node
            self.filename=filename
        # print(self.filename)
        self.cf=self.load_ini(self.filename)
        
    # 加载文件
    def load_ini(self,filename):
        cf=configparser.ConfigParser()
        cf.read(filename)
        return cf
    # 获取value值
    def get_value(self,node,key):
        data=self.cf.get(section=node,option=key)
        return data


if __name__ =='__main__':
    ReadIni(os.path.join(os.getcwd()+"\\config\\LoginElement.ini"))
    
