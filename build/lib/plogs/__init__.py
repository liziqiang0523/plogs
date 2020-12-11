#!/usr/local/bin/python3
#coding=utf-8
#author:liziqiang
#creat_at:20201210
import time
import logging
import os
import sys
from . import logzero

'''
日志工具
彩色日志，日志保存，json日志格式
'''

#记录日志文件
if not os.path.exists('./log'):
    os.mkdir('./log')
#运行的python文件名称作为log文件名
file_name = os.path.split(sys.argv[0])[-1].split('.')[0]
log_time = time.strftime("%Y-%m-%d", time.localtime())
log_file = "./log/{}.log".format(file_name)
#设置日志保存文件并控制日志输出到屏幕
logzero.logfile(log_file, disableStderrLogger=False)
#设置日志格式
log_format = '%(color)s[%(levelname)1.3s %(asctime)s %(module)s:%(lineno)d] %(message)s%(end_color)s'
#log_format = '%(color)s[%(levelname)1.3s %(asctime)s %(module)s:%(lineno)d] %(message)s%(end_color)s'
#设置日志时间格式
formatter = logzero.LogFormatter(fmt=log_format,datefmt=time.strftime("%Y-%m-%d %H:%M:%S"))
logzero.formatter(formatter)
#得到一个普通格式日志对象
logger = logzero.setup_logger(name='log',logfile=log_file,level=logging.DEBUG,formatter=formatter)
#得到一个json格式日志对象
logger_json = logzero.setup_logger(name='json_log',logfile=log_file,level=logging.DEBUG,formatter=formatter,json=True)


