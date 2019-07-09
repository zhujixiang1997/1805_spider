# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# from FangTianXia.db.mysql_helper import MySQLORMHelper
from FangTianXia.db.models import FTX
from FangTianXia.items import FangtianxiaItem

from FangTianXia.db.mysql_sql import MySQLHelper
minst = MySQLHelper()
session = minst.create_session()
import pymysql
connet = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='lajishuju', port=3306)
cursor = connet.cursor()
class FangtianxiaPipeline(object):

    def open_spider(self, spider):
        print('爬虫开始了')

    def process_item(self, item, spider):
        # fang = FTX(
        #     name=item['name'],
        #     score=item['score'],
        #     price=item['price'],
        #     phone=item['phone'],
        #     label=item['label'],
        #     doormodel=item['doormodel'],
        #     address=item['address'],
        #     time=item['time']
        # )
        # print(item)
        # print(type(fang))
        # minst.add_records(session,fang)
        # print("添加成功")
        # return item
        # 连接数据库
        sql = "insert into fangtianxia(name,score,price,phone,label,doormodel,address,time) " \
              "values (%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, (item['name'],item['score'],item['price'],item['phone'],item['label'],item['doormodel'],item['address'],item['time']))
        connet.commit()  # 映射到数据库中
        print("添加成功！")

    def close_spider(self, spider):
        connet.close()
        print('爬虫结束了')

