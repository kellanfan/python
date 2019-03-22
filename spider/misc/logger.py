#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Tue 28 Aug 2018 10:55:09 PM CST

# File Name: logger.py
# Description:

"""
import logging
import yaml
import threading
from logging.handlers import RotatingFileHandler

class Logger(object):
    def __init__(self, config_file):
        '''init logger'''
        self.logger = logging.getLogger('Logger')
        config = self.__getconfig(config_file)

        mythread=threading.Lock()
        mythread.acquire()
      
        self.log_file_path = config.get('log_file_path')
        self.maxBytes = eval(config.get('maxBytes'))
        self.backupCount = int(config.get('backupCount'))
        self.outputConsole_level = int(config.get('outputConsole_level'))
        self.outputFile_level = int(config.get('outputFile_level'))
        self.outputConsole = int(config.get('outputConsole'))
        self.outputFile = int(config.get('outputFile'))
        self.formatter = logging.Formatter('%(asctime)s  %(levelname)s -%(thread)d- %(filename)s : %(message)s')
  
        mythread.release()

    def __call__(self):
        return self.outputLog()

    def outputLog(self):
        '''put out log'''
        if self.outputConsole == 1:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            self.logger.setLevel(self.outputConsole_level)
            self.logger.addHandler(console_handler)
        else:
            pass
   
        if self.outputFile == 1:
            file_handler = RotatingFileHandler(self.log_file_path, maxBytes=self.maxBytes, backupCount=self.backupCount)
            file_handler.setFormatter(self.formatter)
            self.logger.setLevel(self.outputFile_level)
            self.logger.addHandler(file_handler)
        else:  
            pass  
   
        return self.logger 

    def __getconfig(self,config_file):
        with open(config_file) as f:
            configs = yaml.load(f.read())
        return configs

if __name__ == '__main__':
    mylog = Logger('logger.yml')
    aa = mylog()
    aa.error('aaa')
