# -*- coding: utf-8 -*-
__author__ = 'zjx'
__date__ = '2018/12/19 上午9:59'

'''
自定义orm业务模型类
'''

from ScrapyProjects.BookToscrape.BookToscrape.db.mysql_helper import MySQLORMHelper, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Text
import json


class Book(Base):
	__tablename__ = "books"
	id = Column(Integer, primary_key=True)  #db can set it auto_increment
	book_title = Column(String(200))
	image_url = Column(String(200))
	book_url = Column(String(300))
	book_url_fprint = Column(String(50), unique=True)
	book_price = Column(String(10))


	def __str__(self):
		res_dict = dict(
			id = self.id,
			book_title = self.book_title,
			image_url = self.image_url,
			book_price = self.book_price,
		)
		return json.dumps(res_dict)


class BookDetail(Base):
	__tablename__ = "book_detail"
	id = Column(Integer, primary_key=True)
	book_url_fprint = Column(String(50), ForeignKey(Book.book_url_fprint))
	#book_url_fprint = Column(String(50))
	book_description = Column(Text)



def synchronous():
	minst = MySQLORMHelper()
	session = minst.create_session()
	return (minst, session)


	#print(session)
	#
	# #result = minst.query_conditions(session, Book, Book.id, 21)
	#
	#
	#
	# #minst.update_record(session, Book, Book.id, 21, {Book.book_price:2000})
	#
	# #minst.delete_records(session, Book, Book.id, 22)
	#
	#
	# book_list = []
	# for i in range(10):
	# 	book = Book(book_title = f"book-{i}", image_url=f"image-{i}",
	# 				book_price=random.randint(20, 100), book_url=f"http://www.book-{i}.com")
	# 	book_list.append(book)
	#
	# minst.add_records(session, book_list)



if __name__ == "__main__":
	synchronous()











