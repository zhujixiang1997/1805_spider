# -*- coding: utf-8 -*-
__author__ = 'zjx'
__date__ = '2018/12/25 上午10:47' 

'''
采用scrapy内置的twisted网络库中企业级的异步处理db框架 --- adbapi
'''
from twisted.enterprise  import adbapi
from ScrapyProjects.BookToscrape.BookToscrape.settings import DB_SET_MAP
import logging


class AsyncMySQLPipeLine(object):
	def __init__(self, dbpool):
		self.__dbpool = dbpool


	@classmethod
	def from_crawler(cls, *args, **kwargs):
		#cls 等同于 AsyncMySQLPipeLine
		#读取配置文件内容
		dbparams = dict(
			host = DB_SET_MAP['host'],
			db = DB_SET_MAP['db'],
			user = DB_SET_MAP['user'],
			passwd = DB_SET_MAP['passwd'],
			charset = 'utf8',
		)
		#创建mysql数据库实例
		dbpool = adbapi.ConnectionPool("pymysql", **dbparams)

		return cls(dbpool)


	def process_item(self, item, spider):
		'''
	    使用twisted库提供的adbapi进行异步操作
	    :param item:
	    :param spider:
	    :return:
	    '''
		deferd = self.__dbpool.runInteraction(self.db_insert_handle, item, spider)
		deferd.addErrback(self.db_error_process, item, spider)

		#TODO do any other things, such as update, delete

		return item



	def db_insert_handle(self, cursor, item, spider):
		'''
		数据库插入成功的处理函数
		:param cursor:
		:param item:
		:param spider:
		:return:
		'''
		item_name = item.get_name()
		if item_name == "BooktoscrapeItem":
			insert_sql = "insert into books(book_title, image_url, book_url, book_url_fprint,book_price) " \
						 "values(%s, %s, %s, %s, %s)"
			insert_list = (item['book_title'], item['image_url'], item['book_url'], item['book_url_fprint'], item['book_price'])
			cursor.execute(insert_sql, insert_list)
		elif item_name == "BookDetailItem":
			insert_sql = "insert into book_detail(book_url_fprint, book_description) " \
						 "values(%s, %s)"
			insert_list = (
			item['book_url_fprint'], item['book_description'])
			cursor.execute(insert_sql, insert_list)

		return True


	def db_error_process(self, error, item, spider):
		item_name = item.get_name()
		logging.error(f"spider:{spider.name}, item_name:{item_name} db_insert_handle has error with {error}")
		return False





