# -*-coding: utf-8 -*-
__author__ = 'zjx'
__data__ = '2018/12/18 0018 21:49'

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_SET_MAP = {
    'user':'root',
    'password':'123456',
    'host':'127.0.0.1',
    'port':'3306',
    'db':'pachong'
}
mysql_conn_str =f"mysql+pymysql://{DB_SET_MAP['user']}:{DB_SET_MAP['password']}@{DB_SET_MAP['host']}:{DB_SET_MAP['port']}/{DB_SET_MAP['db']}"
engine = create_engine(mysql_conn_str)
Base = declarative_base()


class MySQLHelper(object):
    def _create_db_table(self):
        # 基于engine创建数据库
        Base.metadata.create_all(engine)

    def create_session(self):
        # 创建session，用于增删改查操作.返回session对象
        self._create_db_table()
        Session = sessionmaker(bind=engine)
        session = Session()
        return session

    def add_records(self, session, objs):
        if isinstance(objs, list):  # [obj1, obj2]
            session.add_all(objs)  # 批量添加数据
        else:
            session.add(objs)  # 添加单条
        session.commit()

    def update_record(self, session, Cls, cd_field, cd_value, up_dict):
            '''
            更新数据库数据
            :param session:
            :param Cls:  需要更新的orm类
            :param cd_field:   更新的条件字段
            :param cd_value:   更新条件值
            :param up_dict:   更新字段和值组成字典
            :return:
            '''
            return session.query(Cls).filter(cd_field == cd_value).update(up_dict)

    # 查询数据模型中所有的db数据
    def query_records(self, session, Cls):
        return session.query(Cls).all()

    # 查询满足条件的db数据
    def query_conditions(self, Cls, session, field, value):
        '''
        查询满足条件的db数据
        :param Cls:
        :param session:
        :param field: Cls.field_name  eg : Stduent.sex
        :param value: field_value     eg:   1
        :return:
        '''
        return session.query(Cls).filter(field == value)

    # 删除
    def delete_records(self, Cls, session, field, value):
        obj = session.query(Cls).filter(field == value).delete()
        if obj:
            session.commit()
            return True
        else:
            return False

