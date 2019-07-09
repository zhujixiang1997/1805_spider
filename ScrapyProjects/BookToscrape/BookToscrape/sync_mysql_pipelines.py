# -*- coding: utf-8 -*-


__author__ = 'zhougy'
__date__ = '2018/12/25 上午10:00'
from ScrapyProjects.BookToscrape.BookToscrape.db.models import Book, BookDetail, synchronous
(minst, session) = synchronous()

#
# BOOK_ITEM_MAP = {
# 	'BooktoscrapeItem':(Book, ('book_title', 'image_url', 'book_url', 'book_url_fprint', 'book_price')),
#     'BookDetailItem':(BookDetail, ('book_url_fprint', 'book_description')),
# }


class SyncMySQLBookPipeLine(object):

	def  process_item(self, item, spider):
		'''
		:param item:  item是从spiders通过yield发射过来的对象
		:param spider:  spider是指的不同爬虫 （spider.name）
		:return:
		'''
		try:
			item_name = item.get_name()
			if item_name == "BooktoscrapeItem":
				book = Book(book_title=item['book_title'], image_url=item['image_url'],
							book_url=item['book_url'], book_url_fprint=item['book_url_fprint'],
							book_price=item['book_price'])
				minst.add_records(session, book)
			elif item_name == "BookDetailItem":
				book_detail = BookDetail(book_url_fprint=item['book_url_fprint'],
										 book_description=item['book_description'])
				minst.add_records(session, book_detail)
			#return item
		except Exception as e:
			print(f"MySQLBookPipeLine:process_item has error: {e}")
			#return item
		finally:
			return item
