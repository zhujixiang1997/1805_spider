# -*- coding: utf-8 -*-
import scrapy

from ScrapyProjects.XiaoXiangShuYuan.XiaoXiangShuYuan.items import XiaoxiangshuyuanItem


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['www.xxsy.net']
    start_urls = ['http://www.xxsy.net/search?vip=0&sort=2']
    # nexturl="http://www.xxsy.net/search?s_wd=&vip=0&sort=2&pn="

    def parse(self, response):
        detail_url_list = response.xpath("//div[@class='result-list']/ul/li")
        for detail_url in detail_url_list:
            url = detail_url.xpath("./div[@class='info']/h4/a/@href").extract_first()
            click = detail_url.xpath("./div[@class='info']/p[@class='number']/span[1]/text()").extract_first()
            yield scrapy.Request(url=f"http://www.xxsy.net{url}", callback=self.parse_detail, dont_filter=True,meta={'c':click})

        for i in range(2,7059):
            next_url = f"http://www.xxsy.net/search?s_wd=&vip=0&sort=2&pn={i}"
            # print(next_url)
            yield scrapy.Request(url=next_url,callback=self.parse)




    def parse_detail(self,response):
        book_img = response.xpath("//dl[@class='bookprofile']/dt/img/@src").extract_first()
        book_title = response.xpath("//dl[@class='bookprofile']/dd/div[@class='title']/h1/text()").extract_first()
        book_author = response.xpath("//dl[@class='bookprofile']/dd/div[@class='title']/span/a/text()").extract_first()
        book_state = response.xpath("//dl[@class='bookprofile']/dd/p[@class='sub-cols']/span[2]/text()").extract_first()
        book_label = response.xpath("//dl[@class='bookprofile']/dd/p[@class='sub-tags']//a/text()").extract()
        book_category = response.xpath("//dl[@class='bookprofile']/dd/p[@class='sub-cols']/span[3]/text()").extract_first()
        book_clicks = response.meta.get('c')
        book_updatetime = response.xpath("//dl[@class='bookprofile']/dd/div[@class='sub-newest']/p/span/text()").extract_first()
        book_number = response.xpath("//dl[@class='bookprofile']/dd/p[@class='sub-data']/span[1]/em/text()").extract_first()
        book_score = response.xpath("//div[@id='bookstar']/@data-score").extract_first()
        book_detial = response.xpath("//div[@class='book-profile']/dl/dd//p/text()").extract()
        result = {
            'book_img': "http:"+book_img if book_img else None,
            'book_title': book_title if book_title else None,
            'book_author': book_author if book_author else None,
            'book_state': book_state if book_state else None,
            'book_label': ','.join([str(i) for i in book_label]) if book_label else None,
            'book_category': book_category[3:] if book_category else None,
            'book_clicks': book_clicks[4:] if book_clicks else None,
            'book_updatetime': book_updatetime if book_updatetime else None,
            'book_number': book_number if book_number else None,
            'book_score': book_score if book_score else None,
            'book_detial':','.join([str(i) for i in book_detial]) if book_detial else None,
        }
        shu = XiaoxiangshuyuanItem(
            book_img=result['book_img'],
            book_title=result['book_title'],
            book_author=result['book_author'],
            book_state=result['book_state'],
            book_label=result['book_label'],
            book_category=result['book_category'],
            book_clicks=result['book_clicks'],
            book_updatetime=result['book_updatetime'],
            book_number=result['book_number'],
            book_score=result['book_score'],
            book_detial= result['book_detial']
        )
        yield shu
