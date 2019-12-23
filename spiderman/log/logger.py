#/usr/bin/env python
#coding=utf8
"""
# Author: kellanfan
# Created Time : Tue 28 Aug 2018 10:55:09 PM CST

# File Name: logger.py
# Description:

"""
import os
import logging
from logging.handlers import RotatingFileHandler

class WFLevelFilter(logging.Filter):
    def filter(self, record):
        return (record.levelno > logging.INFO)

logger_name = os.environ.get('LOG_NAME', 'spider')
debug_enabled = os.environ.get("LOGGER_DEBUG", "false")
formatter = logging.Formatter('%(asctime)s  %(levelname)s -%(thread)d- %(filename)s : %(message)s')
rootLogger = logging.getLogger()
log_home = '/var/log/spider'
if not os.path.exists(log_home):
    os.system('mkdir -p {}'.format(log_home))
# to screen
#console = logging.StreamHandler()
#console.setFormatter(formatter)
#rootLogger.addHandler(console)

# to log file
logfile = log_home + "/{}.log".format(logger_name)
files = RotatingFileHandler(logfile, mode='a', maxBytes=100000000, backupCount=10)
files.setFormatter(formatter)
rootLogger.addHandler(files)

# to log file, but only warning/error/fatal messages
logfile = log_home + "/{}.log.wf".format(logger_name)
wffiles = RotatingFileHandler(logfile, mode='a', maxBytes=100000000, backupCount=10)
wffiles_filter = WFLevelFilter()
wffiles.addFilter(wffiles_filter)
wffiles.setFormatter(formatter)
rootLogger.addHandler(wffiles)

logger = logging.getLogger(logger_name)
logger.setLevel(logging.DEBUG if debug_enabled == "true" else logging.INFO)

__all__ = ['logger']
