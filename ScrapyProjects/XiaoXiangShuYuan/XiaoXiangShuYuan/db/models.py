# -*- coding: utf-8 -*-
__author__ = 'zhougy'
__date__ = '2018/12/19 上午9:59' 

'''
自定义orm业务模型类
'''

from ScrapyProjects.XiaoHuaWang.XiaoHuaWang.db.mysql_helper import MySQLORMHelper, Base
from sqlalchemy import Column, String, Integer,Text
import json

class ShuKu(Base):
	__tablename__ = "xxsy2"
	id = Column(Integer, primary_key=True)  #db can set it auto_increment
	book_img = Column(String(255))
	book_title = Column(String(64))
	book_author = Column(String(64))
	book_state = Column(String(64))
	book_label = Column(String(64))
	book_category = Column(String(255))
	book_clicks = Column(String(64))
	book_updatetime = Column(String(64))
	book_number = Column(String(64))
	book_score = Column(String(64))
	book_detial = Column(Text)


def synchronous():
	minst = MySQLORMHelper()
	session = minst.create_session()
	print(session)


if __name__ == "__main__":
	synchronous()











