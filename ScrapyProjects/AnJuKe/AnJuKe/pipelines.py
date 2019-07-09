# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

from AnJuKe.items import AnjukeItem
from db.mysql_helper import MySQLORMHelper
connet = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='lajishuju', port=3306)
cursor = connet.cursor()
minst = MySQLORMHelper()
session = minst.create_session()
class AnjukePipeline(object):
    def open_spider(self, spider):
        print('爬虫开始了')

    def process_item(self, item, spider):
        # Fang = AnjukeItem(
        #     image=item['image'],
        #     name=item['name'],
        #     label=item['label'],
        #     ranking=item['ranking'],
        #     price=item['price'],
        #     open_time=item['open_time'],
        #     make_room=item['make_room'],
        #     door_model=item['door_model'],
        #     address=item['address'],
        #     phone=item['phone']
        # )
        # print(item)
        # a=item['image']
        # print(a)
        # b=Fang
        # print(b)
        # minst.add_records(session,Fang)
        # print("添加成功")
        # return item
        a=item['phone']
        sql = "insert into xinyangfangjia(image,name,label,ranking,price,open_time,make_room,door_model,address,phone) " \
              "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, (item['image'],
                             item['name'],
                             item['label'],
                             item['ranking'],
                             item['price'],
                             item['open_time'],
                             item['make_room'],
                             item['door_model'],
                             item['address'],
                             item['phone']))
        connet.commit()  # 映射到数据库中
        print("添加成功！")



    def close_spider(self, spider):
        connet.close()
        print('爬虫结束了')
