# coding=utf-8
import sys
import time
from typing import ByteString
# sys.path.append("D:\\sihe\\weili")
from selenium import webdriver
from util.read_ini import ReadIni
class FindElement(object):
    def __init__(self,driver,filename):
        self.driver = driver
        self.filename=filename
    
    def get_element(self,node=None,key=None):
        read_ini=ReadIni(self.filename)
        data=read_ini.get_value(node,key)
        by=data.split('>')[0]
        value=data.split('>')[1]
        num=data.split('>')[2]
        
        
        try:
            if num == 'null':
                if by=='id':
                    return self.driver.find_element_by_id(value)
                elif by=='name':
                    return self.driver.find_element_by_name(value)
                elif by=='class':
                    return self.driver.find_element_by_class_name(value)
                elif by=='css':
                    return self.driver.find_element_by_css_selector(value)  
                elif by=='xpath':
                    return self.driver.find_element_by_xpath(value)
                elif by=='tag':
                    return self.driver.find_elements_by_tag_name(value)
                elif by=='elements_id':
                    return self.driver.find_elements_by_id(value)
                elif by=='elements_name':
                    return self.driver.find_elements_by_name(value)
                elif by=='elements_class':
                    return self.driver.find_elements_by_class_name(value)
                elif by=='elements_css':
                    return self.driver.find_elements_by_css_selector(value)
            else:
                if by=='elements_id':
                    return self.driver.find_elements_by_id(value)[int(num)]
                elif by=='elements_name':
                    return self.driver.find_elements_by_name(value)[int(num)]
                elif by=='elements_class':
                    return self.driver.find_elements_by_class_name(value)[int(num)]
                elif by=='elements_css':
                    return self.driver.find_elements_by_css_selector(value)[int(num)]
            
            
        except:
            # self.driver.save_screenshot("D:/sihe/weili/img/%.png"%value)
            print("定位元素",by,"定位值",value,"数值",num,"不存在")
            return False

        # return element
        


        

