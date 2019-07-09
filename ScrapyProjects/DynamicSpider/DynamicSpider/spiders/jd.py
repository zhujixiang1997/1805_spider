# -*- coding: utf-8 -*-
import scrapy

from ScrapyProjects.DynamicSpider.DynamicSpider.utils.bshead import create_bs_driver


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['www.jd.com']
    start_urls = ['http://www.jd.com/']
    query_key = input("请输入关键字:")

    def __init__(self):
        scrapy.Spider.__init__(self, self.name)
        self.driver = create_bs_driver()
        self.driver.set_page_load_timeout(20)

    def __del__(self):
        self.driver.quit()

    def start_requests(self):
        # 重写初始化url请求，携带上信息，下载中间价能识别
        for url in self.start_urls:
            yield scrapy.Request(url=url, meta={'type':'main','query_key':self.query_key}, callback=self.parse, dont_filter=True)

    def parse(self, response):
        print(f"{response.url}")
