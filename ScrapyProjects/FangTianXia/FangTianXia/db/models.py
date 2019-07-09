# -*- coding: utf-8 -*-


__author__ = 'zhougy'
__date__ = '2018/12/19 上午9:59' 

'''
自定义orm业务模型类
'''

from ScrapyProjects.FangTianXia.FangTianXia.db.mysql_helper import MySQLORMHelper, Base
from sqlalchemy import Column, String, Integer,Text
import json

class FTX(Base):
	__tablename__ = "fangtianxia"
	id = Column(Integer, primary_key=True)  #db can set it auto_increment
	name = Column(String(255))
	score = Column(String(255))
	price = Column(String(255))
	phone = Column(String(255))
	label = Column(String(255))
	doormodel = Column(String(255))
	address = Column(String(255))
	time = Column(String(255))


def synchronous():
	minst = MySQLORMHelper()
	session = minst.create_session()
	print(session)
	# Fang = FTX(
	# 	name='name',
	# 	score='score',
	# 	price='price',
	# 	phone='phone',
	# 	label='label',
	# 	doormodel='doormodel',
	# 	address='address',
	# 	time='time'
	# )
	# minst.add_records(session, Fang)


if __name__ == "__main__":
	synchronous()











