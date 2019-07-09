# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from ScrapyProjects.XiaoXiangShuYuan.XiaoXiangShuYuan.db.models import ShuKu
from ScrapyProjects.XiaoXiangShuYuan.XiaoXiangShuYuan.db.mysql_helper import MySQLORMHelper

minst = MySQLORMHelper()
session = minst.create_session()
class XiaoxiangshuyuanPipeline(object):
    def open_spider(self, spider):
        print('爬虫开始了')

    def process_item(self, item, spider):
        shu = ShuKu(
            book_img=item['book_img'],
            book_title=item['book_title'],
            book_author=item['book_author'],
            book_state=item['book_state'],
            book_label=item['book_label'],
            book_category=item['book_category'],
            book_clicks=item['book_clicks'],
            book_updatetime=item['book_updatetime'],
            book_number=item['book_number'],
            book_score=item['book_score'],
            book_detial=item['book_detial'],
        )
        minst.add_records(session,shu)
        print("添加成功")
        return item

    def close_spider(self, spider):
        print('爬虫结束了')