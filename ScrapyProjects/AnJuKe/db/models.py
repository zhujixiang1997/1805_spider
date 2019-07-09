# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/12/19 上午9:59' 

'''
自定义orm业务模型类
'''

from db.mysql_helper import MySQLORMHelper, Base

from sqlalchemy import Column, String, Integer, ForeignKey, Text
import json


class AnJuKe(Base):
	__tablename__ = "xinyangfangjia"
	id = Column(Integer, primary_key=True)  #db can set it auto_increment
	image = Column(String(255))
	name = Column(String(255))
	label = Column(String(255))
	ranking = Column(String(255))
	price = Column(String(255))
	open_time = Column(String(255))
	make_room = Column(String(255))
	door_model = Column(String(255))
	address = Column(String(255))
	phone = Column(String(255))

def synchronous():
	minst = MySQLORMHelper()
	session = minst.create_session()
	return (minst, session)

if __name__ == "__main__":
	synchronous()











