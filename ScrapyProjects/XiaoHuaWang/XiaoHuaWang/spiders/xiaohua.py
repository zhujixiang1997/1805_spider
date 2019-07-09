# -*- coding: utf-8 -*-
import scrapy

from ScrapyProjects.XiaoHuaWang.XiaoHuaWang.db.models import XiaoHua
from ScrapyProjects.XiaoHuaWang.XiaoHuaWang.db.mysql_helper import MySQLORMHelper
from ScrapyProjects.XiaoHuaWang.XiaoHuaWang.items import XiaohuawangItem

minst = MySQLORMHelper()
session = minst.create_session()
class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    allowed_domains = ['www.xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/hua/']
    domain_detail_url = 'http://www.xiaohuar.com/list-1-'
    page_num = 0

    def parse(self, response):
        detail_url_list = response.xpath("//div[@class='item_t']/div[@class='img']/a/@href").extract()
        for detail_url in detail_url_list:
            # print(detail_url)
            yield scrapy.Request(url=detail_url, callback=self.parse_detail,dont_filter=True)

        next_btn=response.xpath("//div[@class='page_num']/b/text()").get()
        if next_btn !='44':
            self.page_num+=1
            suffix=str(self.page_num)+'.html'
            yield scrapy.Request(url=self.domain_detail_url+suffix,callback=self.parse)

    def parse_detail(self,response):
        title = response.xpath("//div[@class='div_h1']/h1/text()").extract_first()
        name = response.xpath("//div[@class='infodiv']/table/tbody/tr[1]/td[2]/text()").extract_first()
        image = response.xpath("//div[@class='infoleft_imgdiv']/a/img/@src").extract_first()
        school = response.xpath("//div[@class='infodiv']/table/tbody/tr[5]/td[2]/text()").extract_first()
        job = response.xpath("//div[@class='infodiv']/table/tbody/tr[6]/td[2]/text()").extract_first()
        age = response.xpath("//div[@class='infodiv']/table/tbody/tr[2]/td[2]/text()").extract_first()

        result = {
            'title': title if title else '信息缺失',
            'image': "http://www.xiaohuar.com"+image if image else '信息缺失',
            'name': name if name else '信息缺失',
            'school': school if school else '信息缺失',
            'job': job if job else '信息缺失',
            'age': age if age else '信息缺失',
        }

        xiaohua = XiaohuawangItem(
            title=result['title'],
            image=result['image'],
            name=result['name'],
            school=result['school'],
            job=result['job'],
            age=result['age'],
        )
        xiaohua2 = XiaoHua(
            title=result['title'],
            image=result['image'],
            name=result['name'],
            school=result['school'],
            job=result['job'],
            age=result['age'],
        )
        minst.add_records(session, xiaohua2)
        print("添加成功！！")

        yield xiaohua







