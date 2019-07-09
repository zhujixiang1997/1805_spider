# -*- coding: utf-8 -*-
import scrapy
from ScrapyProjects.GeYanWang.GeYanWang.db.models import GeYan
from ScrapyProjects.GeYanWang.GeYanWang.db.mysql_helper import MySQLORMHelper

minst = MySQLORMHelper()
session = minst.create_session()
class GeyanSpider(scrapy.Spider):
    name = 'geyan'
    allowed_domains = ['www.geyan123.com']
    start_urls = ['http://www.geyan123.com/']

    def parse(self, response):
        tbox_list = response.xpath("//dl[@class='tbox']/dd/ul/li")
        i = 1
        for tbox in tbox_list:
            title = tbox.xpath("./a/@title").extract_first()
            url = tbox.xpath("./a/@href").extract_first()
            geyan = GeYan(geyan_title=title,geyan_url=f"http://www.geyan123.com{url}")
            minst.add_records(session,geyan)
            print(f"第{i}条数据添加成功！！")
            i += 1
