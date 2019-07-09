# -*- coding: utf-8 -*-
__author__ = 'zhougy'
__date__ = '2018/12/19 上午9:59' 

'''
自定义orm业务模型类
'''

from ScrapyProjects.XiaoHuaWang.XiaoHuaWang.db.mysql_helper import MySQLORMHelper, Base
from sqlalchemy import Column, String, Integer,Text
import json

class Guazi(Base):
	__tablename__ = "guazi"
	id = Column(Integer, primary_key=True)  #db can set it auto_increment
	car_name = Column(String(255))
	car_image = Column(String(255))
	registration_time = Column(String(255))
	mileage = Column(String(255))
	license_plate = Column(String(255))
	displacement = Column(String(255))
	transmission = Column(String(255))
	price = Column(String(255))


def synchronous():
	minst = MySQLORMHelper()
	session = minst.create_session()
	print(session)


if __name__ == "__main__":
	synchronous()











