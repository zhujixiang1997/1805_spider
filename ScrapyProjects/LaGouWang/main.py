# -*- coding:utf-8 -*-
__author__ = 'zjx'
__date__ = '2018/12/21 0021 16:18'
import os, sys
from scrapy.cmdline import execute


sys.path.append(os.path.dirname(os.path.abspath(__file__)))  #当前main.py的文件夹路径

SPIDER_NAME = "lagou"   #此名称是我们采用 scrapy genspider  spider_name 指定的spider_name

execute(["scrapy", "crawl",  SPIDER_NAME])