# -*- coding: utf-8 -*-
__author__ = 'jxk'
__date__ = '2018/12/18 18:57'

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# mysqlconnector

con =  'mysql+pymysql://root:123456@127.0.0.1:3306/lajishuju'
# con =  'mysql+pymysql://root:root@112.74.42.138:3306/books_spider'
engine = create_engine(con)
Base = declarative_base()


class MySQLHelper(object):

    def __create_db_table(self):
        '''
            基于engine创建数据库
        '''

        Base.metadata.create_all(engine)

    def create_session(self):
        '''
        创建一个session用于增删改查操作
        :return:
        '''
        self.__create_db_table()
        Session = sessionmaker(bind=engine)
        session = Session()
        return session

    def add_records(self, session, objs):
        '''
        添加orm对象数据到数据库
        :param session:
        :param objs: 列表对象 or 对象
        :return:
        '''
        if isinstance(objs, list):
            session.add_all(objs)
        else:
            session.add(objs)
        session.commit()

    def update_records(self, session, cls, cd_fields, cd_values, up_dict):
        '''
               更新数据库数据
             :param session:
             :param Cls:
             :param cd_field:   条件字段
             :param cd_value:   条件值
             :param up_dict:   更新字段和值组成字典
             :return:
        '''
        obj=session.query(cls).filter(cd_fields == cd_values).update(up_dict)
        if obj:
            session.commit()
            return True
        else:
            return False

    def query_records(self,session,cls):
        '''
        查询数据模型中的db数据
        :param session:
        :param cls:
        :return:
        '''
        return session.query(cls).all()

    def query_conditions(self,cls,session,field,value):
        '''
        查询满足条件的db数据
        :param cls:
        :param session:
        :param field:
        :param value:
        :return:
        '''
        return session.query(cls).filter(field==value)

    def delete_records(self,cls,session,fields,value):
        obj=session.query(cls).filter(fields==value).delete()
        '''
        删除
        :return:
        '''
        if obj:
            session.commit()
            return True
        else:
            return False

    '''
    给数据库分配权限
    create database toscrape default charset utf8;
    grant all pricilenges on toscrape.* to jxk@'%' identified by '123456';
    flush privileges;
    '''



