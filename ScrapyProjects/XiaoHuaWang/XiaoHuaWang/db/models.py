# -*- coding: utf-8 -*-
__author__ = 'zhougy'
__date__ = '2018/12/19 上午9:59' 

'''
自定义orm业务模型类
'''

from ScrapyProjects.XiaoHuaWang.XiaoHuaWang.db.mysql_helper import MySQLORMHelper, Base
from sqlalchemy import Column, String, Integer,Boolean
import json

class XiaoHua(Base):
	__tablename__ = "xiaohua"
	id = Column(Integer, primary_key=True)  #db can set it auto_increment
	title = Column(String(64))
	image = Column(String(255))
	name = Column(String(64))
	school = Column(String(255))
	job = Column(String(64))
	age = Column(String(64))

	def __str__(self):
		res_dict = dict(
			id = self.id,
			title = self.title,
			image = self.image,
			name = self.name,
			school = self.school,
			job = self.job,
			age = self.age,
		)
		return json.dumps(res_dict)



def synchronous():
	minst = MySQLORMHelper()
	session = minst.create_session()
	print(session)
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











