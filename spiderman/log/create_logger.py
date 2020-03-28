# pylint: disable=no-member
# -*- encoding: utf-8 -*-
'''
@File    :   create_logger.py
@Time    :   2020/02/10 09:31:27
@Author  :   Kellan Fan 
@Version :   1.0
@Contact :   kellanfan1989@gmail.com
@Desc    :   None
'''

# here put the import lib
import os
import logging
from logging.handlers import RotatingFileHandler
import platform

def create_logger(log_name='spider'):
    if platform.system() == 'Linux':
        log_path = '/var/log/spider'
    elif platform.system() == 'Windows':
        log_path = 'C:\\log\\spider'
    else:
        log_path = '.'
    # make sure the log dir exist
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    #create format
    fmt = '%(asctime)s.%(msecs)d %(levelname)s %(process)d-%(thread)d: %(message)s (%(filename)s:%(lineno)d)'
    datefmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(fmt, datefmt)
    # create file handler
    log_file = log_path + '/' + log_name + '.log'
    fh = RotatingFileHandler(log_file, mode='a', maxBytes=100000000, backupCount=10)
    fh.setLevel(logging.DEBUG)
    fh.set_name(log_name)
    fh.setFormatter(formatter)

    # create logger
    logger = logging.getLogger(log_name)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        logger.addHandler(fh)
    return logger