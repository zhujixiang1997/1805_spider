# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from ScrapyProjects.DynamicSpider.DynamicSpider.db.models import Guazi
from ScrapyProjects.DynamicSpider.DynamicSpider.db.mysql_helper import MySQLORMHelper
minst = MySQLORMHelper()
session = minst.create_session()

class DynamicspiderPipeline(object):
    def open_spider(self, spider):
        print('爬虫开始了')

    def process_item(self, item, spider):
        guazi = Guazi(
            car_name=item['car_name'],
            car_image=item['car_image'],
            registration_time=item['registration_time'],
            mileage=item['mileage'],
            license_plate=item['license_plate'],
            displacement=item['displacement'],
            transmission=item['transmission'],
            price=item['price'],
        )
        minst.add_records(session, guazi)
        print("添加成功")
        return item

    def close_spider(self, spider):
        print('爬虫结束了')
