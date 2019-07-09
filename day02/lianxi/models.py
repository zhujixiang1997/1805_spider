# -*-coding: utf-8 -*-
__author__ = 'zjx'
__data__ = '2018/12/18 0018 21:55'

'''
  定义数据模型类
  '''
from sqlalchemy import Column, Integer, String
from day02.lianxi.mysql_helper import Base, MySQLHelper


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)  # create id column, set it auto_increment.
    title = Column(String(255))
    url = Column(String(255))



def synchronous():
    '''
    同步数据到db
    :return:
    '''
    minst = MySQLHelper()
    session = minst.create_session()  # synchronous model class into db.
    return (minst, session)


if __name__ == "__main__":
    synchronous()
