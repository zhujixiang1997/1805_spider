# -*- coding: utf-8 -*-
__author__ = 'zjx'
__date__ = '2018/12/25 下午3:01' 

import pymongo
from ScrapyProjects.BookToscrape.BookToscrape.settings import MONGODB_SETTINGS

class MongoPipeLines(object):
	def __init__(self, db_host, db_name, db_port, collect_book, collect_book_detail):
		self.__db_host = db_host
		self.__db_name = db_name
		self.__db_port = db_port
		self.__collect_book = collect_book
		self.__collect_book_detail = collect_book_detail

	@classmethod
	def from_crawler(cls, *args, **kwargs):
		db_host = MONGODB_SETTINGS['db_host']
		db_name = MONGODB_SETTINGS['db_name']
		db_port = MONGODB_SETTINGS['db_port']
		collect_book = MONGODB_SETTINGS['collect_book']
		book_detail = MONGODB_SETTINGS['collect_book_detail']
		return cls(db_host=db_host, db_name=db_name, db_port=db_port,
				   collect_book=collect_book, collect_book_detail=book_detail)


	def open_spider(self, spider):
		'''
		初始工作，连接数据库操作
		:param spider:
		:return:
		'''
		self.__client = pymongo.MongoClient(host=self.__db_host,
            port=self.__db_port)
		self.__db = self.__client[self.__db_name]


	def process_item(self, item, spider):
		'''
		mongodb 处理数据操作函数
		:param item:
		:param spider:
		:return:
		'''

		item_name = item.get_name()
		if item_name == "BooktoscrapeItem":
			book_collection = self.__db[self.__collect_book]
		else:
			book_collection = self.__db[self.__collect_book_detail]
		data = dict(item)
		book_collection.insert(data)
		return item




	def close(self, spider):
		'''
		清理资源工作
		:param spider:
		:return:
		'''
		self.__client.close()

